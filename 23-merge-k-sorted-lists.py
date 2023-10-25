# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        # узел содержит значение и ссылку на следующий узел
        self.val = val
        self.next = next

from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Внутренняя функция для слияния двух отсортированных связных списков.
        def mergeTwoLists(l1, l2):
            # Если один из списков пуст, вернем другой список.
            if not l1:
                return l2
            if not l2:
                return l1

            # Сравниваем значения первых узлов каждого списка.
            # Меньший узел становится следующим в результирующем списке.
            if l1.val < l2.val:
                l1.next = mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = mergeTwoLists(l1, l2.next)
                return l2
        
        # Если исходный список списков пуст, возвращаем None.
        if not lists:
            return None

        # Получаем длину исходного списка списков.
        length = len(lists)
        # Инициализируем интервал, который будет использоваться для слияния списков.
        interval = 1

        # Цикл продолжается, пока интервал меньше длины исходного списка списков.
        # На каждой итерации удваиваем интервал.
        while interval < length:
            # Сливаем списки попарно, используя заданный интервал.
            for i in range(0, length - interval, interval*2):
                lists[i] = mergeTwoLists(lists[i], lists[i+interval])
            interval *= 2

        # После всех операций слияния результат будет в первом списке.
        return lists[0]
