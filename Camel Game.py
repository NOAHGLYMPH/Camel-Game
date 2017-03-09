#Desert Dash
#Intro
name = input('What is your name? ')
print('Welcome to Desert Dash,', name)
print('You have stolen a camel to make your way across the great Irimina desert.')
print('The natives want their camel back and are chasing you down!')
print('Survive your desert dash and outrun the natives!!!!')
print('Rules:')
print('If you die of hunger, you lose, if you die of thirst, you lose, if the natives catch up to you, you lose, if your camel dies of fatigue, you lose.')

#Vitality/Distance Variables
import random
done = False
miles_traveled = 0
thirst = 0
water = 0
camel_thirst = 0
camel_stamina = 0
natives_traveled = -20
canteen = 5
player_thirst= 0
natives_moving = random.randrange(3,15)
medium_speed = random.randrange(5,15)
full_speed = random.randrange(10,20)

#Player options
while not done:
    print("A. Drink from water sack.")
    print("B. Go at a medium pace.")
    print("C. Speed your camel up to full speed.")
    print("D. Stop to rest your camel overnight.")
    print("E. Make an inventory of your supplies and check the natives progress.")
    print("Q. Give up and allow the natives to take back their camel and kill you.")
    decision = input("Pick an action: ")
    if decision == "q" or decision == "Q":
        print("GAME OVER MAN, GAME OVER!!!")
        done = True
    #Check yo' self and yo' camel and the natives progress
    elif decision == "e" or decision == "E":
        print("Miles traveled:", miles_traveled)
        print("Sips left in Canteen:", canteen) 
        print("The natives have traveled:", natives_traveled) 
        print("Camel's endurance level:", camel_stamina) 
        print("Camel's thirst level:", camel_thirst) 
    #Resting overnight
    elif decision == "d" or decision == "D":
        camel_stamina = 0
        print("You have eaten and are no longer hungry")
        print("Your camel is refreshed and ready, but the natives have moved up to," ,natives_traveled, "miles")
    #full_speed
    elif decision == "c" or decision == "C":
        print("You and your camel have traveled", miles_traveled, "miles")
        miles_traveled += random.randrange(10,20)
        natives_traveled += random.randrange(3,15)
        thirst = camel_thirst + 1
        water = player_thirst + 1      
        camel_stamina += random.randrange(1,5)
        print("Camel Stamina Level:", camel_stamina)
        print("The natives are currently at", natives_traveled, "miles")
    #moderate_speed
    elif decision == "b" or decision == "B":
        print ("you have traveled", miles_traveled, "miles")
        miles_traveled += random.randrange(5,15)
        natives_traveled += random.randrange(3,15) 
        thirst + 1
        water + 1
        camel_stamina += random.randrange(1,5)
        print("Camel Stamina Level:", camel_stamina)
        print("The natives have moved up to," ,natives_traveled, "miles")
    #drinks_from_canteen
    elif decision == "a" or decision == "A":
        print("you drank from your water sack")
        canteen = canteen - 1
        water = 0
    #You are thirsty
    if water >= 3:
        print("you are getting parched")
    #you died of thirst
    if water >=5:
        print("You died from dehydration, GAME OVER")
        done = True
    #Your camel is getting fatigued
    if camel_stamina >= 8:
        print("Your camel is getting tired, it needs a break")
    #Camel Dies
    if camel_stamina >= 10:
        print("Your camel has died, GAME OVER")
        done = True
    #if the natives catch up with you
    if natives_traveled > miles_traveled:
        print("The natives got you! GAME OVER")
        done = True
    #the natives are on the move
    elif natives_traveled >= -10:
        print("The natives are getting closer")
      
    if miles_traveled == 300:
        print("You won and got through the Irimina Desert, you get to keep the camel. YOU WON")
        done = true

    if canteen <= 0:
        print("You ran out of sips")

    elif thirst >= 1:
        miles_traveled = 1 
      
      
        
            
        
        
    
        
        
    
    
