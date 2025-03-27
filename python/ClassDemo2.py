class Demo:
    def __init__(self):     #constructor
        print("Inside constructor")
        
        
    def __del__(self):      #destructor
        print("Inside Destructor")
        
            
obj1 = Demo()
obj2 = Demo()

print("End of Application")
