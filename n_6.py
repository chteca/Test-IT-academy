def probability_of_number(N, M, S):
    p = (7 - S) / 6 
    q = 1 - p 
    from math import factorial
    probability = (factorial(N) / (factorial(M) * factorial(N - M))) * (p ** M) * (q ** (N - M))
    print (probability)