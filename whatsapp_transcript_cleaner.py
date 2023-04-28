import os

print("\nWhatsapp Chat Transcript Modifier")
print("1. Bulk Remove Timestamp and name of the sender")
print("2. Bulk Remove Timestamp and preserve the name of the sender")
print("3. Modify individual files in the directory")

while True:
    choice = input("Enter the Choice: ")
    if choice not in ['1', '2', '3']:
        print("Invalid Choice, please enter a valid choice (1/2/3)")
    else:
        choice = int(choice)
        break

if choice == 1:
    print("\n")
    output_dir = "modified_files"
    os.makedirs(output_dir, exist_ok=True)
    for file_name in os.listdir():
        if file_name.endswith('.txt'):
            with open(file_name, 'r', encoding='utf-8') as inFile, \
                 open(os.path.join(output_dir, file_name), 'w', encoding='utf-8') as outFile:
                for line in inFile:
                    char_to_find = ":"
                    count = 0
                    for i, char in enumerate(line):
                        if char == char_to_find:
                            count += 1
                            if count == 3:
                                mod = line[i+1:]
                                mod = mod.lstrip()
                                outFile.write(mod)
                                break

elif choice == 2:
    print("\n")
    output_dir = "modified_files"
    os.makedirs(output_dir, exist_ok=True)
    for file_name in os.listdir():
        if file_name.endswith('.txt'):
            with open(file_name, 'r', encoding='utf-8') as inFile, \
                 open(os.path.join(output_dir, file_name), 'w', encoding='utf-8') as outFile:
                for line in inFile:
                    mod = line[23:]
                    mod = mod.lstrip()
                    outFile.write(mod)

elif choice == 3:
    print("\n")
    output_dir = "modified_files"
    os.makedirs(output_dir, exist_ok=True)
    for file_name in os.listdir():
        if file_name.endswith('.txt'):
            print("\n")
            print(f"Processing {file_name}")
            print("1. Remove Timestamp and name of the sender")
            print("2. Remove Timestamp and preserve the name of the sender")

            while True:
                file_choice = input("Enter the Choice: ")
                if file_choice not in ['1', '2']:
                    print("Invalid Choice, please enter a valid choice (1/2/3)")
                else:
                    file_choice = int(file_choice)
                    break
            with open(file_name, 'r', encoding='utf-8') as inFile, \
                 open(os.path.join(output_dir, file_name), 'w', encoding='utf-8') as outFile:
                if file_choice == 1:
                    for line in inFile:
                        char_to_find = ":"
                        count = 0
                        for i, char in enumerate(line):
                            if char == char_to_find:
                                count += 1
                                if count == 3:
                                    mod = line[i+1:]
                                    mod = mod.lstrip()
                                    outFile.write(mod)
                                    break
                elif file_choice == 2:
                    for line in inFile:
                        mod = line[23:]
                        mod = mod.lstrip()
                        outFile.write(mod)
