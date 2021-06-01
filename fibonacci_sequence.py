def first_n_fibonacci(n):
    prev_num = 0
    curr_num = 1
    count = 2

    print(prev_num)
    print(curr_num)

    while count < n:
        next_num = curr_num + prev_num
        print(next_num)
        prev_num = curr_num
        curr_num = next_num
        count += 1
m = 7
print('First %d Fibonacci numbers' % m)
first_n_fibonacci(m)

def below_x_fibonacci(x):
    prev_num = 0
    curr_num = 1

    if curr_num < x:
        print(prev_num)
        print(curr_num)
    elif prev_num < x:
        print(prev_num)
    
    while curr_num + prev_num < x:
        next_num = curr_num + prev_num
        print(next_num)
        prev_num = curr_num
        curr_num = next_num
print()

y = 40
print('Fibonacci numbers below %d' % y)
below_x_fibonacci(y)