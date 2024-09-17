def all_variants(text):
    y = len(text)
    for one in range(1, y + 1):
        for two in range(y - one + 1):
            yield text[two:one + two]


a = all_variants("abc")
for i in a:
    print(i)
