from ball_8 import *

ball_prediction = MagicBall()

question = input("Enter your question \n")

if question:
    ball_answer = ball_prediction.PredictFuture()
    print(f"You asked {question}. \nThe Magic Eight Ball predicts {ball_answer}")
else:
    print("No question asked")

print("Thank you!") 
