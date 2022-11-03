import Task01
def count_zero_elements_vector(vector):
    result = len(vector) - Task01.count_non_zero_elements_vector(vector)
    return result