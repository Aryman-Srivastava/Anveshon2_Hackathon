def clean_String(string):
    string1=string.split()
    a=[]
    print(string1)
    for i in string1:
        if(len(i)==22):
            a.append(i)
    return a[0]+"\n"+a[1]


# print(len('01000100110110101110'))
