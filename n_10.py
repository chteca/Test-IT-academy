def f(x):
    return 3*x**3 + 4*x**2 + 5*x + 21

def golden_section_search(a, b, acc):
    golden_ratio = (1 + 5 ** 0.5) / 2
    c = b - (b - a) / golden_ratio
    d = a + (b - a) / golden_ratio
    while abs(c - d) > acc:
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - (b - a) / golden_ratio
        d = a + (b - a) / golden_ratio
    return (b + a) / 2