from abc import ABC, abstractmethod       #abc is module ABC is class(abstract base class) abstractmethod is decorator


class Base(ABC):
    @abstractmethod
    def Addition(self,No1,No2):     #without body(Abstract)
        pass
    

class Derived(Base):
    def Addition(self,No1,No2):
        return No1 + No2        #with body (concrete)
    



dobj = Derived()       
Ret = dobj.Addition(10,11)
print("Addition is :",Ret)

 