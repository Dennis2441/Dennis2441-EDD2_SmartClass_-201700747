import json

hola="""{
    "Cursos": [
        {
            "Codigo": "101",
            "Nombre": "Matemática Básica 1",
            "Creditos": 7,
            "Prerequisitos": "",
            "Obligatorio": true
        },
        {
            "Codigo": "039",
            "Nombre": "Deportes 1",
            "Creditos": 1,
            "Prerequisitos": "",
            "Obligatorio": false
        },
        {
            "Codigo": "348",
            "Nombre": "Quimica General 1",
            "Creditos": 3,
            "Prerequisitos": "",
            "Obligatorio": true
        },
        {
            "Codigo": "103",
            "Nombre": "Matemática Básica 2",
            "Creditos": 7,
            "Prerequisitos": "101",
            "Obligatorio": true
        },
        {
            "Codigo": "005",
            "Nombre": "Técnicas de Estudio e Investigación",
            "Creditos": 3,
            "Prerequisitos": "",
            "Obligatorio": true
        },
        {
            "Codigo": "960",
            "Nombre": "Matemática Cómputo 1",
            "Creditos": 5,
            "Prerequisitos": "103",
            "Obligatorio": true
        },
        {
            "Codigo": "107",
            "Nombre": "Mátematica Intermedia 1",
            "Creditos": 10,
            "Prerequisitos": "103",
            "Obligatorio": true
        },
        {
            "Codigo": "770",
            "Nombre": "Introducción a la Programación y Computación 1",
            "Creditos": 4,
            "Prerequisitos": "103",
            "Obligatorio": true
        },
        {
            "Codigo": "796",
            "Nombre": "Lenguajes Formales y de Programación",
            "Creditos": 3,
            "Prerequisitos": "770,795,960",
            "Obligatorio": true
        },
        {
            "Codigo": "772",
            "Nombre": "Estructuras de Datos",
            "Creditos": 5,
            "Prerequisitos": "771,796,962",
            "Obligatorio": true
        },
        {
            "Codigo": "777",
            "Nombre": "Organización de Lenguajes y Compiladores 1",
            "Creditos": 4,
            "Prerequisitos": "771,796,962",
            "Obligatorio": false
        },
        {
            "Codigo": "018",
            "Nombre": "Filosofia de la Ciencia",
            "Creditos": 3,
            "Prerequisitos": "019",
            "Obligatorio": false
        },
        {
            "Codigo": "774",
            "Nombre": "Sistemas de Bases de Datos 1",
            "Creditos": 5,
            "Prerequisitos": "773",
            "Obligatorio": true
        },
        {
            "Codigo": "281",
            "Nombre": "Sistemas Operativos 1",
            "Creditos": 4,
            "Prerequisitos": "781,778",
            "Obligatorio": true
        },
        {
            "Codigo": "2036",
            "Nombre": "Práctica Intermedia",
            "Creditos": 0,
            "Prerequisitos": "778,777,773,2025",
            "Obligatorio": true
        }
    ]
}"""



if __name__=='__main__':
    data = json.loads(hola)
    for p in data['Cursos']:
        print('Codigo: ' + p['Codigo'])
        print('Nombre: ' + p['Nombre'])
        print('Creditos: ' + str(p['Creditos']))
        print('Prerequisitos: ' +str(p['Prerequisitos']))
        print('Obligatorio: ' + str(p['Obligatorio']))
        print('')