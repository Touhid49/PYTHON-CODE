print("\U0001f600 Math Game ! \U0001f600")
print()
muliTable=int(input("Name your Multiples :"))
yourScore=0
for count in range (1,11,1):
  print()
  print(muliTable,"*",count,"= ?")
  ans=muliTable*count
  print()
  userAns=int(input("Tell me :"))
  
  if userAns == ans:
    print("Great Work! \N{winking face}")
    yourScore+=1
    print()
  else:
    print("Nope! Ans was \N{winking face}",ans)
    print()
   
print("\N{winking face} Your  Total score is :",yourScore,"Out of 10") 