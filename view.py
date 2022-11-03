import Vector
import Task01
import Task02
import Task03
import Task04
import Task06
import Task05

def main():

    vector = Vector.random_vector_elements()

    msg = (f"In vector {vector}: \n"
           f"1)There are {Task01.count_non_zero_elements_vector(vector)} non zero elements \n"
           f"and {Task04.count_zero_elements_vector(vector)} zero elements\n"
           f"2)There are {Task02.count_even_elements(vector)} even numbers\n"
           f"and {Task05.count_odd_elements(vector)} odd numbers \n"
           f"3)There are {Task06.count_minus_elements(vector)} minus numbers\n "
           f"and {Task03.count_plus_element_vector(vector)} plus numbers \n")
    print(msg)
main()