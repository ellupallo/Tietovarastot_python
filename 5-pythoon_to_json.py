import json # sisältyy python asennukseen

# seuraavia python-objekteja voidaan konvertoida suoraan
# PYTHON <> JSON (KONVERSIO molempiin suuntiin)
# ******************************************************
# dict      Object
# list      Array
# tuple     Array
# str       String
# int       Number
# float     Number
# True      true ### HUOM!!!!!
# False     false
# None      null ### HUOM!!!!!
# ******************************************************

# d = dict-tiedosto
d = {
    "first_name":"Christian",
    "is_teacher": True,
    "cars": [
       {"brand": "Audi A2", "registerPlate:": "AAA-111"},
       {"brand": "Audi A3", "registerPlate:": "AAA-112"}
       ]
}
# ******************************************************

# DUMPS convert python dictionary object into string -> DUMPS
d_as_json = json.dumps(d) # dump to string (ei tiedostoon)
print(d_as_json)

d_as_json = json.dumps(d, indent=4, sort_keys=True) # dump to string (ei tiedostoon), sortaus muuttujien aakkosiin # separators= tsekkaa...
print(d_as_json)

print(type(d)) # dict
print(type(d_as_json)) # string

# SAVE json string to json file
with open("5-chrisu_string.json","w", encoding="utf-8") as file:
    file.write(d_as_json)

# DUMP save to file directly form python dictionary object  -> DUMP
with open("5-chrisu_dump.json", "w") as file:
    json.dump(d,file, indent=4)

# ******************************************************
