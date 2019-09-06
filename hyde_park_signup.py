# /usr/bin/python

import requests
import guests
import datetime
import emailer
import configparser


def read_config():
    config = configparser.ConfigParser()
    config.read('./config.ini')

    username = config["DEFAULT"]["USERNAME"]
    password = config["DEFAULT"]["PASSWORD"]

    return username, password


def get_formatted_today():
    return str(datetime.date.today())

def prepare_guest(guest):

    print(guest["email"])
    guest.update(email2 = guest["email"])

    guest.update([('dowhat', 'submitform'),('emailaddress', 'submitform')])

    today = get_formatted_today()

    guest.update(resDate = today)

    return guest

if __name__ == "__main__":

    URL = "http://thehydeparkcafe.com/guestlist-signup.php"

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    guests = guests.guests

    for guest in guests:

        body = prepare_guest(guest)

        r = requests.post(URL, data=body, headers=headers)

        username, password = read_config()
        emailer.send_response_to_email(username, password, guest["email"], r)
