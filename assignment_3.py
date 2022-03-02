# # checks if two given strings are anagrams
def anagrams(s):
    s1, s2 = s.split(' ')
    s1 = [i.upper() for i in s1]
    s2 = [i.upper() for i in s2]

    if sorted(s1) == sorted(s2):
        print("yes: the given input are anagrams")

    else:
        print("No : the given input are not annagram")


s = "Mary Army"

anagrams(s)

