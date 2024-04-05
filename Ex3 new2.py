def main():
    n = int(input("Podaj liczbę żołnierzy: "))
    k = int(input("Wprowadź liczbę przeskoków: "))

    safe_position = 0
    for i in range(2, n + 1):
        safe_position = (safe_position + k) % i
    safe_position += 1

    print("Bezpieczna lokalizacja:", safe_position)

if __name__ == "__main__":
    main()