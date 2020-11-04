import binascii
import grasshopper.main as gh
import protocol.protocol as pr

# reading text from file
def readFile(path):
    pr.add('reading file')
    f = open(path, 'r')
    text = f.read()
    f.close()
    return text

# writing text to file
def writeFile(path, text):
    pr.add('writing to file')
    f = open(path, 'w')
    f.write(text)
    f.close()

# encrypt file from path to path
def encrypt(path, newPath, key):
    pr.add('encrypt file')
    f = open(path, 'r')
    text = f.read()
    f.close()

    K = gh.getKeys(transformKey(key))

    text = gh.encrypt(utf8ToHex(text), K)

    f = open(newPath, 'w')
    f.write(text)
    f.close()

# decrypt file from path to path
def decrypt(path, newPath, key):
    pr.add('decrypt file')
    f = open(path, 'r')
    text = f.read()
    f.close()

    K = gh.getKeys(transformKey(key))

    text = hexToUtf8(gh.decrypt(text, K))

    f = open(newPath, 'w')
    f.write(text)
    f.close()

# turn text from hex to utf8
def hexToUtf8(text):
    pr.add('converting text from hex to utf-8')
    text = binascii.unhexlify(text).decode('utf8')
    return text

# turn text from utf8 to hex
def utf8ToHex(text):
    pr.add('converting text from utf-8 to hex')
    text = binascii.hexlify(text.encode('utf8')).decode('utf8')
    return text

# set key with right length
def transformKey(key):
    key = binascii.hexlify(key.encode('utf8')).decode('utf8')
    count = 64 - len(key) % 64
    while len(key) < 64:
        key += key
    return key[:64]

# integrity control
def integrityControl(path1, path2):
    text1 = readFile(path1)
    text2 = readFile(path2)

    match = text2.find(text1, 0)

    if match == 0:
        return '\nintegrity control was SUCCESSFUL\n'
    else:
        return '\nintegrity control was FAILED\n'
