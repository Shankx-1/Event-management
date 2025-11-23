import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_date():
    while True:
        d = input("put date here like 2023-12-25: ")
        p = d.split("-")

        if len(p) == 3 and len(p[0]) == 4 and len(p[1]) == 2 and len(p[2]) == 2:
            print("ok ok, that works iter guess")
            return d
        else:
            print("ugh lol wrong format, just do 2023-12-25")
