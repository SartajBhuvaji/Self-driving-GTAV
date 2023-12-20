# Citation: Box Of Hats (https://github.com/Box-Of-Hats )

import win32api as wapi

key_combinations = {
    'W': 'W',
    'S': 'S',
    'A': 'A',
    'D': 'D',
    'WA': 'W+A',
    'WD': 'W+D',
    'SA': 'S+A',
    'SD': 'S+D',
}

def key_check():
    keys = []
    for key, key_combination in key_combinations.items():
        if '+' in key_combination:
            key_parts = key_combination.split('+')
            if all(wapi.GetAsyncKeyState(ord(part)) for part in key_parts):
                keys.append(key)
        else:
            if wapi.GetAsyncKeyState(ord(key_combination)):
                keys.append(key)
    #print(keys)            
    return keys

 