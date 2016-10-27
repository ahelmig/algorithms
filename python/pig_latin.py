def eval(string):
    for char in string:
        if string [0] not in ['a','e', 'i', 'o', 'u']:
            if string[1] in ['a', 'e', 'i', 'o', 'u']:
                pig_string = string[1:]+string[0]+'ay'
            else:
                pig_string = string[2:]+string[0:1]+'ay'
        else:
            pig_string = string + 'way'
    print (pig_string)