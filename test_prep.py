import guests
import hyde_park_signup
import configparser

if __name__ == "__main__":

    guests = guests.guests


    username, password = hyde_park_signup.read_config()
    print(username)
    print(password)
    # for guest in guests:
    #     guest = hyde_park_signup.prepare_guest(guest)
    #     print (guest)
