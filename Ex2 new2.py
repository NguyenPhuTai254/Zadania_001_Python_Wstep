def main():
    n = int(input("Wpisz numer n: "))
    
    for a in range(1, n + 1):
        sum_a = 0
        for i in range(1, a // 2 + 1):
            if a % i == 0:
                sum_a += i
        
        b = sum_a
        
        sum_b = 0
        for i in range(1, b // 2 + 1):
            if b % i == 0:
                sum_b += i
        
        if sum_b == a:
            print(a, "-", b)

if __name__ == "__main__":
    main()