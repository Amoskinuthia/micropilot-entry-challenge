from array import*
A = array('i', [])
number_of_zeros = array('i', []) 
n = int(input('please enter the length of the array :'))
def countZeros():
    for items in range(n):
        x = int(input('please enter the next number :'))
        A.append(x)
    for i in A:
            if i==0:
                number_of_zeros.append(i)
    print(len(number_of_zeros))
countZeros()