def createMenu(optionList):
    '''Description:receives a list and creates a menu string with each \
       element as an option.
       Precondition: must receive a list.'''
    tmp = ''; ct = 1
    for opt in optionList:
        tmp += str(ct)+ '. ' + opt + '\n'
        ct += 1
    return tmp
