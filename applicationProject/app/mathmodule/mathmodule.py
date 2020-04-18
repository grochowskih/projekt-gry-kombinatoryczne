#TODO Funkcje odpowiadające za obliczenia matematyczne


def create_all_series(n, k):
    series = [[a+n*r for n in range(k)] for a in range(1, n+1, 1) for r in range(1, int((n-1)/(k-1))+1, 1)]
    series_copy = [[a+n*r for n in range(k)] for a in range(1, n+1, 1) for r in range(1, int((n-1)/(k-1))+1, 1)]
    for ser in series_copy:
        for el in ser:
            if el > n:
                series.remove(ser)
                break
    return series


