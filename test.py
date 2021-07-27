import random

def get_message(message):
    if "!hatch" in message:
        return hatch_dino(message)
    elif "!color" in message:
        return randomize_color()

def hatch_dino(message):
        maxLevel = [int(i) for i in message.split() if i.isdigit()]
        if len(maxLevel) > 0:
            dinoLevel = random.randrange(5, maxLevel[0])
            spawnLevel = dinoLevel / 1.5
            dinoCount = get_dino_count()
            response = "You had " + str(dinoCount) + " babies, level " + str(dinoLevel) + ", spawn level " + str(int(spawnLevel))
            return response
        else:
            return "Unable to process your request, try again in format '!hatch <maxLevel>"

def randomize_color():
    regionRoll = random.randrange(0,5)
    colorRoll = random.randrange(1,226)
    response = "Region " + str(regionRoll) + ", color " + str(colorRoll)
    return response

def get_dino_count():
    roll = random.randrange(1, 100)
    if roll in range(1,3):
        return 3
    elif roll in range(4,13):
        return 2
    else:
        return 1

message = input()

print(get_message(message))