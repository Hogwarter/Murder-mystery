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
        q = input("k")
    if talk_to == "2":
        print(f"The cook: Yes? {title}?")
    if talk_to == "3":
        print(f"The butler: How can I be of service {title}?")

    break









