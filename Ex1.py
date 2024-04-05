def sangnguyento():
    b = [1] * 1000001  
    b[0] = b[1] = 0  
    for i in range(2, 1001):
        if b[i]:  
            for j in range(i * i, 1000001, i):  
                b[j] = 0  
    return b
"""Do wybierania liczb pierwszych używam algorytmu przesiewania liczb pierwszych."""
def main():
    b = sangnguyento()
    n = int(input())
    for i in range(n + 1):
        if b[i]:
            print(i, end=" ")


if __name__ == "__main__":
    main()
