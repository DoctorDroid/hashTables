def word_count(s):
    cache = {}
    s_list = s.lower().split()
    for word in s_list:
        word = word.strip('":;,.-+=/\\|[]}{()*^&')
        if word == '':
            continue
        if not cache.get(word):
            cache[word] = 0

        cache[word] += 1
    return cache

        




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))