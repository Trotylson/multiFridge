import json


items = """{
    "items": [{
        "name": "banan",
        "quantity": 6,
        "unit": "szt",
        "price": 1.29
    },{
        "name": "mleko 2,5%",
        "quantity": 1,
        "unit": "l",
        "price": 2.39
    },{
        "name": "masło",
        "quantity": 1,
        "unit": "szt",
        "price": 5
    },{
        "name": "jogurt",
        "quantity": 4,
        "unit": "szt",
        "price": 1.75
    },{
        "name": "pepsi",
        "quantity": 2.5,
        "unit": "l",
        "price": 7
    },{
        "name": "schab",
        "quantity": 1,
        "unit": "kg",
        "price": 10.99
    },{
        "name": "cukier",
        "quantity": 0.750,
        "unit": "kg",
        "price": 4.40
    },{
        "name": "kawa",
        "quantity": 1,
        "unit": "kg",
        "price": 29.99
    }]
}"""


seed = json.loads(items)