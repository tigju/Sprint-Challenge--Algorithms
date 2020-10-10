'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# no recursion
# def count_th(word):
#     # TBC
#     if len(word) <= 1:
#         return 0
#     else:
#         return word.count("th")

# recursion

def count_th(word):
    # TBC
    count = 0
    if len(word) <= 1:
        return count
    else:
        if word[:2] == "th":
            count += 1

        return count + count_th(word[1:])


w = "abcthefthghith"
print(count_th(w))
