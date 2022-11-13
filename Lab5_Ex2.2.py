class Node:
    def __init__ (self,Val):
        self.Val = Val
        self.NextL = ""
        self.NextR = ""
    def insert(self,Val):
        while True:
            if Val > self.Val:
                if self.NextR == "":
                    self.NextR = Node(Val)
                    break
                else:
                    self = self.NextR
            elif Val < self.Val:
                if self.NextL == "":
                    self.NextL = Node(Val)
                    break
                else:
                    self = self.NextL
    def delete(self,Val):
        while True:
            if Val > self.Val:
                if Val > self.NextR.Val:
                    self.NextR = self.NextR
                    print("X")
                    break
                ################### Delete Right ########################
                
