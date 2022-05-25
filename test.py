

def encrpy(s):
    l=list(s)
    length=len(l)
    for i in range(length):
        if(l[i] in vowels):
            l[i]=l[i].upper()
        if(l[i] in cons):
            index=cons.index(l[i])
            l[i]=cons[(index+3)%21]
    return ''.join(map(str, l))


def decrpy(s):
    l=list(s)
    length=len(l)
    vowels=['A','E','I','O','U']
    for i in range(length):
        if(l[i] in vowels):
            l[i]=l[i].lower()
        if(l[i] in cons):
            index=cons.index(l[i])
            l[i]=cons[(index-3)%21]
    return ''.join(map(str, l))

s=input()
vowels=['a','e','i','o','u']
cons=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r','s', 't', 'v', 'w', 'x', 'y','z']

print(s)

cipher=encrpy(s)
print(cipher)

plaintext=decrpy(cipher)
print(plaintext)