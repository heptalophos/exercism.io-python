def find(list_of_numbers, number):
    min, max = 0, len(list_of_numbers) - 1
    while (max - min >= 0):
        mid = (min + max) >> 1
        if number == list_of_numbers[mid]:
            return mid
        if list_of_numbers[mid] < number:
            min = mid + 1
        else:
            max = mid - 1
    raise ValueError('value not in array')
