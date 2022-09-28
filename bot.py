import logging
from aiogram import Bot,Dispatcher,types,executor
import requests
import json



from aiogram.types import user


btn = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
btn.add("USD-UZS","RUB-UZS","EURO-UZS","CNY-UZS","VON-UZS", "DINOR-UZS")


token = "5422065810:AAG-YaecuT8Yu9IwGuZbA2tr-56nIy_vzao"
bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)



@dp.message_handler(commands=["start"])
async def first(message: types.Message):
    rasm1 = open("bank.jpeg", "rb")
    cap = f"Assalomu-aleykum, ShomaSunnatov | Valyuta Ayirboshlash | Botga Xush kelibsiz!"
    await bot.send_photo(message.chat.id, rasm1, caption=cap, reply_markup=btn)



@dp.message_handler(content_types=["text"])
async def second(message: types.Message):
    global inputs,outputs,result,cap,rasm
    text = message.text
    if text == "USD-UZS":
        inputs = "USD"
        outputs = "UZS"
        rasm = open("usd.jpeg","rb")
        cap = "Dollarning So'mdagi qiymati 👇"
    if text == "RUB-UZS":
        inputs = "RUB"
        outputs = "UZS"
        rasm = open("rub.jpeg","rb")
        cap = "Rublning So'mdagi qiymati 👇"
    if text == "DINOR-UZS":
        inputs = "DINOR"
        outputs = "UZS"
        rasm = open("dinor.jpeg","rb")
        cap = "Dinorning So'mdagi qiymati 👇"
    if text == "EURO-UZS":
        inputs = "EURO"
        outputs = "UZS"
        rasm = open("euro.jpeg","rb")
        cap = "Euroning So'mdagi qiymati 👇"
    if text == "VON-UZS":
        inputs = "VON"
        outputs = "UZS"
        rasm = open("von.jpeg","rb")
        cap = "Vonning So'mdagi qiymati 👇"



    url = "https://v6.exchangerate-api.com/v6/5d3f18bd0729d305e60f295c/latest/" + inputs
    respons = requests.get(url)
    rest = json.loads(respons.text)
    result = rest["conversion_rates"]["UZS"]
    if message.text.isdigit():
        print(int(message.text)*result)
        await bot.send_photo(message.chat.id, rasm, caption=cap)
        await bot.send_message(message.chat.id, int(message.text)*(result))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)