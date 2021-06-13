PLACEHOLDER = "[name]"

with open("/Users/Prana/Documents/pythonProjects/mail/Mail Merge Project Start/Input/Names/invited_names.txt",
          ) as names_file:
    names = names_file.readlines()

with open("/Users/Prana/Documents/pythonProjects/mail/Mail Merge Project Start/Input/Letters/starting_letter.txt",
          mode="r") as letter:
    letter_contents = letter.read()
    for name in names:
        name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER,name)
        with open(f"/Users/Prana/Documents/pythonProjects/mail/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt",
                  mode="w") as final_letter:
            final_letter.write(new_letter)




