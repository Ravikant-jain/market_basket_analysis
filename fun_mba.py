#fun_mba stands for Functions for Market Basket analysis

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


def find_common_subsets(main_list, n): # This function returns mega set by combining 2 smaller sets and have atleast one element common
    common_subsets = []
    
    for subset1, subset2 in crazy(main_list, 2):
        # print(subset1, subset2)
        common_elements = set(subset1) & set(subset2)
        if len(common_elements) > 0:
            combined_subset = sorted(set(subset1) | set(subset2))
            if len(combined_subset) == n and combined_subset not in common_subsets :
                common_subsets.append(combined_subset)
    if len(common_subsets)==0:
        return None
    else:
        return common_subsets

def dekhao(fino,ms,transactions): # This function prints the associations rules by taking final list as input.
    print(f'Association Rules are:\n')
    for hid in fino:
        nfino=[]
        numerator=[]
        rhs=[]
        Lconfv=[]
        Rconfv=[]
        for i2 in hid:
            nfino.append(i2)
            numerator.append(ms)
        lhs=crazy(nfino,2)

        for i3 in lhs:
            for i4 in hid:
                if i4 in i3:
                    pass
                else:
                    rhs.append([i4])

        Ldenominator=kount(transactions,lhs)
        Rdenominator=kount(transactions,rhs)

        for i in range(len(hid)):
            Lconfv.append((round(((numerator[i]/Ldenominator[i])*100),2)))
            Rconfv.append((round(((numerator[i]/Rdenominator[i])*100),2)))

        for indxx,i5 in enumerate(lhs):
            print(f' {i5[0]} and {i5[1]} supports {rhs[indxx][0]} with confidence level {Lconfv[indxx]} ')

        for indxx,i5 in enumerate(lhs):
            print(f' {rhs[indxx][0]} supports {i5[0]} and {i5[1]} with confidence level {Rconfv[indxx]} ')
            
def showtime(alle,ms,transactions):
    sw=True
    n=0
    primealle=alle.copy()
    while sw:
        n=n+1
        if n==1:
            primealle=elip(ms,primealle,kount(transactions,crazy(primealle,n)))
            n=n+1
        if n==2:
            primealle=elip(ms,crazy(primealle,n),kount(transactions,crazy(primealle,n)))
            n=n+1
        if n>=3 and find_common_subsets(primealle,n)is not None:

            # print('-->',find_common_subsets(primealle,n))
            primealle=elip(ms,find_common_subsets(primealle,n),kount(transactions,find_common_subsets(primealle,n)))
        # sw=False
        n=n+1
        # print('this is ',n)
    # print('Ended')
        if find_common_subsets(primealle,n)is None:
            sw=False
            dekhao(primealle,ms,transactions)