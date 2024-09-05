from typing import Any
from collections import abc
from dataclasses import dataclass

class House:
    def __init__(self, price:float) -> None:
        self._price = price
        self._address = None

    @property
    def price(self) -> float:
        return self._price
        
    @price.setter
    def price(self, price:float) -> None:
        if price > 0:
            self._price = price
    
    @property
    def address(self) -> str|None:
        return self._address

    @address.setter
    def address(self, address:str) -> None:
        self._address = address

    @address.deleter
    def address(self) -> None:
        self._address = None

    def __eq__(self, value: object) -> bool:
        if isinstance(value, House):
            return self.address == value.address and self.price == value.price
        else:
            raise TypeError('Skicka in ett hus för fasen!! Inte något annat skit!')
        

    def __lt__(self, value:object) -> bool:
        if isinstance(value, House):
            return self.price < value.price
        else:
            raise TypeError('Skicka in ett hus för fasen!! Inte något annat skit!')
        

    # def __gt__(self, value:object) -> bool:
    #     if isinstance(value, House):
    #         return self.price > value.price
    #     else:
    #         raise TypeError('Skicka in ett hus för fasen!! Inte något annat skit!')
        
    def __le__(self,value:object) -> bool:
        if isinstance(value, House):
            return self.price > value.price 
        else:
            raise TypeError('Skicka in ett hus för fasen!! Inte något annat skit!')
         
    def __repr__(self) -> str:
        return f"House({self.price})"
    
    def __del__(self) -> str:
        # print(self.price)
        # print('Spränger Huset!')
        # self.house = House(22)
        # House(88)
        # self.house = House(33)
        # self.house = House(44)
        # self.house = House(55)
        # self.house = House(66)
        # self.house = House(77)
        # self.house = House(88)
        # self.house = House(99)
        pass

    def __enter__(self,*args) -> 'House':
        print(args)
        print('Bygger upp huset!!')
        return self

    def __exit__(self, *args) -> None:
        print(args)
        print('River huset!!')
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(args)
        print(kwds)

# hus = House(3_000_000.00)
# print(hus)
# hus.price = 3100000
# print(hus)
# del hus
# print(hus)
# with House(20000) as house:
#     print(house)
#     print(house(1,2,3,hej='hej',då='då'))

hus1 = House(10)
hus1.address = 'Ankeborgsgatan 10'
hus2 = House(11)
hus2.address = 'Ankeborgsgatan 10'
print(f'{hus1==hus2=:}')
print(f'{hus1<hus2=:}')
print(f'{hus1>hus2=:}')
hus2.price = 10
print(f'{hus1==hus2=:}')
print(f'{hus1<hus2=:}')
print(f'{hus1>hus2=:}')
print(f'{hus1>=hus2=:}')

hus3 = House(10)

@dataclass
class SuperHouse:
    price:float
    address: str

shus1 = SuperHouse(10, 'asdf')
shus2 = SuperHouse(10, 'asdf')
print(f'{shus1==shus2=:}')
print(f'{shus1 is shus2=:}')
print(f'{id(shus1)=:} -- {id(shus2)=:}')
print(f'{id(shus1) == id(shus2)=:}')



# def gen(x) -> abc.Generator[int,str,str]:
#     i = 0
#     def print_fun(val:Any):
#         print(type(val))
#         print(val)

#     while i < x:
#         print_fun((yield i))
#         # print(stupid:=(yield i))
#         # stupid = print((yield i))
#         # yield i
#         stupid = True
#         if stupid:
#             print(F'This was sent to the generator: {stupid}')
#         else:
#             print(F'Nothing sent to the generator! {stupid=:}')        
#         i+=1

#     return 'End of generator!'

# try:
#     it = iter(gen(4))
#     print(it.send(None))
#     print(it.send(('Sending message 1',34))) 
#     print(it.send(('Sending message 2',11))) 
#     print(next(it)) 
#     print(next(it)) 
#     print(next(it))
# except StopIteration as e:
#     print(e) 