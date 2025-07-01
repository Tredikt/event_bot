answer_choices = [
    {
        "options": ["Логика и интерфейс", "Ядро и приложение", "Винт и шуруп", "Чайник и процессор"],
        "correct_index": 0
    },
    {
        "options": ["Через прямое подключение к базе данных", "API", "Почтового голубя", "Телеграм-бота"],
        "correct_index": 1
    },
    {
        "options": ["Не понимаю", "Что такое ЖКХ", "Понимаю", "Я сам участвовал в реализации этого проекта"],
    }
]

horoshutina_sequence = [
    {"word": "Демоиспользование", "order": 3, "id": "demo"},
    {"word": "Выявление потребности", "order": 1, "id": "need"},
    {"word": "Контрактование", "order": 6, "id": "contract"},
    {"word": "Итоговое формирование условий", "order": 5, "id": "terms"},
    {"word": "Показ", "order": 2, "id": "show"},
    {"word": "Дожим", "order": 4, "id": "push"},
]

horoshutina_right_answer = "1️⃣ Выявление потребности\n\n2️⃣ Показ\n\n3️⃣ Демоиспользование\n\n4️⃣ Дожим\n\n5️⃣ Итоговое формирование условий\n\n6️⃣ Контрактование"

photo_id = [
    "AgACAgIAAxkBAAMFaFcQ_bAajmdRRrRUPc1WLuF5uVcAAgLvMRukirlKyfZiVwEziscBAAMCAAN5AAM2BA",
    "AgACAgIAAxkBAAMHaFcTMPZN7jYfB-b3uR_WFMsk_QQAAhXvMRukirlKGXtiRMCU904BAAMCAAN4AAM2BA",
    "AgACAgIAAxkBAAMKaFcTvstEOfy671PFkdA_LtsbjBYAAhbvMRukirlKOh275kqGKBkBAAMCAAN5AAM2BA",
    "AgACAgIAAxkBAAMMaFcTx-ZSxh7F174w_axhQOWSPCsAAhfvMRukirlKgRT9cB-qn2sBAAMCAAN5AAM2BA"
]

sadriev_test = {
    "options": [
        "от 100 млн до 500 млн", 
        "от 500 млн до 1 млрд", 
        "от 1 млрд до 2 млрд", 
        "от 2 млрд до 3 млрд", 
        "более 3 млрд"
    ],
    "correct_index": 2
}


QUESTIONS = [
    "Почему заказчик купит именно решение БАРС?",
    "Разве федералы уже не сделали такую систему: Все регионы сдают им отчетность.",
    "Какая стоимость данного решения сейчас? Какие сроки внедрения?"
]

nurkhametova_correct_answers = {
    "question_1": 0,  # "Семейные права"
    "question_2": 0,  # "Право на справедливый суд (ст. 46 Конституции)"
    
    # Старые ключи для совместимости
    "menu": 0,    # "Семейные права"
    "start": 0,   # "Право на справедливый суд (ст. 46 Конституции)"
}
