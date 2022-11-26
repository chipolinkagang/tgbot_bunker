from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('⬅️ Главное меню')
# main menu
btnGame = KeyboardButton('🕹ИГРА')
btnChange = KeyboardButton('ℹ️Помощь')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnGame, btnChange)

# game menu
btnCreate = KeyboardButton('🕹Новая игра')
btnChange = KeyboardButton('🔁Сменить карту')
gameMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCreate, btnChange, btnMain)

# change menu
btnBunker = KeyboardButton('📟БУНКЕР')
btnPerson = KeyboardButton('🙍‍♂ПЕРСОНАЖ')
btnDisaster = KeyboardButton('🎇КАТАСТРОФА')
changeMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnBunker, btnPerson, btnDisaster, btnMain)

# help menu
helpMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMain)
