# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

weight = float(weight)
height = float(height)
bmi = weight/(height**2)
print(int(bmi))