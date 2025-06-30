from aiogram import Router, F
from aiogram.enums import ContentType
from aiogram.types import CallbackQuery, Message

from core.utils.enums import Variables

router = Router(name="belozyortseva_router")

# Массив с пояснениями для каждого вопроса теста
explanations = {
    1: "Бэкенд — это серверная часть приложения, где происходит обработка данных, логика, хранение и выдача информации клиенту.",
    2: "Фронтенд — это адаптивное веб-приложение, которое общается с сервером через API (обычно REST или GraphQL)."
    # Можно добавить другие номера вопросов, если будет больше вопросов
}

# Массив с текстами следующих вопросов (если нужно)
next_questions = {
    2: "Фронтенд — это адаптивное веб-приложение, которое общается с сервером через…"
    # Если больше вопросов, добавляй сюда по ключу номер_теста
}

@router.message(F.content_type == ContentType.PHOTO)
async def handle_photo(message: Message):
    # Берём самое большое изображение (последний элемент списка)
    photo = message.photo[-1]
    photo_id = photo.file_id

    await message.answer(f"photo_id: {photo_id}")


@router.callback_query(F.data.startswith("belozyortseva_test_"))
async def belozyortseva_callback_handler(call: CallbackQuery, variables: Variables):
    parts = call.data.split("_")
    number_test = int(parts[-2])
    is_correct = parts[-1] == "true"

    correct_explanation = explanations.get(number_test, "")
    if is_correct:
        text = f"✅ Верно!\n\n{correct_explanation}"
    else:
        text = f"❌ Неверно!\n\n{correct_explanation}"

    # Меняем сообщение с вариантами на результат
    await call.message.edit_text(text=text)

    number_test += 1

    # Если есть следующий вопрос, отправляем его
    next_question_text = next_questions.get(number_test)
    if next_question_text:
        await call.message.answer(
            text=next_question_text,
            reply_markup=await variables.keyboards.menu.belozyortseva_menu(number_test=number_test)
        )
    await call.answer()