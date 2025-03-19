from abc import ABC, abstractmethod       #abc is module ABC is class(abstract base class) abstractmethod is decorator


class Base(ABC):
    @abstractmethod
    def Addition(self,No1,No2):
        pass
    

class Derived(Base):
    pass


dobj = Derived()        #error