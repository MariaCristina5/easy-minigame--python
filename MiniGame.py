print("Welcome to my mini game")

name = input("What is your name? ")
age = int(input("What is your age? "))
print("Hello", name, "you are", age, "years old.")

health = 10

print("You are starting with", health, "health")

if age >= 18:
    print("You are old enough to play!")
    wants_to_play = input("Do you want to play? Type yes if you do. ").lower()
    if wants_to_play == "yes":
        print("Let's play!")
        left_or_right = input("Fist choice... Left or Right (left/right)? ")
        if left_or_right == "left":
            ans = input("Nice, you follow the path ans reach a lake... Do you swim across or go around (across/around)? ")

            if ans == "around":
                print("You went around and reached the other side of the lake")
            elif ans == "across":
                print("You managed to get acriss, but were bit by a fish and lost 5 health")
                health -= 5
                
            ans = input("You notice a house and a river. Which do you go to (river/house)? ")
            if ans =="house":
                print("You go to the house and greted by the owner... He is not in the mood and you lose 5 health")
                health -=5

                if health <= 0:
                    print("You now have 0 health and you lose the game...")
                else:
                    print("You survived! You win!")

            else:
                print ("You fell in the river and lost.")
        else: 
            print("You fell down and lost...")
    else:
        print("Cya...")
else: 
    print("You are not old enough to play. You need to be 18.")