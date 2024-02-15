def readFile(text):
    f = open(text, 'r', encoding="UTF-8")
    n = int(f.readline()) #считываем кол-во трюков
    tricks = list()
    orderTricks = list()
    for i in range(n): #проходим n раз по файлу и записываем в каком порядке распологаются карты после n-го трюка (перед каждым n-ым трюков колода карт находится в изначальном положении)
        tricks.append(f.readline())
    while True:
        line = f.readline() #записываем порядок выполнения трюков пока не кончится файл
        if not line:
            break
        orderTricks.append(int(line))
    return tricks, orderTricks

def orderDeeck(tricks, orderTricks):
    from copy import copy
    D, D1 = dict(), dict()
    D = {k: k for k in range(1, 52 + 1)} #заполняем ключи и значения цифрами по порядку 1:1 2:2 3:3 и тд
    for trick in orderTricks: #проходимся по последовательности трюков
        for j, i in enumerate(tricks[int(trick)-1].split(), start = 1): #производим перестановку, j это цифры по порядку, i индекс карты
            i = int(i)
            D1[j] = D.get(i) #заполняем D1 в формате j номер по порядку: индекс карты
        D = copy(D1)
    return D

def makeDeck() -> dict: #создаем словарь порядковый номер: название карты
    from itertools import product
    return {k: f"{v[1]} of {v[0]}" for k, v in enumerate(product(["Clubs", "Diamonds", "Hearts", "Spades"], list(range(2, 10 + 1)) + ["Jack", "Queen", "King", "Ace"]), start = 1)}

print("Начальная колода")
print(makeDeck().items())
print("Тест 1")
print(*[makeDeck()[i[1]] for i in orderDeeck(*readFile("text.txt")).items()], sep = "\n")
print("Тест 2")
print(*[makeDeck()[i[1]] for i in orderDeeck(*readFile("text2.txt")).items()], sep = "\n")
print("Тест 3")
print(*[makeDeck()[i[1]] for i in orderDeeck(*readFile("text3.txt")).items()], sep = "\n")
print("Тест 4")
print(*[makeDeck()[i[1]] for i in orderDeeck(*readFile("text4.txt")).items()], sep = "\n")
print("Тест 5")
print(*[makeDeck()[i[1]] for i in orderDeeck(*readFile("text5.txt")).items()], sep = "\n")