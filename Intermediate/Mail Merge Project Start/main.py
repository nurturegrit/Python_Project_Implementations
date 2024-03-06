#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
def mail():
    with open("./Input/Letters/starting_letter.txt",'r') as file:
        contents = file.read()
    return contents

def name_list():
    name_list = []
    with open("./Input/Names/invited_names.txt",'r') as file:
        for line in file.readlines():
            name_list.append(line.strip())
        return name_list

def personlize_letter(name,letter):
    letter = letter.replace('[name]',name)
    return letter

def main():
    for name in name_list():
        letter = mail()
        letter = personlize_letter(name,letter)
        with open(f'./Output/ReadyToSend/{name}.txt','w+') as file:
            file.write(letter)

if __name__ == '__main__':
    main()