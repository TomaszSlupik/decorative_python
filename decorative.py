import sys
import time

# Przykład 1
# Dekoratory Main Watch udekorował funkcję PythonVersion()
def pythonVersion():
     print(f"Wersja Pythona{sys.version}")


def mainWatch(func):
    def wrapper ():
        print('---' * 32)
        func()
        print('---' * 32)
    return wrapper

mainWatch = mainWatch(pythonVersion)
mainWatch()

print('---')

# Przykład 2
# Zamiana na duże litery 
def describe():
    return f"Dzisiaj mamy zawody"


def mainDescribe(func):
    def wrapper():
        return func().upper()
    return wrapper

mainDescribe = mainDescribe(describe)

print(mainDescribe())

print('---')

# Przykład 3 - przywitanie osoby jaką chcemy 
def hi(func):
    def wrapper(*args, **kwargs):
        print("Cześć")
        return func(*args, **kwargs)
    return wrapper

@hi
def hello (name):
    return f"Hello {name}"

helloTom = hello('Tom')
print(helloTom)

#  Przykład 4 - timer, obliczanie czasu 
def timer (func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Łączny czas {end - start: .2f}")
    return wrapper

@timer
def sleep():
    print('Uśpienie na 1 sekundy')
    time.sleep(1)


timer = timer(sleep)
timer()

print('---')

# Przykład 5 - powtórzenie 2x 
def repeat(func):
    def wrapper(*args, **kwargs):
        myList = []
        for _ in range(2):
            myList.append(*args, **kwargs)
        return myList
    return wrapper

@repeat
def myName (name):
    return f"{name}"


print(myName('Tomek'))