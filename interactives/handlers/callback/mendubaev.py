from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from core.bot_states import BotStates
from core.utils.enums import Variables
from core.utils.mendubaev_texts import mendubaev_texts

router = Router(name="mendubaev_callback_router")


@router.callback_query(F.data == "mendubaev")
async def first_mendubaev(call: CallbackQuery, state: FSMContext, variables: Variables):
    await state.set_state(BotStates.base)
    await state.update_data(interactive_name="mendubaev")
    text = mendubaev_texts[0]
    keyboard = await variables.keyboards.menu.mendubaev_start()
    await call.message.answer(
        text=text,
        reply_markup=keyboard
    )


@router.callback_query(F.data.startswith("mendubaev"))
async def second_mendubaev(call: CallbackQuery, variables: Variables):
    mode = call.data.split("_")[-1]
    if mode == "1":
        text = mendubaev_texts[1]
        keyboard = await variables.keyboards.menu.mendubaev_1()
        await call.message.edit_text(
            text=text,
            reply_markup=keyboard
        )
    else:
        text = mendubaev_texts[2]
        keyboard = await variables.keyboards.menu.mendubaev_2()
        await call.message.edit_text(
            text=text,
            reply_markup=keyboard
        )


@router.callback_query(F.data.startswith("1_mendubaev_"))
async def third_mendubaev(call: CallbackQuery, variables: Variables):
    mode = call.data.split("_")[-1]
    if mode == "1":
        text = mendubaev_texts[3]
        keyboard = await variables.keyboards.menu.mendubaev_final_1()
        await call.message.edit_text(
            text=text,
            reply_markup=keyboard
        )
    else:
        text = mendubaev_texts[4]
        keyboard = await variables.keyboards.menu.mendubaev_final_1()
        await call.message.edit_text(
            text=text,
            reply_markup=keyboard
        )


@router.callback_query(F.data.startswith("2_mendubaev_"))
async def fourth_mendubaev(call: CallbackQuery, variables: Variables):
    mode = call.data.split("_")[-1]
    if mode == "1":
        text = mendubaev_texts[5]
        keyboard = await variables.keyboards.menu.mendubaev_final_2()
        await call.message.edit_text(
            text=text,
            reply_markup=keyboard
        )
    else:
        text = mendubaev_texts[6]
        keyboard = await variables.keyboards.menu.mendubaev_final_2()
        await call.message.edit_text(
            text=text,
            reply_markup=keyboard
        )


@router.callback_query(F.data.startswith("final_mendubaev"))
async def final_mendubaev(call: CallbackQuery, variables: Variables):
    mode = call.data.split("_")[-1]
    if mode == "1":
        text = mendubaev_texts[7]
    else:
        text = mendubaev_texts[8]

    await call.message.edit_text(
        text=text
    )
    await call.edit_text(
        text="Как вам это выступление? / материалы спикера в easy",
        reply_markup=await variables.keyboards.menu.ending()
    )