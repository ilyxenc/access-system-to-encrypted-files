import db.db_actions as db
import protocol.protocol as pr
from time import sleep
import sys
import text as txt

# Username and password input
username = str(input('Enter username: '))
password = str(input('Enter password: '))
# username, password = 'admin', '12345678'

# First action
# db.createTableUsers()
# Second action
# db.insertUser(username, password)

access = db.isThereAUserOrNot(username, password)
if access == db.accessed:
    # Continue if accessed
    sleep(0.1)
    print(access)
else:
    sleep(0.1)
    print(access)
    # Close program if access denied
    sys.exit(0)

while True:
    text = 'Action list:\nEnter 1 to write file\nEnter 2 to encrypt file\nEnter 3 to decrypt file\nEnter 4 to see protocol\nEnter 5 to see text from file\nEnter 0 to exit\nAction : '
    action = str(input(text))
    if action == '0':
        break
    elif action == '1':
        path = str(input('Enter file path : ')) # 'files/file.txt'
        text = str(input('Enter text      : ')) # YOUR_TEXT_HERE
        txt.writeFile(path, text)
    elif action == '2':
        path = str(input('Enter file path         : ')) # 'files/file.txt'
        newPath = str(input('Enter encrypt file path : ')) # 'files/file-encrypt.txt'
        key = str(input('Enter key               : ')) # YOUR_KEY_HERE
        txt.encrypt(path, newPath, key)
    elif action == '3':
        oldPath = str(input('Enter old file path     : ')) # files/file.txt
        path = str(input('Enter encrypt file path : ')) # 'files/fileEncrypt.txt'
        newPath = str(input('Enter decrypt file path : ')) # 'files/fileDecrypt.txt'
        key = str(input('Enter key               : ')) # YOUR_KEY_HERE
        txt.decrypt(path, newPath, key)
        sleep(0.3)
        print(txt.integrityControl(oldPath, newPath))
    elif action == '4':
        type = str(input('What do you want to see?\nEnter 1 to see a string\nEnter 2 to see all\nType : '))
        if type == '1':
            n = str(input('Enter number of line : '))
            print('\n', pr.show(n))
        elif type == '2':
            print(pr.showAll())
    elif action == '5':
        path = str(input('Enter file path : '))
        print(txt.readFile(path))
