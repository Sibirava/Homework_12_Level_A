
def count_even_elements(vector):
    count = 0

    for element in vector:
        if element % 2 == 0:
            count += 1
    return count