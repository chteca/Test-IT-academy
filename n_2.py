def cosine_distance(vector1, vector2):
    if len(vector1) != len(vector2):
        print("Длины векторов должны быть одинаковы")
        return None
    
    dot_product = 0
    norm1 = 0
    norm2 = 0
    
    for i in range(len(vector1)):
        dot_product += vector1[i] * vector2[i]
        norm1 += vector1[i] ** 2
        norm2 += vector2[i] ** 2
        
    if norm1 == 0 or norm2 == 0:
        print("Между нулевыми векторами нельзя рассчитать косинусное расстояние")
        return None
    
    cosine_similarity = dot_product / ((norm1**0.5) * (norm2**0.5))
    cosine_distance = 1 - cosine_similarity
    
    return cosine_distance