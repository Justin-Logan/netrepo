class Game:
    def __init__(self):
        self.difficulty = 0
        self.targetNumber = 0
        self.attempts = 0
        self.maxAttempts = 0
        self.player = Player()

class Player:
    def set_player_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name.strip()
        count = 0
        if not self.name:
            return 3
        for c in self.name:
            count += 1
            if not c.isalpha():
                return 2
        if count <= 2:
            return 1
        return 0

def generate_random_number(min_value, max_value):
    import random
    return random.randint(min_value, max_value)

def heat(guess, target):
    if abs(guess - target) == 1:
        return "You're Burning Hot!"
    elif abs(guess - target) in [2, 3]:
        return "You're Warm..."
    elif abs(guess - target) in [4, 5, 6]:
        return "You're Cold."
    return "You're Super Cold!"
