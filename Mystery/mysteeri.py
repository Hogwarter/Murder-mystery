ur_name = input("What shall you be referd to as? (ex. Mrs. Fellow)")
title = "detective"
print("The murderd victim: Lord Robert Gallowgate")

while True:
    print("The suspects are:")
    print("1. The wife, Lady Anne Gallowgate")
    print("2. The cook, Marie Fraser")
    print("3. The Butler, Charles Fraser")
    print("")
    talk_to = input(f"Who do you wish to converse with, {ur_name}?")
    if talk_to == "1":
        print(f"The wife: Yes? What did you need {ur_name}?")
    if talk_to == "2":
        print(f"The cook: Yes? {title}?")
    if talk_to == "3":
        print(f"The butler: How can I be of service {title}?")

    break









