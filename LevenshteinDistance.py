def text_similarity(text1, text2):
    
    m = len(text1)
    n = len(text2)
    
    distance = []
    for i in range(m + 1):
        row = [0] * (n + 1)
        distance.append(row)

    for i in range(m + 1):
        distance[i][0] = i
    for j in range(n + 1):
        distance[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                cost = 0
            else:
                cost = 1
            distance[i][j] = min(distance[i - 1][j] + 1, 
                                  distance[i][j - 1] + 1, 
                                  distance[i - 1][j - 1] + cost)

    max_distance = max(m, n)
    similarity = 1 - (distance[m][n] / max_distance)

    return similarity


print(text_similarity("the quick brown fox", "a fast brown dog"))