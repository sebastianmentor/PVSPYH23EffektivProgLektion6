from typing import Any
from collections import abc

class House:
    def __init__(self, price:float) -> None:
        self._price = price

    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, price:float) -> None:
        pass

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass


def gen(x) -> abc.Generator[int,str,None]:
    i = 0
    while i < x:
        stupid = print((yield i))
        # yield i
        stupid = True
        if stupid:
            print(F'This was sent to the generator: {stupid}')
        else:
            print(F'Nothing sent to the generator! {stupid=:}')        
        i+=1

    return 'End of generator!'

try:
    it = iter(gen(4))
    print(it.send(None))
    print(it.send('Sending message 1')) 
    print(it.send('Sending message 2')) 
    print(next(it)) 
    print(next(it)) 
    print(next(it))
except StopIteration as e:
    print(e) 