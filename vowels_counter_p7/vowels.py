def vowel_counting(name):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    results = 0
    for vowel in name:
        if vowel in vowels:
            results += 1
    return results


