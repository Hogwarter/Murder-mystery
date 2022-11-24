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
    print("4. I know who did it!")
    talk_to = input(f"Who do you wish to converse with, {ur_name}?\n")
    if talk_to == "1":
        print(f"The wife: Yes? What did you need {ur_name}?")
        print("1. How would you describe your relationship with the victim?")
        print("2. Could you describe for me last night's events?")
        q = input("What shoud I ask?")
        if q == "1":
            print("The wife: You mean my husband Robert? Everything was just exemplary, perfect even.")
            print("(“She seems like she’s leaving something out”)")

        if q == "2":
            print("The wife: I was fast asleep. So I couldn*t say.")
            print("The wife: I might have called Marie to fetch me some water.")
            print("(“How could she not be sure? Seems like she knows more than she is letting on.”)")
            print("What shall I say?")
            print("1. Could you describe for me last night's events?")
            print("2. I’ll find out anyway so can you go into more detail?")
            i = input("")
            if i == "1":
                print("The wife: You mean my husband Robert? Everything was just exemplary, perfect even.")
                print("(“She seems like she’s leaving something out”)")
                
            if i == "2":
                print("The wife: I understand, but yesterday I just took my sleeping narcotics and slept like a baby.")
                print("(hmm, sleeping narcotics can be used as poison)")



    if talk_to == "2":
        print(f"The cook: Yes? {title}?")
        print("1. How would you describe your relationship with the victim?")
        print("2. Could you describe for me last night's events?")
        q = input("What shoud I ask?")
    if talk_to == "3":
        print(f"The butler: How can I be of service {title}?")
        print("1. How would you describe your relationship with the victim?")
        print("2. Could you describe for me last night's events?")
        q = input("What shoud I ask?")

    break









