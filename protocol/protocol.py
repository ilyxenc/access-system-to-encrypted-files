import datetime

# Recording actions
def add(data, time = datetime.datetime.now().strftime("%c")):
    f = open('protocol/protocol.txt', 'a')
    f.write(time + ' | ' + data + '\n')
    f.close()

# Show line from `protocol`
def show(n):
    f = open('protocol/protocol.txt', 'r')
    data = ''
    for i, line in enumerate(f):
        if int(i) == int(n):
            data = line
    f.close()
    add('protocol ' + n + ' line have shown')
    return data

# Show all lines from `protocol`
def showAll():
    f = open('protocol/protocol.txt', 'r')
    data = f.read()
    f.close()
    add('protocol have shown')
    return data
