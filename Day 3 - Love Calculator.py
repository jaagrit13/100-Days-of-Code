# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()
tcount = name1_lower.count("t") + name2_lower.count("t")
rcount = name1_lower.count("r") + name2_lower.count("r")
ucount = name1_lower.count("u") + name2_lower.count("u")
ecount = name1_lower.count("e") + name2_lower.count("e")

truecount = tcount + rcount + ucount + ecount

lcount = name1_lower.count("l") + name2_lower.count("l")
ocount = name1_lower.count("o") + name2_lower.count("o")
vcount = name1_lower.count("v") + name2_lower.count("v")

lovecount = lcount + ocount + vcount + ecount

lovescore = truecount*10 + lovecount

if lovescore < 10 or lovescore > 90:
  print("Your score is {}, you go together like coke and mentos.".format(lovescore))
elif lovescore > 40 and lovescore < 50:
  print("Your score is {}, you are alright together.".format(lovescore))
else:
  print("Your score is {}.".format(lovescore))