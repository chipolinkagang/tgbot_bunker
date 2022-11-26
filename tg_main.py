from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher

import db_main
from aiopg.sa import create_engine

import markups as nav
import take_random_funcs

bot = Bot(token='')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    uid = message.from_user.id  # записал id
    uname = message.from_user.full_name  # имя
    person = {"name": uname, "tg_id": str(uid)}
    async with create_engine(user='postgres',
                             database='postgres',
                             host='127.0.0.1',
                             password='123456') as engine:
        if not await db_main.reg_check(engine, person["tg_id"]):
            await db_main.registration(engine, person)
            await message.reply("Регистрация успешно пройдена!", reply_markup=nav.mainMenu)
        else:
            await message.reply("Вы уже зарегистрированы. Переходим к меню", reply_markup=nav.mainMenu)

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

@dp.message_handler()
async def echo_message(message: types.Message):
    if message.text == "⬅️ Главное меню":
        await bot.send_message(message.from_user.id, "Вернулись в главное меню.", reply_markup=nav.mainMenu)

    if message.text == "🕹ИГРА":
        await bot.send_message(message.from_user.id, "Меню создания игры.\nИгра рассчитана на состав не менее 6 человек. Оптимально от 8 до 12 человек.", reply_markup=nav.gameMenu)
    #gameMenu:
    if message.text == "🕹Новая игра":
        await bot.send_message(message.from_user.id, "Введите кол-во игроков:", reply_markup=nav.gameMenu)
    if isint(message.text):
        if int(message.text) < 17:
            # делает персонажей по введенному числу
            for i in range(1, int(message.text)+1):
                x = take_random_funcs.generate_person()
                person = '''            Пол: <tg-spoiler>''' + x["gender"] + '''</tg-spoiler>
                Возраст: <tg-spoiler>''' + x["age"] + '''</tg-spoiler> Фертильность: <tg-spoiler>''' + x["fertility"] + '''</tg-spoiler>
                Рост: <tg-spoiler>''' + x["height"] + '''</tg-spoiler> Телосложение: <tg-spoiler>''' + x["body_type"] + '''</tg-spoiler>
                Профессия: <tg-spoiler>''' + x["profession"] + '''</tg-spoiler> Стаж: <tg-spoiler>''' + x["experience"] + ''' лет</tg-spoiler>
                Здоровье: <tg-spoiler>''' + x["health"] + " " + x["health_pcs"] + '''%</tg-spoiler>
                Хобби: <tg-spoiler>''' + x["hobby"] + '''</tg-spoiler>
                Фобия: <tg-spoiler>''' + x["phobia"] + '''</tg-spoiler>
                Черта характера: <tg-spoiler>''' + x["trait"] + '''</tg-spoiler>
                Багаж: <tg-spoiler>''' + x["baggage"] + '''</tg-spoiler>
                Доп. инфа: <tg-spoiler>''' + x["information"] + '''</tg-spoiler>
                Карта действия №1: <tg-spoiler>''' + x["card1"] + '''</tg-spoiler>
                Карта действия №2: <tg-spoiler>''' + x["card2"] + '''</tg-spoiler>
                '''
                await bot.send_message(message.from_user.id, "Карта персонажа №:" + str(i) + "\n\n" + person,
                                       reply_markup=nav.changeMenu, parse_mode=types.ParseMode.HTML)
            # делает катастрофу
            d = take_random_funcs.generate_disaster()
            await bot.send_message(message.from_user.id, "Новая катастрофа:\n\n" + d, reply_markup=nav.changeMenu,
                                   parse_mode=types.ParseMode.HTML)
            # делает бункер
            b = take_random_funcs.generate_bunker()
            bunker = '''Площадь: ''' + b["size"] + ''' кв.м.
            Комнаты: ''' + b['rooms'][0] + ''', ''' + b['rooms'][1] + ''', ''' + b['rooms'][2] + '''.
            Предметы: ''' + b['items'] + '''.'''
            await message.answer("Новый бункер:\n\n<tg-spoiler>" + bunker + "</tg-spoiler>",
                                 parse_mode=types.ParseMode.HTML)

        else:
            await bot.send_message(message.from_user.id, "Слишком большое число игроков.", reply_markup=nav.changeMenu)

    if message.text == "🔁Сменить карту":
        await bot.send_message(message.from_user.id, "Замена карты.", reply_markup=nav.changeMenu)

    #changeMenu:
    if message.text == "📟БУНКЕР":
        b = take_random_funcs.generate_bunker()
        bunker = '''Площадь: ''' + b["size"] + ''' кв.м.
Комнаты: ''' + b['rooms'][0] + ''', ''' + b['rooms'][1] + ''', ''' + b['rooms'][2] + '''.
Предметы: ''' + b['items'] + '''.'''
        await message.answer("Новый бункер:\n\n<tg-spoiler>" + bunker + "</tg-spoiler>", parse_mode=types.ParseMode.HTML)
    if message.text == "🙍‍♂ПЕРСОНАЖ":
        x = take_random_funcs.generate_person()
        person = '''Пол: <tg-spoiler>''' + x["gender"]+'''</tg-spoiler>
Возраст: <tg-spoiler>''' + x["age"]+'''.</tg-spoiler> Способность к оплодотворению: <tg-spoiler>''' + x["fertility"]+'''</tg-spoiler>
Рост: <tg-spoiler>''' + x["height"]+'''.</tg-spoiler> Телосложение: <tg-spoiler>''' + x["body_type"]+'''</tg-spoiler>
Профессия: <tg-spoiler>''' + x["profession"]+'''.</tg-spoiler> Стаж: <tg-spoiler>''' + x["experience"]+''' лет</tg-spoiler>
Здоровье: <tg-spoiler>''' + x["health"] + " " + x["health_pcs"] + '''%</tg-spoiler>
Хобби: <tg-spoiler>''' + x["hobby"]+'''</tg-spoiler>
Фобия: <tg-spoiler>''' + x["phobia"]+'''</tg-spoiler>
Черта характера: <tg-spoiler>''' + x["trait"]+'''</tg-spoiler>
Багаж: <tg-spoiler>''' + x["baggage"]+'''</tg-spoiler>
Доп. инфа: <tg-spoiler>''' + x["information"]+'''</tg-spoiler>
Карта действия №1: <tg-spoiler>''' + x["card1"]+'''</tg-spoiler>
Карта действия №2: <tg-spoiler>''' + x["card2"]+'''</tg-spoiler>
'''
        await bot.send_message(message.from_user.id, "Новая карта персонажа:\n\n" + person, reply_markup=nav.changeMenu, parse_mode=types.ParseMode.HTML)
    if message.text == "🎇КАТАСТРОФА":
        d = take_random_funcs.generate_disaster()
        await bot.send_message(message.from_user.id, "Новая катастрофа:\n\n" + d, reply_markup=nav.changeMenu, parse_mode=types.ParseMode.HTML)


    if message.text == "ℹ️Помощь":
        await bot.send_message(message.from_user.id, "Тут будет туториал по игре.", reply_markup=nav.helpMenu)



if __name__ == '__main__':
    executor.start_polling(dp)