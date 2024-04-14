import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
bot = Bot(token="6742444254:AAHybu2gPK7oEToK2yxkcBH_kIfljF0bHfY")
dp = Dispatcher()
    
@dp.message(Command("старт"))
async def cmd_start(message: types.Message):
    await message.answer("Приветствую вас в нашем боте, который специализируется по оценке детского питания! Здесь вы найдете: \n❕полезную информацию о правильном питании для малыша\n❕проверку качества продукта \n❕рекомендации по выбору лучших продуктов для здоровья вашего ребенка \nНе стесняйтесь обращаться к нам за помощью! Выберите команду: \n/скан - сканировать фото продукта\n/инфо - информация о продукте по названию\n/противопоказания - противопоказания")

@dp.message(Command("скан"))
async def with_puree(message: types.Message):
    await message.reply("Загрузите фото продукта")

@dp.message(Command("инфо"))
async def without_puree(message: types.Message):
    await message.reply('Название: Йогурт "Агуша" с клубникой и Бананом \nКатегория: Десерт на молочной основе \nВозрастная маркировка: от 8 месяцев \nВ составе продукта указывается: ❌️сахар, соки концентрированные (из красной свёклы,  лимонный) \n\nПРЕДУПРЕЖДЕНИЕ ❗Продукт не рекомендуется детям от 8 месяцев в связи с большим количеством сахара')


@dp.message(Command("противопоказания"))
async def withoutg_puree(message: types.Message):
    await message.reply("Данный продукт не подходит детям с такими заболеваниями как:\n– сахарный диабет. Рекомендуемо использовать продукты с наименьшим содержанием сахара и концентрированных соков\n– ожирение. Рекомендуемо сократить количество углеводов\n– аллергией на фрукты. Рекомендуемо заменить продукты, вызывающие аллергию")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    