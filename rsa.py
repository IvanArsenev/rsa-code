def euler(n):
    f = n
    if n%2 == 0:
        while n%2 == 0:
            n = n // 2
        f = f // 2
    i = 3
    while i*i <= n:
        if n%i == 0:
            while n%i == 0:
                n = n // i
            f = f // i
            f = f * (i-1)
        i = i + 2
    if n > 1:
        f = f // n
        f = f * (n-1)
    return f

def keys(d_type):
    if d_type == 1:
        d, n = map(int, input("Введите закрытый ключ: ").split())
    elif d_type == 2:
        e, n = map(int, input("Введите открытый ключ: ").split())
        for i in range(1, n):
            if (i*e)%euler(n) == 1:
                d = i
                print(f"Закрытый ключ: {d} {n}")
                break
    return str(f'{d} {n}')

def decode():
    d = 0
    code = [int(x) for x in input("Введите вашу строку: ").split()]
    d, n = keys(int(input("Режим дешифровки:\n1) Знаю закрытый ключ\n2) Знаю открытый ключ\nВыберите: "))).split()
    d, n = int(d), int(n)
    s = (chr(96+(code[0]**d)%n))
    for i in range(1,len(code)):
        if ((code[i]**d)%n-code[i-1]) < 0:
            s += (chr(96+(code[i]**d)%n-code[i-1]+n))
        else:
            s += (chr(96+(code[i]**d)%n-code[i-1]))
    print(f"Расшифрованная строка: {s}")

def encode():
    string = str(input('Введите вашу строку (английские бувы, без пробелов): '))
    e, n = map(int, input("Введите открытый ключ: ").split())
    coded_s = ( (ord(string[0]) - 96) ** e ) % n
    s = str(coded_s)+' '
    for i in range(1, len(string)):
        s += str(((ord(string[i])-96+coded_s)**e)%n) + ' '
        coded_s = ((ord(string[i])-96+coded_s)**e)%n
    print(f"Зашифрованная строка: {s}")

code_type = int(input("Что сделать?:\n1) Расшифровать\n2) Зашифровать\nВыберите: "))
if code_type == 1: decode()
else: encode()
