
from sorting import SortStatistics


ten_numbers_in_almost_sorted_order = ["10 almost sorted numbers", 15, 20, 25, 30, 27, 35, 40, 45, 50, 55]
ten_numbers_in_random_order = ["10 random numbers", 23, 1, 67, 99, 12, 55, 73, 8, 45, 20]
ten_numbers_in_almost_sorted_reversed_order = ["10 almost sorted reversed numbers", 10, 9, 8, 2, 7, 6, 3, 1, 4]

thirty_numbers_in_almost_sorted_order = ["30 almost sorted numbers", 1, 2, 3, 4, 5, 18, 14, 21, 9, 10, 11, 12, 13, 6, 7, 8, 29, 27, 23, 19, 20, 15, 16, 17, 22, 24, 25, 26, 30, 28]
thirty_numbers_in_random_order = ["30 random numbers", 16, 28, 7, 24, 29, 22, 14, 3, 15, 20, 23, 26, 2, 30, 11, 17, 27, 18, 9, 1, 19, 25, 8, 12, 10, 6, 5, 13, 21, 4]
thirty_numbers_in_almost_sorted_reversed_order = ["30 almost reversed numbers", 28, 30, 29, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 15, 16, 14, 13, 12, 11, 10, 9, 8, 7, 6, 4, 5, 3, 2, 1]

fifty_numbers_in_almost_sorted_order = ["50 almost sorted numbers", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 25, 24, 20, 21, 22, 23, 16, 17, 18, 19, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 28, 29, 30, 45, 42, 44, 50, 46, 47, 48, 49, 41, 26, 43]
fifty_numbers_in_random_order = ["50 random numbers",16, 45, 32, 12, 39, 27, 38, 1, 23, 49, 29, 6, 8, 33, 46, 3, 11, 7, 28, 10, 48, 37, 40, 26, 43, 17, 2, 22, 18, 25, 21, 36, 50, 4, 14, 42, 47, 31, 19, 24, 5, 20, 13, 41, 30, 34, 9, 15, 44, 35]
fifty_numbers_in_almost_sorted_reversed_order = ["50 almost sorted reversed numbers", 48, 50, 49, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 35, 36, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 19, 20, 18, 17, 16, 15, 14, 13, 12, 11, 9, 10, 8, 7, 6, 5, 4, 3, 2, 1]


ten_array_groups = [ten_numbers_in_almost_sorted_order, ten_numbers_in_random_order, ten_numbers_in_almost_sorted_reversed_order]
thirty_array_groups = [thirty_numbers_in_almost_sorted_order, thirty_numbers_in_random_order, thirty_numbers_in_almost_sorted_reversed_order]
fifty_array_groups = [fifty_numbers_in_almost_sorted_order, fifty_numbers_in_random_order, fifty_numbers_in_almost_sorted_reversed_order]

print("Groups with 10 numbers:")
print("=======================")
for group in ten_array_groups:

    ss = SortStatistics(group)
    ss.exec_all_sorts()

print("Groups with 30 numbers:")
print("=======================")
for group in thirty_array_groups:

    ss = SortStatistics(group)
    ss.exec_all_sorts()

print("Groups with 50 numbers:")
print("=======================")
for group in fifty_array_groups:

    ss = SortStatistics(group)
    ss.exec_all_sorts()


