"""
    In this programming assignment you will implement one or more of the integer multiplication algorithms described in lecture.
    To get the most out of this assignment, your program should restrict itself to multiplying only pairs of single-digit numbers.
    You can implement the grade-school algorithm if you want, but to get the most out of the assignment you'll want to implement
 recursive integer multiplication and/or Karatsuba's algorithm.
    So: what's the product of the following two 64-digit numbers?
    3141592653589793238462643383279502884197169399375105820974944592
    2718281828459045235360287471352662497757247093699959574966967627

"""
import time

def karatsuba(x, y):
    a_string = str(x)
    b_string = str(y)
    if x < 10 or y < 10:
        return x* y

    max_length = max(len(a_string), len(b_string))
    split_length = max_length // 2

    # split string
    a, b = int(a_string[:-split_length]), int(a_string[-split_length:])
    c, d = int(b_string[:-split_length]), int(b_string[-split_length:])

    # print(a)
    # print(b)
    # print(c)
    # print(d)

    # z0 = a * c
    # z1 = b * d
    # z2 = (a + b) * (c + d)

    # print(z0)
    # print(z1)
    # print(z2)

    # spliting until the 2 digits multiplication
    z0 = karatsuba(a, c)
    z1 = karatsuba(b, d)
    z2 = karatsuba((a +b), (c + d))

    return (z0 * 10**(2*split_length)) + ((z2 - z1 - z0) * 10**split_length) + z1


if __name__ == '__main__':
    
    a = 3141592653589793238462643383279502884197169399375105820974944592
    b = 2718281828459045235360287471352662497757247093699959574966967627

    start = time.time()
    print(karatsuba(a, b))
    print('Total time: %f' % (time.time() - start))

    # 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
    
