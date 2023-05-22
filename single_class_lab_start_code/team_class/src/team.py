#THE ARGUMENTS ALWAYS START WITH SELF

class Team:
    def __init__(self, name, players, coach):
        # breakpoint()
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0
    
    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player):
        if player in self.players: 
            return True
        else: 
            return False
        
    def play_game(self, playing):
        if playing == True:
            self.points += 3
        else:
            self.points = 0
