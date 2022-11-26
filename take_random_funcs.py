import random

data_person = {
    "gender": ["мужчина", "женщина"],
    "fertility": ["Есть", "Нет", "Чайлдфри"],
    "body_type": ["Норма", "Крепкое", "Ожирение (1 степень)", "Ожирение (2 степень)", "Ожирение (3 степень)", "Анорексия",
                  "Мускулистое"],
    "profession": ["Химик", "Биоинженер", "Композитор", "Наркодилер", "Президент", "Программист", "Вор", "Модель",
                   "Грузчик", "Сценарист", "Ветеринар", "Сварщик", "Юрист", "Строитель", "Плотник", "Археолог", "Космонавт",
                   "Актер", "Учитель младших классов", "Психолог", "Садовод", "Электрик", "Иммунолог", "Гитарист", "Художник",
                   "Бухгалтер", "Спортсмен", "Терапевт", "Инструктор по выживанию", "Ученый", "Экономист", "Блогер", "Ботаник",
                   "Певец", "Инженер", "Географ", "Искуствовед", "Сценарист", "Журналист", "Повар", "Математик", "Летчик",
                   "Кинолог", "Историк", "Философ", "Адвокат", "Переводчик", "Зоолог", "Клоун", "Режиссер", "Фотограф",
                   "Водитель", "Киллер", "Военный", "Хирург", "Банкир", "Охранник", "Предприниматель", "Официант",
                   "Таксист", "Фермер", "Телохранитель", "Скульптор", "Авиадиспетчер", "Прокурор", "Фармацевт", "Диджей",
                   "Иммунолог", "Геолог", "Менеджер"],
    "health": ["Полностью здоров(% не применимы)", "Простуда(% не применимы)", "Туберкулез", "Гепатит А", "Лейкоз", "Порок сердца",
               "Болезнь Альцгеймера", "Дисбактериоз", "Без руки(% не применимы)", "Несвертываемость крови", "Шизофрения", "Заикание",
               "Невроз", "Язва желудка", "Диабет", "ВИЧ", "Гепатит В", "Гепатит C", "Аллергия на шерсть", "Немой(% не применимы)", "Депрессия",
               "Без ноги(% не применимы)", "Бессонница", "Биполярное расстройство", "Был инсульт(% не применимы)", "Псориаз",
               "Рак", "Сифилис", "Перелом ноги", "Остеохондроз", "Коронавирус", "Вши", "Плоскостопие", "Дрожь в конечностях",
               "Аллергия на лекарства", "Вегето сосудистая дистония", "СПИД", "Астигматизм", "Бешенсто", "Облысение", "Прыщи",
               "Диарея", "Психическая неустойчивость", "Малярия", "Галлюцинации", "Паранойя", "Язва желудка", "Аллергия на шерсть",
               "Косоглазие", "Алкоголизм"],
    "hobby": ["Гербарий", "Авиамоделирование", "Спортивное ориентирование", "Футбол", "Парашютный спорт", "Рыбалка",
              "Изучение диких видов животных", "Стрельба", "Жарит шашлыки", "Зоология", "Исторические реконструкции",
              "Разработка сайтов", "Косплей", "Вязание и Шитье", "Любит собирать грибы", "Баскетбол", "Резьба по дереву",
              "Косплей", "Фитнес", "Йога", "Бодибилдинг", "Велопрогулки", "Восточные танцы", "Пение", "Нумизматика",
              "Теннис", "Массаж", "Стрельба", "Серфинг", "Боевые искусства", "Психология", "Бег", "Паркур",
              "Исторические реконструкции", "Изучение растений", "Шахматы", "Стриминг", "Лепка из глины", "Плавание",
              "Хиромантия", "Лыжи", "Дизайн одежды", "Решение математических задач", "Сбор грибов", "Изготовление вина",
              "Охота", "Гидропоника(выращивание растений без почвы)", "История", "Туризм", "Компьютерные игры", "Взломщик",
              "Лечебное голодание", "Танцы"],
    "phobia": ["Фенгофобия (Боязнь света)", "Никрофобия (Боязнь темноты)", "Земмифобия (Испуг от вида крыс)", "Акрофобия (Боязнь высоты)",
               "Гоплофобия (Боязнь при виде огнестрельного оружия)", "Фасмофобия (Боязнь приведений)", "Анирофобия (Паникует во время перехода через улицу)",
               "Барофобия (Боязнь поднимать тяжести)", "Гравидофобия (Боязнь беременности)", "Гимнофобия (Боится наготы)",
               "Ангрофобия (Страх перед своим гневом или гневом других людей)", "Антлофобия (Боязнь наводнений/утонуть)",
               "Гаптофобия (Боязнь касаний)", "Инсектофобия (Боязнь и страх всех насекомых)", "Киберофобия (Боязнь компьютерной техники)",
               "Клаустрофобия", "Аулофобия (Боязнь флейт)", "Зоофобия (Боязнь животных)", "Коулрофобия (Боязнь клоунов)",
               "Земмифобия (Испуг от вида крыс)", "Гематофобия (Боязнь крови)", "Офидиофобия (Боязнь змей)", "Виккафобия (Боязнь колдовства)",
               "Ахлуофобия(боязнь оказаться в темноте)", "Гомофобия", "Айхмофобия (Страх острых предметов)", "Арахнофобия (Боязнь пауков)",
               "Децидофобия (Боязнь принятия самостоятельных решений)", "Мелофобия (Боязнь музыки)", "Мизофобия (Боязнь грязи и микробов)",
               "Кинофобия (Боязнь собак)", "Нет фобий"],
    "trait": ["Бесстрашный", "Весельчак", "Жадный", "Равнодушный", "Героический", "Вредный", "Жестокий", "Агрессивный",
              "Мелочный", "Ловкий", "Навязчивый", "Заботливый", "Смышленый", "Понимающий", "Вежливый", "Гордый",
              "Грустный", "Ворчливый", "Исполнительный", "Тихий", "Властный", "Ответственный", "Храбрый", "Справедливый",
              "Бесконфликтный", "Надоедливый", "Выносливый", "Убедительный", "Азартный", "Сплетник", "Верующий", "Невезучий",
              "Нежный"],
    "baggage": ["Таблетки от аллергии", "Грудной ребёнок", "Четыре рации", "Губная гармошка", "Фильтр для воды", "Три респираторные маски",
                "Лук и стрелы", "Молоток и гвозди", "Фотоаппарат", "Газовая горелка", "Детские игрушки", "Перочинный нож",
                "Карточки черепашки ниндзя", "Семена", "Кассеты с фильмами", "Десять пачек чипсов", "Компьютер", "Складная табуретка",
                "Десять одноразовых медицинских масок", "Рулоны туалетной бумаги", "10 шоколадок", "Семена пшеницы", "Аптечка",
                "Комиксы", "Энциклопедия грибника", "Кот", "Косметичка", "10 коробков спичек", "Удочка и черви", "Компас",
                "Отмычка", "Палатка", "Ящик пива", "Фонарик и запасные батарейки", "Гитара", "Ферма грибов", "Набор для вышивки",
                "Спицы для вязания", "Антена для усиления сигнала", "Палатка", "Зонтик", "Игровая приставка с играми",
                "Игральные карты", "Книга по охоте", "Ружье и 10 патрон"],
    "information": ["Пережил(а) три покушения", "Рос в семье уголовников", "Побывал(а) на вершине Эвереста", "что эта катастрофа - заговор рептилий",
                    "Умеет делать и чинить часы", "Был(а) вожатым в лагере", "Верит в сверхъестественных существ",
                    "Продал(а) почку", "По первому образованию - терапевт", "Хорошо играет в карты", "Знает язык жестов",
                    "Смотрел фильмы про апокалипсис", "Является резидентом Comedy Club", "В прошлом мастер спорта по борьбе",
                    "В прошлом гроссмейстер", "Верит в экстрасенсов", "Ограбил(а) банк", "Рос в семье врачей",
                    "Ведёт личный дневник", "Умеет очищать воду", "Не переносит алкоголь", "Ненавидит современную музыку",
                    "Читал книги про зомби", "Гадает по картам", "Знает наизусть все стихи Пушкина", "Имеет два высших образования",
                    "Побывал(а) в восемнадцати странах", "Является вегетарианцем", "Проходил курсы по выживанию",
                    "Проходил(а) курс по самообороне", "Поставил(а) мировой рекорд по поеданию бургеров",
                    "Верит в пришельцев", "Сидел(а) в тюрьме", "Выиграл(а) в лотерее целое состояние", "Ненавидит кофе",
                    "Читал(а) книгу про выживание на необитаемом острове", "Может оказать первую помощь", "Умеет вскрывать замки",
                    "Быстро бегает"],
    "cards": ["Возле вас находится бункер с агрессивно настроенными выжившими", "Храни карту в тайне. Друг(Игрок справа от тебя обязательно должен попасть в бункер)",
              "Вы можете активировать карту №1 игрока по выбору", "Изменить свой багаж на новый", "В 100 м от вас есть бункер с мужчинами(Здоровыми и Плодовитыми)",
              "Ты можешь поменять свою карту профессии на новую из колоды", "В 30 м от бункера есть погреб с вином",
              "Рядом с вами второй бункер и он настроен недоброжелательно", "Лечит любого игрока или вас",
              "Все должны переголосовать заново, выбирая другого кандидата", "Вы можете активировать карту №2 игрока по выбору",
              "Любой игрок по выбору раскрывает свою характеристику по вашему выбору", "Поменяться хобби с другим игроком",
              "Возле вас находится бункер с двумя женщинами-химиками(Полностью здоровые/возраст: 25-45 лет)",
              "Храни карту в тайне. Враг(Игрок справа от тебя не должен попасть в бункер)",
              "Все узнают, что поблизости находится бункер всего лишь с двумя выжившими, мужчины это или женщины - неизвестно",
              "Ваш бункер находится на необитаемом острове", "Ваш голос считается за два", "Ты можешь поменяться здоровьем с другим человеком",
              "В 100 м от вас есть бункер с мужчинами(Здоровыми и Плодовитыми)", "Данная карта разрешает перекинуть один голос с вас на другого",
              "Защищает любого игрока на один ход", "Отменить последнюю карту действия", "Обмен профессиями справа налево",
              "Ваш бункер находится около пресного озера", "Изменить свой багаж на новый", "Любой игрок по выбору раскрывает свое здоровье",
              "У тебя есть защита на 1 игровой круг (Если против твоего персонажа максимальное кол-во голосов)",
              "Вернуть игрока в бункер", "Ты можешь обменять свою фобию на фобию другого игрока",
              "Убирает одно место в бункере", "Добавляет 1 место в бункер", "В 50 м от бункера есть склад с оружием",
              "Лечит любого игрока или вас", "Поменяться багажем с другим игроком(на ваш выбор)"
              ]
}

