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
        
Header = Node(50)
Header.insert(25)
Header.insert(75)
Header.insert(30)
Header.insert(60)
Header.insert(40)
