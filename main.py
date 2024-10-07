class Calculator:
    def __init__(self, symbol: str, number: float) -> None:
        self.symbol = symbol
        self.number = number
    
    def add(self,sk) -> float:
        return self.number+sk

    def sub(self,sk) -> float:
        return self.number-sk

    def div(self,sk) -> float:
        return self.number/sk

    def mul(self,sk) -> float:
        return self.number*sk
        
    def calculate(self, sk) -> float:
        if self.symbol == "/":
            return self.div(sk)