def find(list_of_numbers, number):
    low, high = 0, len(list_of_numbers) - 1
    while (high - low >= 0):
        mid = (low + high) // 2
        if number == list_of_numbers[mid]:
            return mid
        if list_of_numbers[mid] < number:
            low = mid + 1
        else:
            high = mid - 1
    raise ValueError(f'{number} cannot be found in list')
