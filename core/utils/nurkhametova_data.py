explanations = {
    "question_1": "Cемейные права включают право родителей и детей на общение и участие в воспитании (ст. 55 Семейного кодекса РФ).",
    "question_2": "Право на справедливый суд — это возможность обжаловать решения государственных органов (ст. 46 Конституции РФ).",
}

# Персонализированные ответы для вопросов
nurkhametova_answers = {
    "question_1": {
        "correct": "<b>Семейные права.</b> В точку 🎯\n<i>Семейные права — это и есть право родителей и детей на общение и участие в воспитании (ст. 55 СК РФ).</i>\n\n🎉 <b>+1 балл.</b> Двигаемся дальше!",
        "incorrect": {
            1: "❌ <b>Не совсем так.</b>\n<i>Гражданские права — это про имущество, сделки, договоры. Здесь речь о воспитании и взаимодействии в семье.</i>",
            2: "❌ <b>Мимо.</b>\n<i>Административные права здесь ни при чём. Это совсем другая область — речь идёт именно о семейном кодексе.</i>"
        }
    },
    "question_2": {
        "correct": "🟢 Абсолютно верно\n\nЭто право гарантирует каждому возможность обжаловать действия госорганов (ст. 46 Конституции РФ).\n\n🎯 <b>+1 балл.</b> Отличная работа!",
        "incorrect": {
            1: "❌ <b>Не туда.</b>\n\n<i>Гражданское право — это другая плоскость.</i> <b>Здесь речь идёт о правах, закреплённых в Конституции.</b>",
            2: "❌ <b>Совсем не то.</b>\n\n<i>Образование тут ни при чём. <b>Нарушено именно право на судебную защиту</b> — это фундаментальный пункт.</i>"
        }
    }
}

buttons_1 = {
        "Cемейные права": "nurkhametova_question_1_0",
        "Гражданские права": "nurkhametova_question_1_1", 
        "Административные права": "nurkhametova_question_1_2"
    }

buttons_2 = {
    "Социальное право": "nurkhametova_question_2_0",
    "Гражданское право": "nurkhametova_question_2_1",
    "Право на образование": "nurkhametova_question_2_2"
}