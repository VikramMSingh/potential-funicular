import random

class MagicBall:
    def __init__(self, answer=['Yes','No','There is a slight probability']):
        self.answer = answer

    def PredictFuture(self):
        prediction = random.choice(self.answer)
        return prediction
        
