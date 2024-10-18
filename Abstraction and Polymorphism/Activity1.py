from abc import ABC , abstractmethod

class AbsClass(ABC):

    def print(self,x):
     print("Passsed Value: ", x)

    @abstractmethod
    def task(self):
       print("We Are Inside Absclass task")

class test_class(AbsClass):
   def task(self):
      print("We are inside test_class task")

test_obj = test_class()
test_obj.task()
test_obj.print(100)