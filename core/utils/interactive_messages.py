from core.utils.mendubaev_texts import mendubaev_texts

interactive_messages = {
    "admakin": {
        "end": "Как вам это выступление? / материалы спикера в easy (ссылка)"
    },
    "balukov": {
        "end": "Как вам это выступление? / материалы спикера в easy (ссылка)"
    },
    "belozertseva": {
        "start": "Чтобы начать интерактив Белозёрцевой, нажмите кнопку внизу ⬇",
        "end": "Как вам это выступление? / материалы спикера в <a href='https://t.me/Easyontelegram_bot?startapp=courses_bc69287c-b6e4-4e85-804c-628b63778891'>easy</a>"
    },
    "gavrikov": {
        "start": "Ну что же, начнём?",
        "end": "Как вам это выступление? / материалы спикера в easy (ссылка)"
    },
    "zabegaev": {
        "start": "Чтобы начать интерактив Забегаева, нажмите кнопку внизу ⬇",
        "end": "Как вам это выступление? / материалы спикера в easy (ссылка)"
    },
    "mendubaev": {
        "end": "Как вам это выступление? / материалы спикера в easy (ссылка)"
    },
    "nurhametova": {
        "start": "Чтобы начать интерактив Нурхаметовой, нажмите кнопку внизу ⬇",
        "end": "Как вам это выступление? / материалы спикера в easy (ссылка)"
    },
    "sadriev": {
        "start": "Чтобы начать интерактив Садриева, нажмите кнопку внизу ⬇",
        "end": "Как вам это выступление? / материалы спикера в easy (ссылка)"
    },
    "horoshutina": {
        "start": "Соберите правильную цепочку «шагов продаж»:",
        "end": "Как вам это выступление? / материалы спикера в easy (ссылка)"
    },
    "gilmanova": {
        "end": "Как вам это выступление? / материалы спикера в easy (ссылка)"
    }
}

def get_interactive_message(speaker_name: str, message_type: str) -> str:
    """Получает сообщение для интерактива спикера"""
    if speaker_name in interactive_messages:
        return interactive_messages[speaker_name].get(message_type, f"Сообщение для {speaker_name}")
    if message_type == "start":
        return f"🔴 Начинается интерактив от {speaker_name}!"
    else:
        return f"✅ {speaker_name} завершил(а) выступление." 