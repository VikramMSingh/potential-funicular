import random
alien_color = random.choice(["green","red", "yellow", "blue"])
point_earned = 0

if alien_color == "green":
    point_earned += 5 
    print(f"You've earned {point_earned} points")
elif alien_color == "yellow":
    point_earned += 10 
    print(f"You've earned {point_earned} points")
elif alien_color == "red":
    point_earned += 15
    print(f"You've earned {point_earned} points")
else:
    print("Alien is alive, keep fighting")
