class Cricket(object):
    def __init__(self,team,name,position,status):
        self.team=team
        self.name=name
        self.position=position
        self.status=status
    def captain(self):
        self.status="captain"
    def retire(self):
        self.status="retired"
    def __str__(self):
        return"%s is playing in %s as %s -%s"%(self.name,self.team,self.position,self.status)

        
player1=Cricket("India","Dhoni","wicketkeeper","player")
player2=Cricket("India","Kohli","batsman","player")
player3=Cricket("India","Sachin","batsman","player")
player1.captain()
player3.retire()
print player1
print player2
print player3 
