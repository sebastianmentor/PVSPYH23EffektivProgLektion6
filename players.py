from dataclasses import dataclass
# from itertools import map
# from functools import 

@dataclass
class Player:
    Name: str
    Goals: int
    Assists: int

lista = [Player('Stefan', 12, 22), Player('Mats',11,99), Player('Foppa',11,77)] 


sorterad_lista = [] # 

sort_players = lambda x: x.Goals + x.Assists

lista.sort(key=lambda x: x.Goals + x.Assists)

print(lista)
print(sort_players)
print(sort_players(lista[0]))