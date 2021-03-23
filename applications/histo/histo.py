def histogram():
    with open('C:\\Users\\Timothy Eakin\\hashTables\\applications\\histo\\robin.txt','r') as file_output:
        data = file_output.read()
    cache = {}
    words = data.lower().split()
    for word in words:
        word = word.strip('":;,.-+=/\\|[]}{()*^&')
        if word == '':
            continue
        if not cache.get(word):
            cache[word] = []

        cache[word].append('#')
    return cache

histo = histogram()

for word in histo:
    print("".join(histo[word]),word)