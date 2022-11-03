import Task02
import Task04
def count_odd_elements(vector):
    result = (len(vector) - Task02.count_even_elements(vector)
              - Task04.count_zero_elements_vector(vector))
    return result