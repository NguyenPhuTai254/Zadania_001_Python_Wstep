def suma_dzielnikow_liczb(a):
    sum = 0
    for i in range(1, a // 2 + 1):
        if a % i == 0:
            sum += i
    return sum

def main():
    n = int(input("Wpisz numer n: "))
    for a in range(1, n + 1):
        b = suma_dzielnikow_liczb(a)
        if suma_dzielnikow_liczb(b) == a:
            print(a, "-", b)

if __name__ == "__main__":
    main()
