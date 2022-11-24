from time import sleep

ur_name = input("What shall you be referd to as? (ex. Mrs. Fellow)\n")
title = "detective"
print("The murderd victim: Lord Robert Gallowgate")
print("As you arrive")
print("1. House tour")
print("2. Call forensics")
print("3. I'd rather just go straight to the suspects")
choise = input("What shall you do?\n")
if choise == "1":
    print("Tour")
if choise == "2":
    print("call")
if choise == "3":
    pass

while True:
    print("The suspects are:")
    print("1. The wife, Lady Anne Gallowgate")
    print("2. The cook, Marie Fraser")
    print("3. The Butler, Charles Fraser")
    print("4. I should tour the house")
    sleep(1)
    talk_to = input(f"Who do you wish to converse with, {ur_name}?\n")
    if talk_to == "1":
        print(f"The wife: Yes? What did you need {ur_name}?")
        sleep(1)
        print("1. How would you describe your relationship with the victim?")
        print("2. Could you describe for me last night's events?")
        sleep(1)
        q = input("What shoud I ask?")
        if q == "1":
            sleep(1)
            print("The wife: You mean my husband Robert? Everything was just exemplary, perfect even.")
            sleep(1)
            print("(She seems like she’s leaving something out)")
            print("What shall I say?")
            sleep(1)
            print("1. Could you describe for me last night's events?")
            print("2. I’ll find out anyway so can you go into more detail?")
            i = input("")
            if i == "1":
                sleep(1)
                print("The wife: I was fast asleep. So I couldn't say.")
                sleep(1)
                print("The wife: I might have called Marie to fetch me some water.")
                sleep(1)
                print("(How could she not be sure? Seems like she knows more than she is letting on.)")
            if i == "2":
                sleep(1)
                print("The wife: We had our ups and downs. But that’s just what married life is like. I loved him dearly.")
                sleep(1)
                print("(At least she seems to be honest)")
        if q == "2":
            sleep(1)
            print("The wife: I was fast asleep. So I couldn*t say.")
            sleep(1)
            print("The wife: I might have called Marie to fetch me some water.")
            sleep(1)
            print("(How could she not be sure? Seems like she knows more than she is letting on.)")
            sleep(1)
            print("What shall I say?")
            print("1. How would you describe your relationship with the victim?")
            print("2. I’ll find out anyway so can you go into more detail?")
            i = input("")
            if i == "1":
                sleep(1)
                print("The wife: You mean my husband Robert? Everything was just exemplary, perfect even.")
                sleep(2)
                print("(She seems like she’s leaving something out)")
            if i == "2":
                sleep(1)
                print("The wife: I understand, but yesterday I just took my sleeping narcotics and slept like a baby.")
                sleep(3)
                print("(hmm, sleeping narcotics can be used as poison)")



    if talk_to == "2":
        print(f"The cook: Yes? {title}?")
        sleep(1)
        print("1. How would you describe your relationship with the victim?")
        print("2. Could you describe for me last night's events?")
        q = input("What shoud I ask?")
        if q == "1":
            sleep(1)
            print("The cook: We had a professional relationship.")
            sleep(1)
            print("(She seems quite neutral)")
            sleep(1)
            print("What shall I say?")
            print("1. Could you describe for me last night's events?")
            print("2. I’ll find out anyway so can you go into more detail?")
            i = input("")
            if i == "1":
                sleep(1)
                print("The cook: I left to meet with a friend of mine after dinner. Though when I returned in the wee hours of the morning, I’m certain I saw a shadow moving near the woods north of here.")
                sleep(1)
                print("(Hmm, could the shady person be the killer…)")
            if i == "2":
                sleep(1)
                print("The cook: I worked for him, nothing more, nothing less.")
                sleep(1)
                print("(It seems that the victim and Marie are not that close. At least based on her answers…)")
        if q == "2":
            sleep(1)
            print("The cook: I left to meet with a friend of mine after dinner. Though when I returned in the wee hours of the morning, I’m certain I saw a shadow moving near the woods north of here.")
            sleep(1)
            print("(Hmm, could the shady person be the killer…)")
            sleep(1)
            print("What shall I say?")
            print("1. How would you describe your relationship with the victim?")
            print("2. I’ll find out anyway so can you go into more detail?")
            i = input("")
            if i == "1":
                sleep(1)
                print("The cook: I worked for him, nothing more, nothing less.")
                sleep(1)
                print("(It seems that the victim and Marie are not that close. At least based on her answers…)")
            if i == "2":
                sleep(1)
                print("The cook: It was very dark so I could not see very well but it looked like a big man's shadow. It was around 11pm I believe.")
                sleep(1)
                print("(it would've been dark by 11pm.. maybe she had a torch)")


    if talk_to == "3":
        print(f"The butler: How can I be of service {title}?")
        sleep(1)
        print("1. How would you describe your relationship with the victim?")
        print("2. Could you describe for me last night's events?")
        q = input("What shoud I ask?")
        if q == "1":
            sleep(1)
            print("He was the best man that I’ve ever… worked for.")
            sleep(1)
            print("What shall I say?")
            print("1. Could you describe for me last night's events?")
            print("2. I’ll find out anyway so can you go into more detail?")
            i = input("")
            if i == "1":
                sleep(1)
                print("It was freezing last night so I took care of the fires at the hall.")
            if i == "2":
                sleep(1)
                print("Well… He was… a good man but I didn’t really know him well.")
                sleep(1)
                print("(At least she seems to be honest)")
        if q == "2":
            sleep(1)
            print("It was freezing last night so I took care of the fires at the hall.")
            sleep(1)
            print("What shall I say?")
            print("1. How would you describe your relationship with the victim?")
            print("2. I’ll find out anyway so can you go into more detail?")
            i = input("")
            if i == "1":
                sleep(1)
                print("He was the best man that I’ve ever… worked for.")
                sleep(1)
                print("(She seems like she’s leaving something out)")
            if i == "2":
                sleep(1)
                print("I remember hearing some noises from outside when I was aand todaydding wood to the fireplace.")
                sleep(2)
                print("(Hmm could that have been noises from the murder?)")
    if talk_to == "4":
        print("Onwards, says the milk man!")

    break

