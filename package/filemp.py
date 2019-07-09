
import main.py

class Employe:
    def __init__(self,no,name,sal):
        self.__no=0
        self.__name=' '
        self.__salary=0.0

    def add(self):
             e=Employe()
             e.add()
             file=open("data.txt",'w')
             file.seek(0,2)
             file.write(to_string())

    def query():
       n=int(input("enter number of employee you want to search for?"))
       file.seek(0,0)
       u=line.find(",",0,5)
       str_no-int(line[0:u])
       for line in file:
           if n==str_no:
               print(line,end='')
               break;
                     

    def edit():
       n=int(input("enter number of employee you want to search for?"))
       file.seek(0,0)
       u=line.find(",",0,5)
       str_no-int(line[0:u])
       for line in file:
           if n==str_no:
               print(line,end='')
               break;
            else:
                file.write(line)
                file.close()
                file1.close()
                os.remove("empl.txt")
                os.remove("data.txt","empl.txt")

    def delete():
       n=int(input("enter number of employee you want to search for?"))
       file.seek(0,0)
       u=line.find(",",0,5)
       str_no-int(line[0:u])
       for line in file:
           if n==str_no:
               print(line,end='')
               break;
            else:
                file.write(line)
                file.close()
                file1.close()
                os.remove("empl.txt")
                os.remove("data.txt")


empl_list=[]
while True:
       
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
