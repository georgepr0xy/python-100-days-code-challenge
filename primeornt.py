# user = int(input("enter the number:"))
# if user > 0:
#     for i in range ( 2, int(user/2)+1):
#         if (user%i==0):
#             print("the is number is not prime")
#             break
#     else:
#        print("the number is prime")

# else:
#     print("the number is not prime")        

         

# def reverseWord():
#     #your code here
#     t = input()
#     print(t[::-1])
    
# reverseWord()

# st = "geprge provincce is good boy"
# print(st.isupper())
# print(st[0:5])
# print(st.split(" "))
# print(st.(" "))


# class superclass1():
#     def __init__(self,name,companyname):
#         self.name= name
#         self.companyname=companyname

#     def show_details(self):
#          print(f"The name is {self.name} and age is {self.companyname}")

# A = superclass1("george","apple")
# # A.name = "George"
# # A.companyname = "apple"
# A.show_details()


# class subclass(superclass1):
#     def __init__(self, sound):
#        superclass1.__init__(self,name="george",companyname="apple")
#        self.sound =sound
#     def show(self):
#         print(f"the name is {self.name} and companyname is {self.companyname} and sound {self.sound}") 

# a = subclass("bark")           
# a.show()


import pygame
import random
import os  # Import the os module to handle file paths

# Initialize pygame
pygame.init()

# Game constants
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Load car image
car_image_path = os.path.join("path_to_your_image_folder", "car.png")
car_image = pygame.image.load(car_image_path)
car_width, car_height = 50, 100

# Initialize variables
clock = pygame.time.Clock()
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 20
car_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle car movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed

    # Keep car within screen bounds
    car_x = max(0, min(WIDTH - car_width, car_x))

    # Update display
    screen.fill(WHITE)
    screen.blit(car_image, (car_x, car_y))
    pygame.display.flip()

    # Limit frames per second
    clock.tick(FPS)

# Clean up and quit
pygame.quit()
