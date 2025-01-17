# created 2023-04-27 by Zane Globus-O'Harra
# 

import time
import hashlib, hmac

import deviceutils


# {"user" : key} (these are entered into the table the first time the 
# user logs in with their account on the device)
SECRET_KEY_TABLE = {} 

# host/port info for the validation server.
# fixed here
# production version could read from file, user input, or scanned QR code
HOST = "127.0.0.1"
PORT = 65432

# functions to get user and key info
# fixed returns for this version
# production version could select user via input or QR code
# and key from stored key(s)
def get_user():
    return "test_user"


# gets the key for this device (single user)
# production version would probably read this from disk
def get_key():
    return "test_key"


# function to return an identifier
# for testing, using a fixed value
# for production, prompt for user entry or use command line
def get_identifier():
    # return 123456
    val = int(input("Enter identifier: "))
    return val


def set_host():
    h = input("Enter host address: ")
    return h


def set_port():
    p = int(input("Enter port number: "))
    return p

    
# alternate version using 
def generate_pin(identifier):
    time_s = int(time.time()) # get the time since epoch in seconds
    # print(time_s)
    msg = str(time_s ^ identifier)
    h = hmac.new(
        get_key().encode('utf-8'), 
        msg.encode('utf-8'), 
        hashlib.sha256
    )
    return h.hexdigest()


def main():
    host = set_host()
    # print("Host set to: ", host)
    port = set_port()
    id = get_identifier()
    user = get_user()
    pin = generate_pin(id)
    # print("Generated PIN: ", pin)
    # deviceutils.send_message(HOST, PORT, user, pin)
    deviceutils.send_message(host, port, user, pin)


if __name__ == "__main__":
    main()