class Myclass:
    __privateVar = 29;

    def __privateMeth(self):
        print("Im inside Myclass")

    def hello(self):
        print("\nPrivate Variable: ",Myclass.__privateVar)

foo = Myclass()
foo.hello()
foo.__privateMeth
