from package.emp import Employe
def display():
       print("1.Add record")
       print("2.Display record")
       print("3.Query record")
       print("4.Edit record")
       print("5.Delete record")
       print("6.Quit record")

def add():
       e=Employe()
       e.add()
       empl_list.append(e)

def show():
       for e in empl_list:
              e.show()

def query():
       b=int(input("enter number of employee you want to search for?"))
       for e in empl_list:
              if(e.getno()==b):
                     e.show()
                     break;
                     

def edit():
       b=int(input("enter number of employee you want to search for?"))
       for e in empl_list:
              if(e.getno()==b):
                     e.add()
                     break;

def delete():
       b=int(input("enter number of employee you want to search for?"))
       for e in empl_list:
              if(e.getno()==b):
                     empl_list.remove(e)
      

def quitt():
       e=Employe()
       e.quitt()


def to_string():
       return str(self.__no)+","+self.__name+","+(self.__sal)
       





empl_list=[]
while True:
       display()
       ch=int(input("enter your choice!!!"))
       if(ch==1):
              add()
       elif(ch==2):
             show()
       elif(ch==3):
              query()
       elif(ch==4):
              edit()
       elif(ch==5):
              delete()
       else:
             quitt()





                            
