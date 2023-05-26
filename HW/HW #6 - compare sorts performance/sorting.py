from datetime import datetime
import pprint 
pp = pprint.PrettyPrinter(width=55)

class SortStatistics:
    def __init__(self, array):
        self.comparisons = 0
        self.swaps = 0
        self.execution_time = None
        self.sorted_array = None
        self.original_array = array[1:]
        self.title = array[0]
        self.stats = {}

    def compare(self):
        self.comparisons += 1


    def swap(self):
        self.swaps += 1


    def original_array(self):

        return (self.title, self.original_array)
    
    def bubble_sort(self, array):
        n = len(array)
        for i in range(n):
            
            for j in range(0, n-i-1):

                # count comparisons
                self.compare()
                if array[j] > array[j+1]:
                    # swap the numbers
                    array[j], array[j+1] = array[j+1], array[j]
                    self.swap()
        return array

    def quick_sort(self, array):

        if len(array) <= 1:
            return array
        else:
            # take pivot at middle
            pivot_index = len(array) // 2
            pivot = array[pivot_index]

            # divide array into two by the pivot
            smaller = []
            larger = []
            for i in range(len(array)):
                if i != pivot_index:
                # count number of comparisons
                    self.compare()
                    if array[i] <= pivot:
                        smaller.append(array[i])
                    else:
                        larger.append(array[i])
            # sort what's on the left (smaller numbers)
            sorted_left = self.quick_sort(smaller)

            # sort what's on the right (larger numbers)
            sorted_right = self.quick_sort(larger)

            # concatenate 
            sorted_arr = sorted_left + [pivot] + sorted_right

            # count number of swaps
            self.swaps += len(sorted_left) + len(sorted_right)

            return sorted_arr

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                self.compare()
                arr[j+1] = arr[j]
                self.swap()
                j -= 1
            arr[j+1] = key
        return arr


    def exec_sort(self, func, arr):
        self.sorted = arr.copy()
        self.comparisons = 0
        self.swaps = 0
        start_time = datetime.now()
        sorted_arr = func(self.sorted)
        self.sorted_array = sorted_arr
        end_time = datetime.now()
        self.execution_time = (end_time - start_time).total_seconds() * 1000
        self.stats.update({"Title": self.title,
                      "original Array": self.original_array,
                      "comparisons": self.comparisons,
                      "swaps": self.swaps,
                      "execution time (sec)": self.execution_time,
                      "sorted array": self.sorted_array})
        return self.stats
    
    def print_all_stats(self):
        pprint.pprint(self.stats, compact=True)
        print('==============================\n')


    def exec_all_sorts(self):
        print("Applying Bubble sort...")
        print('------------------------')
        self.exec_sort(self.bubble_sort, self.original_array)
        self.print_all_stats()

        print("Applying Quick sort...")
        print('------------------------')
        self.exec_sort(self.quick_sort, self.original_array)
        self.print_all_stats()

        print("Applying Insetion sort...")
        print('------------------------')
        self.exec_sort(self.insertion_sort, self.original_array)
        self.print_all_stats()