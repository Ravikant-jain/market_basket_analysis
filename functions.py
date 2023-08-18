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


def kount(transactions,lis): # This returns the count of the element in all the transactions
    
    nlis=[0 for i in range(len(lis))]
    for tr in transactions:
        tl=cegg(tr.items,lis)
        for indexx,ind in enumerate(tl):
            if ind:
                # print('ind: ',indexx)
                nlis[indexx] +=1
    return nlis

def elip(ms,wholelist,clist): # This returns the list with elements that surpasses the minimum support
    for indx , i in enumerate(clist):
        # print(f'indx: {indx} : i ki value: {i} :item {wholelist[indx]}')
        if i < ms:
            # print(f'Item {wholelist[indx]} is removed from the list as it has count {i}. ')
            print(f'{wholelist[indx]} with count {i} is removed. ')
            wholelist[indx]='*'
    while '*' in wholelist:
        wholelist.remove('*')
    print(f'Updated list is {wholelist}\n ')
    return wholelist