#EL FLASK TIENE SISTEMA DE REFLESH

from flask import Flask, render_template

app = Flask(__name__)

"""App es una decoradora de herencia"""
@app.get("/")
def index():
    return render_template("index.html")

@app.get("/contacto")
def contacto():
    return render_template("contactos/index.html")



@app.get("/contacto/<contactoId>/edit")
def editarContacto(contactoId):
    suma = 2+2
    

    return render_template("contactos/editar.html",contactoId = contactoId, suma=suma)
 
#http://127.0.0.1:5000/contacto/3/edit



#Ejerccio sencillo
#edad/27/Naciste en el año tal
@app.get("/contacto/<int:miEdadId>/edad")
def actualEdad(miEdadId):

    actual = 2022 - miEdadId
    return render_template("contactos/edad.html",actual = actual)



app.run(debug=True)



