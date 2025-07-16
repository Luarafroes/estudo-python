# phonenumbers = {
#     "Manar": "1569741262",
#     "Nachos": "6884161179",
#     "Felix": "564852164126",
#     "Rodrigo": "65945165516",   
# }
# for key in sorted (phonenumbers.keys()):
#     print(key,":", phonenumbers[key])

import json
with open("data.json", "r") as file:
    data = json.load(file)

print(data)
print(data["Manar"])