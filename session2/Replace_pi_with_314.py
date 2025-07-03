def ReplacePi(s):
    if len(s) == 0:
        return ""
    if s[0] == 'p' and s[1] == 'i':
        return "3.14" + ReplacePi(s[2:])
    else:
        return s[0] + ReplacePi(s[1:])

s = input("Enter a string: ")
result = ReplacePi(s)