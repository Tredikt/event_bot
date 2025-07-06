import asyncio

from aiogram import Router, F
from aiogram.enums import ChatAction
from aiogram.types import CallbackQuery

from core.utils.enums import Variables
from core.utils.scoring_utils import add_user_score


router = Router(name="gavrikov_router")


@router.callback_query(F.data == "gavrikov_start")
async def gavrikov_callback_handler(call: CallbackQuery, variables: Variables):
    await call.answer()
    user_id = call.from_user.id

    await call.message.delete()

    await variables.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)
    await asyncio.sleep(1)

    photo = "AgACAgIAAxkBAAIzr2hqLvm5si1sgk__Qi1yZyplJVpmAALY7jEbYIVRSw_hHWc3efnvAQADAgADeQADNgQ"
    await call.message.answer_photo(
        photo=photo, 
        caption="📍 <b>Вопрос для разогрева\n\nКто понимает, откуда берутся все эти цифры и как формируются начисления?</b>",
        reply_markup=await variables.keyboards.menu.gavrikov_start()
    )


@router.callback_query(F.data.startswith("gavrikov_pictures"))
async def gavrikov_pictures(call: CallbackQuery, variables: Variables):
    await call.answer()
    user_id = call.from_user.id

    await variables.bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)
    await asyncio.sleep(1)

    text = "Круто, сейчас посмотрим, сколько таких же как ты"
    await call.message.edit_caption(caption=text)
    await add_user_score(call=call, variables=variables, interactive_name="gavrikov_question_1", points=1)
