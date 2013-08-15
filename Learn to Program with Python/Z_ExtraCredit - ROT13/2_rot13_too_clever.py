def rot13(s):
    rot=lambda x:chr(ord(x)+13) if chr(ord(x.lower())+13).isalpha()==True else chr(ord(x)-13)
    s=[rot(i) for i in filter(lambda x:x!=',',map(str,s))]
    return ''.join(s)

#########################################################

print(rot13(input("Text to be rot13'ed: ")))
