import json

# The below converts a JSON 'file' to a Python dct
with open ("json.json") as data:
    python_dict = json.load(data)

print(python_dict)

# The below converts a Python serialized string (of JSON content) to a Python dict
with open("json.json") as data:
    json_string = data.read()

print(json_string) # Halfway point - print this prints the raw file contents including formatting, line spacing and indentation
python_dict = json.loads(json_string)

print(python_dict)
