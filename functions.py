class trans:
    def __init__(self,amt,items):
        self.amt = amt
        self.items = items

def crazy(input_list, n):
    if n == 0:
        return [[]]  # Base case: Return a list with an empty sublist

    if not input_list:
        return []  # Base case: Return an empty list if input_list is empty

    first_element = input_list[0]
    rest_of_list = input_list[1:]

    combinations_with_first = crazy(rest_of_list, n - 1)
    combinations_without_first = crazy(rest_of_list, n)

    result = []
    for combo in combinations_with_first:
        result.append([first_element] + combo)
    result.extend(combinations_without_first)
    
    return result
