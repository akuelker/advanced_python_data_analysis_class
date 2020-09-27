import json
roster = ('Python', 7)
try:
    with open('data_file.json', 'w') as write_file:
        json.dump(roster, write_file)
except IOError as e:
    print('Error writing to a file', e)
finally: 
    write_file.close()
try:
    with open('data_file.json', 'r') as read_file:
        decoded_roster = json.load(read_file)
except IOError as e:
        print('Error opening file', e)
finally:
    read_file.close()
#print('Decoded', decoded_roster)
#print('Decoded == Encoded', decoded_roster == encoded_roster)
print('Tuple Decoded', roster == tuple(decoded_roster))