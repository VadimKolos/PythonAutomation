import json

# TXT file
with open("example.txt", "w") as txtFile:
    txtFile.write("Text")
    txtFile.write("Rewrighted text.\n")
    myText = open("example.txt")
print(myText.read())

with open("example.txt", "w") as txtFile:
    txtFile.write("EditedText")
    print("Done.")

#JSON
data = {
    "username": "user",
    "password": 1234
}

with open("JSONexample.json", "w") as jsonFile:
    json.dump(data, jsonFile)

editedJson = open("JSONexample.json")
print(editedJson.read())
