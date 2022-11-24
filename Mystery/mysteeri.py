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
    talk_to = input(f"Who do you wish to converse with, {ur_name}?\n")
    if talk_to == "1":
        print(f"The wife: Yes? What did you need {ur_name}?")
        print("1. How would you describe your relationship with the victim?")
        print("2. Could you describe for me last night's events?")
        q = input("What shoud I ask?")
        if q == "1":
            print("The wife: You mean my husband Robert? Everything was just exemplary, perfect even.")
            print("(She seems like she’s leaving something out)")
            print("What shall I say?")
            print("1. Could you describe for me last night's events?")
            print("2. I’ll find out anyway so can you go into more detail?")
            i = input("")
            if i == "1":
                print("The wife: I was fast asleep. So I couldn't say.")
                print("The wife: I might have called Marie to fetch me some water.")
                print("(How could she not be sure? Seems like she knows more than she is letting on.)")
            if i == "2":
                print("The wife: We had our ups and downs. But that’s just what married life is like. I loved him dearly.")
                print("(At least she seems to be honest)")
        if q == "2":
            print("The wife: I was fast asleep. So I couldn*t say.")
            print("The wife: I might have called Marie to fetch me some water.")
            print("(How could she not be sure? Seems like she knows more than she is letting on.)")
            print("What shall I say?")
            print("1. How would you describe your relationship with the victim?")
            print("2. I’ll find out anyway so can you go into more detail?")
            i = input("")
            if i == "1":
                print("The wife: You mean my husband Robert? Everything was just exemplary, perfect even.")
                print("(She seems like she’s leaving something out)")
            if i == "2":
                print("The wife: I understand, but yesterday I just took my sleeping narcotics and slept like a baby.")
                print("(hmm, sleeping narcotics can be used as poison)")



    if talk_to == "2":
        print(f"The cook: Yes? {title}?")
        print("1. How would you describe your relationship with the victim?")
        print("2. Could you describe for me last night's events?")
        q = input("What shoud I ask?")
        if q == "1":
            print("The cook: We had a professional relationship.")
            print("(She seems quite neutral)")
            print("What shall I say?")
            print("1. Could you describe for me last night's events?")
            print("2. I’ll find out anyway so can you go into more detail?")
            i = input("")
            if i == "1":
                print("The cook: I left to meet with a friend of mine after dinner. Though when I returned in the wee hours of the morning, I’m certain I saw a shadow moving near the woods north of here.")
                print("(Hmm, could the shady person be the killer…)")
            if i == "2":
                print("The cook: I worked for him, nothing more, nothing less.")
                print("(It seems that the victim and Marie are not that close. At least based on her answers…)")
        if q == "2":
            print("The cook: I left to meet with a friend of mine after dinner. Though when I returned in the wee hours of the morning, I’m certain I saw a shadow moving near the woods north of here.")
            print("(Hmm, could the shady person be the killer…)")
            print("What shall I say?")
            print("1. How would you describe your relationship with the victim?")
            print("2. I’ll find out anyway so can you go into more detail?")
            i = input("")
            if i == "1":
                print("The cook: I worked for him, nothing more, nothing less.")
                print("(It seems that the victim and Marie are not that close. At least based on her answers…)")
            if i == "2":
                print("The cook: It was very dark so I could not see very well but it looked like a big man's shadow. It was around 11pm I believe.")
                print("(it would've been dark by 11pm.. maybe she had a torch)")


    if talk_to == "3":
        print(f"The butler: How can I be of service {title}?")
        print("1. How would you describe your relationship with the victim?")
        print("2. Could you describe for me last night's events?")
        q = input("What shoud I ask?")
        q = input("What shoud I ask?")
        if q == "1":
            print("He was the best man that I’ve ever… worked for.")
            print("What shall I say?")
            print("1. Could you describe for me last night's events?")
            print("2. I’ll find out anyway so can you go into more detail?")
            i = input("")
            if i == "1":
                print("It was freezing last night so I took care of the fires at the hall.")
            if i == "2":
                print("Well… He was… a good man but I didn’t really know him well.")
                print("(At least she seems to be honest)")
        if q == "2":
            print("It was freezing last night so I took care of the fires at the hall.")
            print("What shall I say?")
            print("1. How would you describe your relationship with the victim?")
            print("2. I’ll find out anyway so can you go into more detail?")
            i = input("")
            if i == "1":
                print("He was the best man that I’ve ever… worked for.")
                print("(She seems like she’s leaving something out)")
            if i == "2":
                print("I remember hearing some noises from outside when I was aand todaydding wood to the fireplace.")
                print("(Hmm could that have been noises from the murder?)")
    if talk_to == "4":
        print("Onwards, says the milk man!")

    break









