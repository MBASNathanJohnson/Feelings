import random


def happy():
    # picks a random number 1-3 then chooses a quote based on that number
    randomnum = random.randint(1, 3)
    if randomnum == 1:
        print("“Learn to value yourself, which means: fight for your happiness.” – Ayn Rand")
    elif randomnum == 2:
        print(
            "“The true secret of happiness lies in the taking a genuine interest in all the details of daily life.” – "
            "William Morris")
    else:
        print(
            "“The greatest happiness you can have is knowing that you do not necessarily require happiness.” – "
            "William Saroyan")


def sad():
    # picks a random number 1-3 then chooses a quote based on that number
    randomnum = random.randint(1, 3)
    if randomnum == 1:
        print("“The secret of happiness is freedom, the secret of freedom is courage.” – Carrie Jones")
    elif randomnum == 2:
        print("“Nobody really cares if you’re miserable, so you might as well be happy.” – Cynthia Nelms")
    else:
        print(
            "“We can’t control the world. We can only (barely) control our own reactions to it. Happiness is largely "
            "a choice, not a right or entitlement.” – David C. Hill")


def inspired():
    # picks a random number 1-3 then chooses a quote based on that number
    randomnum = random.randint(1, 3)
    if randomnum == 1:
        print(
            "“Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible.” - "
            "Francis of Assisi")
    elif randomnum == 2:
        print(
            "“I can't change the direction of the wind, but I can adjust my sails to always reach my destination.” - "
            "Jimmy Dean")
    else:
        print("“The sooner you give up, the sooner you can move on.” - Nathan Johnson")


def poor():
    # picks a random number 1-3 then chooses a quote based on that number
    randomnum = random.randint(1, 3)
    if randomnum == 1:
        print("“Stocks only go up” - Nathan Johnson")
    elif randomnum == 2:
        print("“Price is what you pay. Value is what you get.” - Warren Buffet")
    else:
        print("“When in doubt, zoom out.” -Davincij15")


# Sets done to False to allow the loop to run
done = False
# Asks the user their name
name = input("What is your name? ")
while not done:
    print("""
###############################################
#               Feelings Menu                 #
#                                             #
#                                             #
# A. Happy                                    #
# B. Sad                                      #
# C. Inspired                                 #
# D. Poor                                     #
#                                             #
###############################################
    """)
    # prints the users name to add to the "experience"
    print("Hi", name)
    # Gets the user input and stores it in selection
    selection = input("How are you feeling? ")
    # if you pick Happy
    if selection in ("A", "a"):
        happy()

    # if you pick sad
    if selection in ("B", "b"):
        sad()

    # if you pick Inspired
    if selection in ("C", "c"):
        inspired()

    # if you pick poor
    if selection in ("D", "d"):
        poor()
