print("Loan Calculator")
print("===========================")
totalAmmount=float(input("Enter the total ammount of money to know the total interest over 10 Years :"))

year=0
totalInterest=0
for counter in range(10):
  interestCalculate = ((totalAmmount*5)/100)
  perYearinterest=totalAmmount+interestCalculate
  paidperYear=round(perYearinterest,2)
  year+=1
  print(" Your",year," Year interest is :",paidperYear,"$")
  totalAmmount=paidperYear
  totalInterest=round((totalInterest+interestCalculate),2)
  
print()  
print("After 10 years total interest ammount will be :",totalInterest,"$")