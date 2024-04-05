from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, InputFile
from dotenv import load_dotenv
load_dotenv()
import os

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Crypto', 'NFT')

Crypto = ReplyKeyboardMarkup(resize_keyboard=True)
Crypto.add('Bitcoin', 'Toncoin', 'Tether', 'Ethereum', 'Arbitrum', 'Back')

nft = ReplyKeyboardMarkup(resize_keyboard=True)
nft.add('BAYC', 'CryptoPunk', 'Fidenza', 'Everydays', 'Beeple', 'Back')

#crypto
photo_btc = InputFile('bitcoin.jpg')
photo_ton =InputFile('toncoin.jpg')
photo_usdt = InputFile('tether.jpg')
photo_ethereum = InputFile('ethereum.jpg')
photo_arbitrum = InputFile('arbitrum.jpg')

#NFT
photo_BAYC = InputFile('BAYC.jpg')
photo_crypto_punk = InputFile('cryptopunk.jpg')
photo_fidenza = InputFile('fidenza.jpg')
photo_everydays = InputFile('everydays.jpg')
photo_beeple = InputFile('beeple.jpg')

@dp.message_handler(text='Beeple')
async def beeple(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=photo_beeple)

@dp.message_handler(text='Everydays')
async def everydays(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=photo_everydays)

@dp.message_handler(text='Fidenza')
async def fidenza(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=photo_fidenza)

@dp.message_handler(text='CryptoPunk')
async def crypto_punk(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=photo_crypto_punk)

@dp.message_handler(text='BAYC')
async def bayc(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=photo_BAYC)

@dp.message_handler(text='Bitcoin')
async def bitcoin(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=photo_btc)

@dp.message_handler(text='Toncoin')
async def toncoin(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=photo_ton)

@dp.message_handler(text='Tether')
async def tether(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=photo_usdt)

@dp.message_handler(text='Ethereum')
async def ethereum(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=photo_ethereum)

@dp.message_handler(text='Arbitrum')
async def arbitrum(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=photo_arbitrum)

@dp.message_handler(text='Back')
async def back(message: types.Message):
    await message.answer('...',reply_markup=main)

@dp.message_handler(text='Crypto')
async def crypto(message: types.Message):
    await message.answer("Choose crypto to get info", reply_markup=Crypto)

@dp.message_handler(text='NFT')
async def nft_gg(message: types.Message):
    await message.answer("Here is list of top NFT", reply_markup=nft)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAMFZg6TkCqy9Q4Csuz8HxdZ207W9v4AAsYBAAIWQmsKSiPU9MnbeUc0BA')
    await message.answer(f"Hey @{message.from_user.username}, here you can get info about crypto and NFT", reply_markup=main)

    if message.from_user.id == int(os.getenv('ID')):
        await message.answer('You logged in as admin! ')


if __name__ == '__main__':
    executor.start_polling(dp)

