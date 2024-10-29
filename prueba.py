import requests
from pprint import pprint
from tkinter import *

#Alumno: Gómez Gaona Jessica Janet
#Despliegue de aplicaciones

max_results = 10
# Crear la ventana
ventana_principal = Tk()
ventana_principal.title("Terremotos")
ventana_principal.minsize(width=300, height=400)
ventana_principal.config(padx=35, pady=35)
search_text = StringVar(ventana_principal)


# Crear caja de texto
caja_text = Entry(width=20, font=("Arial", 14), textvariable=search_text)
caja_text.grid(column=0, row=2)

labels = []
for i in range(max_results):
    labels.append(Label(text="", font=("Arial", 14)))
    labels[i].grid(column=0, row=10 + (i*10), pady=5)

def search():
    print(search_text.get())
    data = search_text.get()
    data = data.split(",")
    print(data)
    url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={data[0]}&endtime={data[1]}"
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
        places = []
        for e in data["features"]:
            places.append(e["properties"]["place"])
        places = places[:max_results]
        i = 0
        for place in places:
            labels[i].config(text=place)
            print(place)
            i += 1
            
# Crear la etiqueta para mostrar resultados
etiqueta_resultado = Label(text="", font=("Arial", 14))
etiqueta_resultado.grid(column=0, row=10, pady=20)

# Creación de botones
boton = Button(text="Buscar", font=("Arial", 14), command=search, )
boton.grid(column=0, row=3, pady=10)


ventana_principal.mainloop()



        
