def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert


def partition(arr, left, right):
    i = (left - 1)
    key = arr[right]

    for j in range(left, right):
        if arr[j] < key:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quick_sort(arr, left, right):
    if left < right:
        key_index = partition(arr, left, right)
        quick_sort(arr, left, key_index - 1)
        quick_sort(arr, key_index + 1, right)


library_num = [124, 235, 456, 123, 756, 476, 285, 998, 379, 108]
print("Initial array:", library_num)
quick_sort(library_num, 0, len(library_num) - 1)
print("Sorted array:", library_num)

array_len = int(input("Enter the number of elements: "))
array = []
for n in range(array_len):
    array.append(int(input("Enter the number {}: ".format(n + 1))))

sort_types = {
    1: bubble_sort,
    2: selection_sort,
    3: insertion_sort,
    4: quick_sort
}

sort_type = int(input("Enter sort type:\n"
                      "1 - Outputting the result using Bubble sort\n"
                      "2 - Outputting the result using Sort by selection method\n"
                      "3 - Outputting the result using Insert sort\n"
                      "4 - Outputting the result using Quick sort\n"))

if sort_type == 4:
    sort_types[sort_type](array, 0, len(array) - 1)
else:
    sort_types[sort_type](array)

print(array)
