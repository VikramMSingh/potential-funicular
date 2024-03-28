from random import choice
class Lottery:
    def __init__(self, list=[]):
        self.list = list

    def lottery_winner(self, ticket):
        self.ticket = ticket
        active = True
        count = 0
        while active:
            count += 1
            winner = choice(self.list)
            if winner == self.ticket:
                print(f"Your {self.ticket} is the same as {winner}, congo!")
                print(f"You won on attempt {count}")
                active = False
                break
            else:
                print(f"{winner} is not the same as your ticket, attempt {count}")
            #print(f"You have won a prize if you have this {winner}")


