def convert_to_int(s1):
    try:
        res = int(s1)
        return res
    except ValueError:
        print("Conversion not possible")


str1 = input()

print(convert_to_int(str1))
