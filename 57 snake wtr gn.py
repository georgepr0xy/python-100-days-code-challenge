user1=str(input("enter player 1:"))
user2=str(input("enter player 2:"))


if(user1=="snake" and user2=="snake"):
     print("draw")
elif(user1=="water" and user2=="snake"):
     print("player 1 is the winner ")
elif(user1=="gun" and user2=="snake"):
     print("player 1 is the winner ")
elif(user1=="snake" and user2=="water"):
     print("player 2 is the winner ")
elif(user1=="water" and user2=="water"):
     print("draw ")
elif(user1=="gun" and user2=="water"):
     print("player 2 is the winner ")     
elif(user1=="snake" and user2=="gun"):
     print("player 2 is the winner ")     
elif(user1=="water" and user2=="gun"):
     print("player 1 is the winner ")     
elif(user1=="gun" and user2=="gun"):
     print("draw ")   
