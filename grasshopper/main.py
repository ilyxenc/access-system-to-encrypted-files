import protocol.protocol as pr
import grasshopper.transformations as tr

X = tr.xor_func # операция XOR
S = tr.nonlinear_transformation # нелинейное преобразование в режиме простой замены
L = tr.linear_transformation # линейное преобразование

# Ключ шифрования должен быть задан в 16-ричной системе счисления
# key = '7766554433221100FFEEDDCCBBAA9988EFCDAB89674523011032547698BADCFE'

def getKeys(key):
    pr.add('generation keys')
    C = [] # константы
    F = [] # ячейки Фейстеля
    K = [key[:int(len(key) / 2)], key[int(len(key) / 2) :]]

    for i in range(32):
        if len(hex(i + 1)[2:]) == 1:
            C.append(L('0' + hex(i + 1)[2:] + '000000000000000000000000000000').upper())
        else:
            C.append(L(hex(i + 1)[2:] + '000000000000000000000000000000').upper())

    # формирование ячеек Фейстеля
    F.append([ K[1], X(L(S(X( K[0], C[0]))),  K[1])])
    for i in range(32):
        K = [ F[i][1], X(L(S(X( F[i][0], C[i]))),  F[i][1])]
        F.append(K)

    # разбиение заданного ключа пополам
    K = [key[:int(len(key) / 2)], key[int(len(key) / 2) :]]

    # формирование новых ключей из ячеек Фейстеля
    for i in range(len(F)):
        if (i + 1) % 8 == 0:
            K.append(F[i][0])
            K.append(F[i][1])
    return (K)

# Расшифровка текста
def encrypt(text, K):
    pr.add('text encrypt')
    count = 32 - len(text) % 32
    if count != 0 and count != 32:
        for i in range(count):
            text += '0'
    textArray = []
    for i in range(int(len(text) / 32)):
        textArray.append(text[i * 32 : i * 32 + 32])

    textEncrypt = []
    for j in textArray:
        # шифрование текста
        textEncrypted = j
        for i in range(9):
            textEncrypted = L(S(X(textEncrypted, K[i])))
        textEncrypted = X(textEncrypted, K[9])
        textEncrypt.append(textEncrypted)
    return(''.join(textEncrypt))

# Шифрование текста
def decrypt(text, K):
    pr.add('text decrypt')
    textArray = []
    for i in range(int(len(text) / 32)):
        textArray.append(text[i * 32 : i * 32 + 32])

    textDecrypt = []
    for j in textArray:
        # расшифровка текста
        textDecrypted = j
        for i in range(9, 0, -1):
            textDecrypted = S(L(X(textDecrypted, K[i]), 'reverse'), 'reverse')
        textDecrypted = X(textDecrypted, K[0])
        textDecrypt.append(textDecrypted)
    return(''.join(textDecrypt))
