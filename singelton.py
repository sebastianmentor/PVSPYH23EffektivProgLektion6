import time

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance



# Testa singleton-mönstret
singleton1 = Singleton()
singleton2 = Singleton()
print('1')
print(f'{Singleton._instance=:}')
print(singleton1 is singleton2)  # Output: True, båda är samma instans
print('2')
singleton1._secret = 'Hemlighet'
print(singleton2._secret)
print('3')
del singleton1
Singleton._instance = None
new_singel = Singleton()
print(new_singel)
print(f'{Singleton._instance=:}')
print('4')
print(singleton2)
print(singleton2._secret)
del singleton2
print('5')
time.sleep(2)
print(f'{Singleton._instance=:}')
print('6')
print(f'{Singleton._instance=:}')
singleton3 = Singleton()
# print(singleton3._secret)
print(f'{Singleton._instance=:}')

