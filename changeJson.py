import pprint
json = {"hola":"hola",
        "adios":{"hola":"hola",
                "adios":{"adios":"adios"},
                "buenas":"caca",
                "que":"caca",
                "tal":"caca",
                "estamos":"caca",
                "muy":"caca",
                "bien":"caca"
                },
        "buenas":"caca",
        "que":"caca",
        "tal":"caca",
        "estamos":"caca",
        "muy":"caca",
        "bien":"caca"
        }

def changeJsonKeysRecursively(json, key, newkey):
    if 'adios' in json:
        json[newkey] = json.pop(key)
        
    for k, v in json.items():
        if isinstance(v, dict):
            changeJsonKeysRecursively(v, key, newkey)
    

def changeJsonValuesRecursively(json, val, newval):
    for k, v in json.items():
        if v == val:
            json[k] = newval
        else:
            if isinstance(v, dict):
                changeJsonValuesRecursively(v, val, newval)
    pprint.pprint(json)
#changeJsonKeysRecursively(json, 'adios', 'adios2')
changeJsonValuesRecursively(json, 'caca', 'vamoss')