def count_minus_elements(vector):
    count = 0

    for element in vector:
        if element < 0:
            count += 1
    return count