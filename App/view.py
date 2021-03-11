"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- REQ. 1: Encontrar buenos videos por categoría y país")
    print("3- REQ. 2: Encontrar video tendencia por país")
    print("4- REQ. 3: Encontrar video tendencia por categoría")
    print("5- REQ. 4: Buscar los videos con más likes")
    

def initCatalog(tipo):
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog(tipo)


def loadData(catalog):
    
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)

def printResultsReq_1(info,tamaño):
    lista=info[1]
    size = lt.size(lista)
    if size >= tamaño:
        print("Los primeros ", tamaño, " videos ordenados son:")
        i=1
        while i <= tamaño:
            video = lt.getElement(lista,i)
            print(' Fecha Trending: ' + video['trending_date'] + "," + ' Nombre: ' +
                  video['title'] + ","+ ' Canal: ' + video['channel_title'] + ","+ " Fecha de Publicacion: "+ video["publish_time"] +
                  "," + " Visitas: " + video["views"]+ ","+ " Likes: "+ video["likes"]+ "," + " Dislikes: " +video["dislikes"])
            i+=1
    print(info[0])

def printResultsReq_3(info):
    video=info[0]
    days=str(info[1])
    print("El video que mas dias ha sido trending es: ")
    print("Nombre: " + video["title"] + "," + "Canal: " + video["channel_title"] + ","+ "Categoria_ID: " + video["category_id"] + ","+ "Dias: " + days)




"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        tipo = input("seleccione el tipo de estructura de datos escribiendo textualmente: ARRAY_LIST o SINGLE_LINKED: ")
        catalog = initCatalog(tipo)
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['categorias'])))
    elif int(inputs[0]) == 2:
        size = int(input("Tamaño límite de videos a ordenar:"))
        sample=int(input("Tamaño de la muestra a imprimir: "))
        country=input("Escoja el pais: ")
        category=input("Escriba la categoria: ")
        tipo = input(" Seleccione el tipo de algoritmo de ordenamiento"+
            "iterativo escribiendo textualmente alguna de estas opciones:"+
            "Insertion, Selection, Shell, Merge, Quick: ")
        sorted_list=controller.sameCountryCategory(catalog,country,category)
        try:
            printResultsReq_1(controller.sortVideos(sorted_list,size,tipo),sample)
        except TypeError:
            print("No hay suficientes videos de este tipo y categoria, intente ordenar una cantidad menor.")
        
    elif int(inputs[0]) == 3:
        country=input("Escriba el país a buscar:")
        rta=controller.llamar_Trending(catalog,country)
        iterador= it.newIterator(rta)
        element=it.next(iterador)
        print(("Title: {} , Channel_title:{} , Country: {} , Numero dias: {}").format(element['title'], element['channel_title'], element['country'], element['trending_date']))
    elif int(inputs[0]) == 4:
        category=input("Escriba la categoria la cual quiere buscar: ")
        printResultsReq_3(controller.categoryTrending(catalog,category))
    elif int(inputs[0]) == 5:
        country = str(input("Ingrese país: "))
        videos_num = int(input("Ingrese cantidad: "))
        tag = str(input("Ingrese tag (año): "))
        lst = controller.videos_mas_likes(catalog,country,videos_num,tag)
        for video in lt.iterator(lst):
            print("video: " +str(video["title"])+", "+str(video["cannel_title"])+", "+str(video["publish_time"])+
                    ", views: "+str(video["views"])+", likes: " +str(video["likes"])+", dislikes: "+str(video["dislikes"])+
                    ", tags: "+str(video["tags"]))

    else:
        sys.exit(0)
sys.exit(0)
