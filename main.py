# creating a dictonary


new_dict = {"trouble":"problem",
            "c++":"computer language",
            "update":"a new change",
            "dictionary":"a refrence eof book containing an alphabet list of words with information",
            "satya":"best place for student bright future"
            }

# if input founds
try:
    # taking inputs from the user
    inp1 = input("word:")

    # making non-case sensitive
    lowerinput = inp1.lower()

    # giving output to user
    for keys in new_dict:
        resultskeys = keys.find(lowerinput)
        if resultskeys != -1:
            print(keys + " means : " + new_dict[keys])

# if input not founds
except:
    print("No found")