data_bunker = {
    "size": ["100", "150", "200", "250", "300", "350"],
    "rooms": ["Склад", "Теплица", "Лаборатория", "Оружейная", "Мед.кабинет", "Спортзал", "Мастерская", "Кабинет психолога",
              "Погреб с вином", "Генератор", "Пустая комната", "Оранжерея", "Кинотеатр", "Барьер для животных (место содержания животных)"],
    "items": ["Радио", "Библиотека с книгами для выживания", "Книги по очистке воды", "Охотничьи ножи", "Книга по ремонту техники",
              "Аптечка первой помощи", "Плодородная почва", "Инкубатор с яйцами", "Автомобиль (полный бак)"]
}

data_disaster = [
    "    <b>Экологическая катастрофа и глобальный голод.</b>\n    Интенсивное ведение сельского хозяйства и деградация почв вкупе с засухой привели к пыльным бурям которые массово уничтожают посевы и приводят к неурожаю и значительному уменьшению запасов пищи. Концентрация кислорода в атмосфере падает и климат значительно ухудшается.\n    Остаток выжившего населения: 17%.\n    Разрушения на поверхности: 4%.\n    В бункере необходимо провести 1 год 6 месяцев.",
    "    <b>Суперкомпьютер.</b>\n    Искусственный интеллект который задумывался для управления системами обороны вышел из строя и посчитал человечество большой опасностью. Это привело к тому что искусственный интеллект отключил инструкцию «не убивать человека» и взял под контроль процедуры управления военными роботами которые начали истреблять человечество. Суперкомпьютер захватил власть над планетой выжившим людям пришлось прятаться в старых бункерах.\n    Остаток выжившего населения: 4%.\n    Разрушения на поверхности: 32%.",
    "    <b>Супервулкан.</b>\n    Взрыв Йеллоустонского супервулкана пошатнул Землю, выброшенный в атмосферу пепел закрыл Солнце на несколько месяцев. На планете началась «ядерная зима», средняя температура опустилась на 11 градусов, погибли 80% существ населявших Землю. Климат существенно изменился. На планете теперь царит глобальная засуха.\n    Остаток выжившего населения: 7%.\n    Разрушения на поверхности: 9%.\n    В бункере необходимо провести 2 года.",
    "    <b>Зомби-апокалипсис.</b>\n    Неизвестный возбудитель стал причиной превращения людей в кровожадных зомби Коллапс системы Больницы более не функционируют Тотальная паника армия начинает стрелять на поражение при попытке покинуть карантинную зону Власть уже не может контролировать ситуацию Начинается тотальное мародерство и анархия После выхода из бункера малый процент зомби останется в живых.\n    Остаток выжившего населения: 21%.\n    Разрушения на поверхности: 12%.\n    В бункере необходимо провести 2 года.",

]

