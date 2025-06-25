from typing import List
from core.utils.answer_choices import gilmanova_answers


class AnswerValidator:
    
    @staticmethod
    async def check_gilmanova_answer(user_answer: str) -> bool:
        """
        Проверяет, содержит ли ответ пользователя один из ключевых слов из списка gilmanova_answers
        """
        return await AnswerValidator._contains_keywords(user_answer, gilmanova_answers, min_matches=1)
    
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
