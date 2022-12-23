PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as f_names:
    names = f_names.readlines()

with open("./Input/Letters/starting_letter.txt") as file:
    let = file.read()
    for name in names:
        striped_name = name.strip()
        new_letter = let.replace(PLACEHOLDER, striped_name)
        with open(f"./Output/ReadyToSend/letter_of_{striped_name}.txt", mode="w") as complete:
            complete.write(new_letter)