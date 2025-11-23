import csv
import os

def save_stuff(file_name, stuff, headers):
    print("ok starting to save...")

    f = open(file_name, "w", newline="")
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()

    for pos in range(len(stuff)):
        row = stuff[pos]
        writer.writerow(row)
        print("just saved row", pos)

    f.close()
    print("yay! all done saving :)")

def read_file(file_name):
    if not os.path.exists(file_name):
        print("uh oh file not found :(")
        return []

    f = open(file_name, "r")
    reader = csv.DictReader(f)

    all_rows = []
    for element in reader:
        all_rows.append(element)
        print("read a row...")

    f.close()
    print("all done reading :)")
    return all_rows

def save_to_csv(file_name, data, headers):
    return save_stuff(file_name, data, headers)

def load_from_csv(file_name):
    return read_file(file_name)
