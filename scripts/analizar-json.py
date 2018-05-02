# http://www.pythondiario.com/2017/10/analisis-de-json-con-python.html


import json

users = '''
[
{ "id" : "001",
"edad" : "21",
"nombre" : "Luis"
},
{ "id" : "002",
"edad" : "25",
"nombre" : "Andres"
},
{ "id" : "003",
"edad" : "34",
"nombre" : "Jose"
},
{ "id" : "004",
"edad" : "29",
"nombre" : "Jesus"
}
]'''

info = json.loads(users)
print('Cantidad de usuarios:', len(info))
for elemento in info:
    print('Nombre', elemento['nombre'])
    print('Id', elemento['id'])
    print('Edad', elemento['edad'])
    print("\n")