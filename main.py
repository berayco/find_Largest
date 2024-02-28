def find_largest_element(array):
    if not array:
        return None  

    max_element = array[0]

    for element in array:
        if element > max_element:
            max_element = element

    return max_element



numbers = [3, 6, 2, 8, 4, 10]
largest = find_largest_element(numbers)
print("Dizideki en büyük eleman:", largest)