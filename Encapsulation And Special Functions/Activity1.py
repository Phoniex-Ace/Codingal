class myclass:

    __privateVar = 27

    def __privMeth(self):
        print("I Am Inside Class myclass")

    def hello(self):
        print("Private Variable Value:",myclass.__privateVar)

foo = myclass()
foo.hello()
foo.__privMeth()