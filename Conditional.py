userReply = input("Do you need to ship a package? (Enter yes or no) ")

if userReply == "yes":
    print("we can help you ship that package!")
else:
    print("Please come back when you need to ship a a package. Thank you")
    
userReplyy = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReplyy == "stamps":
    print("We have many stamp designs to choose from.")
elif userReplyy == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReplyy == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")