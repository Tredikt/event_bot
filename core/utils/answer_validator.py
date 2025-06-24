from typing import List


class AnswerValidator:
    
    @staticmethod
    async def check_gilmanova_answer(user_answer: str) -> bool:
        keywords: List[str] = [
            "общий язык",
            "глоссарий", 
            "глоссарии",
            "обучали аналитиков",
            "обучение аналитиков",
            "биологические понятия",
            "медицинские понятия",
            "генетиков",
            "ит-термины",
            "it-термины",
            "цифровые решения",
            "единая команда",
            "единую команду",
            "понимать друг друга"
        ]
        
        return await AnswerValidator._contains_keywords(user_answer, keywords, min_matches=1)
    
    @staticmethod
    async def _contains_keywords(text: str, keywords: List[str], min_matches: int = 1) -> bool:
        text_lower: str = text.lower()
        matches: int = 0
        found_keywords: List[str] = []
        
        for keyword in keywords:
            if keyword.lower() in text_lower:
                matches += 1
                found_keywords.append(keyword)
                
        return matches >= min_matches
