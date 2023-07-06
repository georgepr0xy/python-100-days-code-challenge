questions=[["Which language is used to create facebook ?","python","french","javascript","php","none",4],["Which language is used to create facebook ?","python","french","javascript","php","none",4],["Which language is used to create facebook ?","python","french","javascript","php","none",4],["Which language is used to create facebook ?","python","french","javascript","php","none",4],["Which language is used to create facebook ?","python","french","javascript","php","none",4],["Which language is used to create facebook ?","python","french","javascript","php","none",4],["Which language is used to create facebook ?","python","french","javascript","php","none",4],["Which language is used to create facebook ?","python","french","javascript","php","none",4],["Which language is used to create facebook ?","python","french","javascript","php","none",4],["Which language is used to create facebook ?","python","french","javascript","php","none",4],["Which language is used to create facebook ?","python","french","javascript","php","none",4],["Which language is used to create facebook ?","python","french","javascript","php","none",4],["Which language is used to create facebook ?","python","french","javascript","php","none",4],["Which language is used to create facebook ?","python","french","javascript","php","none",4],["Which language is used to create facebook ?","python","french","javascript","php","none",4],]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]

money =0

for i in range(0, len(questions)):
    question = questions[i]

    print(f"\n\nQUestion for RS.{levels[i]}")

    print(f"a.{question[1]}       B.{question[2]}")
    print(f"C.{question[3]}       D.{question[4]}")

    reply=int(input("enter your answer 1-4  or press 0 to QUIT\n"))
    if(reply == 0):
      money = levels[i-1]
      print(f"money for home {money}")
      break
    if(reply == question[-1]):
       print(f"correct answer you won  Rs.{levels[i]}")
       if(i == 4):
         money=10000
       elif(i == 9):
         money=320000
       elif(i == 14):
         money=10000000
    else:
     print(f"wrong Answer monry for home{money}")
     break
    
