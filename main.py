# by Nicholas Keng and Ryan McAlpine

import math
from typing import List

def karatsuba_mult( A, B ) -> List[int]:
    # Base case: single digits
    if len(A) == 1 and len(B) == 1:
        c = int(A[0]) * int(B[0])
        C = get_int_array(c)
        return C

    # Ensure arrays' int values are both <= 1000
    #numA = get_array_int_val(A)
    #numB = get_array_int_val(B)
    #if numA > 1000 or numB > 1000:
    #    return -1

    # Ensure arrays are same length by padding 0's if necessary
    while len(A) < len(B):
        A.insert(0, int(0))
    while len(B) < len(A):
        B.insert(0, int(0))

    # m = middle index
    m = math.ceil(len(A)/2)

    # split arrays
    x1 = A[:m]
    x0 = A[m:]

    y1 = B[:m]
    y0 = B[m:]

    # z0 = x0y0
    # z1 = x1y0 + x0y1 = (x1 + x0)(y1 + y0) - x1y1 - x0y0
    # z2 = x1y1
    # Find z0 and z2 first for use in calculating z1
    z0 = karatsuba_mult(x0, y0)
    z2 = karatsuba_mult(x1, y1)
    z1 = karatsuba_mult(add_arrays(x1, x0), add_arrays(y1, y0)) # = (x1 + x0)(y1 + y0)
    z1 = subtract_arrays(z1, z2)    # ... - x1y1 ...
    z1 = subtract_arrays(z1, z0)    # ... - x0y0

    l = len(A)
    m = l - m   # because we index array from left, but digit significance is from right
    # xy = z2(B^2m) + z1(B^m) + z0
    # base 10 --> B = 10
    # return (z2 * math.pow(10, m * 2)) + (z1 * math.pow(10, m)) + z0

    # (z2 * math.pow(10, m * 2))
    for i in range(m*2):
        z2.append(int(0))
    # (z1 * math.pow(10, m))
    for i in range(m):
        z1.append(int(0))

    # z2 + z1 + z0
    return add_arrays( add_arrays(z2, z1), z0 )

def exp( A, B ) -> List[int]:
    if get_array_int_val(A) < 0 or get_array_int_val(B) < 0 or get_array_int_val(A) > 1000 or get_array_int_val(B) > 1000:
        print( "Invalid input\n" )
        return [0]

    if get_array_int_val(B) == 0:
        return [1]

    C = []

    if (get_array_int_val(B) % 2) == 0:
        C = C + exp(A, halve_array(B))
        return karatsuba_mult( C, C )

    z = [1]
    C = C + exp(A, halve_array(subtract_arrays(B, z)))
    C = karatsuba_mult( C, C )
    C = karatsuba_mult( A, C )
    return C

def add_arrays(A, B) -> List[int]:
    # Ensure the arrays are of even length by padding 0's if necessary
    while len(A) < len(B):
        A.insert(0, int(0))
    while len(B) < len(A):
        B.insert(0, int(0))

    C = []  # return value is also an array
    i = len(A) - 1  # start with least-significant digit
    carry = 0
    while i >= 0:   # for each digit in arrays
        c = A[i] + B[i]
        c += carry
        if c > 9:   # if c is 2 digits, carry the extra
            carry = c / 10
            c = c % 10
        else:
            carry = 0
        C.insert(0, int(c))
        i -= 1

    # Account for possible C of length len(A)+1 (e.g. 5 + 5 = 10)
    if carry != 0:
        C.insert(0, int(carry))

    return C

def subtract_arrays(A, B) -> List[int]:  # Only works for A <= B
    # Ensure the arrays are of even length by padding 0's if necessary
    while len(A) < len(B):
        A.insert(0, int(0))
    while len(B) < len(A):
        B.insert(0, int(0))

    C = []  # return value is also an array
    i = len(A) - 1  # start with least-significant digit
    while i >= 0:   # for each digit in arrays
        c = A[i] - B[i]
        if c < 0:
            A[i-1] -= 1
            c = 10 + c
        C.insert(0, int(c))
        i -= 1

    return C

def halve_array( A ) -> List[int]:
    Q = []  # Quotient in array
    i = 1
    d = [int(A[0])]
    while i <= len(A):
        if get_array_int_val(d) / 2 >= 1:
            Q.append( math.floor(get_array_int_val(d) / 2) )
            d = [int(get_array_int_val(d) % 2)]
        else:
            if i == len(A) and get_array_int_val(d) == 0:
                return Q
            elif i == len(A) and get_array_int_val(d) != 0:
                # We are only dividing even numbers, so should never reach this
                print("Halved array with remainder ", get_array_int_val(d), "\n")
            else:
                d.append(int(A[i]))
                #if A[i] == 0:
                if get_array_int_val(d) == 0:
                    Q.append(int(0))

            i += 1

    return Q

def get_array_int_val( A ):
    num = 0
    numstr = ""
    for c in A:
        numstr += str(c)
    if numstr != "":
        num += int(numstr)
    return int(num)

def get_int_array( num: int ):
    A = [int(n) for n in str(num)]
    return A

def get_array_str( A ):
    padRemoved = 0
    S = ""

    for n in A:
        if n != 0:
            padRemoved = 1
        if padRemoved == 1:
            S += str(n)

    if len(S) == 0:
        S += "0"

    return S

def main():
    # Get input values
    num1 = int(input("> Enter a number A (<= 1000):\n"))
    num2 = int(input("> Enter a number B (<= 1000):\n"))

    # Store values as digit arrays
    A = get_int_array(num1)
    B = get_int_array(num2)

    choice = input("> Enter '1' for multiplication, '2' for exponentiation, or '3' to quit:\n")

    if choice == '1':
        # Output result of multiplication
        print("\nA * B = ", get_array_str(karatsuba_mult(A, B)), "\n")
    elif choice == '2':
        # Output result of exponentiation
        print("\nA ^ B = ", get_array_str(exp(A, B)), "\n")
    elif choice == '3':
        quit()
    else:
        print("\nInvalid selection. Please choose task 1, 2, or 3.\n")
if __name__ == "__main__":
    while True:
        main()