def ends_with(s1, s2):
    if s1.endswith(s2):
        return True
    else:
        return False


str1 = input()
str2 = input()

print(ends_with(str1, str2))
