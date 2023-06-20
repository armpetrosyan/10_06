def swap_strings(s1, s2):
    temp = s1
    s1 = s2
    s2 = temp
    return s1, s2


str1 = input()
str2 = input()

print(swap_strings(str1, str2))
