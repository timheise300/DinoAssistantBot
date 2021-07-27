import responseutils

def get_message(message):
    if "!hatch" in message:
        return responseutils.hatch_dino(message)
    elif "!color" in message:
        return responseutils.randomize_color()

message = input()

print(get_message(message))