def starts_with(s1, s2):
    if s1.startswith(s2):
        return True
    else:
        return False


str1 = input()
str2 = input()

print(starts_with(str1, str2))

