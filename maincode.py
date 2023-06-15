def encrypt(text, key):
    dec = 0
    for i in key:
        dec += ord(i)

    a = []
    b = []
    dec = dec // 26

    for i in range(32, 127):
        a.append(str(chr(i)))

    for i in range(len(text)):
        for j in range(len(a)):
            if text[i] == a[j]:
                b.append(j - dec)
    en = ""
    for i in b:
        en = en + a[i]
    return en


def decrypt(text, key):
    dec = 0
    for i in key:
        dec += ord(i)

    a = []
    b = []

    crypt = []

    dec = dec // 26

    for i in range(32, 127):
        a.append(str(chr(i)))

    for i in range(len(text)):
        for j in range(len(a)):
            if text[i] == a[j]:
                b.append(j)

    for i in b:

        if i + dec < len(a):
            crypt.append(a[i + dec])

        else:
            crypt.append(a[(i + dec) - 95])
    decry = ""
    for i in crypt:
        decry = decry + i
    return decry
