import math


def karatsuba_mult( A, B ):
    if len(A) == 1 and len(B) == 1:
        return A[0] * B[0]

    num1 = ""
    for c in A:
        num1 += str(c)
    num2 = ""
    for c in B:
        num2 += str(c)
    if int(num1) > 1000 or int(num2) > 1000:
        return -1

    while len(A) < len(B):
        A.insert(0, 0)
    while len(B) < len(A):
        B.insert(0, 0)

    m1 = math.floor(len(A)//2)
    m2 = math.floor(len(B)//2)

    x1 = A[:m1]
    x0 = A[m1:] if len(A) % 2 == 0 else A[m1+1:]

    y1 = B[:m2]
    y0 = B[m2:] if len(B) % 2 == 0 else B[m2 + 1:]

    # z0 = x0y0
    # z1 = x1y0 + x0y1 = (x1 + x0)(y1 + y0) - x1y1 - x0y0
    # z2 = x1y1
    # Find z0 and z2 first for use in calculating z1
    z0 = karatsuba_mult(x0, y0)
    z2 = karatsuba_mult(x1, y1)
    z1 = karatsuba_mult(add_arrays(x1, x0), add_arrays(y1, y0)) - z2 - z0

    return (z2 * math.pow(10, m2 * 2)) + ((z1 - z2 - z0) * math.pow(10, m2)) + z0

def add_arrays(A, B):
    while len(A) < len(B):
        A.insert(0, 0)
    while len(B) < len(A):
        B.insert(0, 0)

    C = []
    i = 0
    carry = 0
    for n in A:
        c = A[i] + B[i]
        c += carry
        if c > 9:
            carry = c / 10
            c = c % 10
        else:
            carry = 0
        C.insert(0, c)
        i += 1

    return C

def main():
    num1 = input("> Enter a number A (<= 1000) to multiply using the Karatsuba Algorithm:\n")
    num2 = input("> Enter a number B (<= 1000) to multiply using the Karatsuba Algorithm:\n")
    A = [int(n) for n in str(num1)]
    B = [int(n) for n in str(num2)]
    print(karatsuba_mult(A, B), "\n")

if __name__ == "__main__":
    while True:
        main()