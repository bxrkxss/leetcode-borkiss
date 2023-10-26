class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        
        # Создаем словарь для подсчета слов
        wordCount = Counter(words)
        wordLen, numWords = len(words[0]), len(words)
        concatLen = wordLen * numWords
        result = []
        
        # Перебираем все возможные начальные позиции в строке s
        for i in range(len(s) - concatLen + 1):
            # Вырезаем подстроку из s
            sub = s[i:i+concatLen]
            # Разбиваем подстроку на слова
            subWords = [sub[j:j+wordLen] for j in range(0, concatLen, wordLen)]
            # Проверяем, соответствует ли подстрока перестановке слов
            if Counter(subWords) == wordCount:
                result.append(i)
        
        return result
