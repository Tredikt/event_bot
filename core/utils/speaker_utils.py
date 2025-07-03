def get_speaker_display_name(speaker_name: str) -> str:
    """Возвращает отображаемое имя спикера"""
    
    name_mapping = {
        "belozertseva": "Белозерцева",
        "gavrikov": "Гавриков", 
        "zabegaev": "Забегаев",
        "mendubaev": "Мендубаев",
        "nurhametova": "Нурхаметова",
        "sadriev": "Садриев",
        "horoshutina": "Хорошутина",
        "gilmanova": "Гильманова"
    }
    
    return name_mapping.get(speaker_name, speaker_name) 