def josephus(n, k):
    if n == 1:
        return 0
    else:
        return (josephus(n - 1, k) + k) % n

def main():
    n = int(input("Podaj liczbę żołnierzy: "))
    k = int(input("Wprowadź liczbę przeskoków: "))

    safe_position = josephus(n, k) + 1
    print("Bezpieczna lokalizacja:", safe_position)

if __name__ == "__main__":
    main()
