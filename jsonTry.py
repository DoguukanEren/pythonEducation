# -*- coding: utf-8 -*-

import json

data = '{"firstname":"Doğukan Eren","lastName":"Özer"}'

y = json.loads(data)

print(y["firstname"])
print(y["lastName"])

customer = {"firstName" : "Eren",
            "lastName"  : "Özer",
            "age"       : "24",
            }

customerJson = json.dumps(customer)

print(customerJson)

print(json.dumps("Eren"))