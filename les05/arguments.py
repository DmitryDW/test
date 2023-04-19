class Arg:

    def __init__(self, num1=7, num2=3, *args, **kwarks):
        self.num1 = num1
        self.num2 = num2
        self.args = args
        self.kwarks = kwarks


    def arguments(self, num1=2, num2=1, *args, **kwarks):
        print(args)
        print(kwarks)
        if num1 is None:
            num1 = self.num1
        if num2 is None:
            num2 = self.num2
        return num1 - num2


arg = Arg(5, 3)

# позиционный аргумент
summa = arg.arguments(3, 4)
print(summa)


# именованые аргументы
summa = arg.arguments(num2=3, num1=5)
print(summa)


# аргументы со значениями по умолчанию
summa = arg.arguments()
print(summa)


# аргументы со звездочкой (*args)
summa = arg.arguments(1, 3, 5, 6, 9)


# аргументы с ** (kwargs)
summa = arg.arguments(3, 3, num3=76, num4=44)
print(summa)
