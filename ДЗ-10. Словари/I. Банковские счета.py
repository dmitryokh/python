input = open('input.txt', 'r')
text = input.readline()
clients = {}
while text != "":
    text = text.split()
    operation = text[0]
    if operation == "DEPOSIT":
        name = text[1]
        money = int(text[2])
        if name in clients:
            clients[name] += money
        else:
            clients[name] = money
    elif operation == "WITHDRAW":
        name = text[1]
        money = int(text[2])
        if name in clients:
            clients[name] -= money
        else:
            clients[name] = money * (-1)
    elif operation == "BALANCE":
        name = text[1]
        if name in clients:
            print(clients[name])
        else:
            print("ERROR")
    elif operation == "TRANSFER":
        name1 = text[1]
        name2 = text[2]
        money = int(text[3])
        if name1 in clients:
            clients[name1] -= money
        else:
            clients[name1] = money * (-1)
        if name2 in clients:
            clients[name2] += money
        else:
            clients[name2] = money
    else:
        percent = int(text[1])
        for name in clients:
            if clients[name] > 0:
                clients[name] = int(clients[name] * (percent + 100) / 100)
    text = input.readline()
