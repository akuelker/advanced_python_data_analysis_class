import json

def encode(stuff, fileName = None):
    encoded = None
    if (fileName != None):
        with open(fileName, "w") as write_file:
                  encoded = json.dump(stuff, write_file)
    else: encoded =json.dumps(stuff)
    return encoded
    
def decode(stuff, objectType = None):
    decoded = json.loads(stuff)
    if objectType == tuple:
        decoded = tuple(decoded)
    return decoded

def decodeFile(fileName, objectType = None):
    decoded = None
    with open(fileName, "r") as read_file:
            decoded = json.load(read_file)
    if objectType == tuple:
        decoded = tuple(decoded)
    return decoded
