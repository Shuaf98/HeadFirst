class Countfromby:
    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incr= i
    def increase(self) -> None:
        self.val += self.incr
        
    def __repr__(self) -> str:
        return str(self.val)
     #This allows us to run print on the object's value, without invoking val
        



    