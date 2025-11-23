import random
import storage
from utils import get_valid_date

FILE_NAME = "events.csv"
FIELDS = ["event_id", "name", "date", "location"]

def add_event():
    print("--- adding new event ---")
    size = input("name: ")
    d = get_valid_date()
    l = input("location: ")

    eid = random.randint(1000, 9999)

    new = {
        "event_id": str(eid),
        "name": size,
        "date": d,
        "location": l
    }

    evs = storage.load_from_csv(FILE_NAME)
    evs.append(new)
    storage.save_to_csv(FILE_NAME, evs, FIELDS)
    print("done! event added, id=", eid)

def list_events():
    evs = storage.load_from_csv(FILE_NAME)
    print("--- all events ---")
    if not evs:
        print("no events yet lol")
    else:
        print("ID       Name                 Date           Location")
        print("-" * 50)
        for e in evs:
            print(e["event_id"], e["name"], e["date"], e["location"])

def delete_event():
    list_events()
    print("--- delete an event ---")
    eid = input("type event id to delete: ")

    evs = storage.load_from_csv(FILE_NAME)
    newlist = []
    found = False

    for e in evs:
        if e["event_id"] != eid:
            newlist.append(e)
        else:
            found = True

    if found:
        storage.save_to_csv(FILE_NAME, newlist, FIELDS)
        print("ok deleted id", eid)
    else:
        print("cant find that id, check and try again")
