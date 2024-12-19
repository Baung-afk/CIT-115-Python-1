#Inputs
PV = float(input("Enter the starting principal: "))
R = float(input("Enter the annual interest rate: ")) / 100
m = float(input("How many times per year is the interest compounded? "))
t = int(input("For how many years will the account earn interest? "))

#Calculation
FV = PV * (1+R/m) ** (m*t)

#Output
print("At the end of " + str(t) + " years you will have $ " + format(FV,',.2f'))
