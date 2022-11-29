def euler(n):
    result=n
    i=2
    while i*i<=n:
        i+=1
        if(n%i==0):
            while(n%i==0):
                n=n/i
                result-=result/n
    if(n>1):
        result-=result/n
    return result

def decode():
    d = 0
    code = [int(x) for x in input("Введите вашу строку: ").split()]
    d_type = int(input("режим дешифровки:\n1-знаю закрытый ключ\n2-знаю открытый ключ\nвыберите: "))
    if d_type == 1:
        d, n = map(int, input("Введите закрытый ключ: ").split())

    elif d_type == 2:
        e, n = map(int, input("Введите открытый ключ: ").split())
        # for i in range(1, n):
        #     if (i*euler(e))%n == 1:
        #         d = i
        #         print(d)
        #         break

        d = e
        print('Функция еще не написана! Определяем по закрытому ключу')

    s = (chr(64+(code[0]**d)%n))
    for i in range(1,len(code)):
        if ((code[i]**d)%n-code[i-1]) < 0:
            s += (chr(64+(code[i]**d)%n-code[i-1]+n))
        else:
            s += (chr(64+(code[i]**d)%n-code[i-1]))
    print(s)

def encode():
    print('Функция еще не написана!')

code_type = int(input("Что сделать?:\n1-Расшифровать\n2-Зашифровать\nвыберите: "))
if code_type == 1: decode()
else: encode()