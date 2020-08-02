class Game:
    def __init__(self,span=[0,100],sub_fun="Square"):
        self.span=span
        self.func_dict = {
            "Square":lambda x: pow(x,2),
            "Odd":lambda x: 1 + (x-1)*2,
            "Even":lambda x: x*2,
            "Identity":lambda x: x,
            "Logarithm":lambda x: pow(10,x-1)
            }
        self.sub_fun = self.func_dict[sub_fun]
    def calculate(self):
        #winning_pos is an array. It determines if landing in the current position will give you a win.
        #True = Win, False = Loss, None = Not yet determined. As per the rules of the game, 0 is initialized as False.
        #This is since if you start on 0, that means your opponent won the previous round.
        #All others are None at the start of the calculation. The lenght is equal to the start and end point, plus 1.
        winning_pos = [False]+[None]*(self.span[1]-self.span[0])
        #Iterate until there no longer are any None-s.
        while winning_pos.count(None)>0:
            #Start with the highest False. Add numbers drawn from sub_fun to it and set those positions to True.
            #If you land on those positions, you can win, because you can then put your opponent in a loosing position.
            hi_false=[i for i,x in enumerate(winning_pos) if x==False][-1]
            i = 1
            while hi_false + self.sub_fun(i) <= self.span[1]:
                winning_pos[hi_false + self.sub_fun(i)] = True
                i+=1
            #Then, set the lowest None to False. From that position, you will always put your opponent in a winning position
            #There might be no None positions left, in that case, a value error is raised.
            try:
                lo_none=winning_pos.index(None)
            except ValueError:
                break
            winning_pos[lo_none]=False
        return winning_pos

if __name__ == "__main__":
    game=Game()
    result=game.calculate()
    print(str(result[-1]))  