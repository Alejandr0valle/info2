import pymongo 
client = pymongo.MongoClient("mongodb+srv://Alejandro_info2:961230@atlascluster.nng8tyw.mongodb.net/?retryWrites=true&w=majority")
db = client.test

mydb=client["Base_de_datos"]
mycol = mydb["Clientes"]


mydict={"Nombre": "juan", "Direccion": "C/ Mayor 1"}

x = mycol.insert_one(mydict)
print(x.inserted_id)

#Para cambiar o actulizar datos dentro de la base de datos
myquery={"Nombre": "juan", "Direccion": "C/ Mayor 1"}
newvalues={ "$set": {"Nombre": "Alejandro" , "Direccion": "Cl 38a#108"}}

mycol.update_one(myquery , newvalues)

for x in mycol.find({"Nombre": "Alejandro"}):
    print(x)