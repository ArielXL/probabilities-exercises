import random

class MontyHall:
    def __init__(self):
        self.prize_door = self.pick_door()
        self.selected_door = None
        self.removed_door = None

    def pick_door(self):
        return random.randint(1, 3)

    def select_door(self):
        self.selected_door = self.pick_door()

    def remove_door(self):
        door = self.pick_door()
        while door == self.selected_door or door == self.prize_door:
            door = self.pick_door()
        self.removed_door = door

    def switch_choice(self):
        self.selected_door = 6 - self.selected_door - self.removed_door

    def user_wins(self):
        if self.selected_door == self.prize_door:
            return True
        else:
            return False

    def run_game(self, switch = True):
        self.select_door()
        self.remove_door()
        if switch:
            self.switch_choice()
        return self.user_wins()