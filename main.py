import math

def karatsuba_mult( A, B ):
    # Base case: single digits
    if len(A) == 1 and len(B) == 1:
        return A[0] * B[0]

    # Ensure arrays' int values are both <= 1000
    numA = get_array_int_val(A)
    numB = get_array_int_val(B)
    if numA > 1000 or numB > 1000:
        return -1

    # Ensure arrays are same length by padding 0's if necessary
    while len(A) < len(B):
        A.insert(0, 0)
    while len(B) < len(A):
        B.insert(0, 0)

    # m = middle index
    m = math.floor(len(A)//2)

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
    z1 = karatsuba_mult(add_arrays(x1, x0), add_arrays(y1, y0)) - z2 - z0

    l = len(A)
    m = l - m   # because we index array from left, but digit significance is from right
    # xy = z2(B^2m) + z1(B^m) + z0
    # base 10 --> B = 10
    return (z2 * math.pow(10, m * 2)) + (z1 * math.pow(10, m)) + z0

def add_arrays(A, B):
    # Ensure the arrays are of even length by padding 0's if necessary
    while len(A) < len(B):
        A.insert(0, 0)
    while len(B) < len(A):
        B.insert(0, 0)

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

def get_array_int_val( A ):
    num = 0
    numstr = ""
    for c in A:
        numstr += str(c)
    if numstr != "":
        num += int(numstr)
    return num

def main():
    # Get input values
    num1 = input("> Enter a number A (<= 1000) to multiply using the Karatsuba Algorithm:\n")
    num2 = input("> Enter a number B (<= 1000) to multiply using the Karatsuba Algorithm:\n")

    # Store values as digit arrays
    A = [int(n) for n in str(num1)]
    B = [int(n) for n in str(num2)]

    # Output result
    print("\n = ", int(karatsuba_mult(A, B)), "\n")

if __name__ == "__main__":
    while True:
        main()