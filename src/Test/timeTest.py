from os import system

swole = lambda gains:gains*2

print(swole(7))


class Mutter:

        def _init_(self, status, sohn):
                self.status = status
                self.sohn = sohn 

mutt1 = Mutter("Gut","Friedrich")
mutt2 = Mutter("Nicht so gut","Hans")

print(mutt1.status)
        


class Daddy:        
   def myMethod(self):
      print ("Building Legacy")

class Sonnen(Daddy): 
   def myMethod(self):
      print ("Yolo")

c = Sonnen()          
c.myMethod() 
p = Daddy()
p.myMethod() 


class MutterCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)

counter = MutterCounter()
counter.count()
counter.count()


print(counter._MutterCounter__secretCount)
print(counter.__secretCount)
