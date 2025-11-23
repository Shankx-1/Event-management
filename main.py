import events
import attendees
import utils

def main_menu():
    while True:
        print("\t===================")
        print("EVENT MANAGEMENT")
        print("===================")
        print("1. add new event")
        print("2. view all events")
        print("3. delete event")
        print("4. register attendee")
        print("5. view all attendees")
        print("6. delete attendee")
        print("7. exit")

        choice = input("pick a number 1-7: ")

        if choice == "1":
            events.add_event()
        elif choice == "2":
            events.list_events()
        elif choice == "3":
            events.delete_event()
        elif choice == "4":
            events.list_events()
            attendees.register_attendee()
        elif choice == "5":
            attendees.view_attendees()
        elif choice == "6":
            attendees.delete_attendee()
        elif choice == "7":
            print("ok bye")
            break
        else:
            print("dude, invalid choice")

        input("press enter to continue...")
        utils.clear_screen()

if __name__ == "__main__":
    utils.clear_screen()
    main_menu()
