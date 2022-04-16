name_list = []
with open("./Input/Names/invited_names.txt") as invited:
    for line in invited:
        name_list.append(line.strip())

for name in name_list:
    with open("./Input/Letters/starting_letter.txt") as start_letter:
        letter_content = start_letter.read()

    with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as test_file:
        letter_content = letter_content.replace("[name]", name)
        test_file.write(letter_content)
