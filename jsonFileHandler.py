import json 

def readJsonFile(filename):
    data=""
    # open the json file using the open function, 
    #and parse the file using json.load.
    # Add a try/except block to make this function more reliable:
    try:
    with open('files/insulin.json') as json_file:
        data = json.load(json_file)
    return data
    except IOError:
        print("Could not read file")
    return data 
# You created a jsonFileHandle module that you can import in other Python files to access the readJsonFile function.