print("(I should go through the site now.)")
sleep(1)
print("You should inspect the entrance hall, the bedroom, the kitchen and the yard.")
sleep(1)
print("(I guess the order does not matter.)")
sleep(1)
print("You walk to the entrance hall")
sleep(1)
print("Do you want to inspect the fireplace (Choice 1) or the room overall (Choice 2)?")
sleep(3)
print("Type 1 or 2")
syoteyksi=input()
 
if syoteyksi==1:
    print("You croush down and look inside the fireplace. You see some remains of what seems to be burned letters.")
    sleep(3)
    print("At the end of one of the letters seems to read 'Lets run away together, I cannot live without you'")
    sleep(3)
    print("(Hmmm...I wonder between whom these letters are.)")
elif syoteyksi==2:
    print("Walking around the room you find nothing interesting.")
 
sleep(2)
print("After leaving the entrance hall, you arrive to the bedroom")
sleep(2)
print("Do you want to inspect the bed (Choice 1) or the nightstand (Choice 2)?")
sleep(2)
print("Type 1 or 2")
syotekaksi=input()
 
 
if syotekaksi==1:
    print("The other side of the bed seems neat and not slept in.")
    sleep(2)
    print("(Seems that the victim did not come to bed last night.)")
elif syotekaksi==2:
    print("You find some strong sleeping narcotics on the nightstand.")
    sleep(2)
    print("(With a big amount one could even possible poison another)")
sleep(2)
print("Next you head to the kitchen.")
sleep(2)
print("You see a very expensive looking ring.")
sleep(2)
print("(I think this is the wife's ring. A fine lady would not hang around in the kitchen for no reason)")
sleep(2)
print("You leave the kitchen and finally arrive at the yard.")
sleep(2)
print("Do you want to inspect the tree where the lord was found hanging from (Choice 1) or the ground for footsteps in the mud (Choice 2)?")
sleep(2)
print("Type 1 or 2")
syotekak=input()
if syotekak==1:
    print("(The branch of the tree seems too slippery for someone to hang themselves from)")
    sleep(2)
    print("(I did not gain any completely new information but now I can be sure that this case was not a suicide)")
elif syotekak==2:
    print("After a closer look you notice two people's footsteps that lead to the tree.")
    sleep(2)
    print("(Could there be multiple culplits. Interesting...)")





#syotekolme = input()

#if syotekolme==1:
#    print("(The branch of the tree seems too slippery for someone to hang themselves from)")
#    sleep(2)
#    print("(I did not gain any completely new information but now I can be sure that this case was not a suicide)")
#elif syotekolme==2:
#    print("After a closer look you notice two people's footsteps that lead to the tree.")
#    sleep(2)
#    print("(Could there be multiple culplits. Interesting...)")

print("Done")







