#TODO Funkcje odpowiadające za obliczenia matematyczne


def create_all_series(n, k):
    series = [[a+n*r for n in range(k)] for a in range(1, n+1, 1) for r in range(1, int((n-1)/(k-1))+1, 1)]
    series_copy = series.copy()
    for ser in series_copy:
        for el in ser:
            if el > n:
                series.remove(ser)
                break
    return series


def series_include_element(el, series):
    result = [ser for ser in series if el in ser]
    return result