def generate_disaster():
    res_dict = data_disaster[random.randint(0, len(data_disaster) - 1)]
    return res_dict

def generate_bunker():
    res_dict = {
        "size": data_bunker["size"][random.randint(0, len(data_bunker["size"]) - 1)],
        "rooms": [data_bunker["rooms"][random.randint(0, len(data_bunker["rooms"]) - 1)], data_bunker["rooms"][random.randint(0, len(data_bunker["rooms"]) - 1)], data_bunker["rooms"][random.randint(0, len(data_bunker["rooms"]) - 1)]],
        "items": data_bunker["items"][random.randint(0, len(data_bunker["items"]) - 1)]
    }
    return res_dict

def generate_person():
    cho = random.randint(0, 3)
    if cho <= 1:
        max_age = 78
        max_health = 100
    else:
        max_age = 55
        max_health = 50
    res_dict = {
        "gender": data_person["gender"][random.randint(0, 1)],
        "age": str(random.randint(18, max_age)),
        "fertility": data_person["fertility"][random.randint(0, len(data_person["fertility"]) - 1)],
        "height": str(random.randint(160, 200)),
        "body_type": data_person["body_type"][random.randint(0, len(data_person["body_type"]) - 1)],
        "profession": data_person["profession"][random.randint(0, len(data_person["profession"]) - 1)],
        "experience": str(random.randint(0, max_age-15)),
        "health": data_person["health"][random.randint(0, len(data_person["health"]) - 1)],
        "health_pcs": str(random.randint(18, max_health)),
        "hobby": data_person["hobby"][random.randint(0, len(data_person["hobby"]) - 1)],
        "phobia": data_person["phobia"][random.randint(0, len(data_person["phobia"]) - 1)],
        "trait": data_person["trait"][random.randint(0, len(data_person["trait"]) - 1)],
        "baggage": data_person["baggage"][random.randint(0, len(data_person["baggage"]) - 1)],
        "information": data_person["information"][random.randint(0, len(data_person["information"]) - 1)],
        "card1": data_person["cards"][random.randint(0, len(data_person["cards"]) - 1)],
        "card2": data_person["cards"][random.randint(0, len(data_person["cards"]) - 1)]
    }
    if cho == 0:
        res_dict["health"] = "Полностью здоров(% не применимы)"
    if cho <= 1:
        res_dict["body_type"] = "Норма"
    if cho <= 2:
        res_dict["fertility"] = "Есть"

    return res_dict

#
# print(len(data_bunker["items"]))