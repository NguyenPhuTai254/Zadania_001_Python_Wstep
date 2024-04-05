class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

def compare_dates(d1, d2):
    if d1.year != d2.year:
        return d1.year < d2.year
    if d1.month != d2.month:
        return d1.month < d2.month
    return d1.day < d2.day

def sort_dates(dates):
    for i in range(len(dates) - 1):
        min_index = i
        for j in range(i + 1, len(dates)):
            if compare_dates(dates[j], dates[min_index]):
                min_index = j
        if min_index != i:
            dates[i], dates[min_index] = dates[min_index], dates[i]

def print_dates(dates):
    for date in dates:
        print(f"{date.day}/{date.month}/{date.year}")

def main():
    n = int(input("Wpisz liczbę dni do ustalenia: "))
    dates = []

    for i in range(n):
        day, month, year = map(int, input(f"Wprowadź dzień, miesiąc i rok dla danego dnia {i + 1} (d m yyyy): ").split())
        dates.append(Date(day, month, year))

    sort_dates(dates)
    print("\nDaty są posortowane rosnąco:")
    print_dates(dates)

if __name__ == "__main__":
    main()
