class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Если nums1 больше, чем nums2, меняем их местами.
        # Это позволяет упростить дальнейшие вычисления.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        
        # Положение разделения массивов
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        median = 0.0
        
        # Основной цикл поиска
        while imin <= imax:
            # Пополам разделяем массив nums1
            i = (imin + imax) // 2
            # Вычисляем позицию разделения в nums2
            j = half_len - i

            # Проверяем элементы слева от разделения в nums1 и nums2
            # Если элемент в nums1 меньше предыдущего элемента в nums2, увеличиваем i
            if i < m and nums1[i] < nums2[j-1]:
                imin = i + 1
            # Если элемент в nums1 больше следующего элемента в nums2, уменьшаем i
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                # Найдена правильная позиция разделения
                max_of_left = 0
                # Находим максимальное значение слева от разделения
                if i == 0: max_of_left = nums2[j-1]
                elif j == 0: max_of_left = nums1[i-1]
                else: max_of_left = max(nums1[i-1], nums2[j-1])

                # Если общее количество элементов нечетное, возвращаем максимум из левой части
                if (m + n) % 2 == 1:
                    return max_of_left

                min_of_right = 0
                # Находим минимальное значение справа от разделения
                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                # Если общее количество элементов четное, возвращаем среднее значение
                return (max_of_left + min_of_right) / 2.0

        return 0.0
