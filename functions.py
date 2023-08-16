class trans:
    def __init__(self,amt,items):
        self.amt = amt
        self.items = items

def crazy(input_list, n): # This Returns all the possible subsets with n elements that can be made from the main set
    if n == 0:
        return [[]]  

    if not input_list:
        return [] 

    first_element = input_list[0]
    rest_of_list = input_list[1:]

    combinations_with_first = crazy(rest_of_list, n - 1)
    combinations_without_first = crazy(rest_of_list, n)

    result = []
    for combo in combinations_with_first:
        result.append([first_element] + combo)
    result.extend(combinations_without_first)
    
    return result

def cegg(mss,ss): # This returns a boolean list generated with the condition: if the the elements of list ss is in list mss
    rt=[]
    # print(type(ss))

    for ele in ss:
        x=0
        # print(ele)
        for i in ele:
            if i in mss:
                x+=1
                
        if x==len(ele):
            rt.append(True)
        else:
            rt.append(False)
    return rt