import json
roster= ('JavaScript', 10)
encoded_roster = json.dumps(roster) #dumping into encoded
try:
    with open("data_file.json", "w") as write_file:
        json.dump(roster, write_file)
except IOError as e:
    print('Error writing a file', e)
finally:
    write_file.close()
print("Encoded: ", encoded_roster, type(encoded_roster))

print("time passes - and now we reopen the file")
decoded_roster = None
try:
    with open("data_file.json", "r") as read_file:
        decoded_roster= json.load(read_file)
except IOError as e:
    print('Error reading a file', e)
finally:
    read_file.close()
if (decoded_roster != None):
    print("Decoded: ", decoded_roster, type(decoded_roster))

    print("Decoded equal roster? ", roster == decoded_roster)
    print("Tuple converted Decoded equal roster? ",
          roster == tuple(decoded_roster))
else: print('Cannot get the old roster')

