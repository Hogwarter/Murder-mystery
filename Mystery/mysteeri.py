from time import sleep


def blame(numberofchar: int):
    print()


def yard():
    print("You are standing in front of the Gallowgate Hall. In the summer the manor's lands are beautiful, but with the approaching winter the view is mounrful.")
    print("The rope that the victim hanged in is swaying in the wind and rain.")
    while True:
        print("What would you like to do?")

print ("It is bleak November. Westwind blows harsh and rain beats the moors.")
sleep(1)
print()
print("You are a consultant. A private detective. Known for your discretion, your name is well known in certain circles.")
sleep(1)
print()
playername = input("What is your name? ")

playertitle = ""
while True:
    if playertitle != "Mr." or playertitle != "Ms." or playertitle != "Detective":
        print("What is your title? \n1) Mr. \n2) Ms. \n3) Detective ")
        plorkok = input("Choose 1, 2 or 3: ")
        if plorkok == "1":
            playertitle = "Mr."
        elif plorkok == "2":
            playertitle = "Ms."
        elif plorkok == "3":
            playertitle = "Detective"
    
    if playertitle == "Mr." or playertitle != "Ms." or playertitle != "Detective":
        break

print(f"You are {playertitle} {playername}. A private detective who enjoys full confidence of the local police department. ")
print()
sleep(2)
print("You get a call from your friend in the police force, Sgt. Thomas.")
print()
sleep(2)
print("The Sergeant tells you that the Lord of the local manor has passed. As he is a man of some importance, they have requested a private detective to take over.")
print()
sleep(2)
print("You arrive in the Gallowgate Hall. The manorhouse is a desolate thing, maple trees surrounding the yard having long lost the rest of autumn's red glow.")
sleep(2)
print("One of the trees still carries the rope that Lord Gallowgate hanged in. The body has been removed and taken to the coroner's office.")
sleep(3)
print("Did the late Lord Gallowgate indeed hang himself? And if so, why were you called?")
while True:
    sleep(3)
    print("What would you like to do?")
    print("1) Go inside.")
    print("2) Study the police report.")
    firsatyeardchoice = input()
    if firsatyeardchoice == "2":
        print("You study the police report.")
        sleep(2)
        print("The deceased is Lord Robert Gallowgate. He was discovered by the Butler who was getting firewood. He called the body in 7 o'clock in the morning. The body was hanging from the tree.")
        print()
        sleep(3)
        print(f"Hanging was considered a potential suicide. However,Lord Gallowgate did not have a history of mental ailments. Because of this the house requested the involvement of you, {playertitle} {playername}.")
        sleep(3)
        print()
        print("The only people present last night were the wife of the victim, Lady Anne Gallowgate, the cook Marie Fraser and her husband the butler, Charles Fraser.")
        sleep(3)
        print()
        print("You should interview them and try to figure out what happened.")
        sleep(4)
        print("The body has been taken to the coroner's office. You should expect a call soon.")
    elif firsatyeardchoice == "1":
        break

sleep(3)
print("You walk up the stairs and knock on the door.")
sleep(2)
print("Knock")
sleep(2)
print("Knock")
sleep(2)
print("Knock")
sleep(3)
# breakpoint()
while True:
    print("A man in a clean pressed black suit opens the door.")
    sleep(2)
    print(f"'You must be {playertitle} {playername}. We have been expecting you.'")
    sleep(4)
    print("This must be the butler, Charles Fraser. He looks distraught.")
    sleep(1)
    print("1) My condolences.")
    print("2) That's me.")
    print("3) No shit Sherlock.")
    print("4) You must be mistaken, I am the milkman.")
    milkmanchoice = input()
    sleep(2)
    if milkmanchoice == "1":
        print("'Thank you.' He says. 'Please come in. There is someone on the phone for you.'")
        break
    elif milkmanchoice == "2":
        print("'Well then detective.' He responds. 'Please follow me. There is someone on the phone for you.'")
        break
    elif milkmanchoice == "3":
        print("He gives you a deadpan stare. 'Come in detective. There is someone on the phone for you.'")
        break
    elif milkmanchoice == "4":
        print("'This is truly no time to jest, *detective*.' He says, barely staying civil. 'There is someone on the phone for you. Come.")
        break
sleep (4)
print("Charles Fraser leads you inside.")
sleep(2)
print("You pick up the phone.")
sleep(2)
print(f"'{playertitle} {playername}?' A familiar voice says. 'I trust you are ready to hear about the gruesome details of the case?' The coroner asks.")
sleep(2)
print("1) Of course.")
print("2) I suppose.")
print("3) Nah, mate.")
print("4) Must I? I'm but a humble milkman")
sleep(2)
while True:
    milk2 = input()
    print()
    if milk2 == "1":
        sleep(1)
        print("'I admire your work ethic. Here we go then.'")
        break
    if milk2 == "2":
        sleep(1)
        print("'Here we go then.' The coroner muses.")
        break
    if milk2 == "3":
        sleep(1)
        print("'Well too bad.', the coroner says in good humour. 'Here goes anyway.'")
        break
    if milk2 == "4":
        sleep(1)
        print("'What is it with you and *milkmen?* Anyway, here goes.'")
        break
print()
sleep(2)
print("'The victim was found hanged, but that wasn't the cause of death. It seems he was lifted up to the tree postmortem. The cause of death seems to be a heavy sedative known as diphenhydramine. It is used in a number of medications. The time of death seems to be between 11 and 1 o'clock last night.")
sleep(5)
print()
print("1) It was murder then.")
print("2) Ominous.")
print("3) In my professional opinion as a milkman that seems pretty sus.")
sleep(2)
while True:
    milk3 = input()
    print()
    if milk3 == "1":
        sleep(1)
        print("'Indeed' He says. 'I sure am glad this is your job and not mine.'")
        break
    if milk3 == "2":
        sleep(1)
        print("'Yes. But nothing you can't handle I'm sure!'")
        break
    if milk3 == "3":
        sleep(1)
        print("'I don't disagree.' He says. 'You should probably focus on figuring out the murder though, and not your life as an aspiring milkman.'")
        break
sleep(3)
print()
print("'Good luck!' He says, hanging up.")
sleep(4)
print()
print("You to the Entrance Hall. The three suspects are waiting for you.")
print()



while True:
    print("The suspects are:")
    print("1. The wife, Lady Anne Gallowgate")
    print("2. The cook, Marie Fraser")
    print("3. The Butler, Charles Fraser")
    print("4. I should tour the house")
    sleep(1)
    talk_to = input(f"Who do you wish to converse with, {playername}?\n")
    if talk_to == "1":
        print(f"The wife: Yes? What did you need {playername}?")
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
        print(f"The cook: Yes? {playertitle}?")
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
        print(f"The butler: How can I be of service {playertitle}?")
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







