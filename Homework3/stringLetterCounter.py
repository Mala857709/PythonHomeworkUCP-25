word = 'testing'

n = len(word)
mid = n // 2

if n % 2 == 1:
    # нечётное
    print(word[mid])
else:
    # чётное
    print(word[mid - 1:mid + 1])