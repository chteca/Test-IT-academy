def choose_plural(amount, variants):
    variant = 2
    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif amount % 10 >= 2 and amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
        variant = 1
    return f'{amount} {variants[variant]}'

def distribution_of_search_queries(search_queries):
    d = {}
    for queries in search_queries:
        a = len(queries.split())
        d[a] = d.get(a, 0) + 1
    all = len(search_queries)
    word = ('слово', 'слова', 'слов')
    for n in range(1, max(d)+1):
        print(f'{choose_plural(n ,word)}: {round(d.get(n, 0)*100/all)}%')
search_queries = ['watch new movies', 'coffee near me', 'how to find the determinant', 'python', 'data science jobs in UK', 'courses for data science', 'taxi', 'google', 'yandex', 'bing','foreign exchange rates USD/BYN', 'Netflix movies watch online free',  'Statistics courses online from top universities']
distribution_of_search_queries(search_queries)

