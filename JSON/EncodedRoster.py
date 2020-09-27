import json
roster= ('JavaScript', 10)
with open("data_file.json", "w") as write_file:
    encoded_roster = json.dump(roster, write_file)
print("Encoded: ", encoded_roster, type(encoded_roster))
