class Employe:
    def __init__(self):
        self.__no=0
        self.__name=' '
        self.__salary=0.0

    def add(self):
        self.__no=int(input("enter number of employee"))
        self.__name=str(input("enter name of employee"))
        self.__salary=float(input("enter salary of employee"))
    
    def show(self):
        print(self.__no,",",self.__name,",",self.__salary)
        
    def getno(self):
        return self.__no

    def quitt(self):
        print("quit the record!!")
