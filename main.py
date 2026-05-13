## Project = CRUD Operations...

## CRUD = Create Read Update Delete

from pathlib import Path 
import os

def readFileandFolder():
    try:
        p = Path('') ## Path empty isliye chora hai kyuki issi folder me work kar rhe hai.
        items = list(p.rglob('*')) ## rglob ek aisa function hai jo us directory me 
        ## present saari files ko bunch krke ek list me store kar dega
        for index,item in enumerate(items):
            print(f"{index + 1} - {item}")
    except Exception as e:
        print(e)

def create_file():
    try:
        readFileandFolder()
        file_name = input('Enter the name of your file :-> ')
        p = Path(file_name)
        if p.exists():
            print('File already exists......')
        else:
            with open(file_name,'w') as file:
                print('File created successfully......')
                content = input("Enter your file content :-> ")
                file.write(content)
                print('Your content is successfully written and saved to the file.....')
    except Exception as e:
        print(e)

def read_file():
    try:
        readFileandFolder()
        file_name = input('Enter the name of your file which you want to read :-> ')
        p = Path(file_name)
        if p.exists():
            with open(file_name,'r') as file:
                print(file.read())
        else:
            print('File does not exists......')
    except Exception as e:
        print(e)

def update_file():
    try:
        readFileandFolder()
        file_name = input('Enter the name of your file which you want to update :-> ')
        p = Path(file_name)
        if p.exists():
            print("Press a if you only want to update.")
            print("Press b if you want to overwrite.")
            ask = input("Enter what do you want to update :-")
            if ask == "a":
                with open(file_name,'a') as file:
                    update = input("Enter your content :->")
                    print('\n')
                    file.write(update)
                    print('Your file is update.....')
            elif ask == "b":
                with open(file_name,'w') as file:
                    write = input("What you want to write :->")
                    file.write(write)
                    print('Your file is overwritten.....')
            else:
                print('Invalid option.....')
        else:
            print('File does not exists.....')
    except Exception as e:
        print(e)

def delete_file():
    try:
        readFileandFolder()
        file_name = input('Enter the name of your file which you want to delete => ')
        p = Path(file_name)
        if p.exists():
            os.remove(p) ## OS is removing path of that file completely.....
            print("File deleted...")
        else:
            print("File does not exists....")
        
    except Exception as e:
        print(e)

def rename_file():
    try:
        readFileandFolder()
        file_name = input('Enter the name of the file you want to rename => ')
        p = Path(file_name)
        if p.exists():
            new_name = input('Enter the new name of your file => ')
            p.rename(new_name)
            print('FILE RENAMED')
        else:
            print('File does not exists...')
    except Exception as e:
        print(e)

def create_folder():
    try:
        readFileandFolder()
        folder_name = input('Enter the name of your folder => ')
        p = Path(folder_name)
        if p.exists():
            print('Folder already exists....')
        else:
            p.mkdir()
            print('Folder created....')
    except Exception as e:
        print(e)

def delete_folder():
    try:
        readFileandFolder()
        folder_name = input('Enter the name of your folder that you want to delete => ')
        p = Path(folder_name)
        if p.exists():
            p.rmdir()
            print('Folder is deleted.....')
        else:
            print('File does not exists.....')
    except Exception as e:
        print(e)

def create_file_in_folder():
    try:
        readFileandFolder()
        folder_name = input('Enter your folder name =>')
        file_name = input('Enter your file name =>')
        p = Path(folder_name)/file_name
        if p.exists():
            print('File already exists....')
        else:
            with open(p,'w') as file:
                print('File created successfully.....')
                content = input('Enter your content :=> ')
                file.write(content)
                print('Your content is successfully written and saved....')    
    except Exception as e:
        print(e)

while True:
    print("Press 1 for creating a file.")
    print("Press 2 for reading a file.")
    print("Press 3 for updating a file.")
    print("Press 4 for deleting a file.")
    print("Press 5 for renaming a file.")
    print("Press 6 for creating a folder.")
    print("Press 7 for deleting a folder.")
    print("Press 8 for creating a file inside a folder.")
    print("Press 0 for exiting......")

    option = int(input("Enter your choice :"))

    if option == 1:
        create_file()
    if option == 2:
        read_file()
    if option == 3:
        update_file()
    if option == 4:
        delete_file()
    if option == 5:
        rename_file()
    if option == 6:
        create_folder()
    if option == 7:
        delete_folder()
    if option == 8:
        create_file_in_folder()
    if option == 0:
        break