st =str(input("enter the message:"))
words = st.split(" ")
coding = False
if(coding):
  nwords=[]
  for word in words:
   
    if (len(word)>=3):
         random1="psg"
         random2="gps"
         stnew= random1 + word[1:] + word[0] + random2
         nwords.append(stnew)
    else:
         nwords.append(word[::-1]) 

  print(" ".join(nwords))


else:
    nwords=[]
    for word in words:
   
     if (len(word)>=3):
        stnew= word[3:-3]
        stnew= stnew[-1] + stnew[:-1]
        nwords.append(stnew)
     else:
        nwords.append(word[::-1])

    print(" ".join(nwords))     
