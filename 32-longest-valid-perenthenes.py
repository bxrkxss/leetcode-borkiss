class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Инициализация двух счетчиков для открытых и закрытых скобок.
        left, right, maxlen = 0, 0, 0

        # Проход слева направо.
        for i in range(len(s)):
            if s[i] == '(':
                left += 1  # Увеличиваем счетчик открытых скобок.
            else:
                right += 1  # Увеличиваем счетчик закрытых скобок.
            if left == right:
                # Если количество открытых и закрытых скобок одинаковое, обновляем максимальную длину.
                maxlen = max(maxlen, 2*right)
            elif right > left:
                # Сбрасываем счетчики.
                left, right = 0, 0

        # Сбрасываем счетчики.
        left, right = 0, 0
        
        # Проход справа налево.
        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlen = max(maxlen, 2*left)
            elif left > right:
                left, right = 0, 0
                
        return maxlen
