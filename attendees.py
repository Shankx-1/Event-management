import storage

FILE_NAME = "attendees.csv"
FIELDS = ["name", "email", "event_id"]

def register_attendee():
    print("\nLet's register a new attendee!")

    event_id = input("Please enter the Event ID you want to join: ")
    name = input("What's the attendee's full name? ")
    email = input("And their email address? ")

    new_attendee = {
        "name": name,
        "email": email,
        "event_id": event_id
    }

    attendees = storage.read_file(FILE_NAME)
    attendees.append(new_attendee)
    storage.save_stuff(FILE_NAME, attendees, FIELDS)

    print(f"Awesome! {name} is now signed up for event {event_id}.")

def view_attendees():
    attendees = storage.read_file(FILE_NAME)

    print("\nHere's the list of all registered attendees:")
    if not attendees:
        print("Nothing here yet, no one has registered.")
    else:
        print(f"{'Event ID':<10} {'Name':<20} {'Email':<30}")
        print("-" * 60)
        for person in attendees:
            print(f"{person['event_id']:<10} {person['name']:<20} {person['email']:<30}")

def delete_attendee():
    view_attendees()

    print("\nIf you need to remove someone, just enter their email below.")
    email = input("Enter the email address to delete: ")

    attendees = storage.read_file(FILE_NAME)
    remaining_attendees = [a for a in attendees if a['email'] != email]

    if len(remaining_attendees) < len(attendees):
        storage.save_stuff(FILE_NAME, remaining_attendees, FIELDS)
        print(f"{email} has been removed from the list. All done!")
    else:
        print("Hmm, can't find that email. Please check and try again.")
