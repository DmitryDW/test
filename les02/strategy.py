class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def do_some_work(self):
        result = self._strategy.do_work()
        return result

class Strategy:
    def do_work(self):
        pass

class ConcreteStrategyA(Strategy):
    def do_work(self):
        return "ConcreteStrategyA"

class ConcreteStrategyB(Strategy):
    def do_work(self):
        return "ConcreteStrategyB"

context = Context(ConcreteStrategyA())
print(context.do_some_work())  # Output: ConcreteStrategyA

context.set_strategy(ConcreteStrategyB())
print(context.do_some_work())  # Output: ConcreteStrategyB