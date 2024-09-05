class FileHandler:
    def __init__(self, filename:str) -> None:
        self._file = open(filename,'r')
    
    def __del__(self):
        self._file.close()


filhanterare = FileHandler('hej.txt')
print(filhanterare._file.readline())
del filhanterare
print(filhanterare)