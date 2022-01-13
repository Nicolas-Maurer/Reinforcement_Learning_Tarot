class Player:
    
    def __init__(self, name):
        
        self.name = name
        self.hand = []
        
        self.actual_score = 0 
        
        self.has_hearts = True
        self.has_spades  = True
        self.has_diamonds  = True
        self.has_clubs = True
        self.has_trumps = True
        
        self.max_trump_playable = 22
