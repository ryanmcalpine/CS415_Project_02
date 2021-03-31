
def karatsuba_mult( A, B ):
    if len(A) > 1000 or len(B) > 1000:
        return -1;

    return 0;

def main():
    num1 = input("> Enter a number A (<= 1000) to multiply using the Karatsuba Algorithm:\n")
    num2 = input("> Enter a number B (<= 1000) to multiply using the Karatsuba Algorithm:\n")
    A = [int(n) for n in str(num1)];
    B = [int(n) for n in str(num2)];
    karatsuba_mult(A, B);

if __name__ == "__main__":
    while True:
        main()