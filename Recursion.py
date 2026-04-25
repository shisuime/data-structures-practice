def find_sum(num):
    if num == 1:
        return 1

    return num + find_sum(num-1)

def fib(n):
    if n == 0 or n == 1:
        return n
    
    return fib(n-1) + fib(n-2)
    
def sum_list(list):
    
    if  len(list) == 1:
        return list[0]
    
    return list[0] + sum_list(list[1:])

def sum_nested_list(x):
    total = 0

    for element in x:
        if type(element) == type([]):
            total= total + sum_nested_list(element)

        else:
            total= total + element

    return total   


def facto(x):
    if x == 0 or x == 1:
        return x
    
    return x * facto(x-1)



#  n+(n-2)+(n-4)... (until n-x =< 0)

def sum_series(n):
    if n <=0:
        return 0
    
    return n + sum_series(n-2)


def power(x,y):
    if x ==0 or y == 0:
        return 0
    elif y == 1:
        return x
    
    return x * power(x,y-1)

if __name__ == '__main__':
    # print(find_sum(10))
    # print(fib(10))
    # print(sum_list([1,2,3,4,5,6,7,8,9,10]))
    # print(sum_nested_list([1, 2, [3,4], [5,6]]))
    # print(facto(10))
    # print(sum_series(10))
    print(power(3,2))