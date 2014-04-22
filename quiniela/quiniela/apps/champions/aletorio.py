import random

class aleatorio:
    __menor=0
    __mayor=0

    def __init__(self,numeroMin,numeroMax):
        self.__menor=numeroMin
        self.__mayor=numeroMax
        
    def obtener(self):
        if self.__mayor==0:
            result=0
            return result
        else:
            result=random.randint(self.__menor,self.__mayor) 
            return result


        
        
        