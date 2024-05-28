from api import short_url

import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "7137394070:AAEoYAS-vTS2-r9AZIHBYCLycMP11age3lA"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

# zxasdas dasd
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: Message, bot: Bot) -> None:
#example1 Qisqa link
    # url1= short_url(message.text)
    # await message.answer(url1)
# example2 Sonlarni kvadrati
    # try:
    #     print(message.text)
    #     print(message.from_user.full_name)
    #     await message.answer(str(int(message.text)**2))
    # except:
    #     await message.answer("Yaxshii emas.... Son kiriting!")
# example3
    try:
        print(message.text)
        print(message.from_user.full_name)
        result = str(int(message.text) ** 2)
        await message.answer(result)
        await bot.set_chat_title(message.chat.id, result)

    except:
        await message.answer("Yaxshii emas.... Son kiriting!")
#example0 So'zlarni qaytarish
    # """
    # Handler will forward receive a message back to the sender
    #
    # By default, message handler will handle all message types (like a text, photo, sticker etc.)
    # """
    # try:
    #     # Send a copy of the received message
    #     await message.send_copy(chat_id=message.chat.id)
    # except TypeError:
    #     # But not all the types is supported to be copied so need to handle it
    #     await message.answer("Nice try!")



async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())