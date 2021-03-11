"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
from DISClib.Algorithms.Sorting import insertionsort as ints
from DISClib.Algorithms.Sorting import selectionsort as sets
from DISClib.Algorithms.Sorting import shellsort as shls
from DISClib.Algorithms.Sorting import quicksort as qcks
from DISClib.Algorithms.Sorting import mergesort as mrgs

import time
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(tipo):
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para las categorias. 
    Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'categorias': None,}

    catalog["videos"] = lt.newList(datastructure=tipo)
    catalog["categorias"] = lt.newList(datastructure=tipo)

    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    if not (video["video_id"]=="#NAME?"):
        lt.addLast(catalog["videos"], video)


def addCategoria(catalog, categoria):
    """
    Adiciona una categoría a su respectiva lista
    """
    tag = newCategoria(categoria["name"], categoria["id"])
    lt.addLast(catalog["categorias"], tag)


# Funciones para creacion de datos

def newCategoria(name, id):
    """
    Esta estructura almacena las categorías de sus respectivos videos.
    """
    categoria = {"name": "", "id": ""}
    categoria["name"] = name
    categoria["id"] = id
    return categoria

# Funciones de consulta

def nameToIdCategory(category_name,categories):
    for i in range(1,lt.size(categories)+1):
        category=lt.getElement(categories,i)
        if category_name==category["name"]:
            return category["id"]
    return None

def mostTrending(sorted_list):
    #sorted_list=catalog["videos"]
    most=0
    most_vid=None
    current=1
    for i in range(1,lt.size(sorted_list)+1):
        current_vid=lt.getElement(sorted_list,i)
        if current_vid==lt.lastElement(sorted_list):
            next_vid=lt.getElement(sorted_list,i-1)
        else:
            next_vid=lt.getElement(sorted_list,i+1)
        if str(current_vid["title"])==str(next_vid["title"]):
            current+=1
        else:
            current=1
        if current>most:
            most=current
            most_vid=current_vid
        
    return (most_vid,most)





# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosbyViews(video1,video2):
    return (int(video1["views"]) > (int(video2["views"])))

def cmpVideosbyName(video1,video2):
    return (str(video1["title"]).lower()>str(video2["title"]).lower())
# Funciones de ordenamiento


def sortVideosName(catalog,size,tipo):
    sub_list = lt.subList(catalog["videos"],1,size)
    sub_list = sub_list.copy()
    if tipo == "Insertion":
        start_time = time.process_time()
        sorted_list = ints.sort(sub_list, cmpVideosbyName)
        stop_time = time.process_time()

    elif tipo == "Selection":
        start_time = time.process_time()
        sorted_list = sets.sort(sub_list, cmpVideosbyName)
        stop_time = time.process_time()

    elif tipo == "Shell":
        start_time = time.process_time()
        sorted_list = shls.sort(sub_list, cmpVideosbyName)
        stop_time = time.process_time()
    
    elif tipo == "Merge":
        start_time = time.process_time()
        sorted_list = mrgs.sort(sub_list, cmpVideosbyName)
        stop_time = time.process_time()

    elif tipo == "Quick":
        start_time = time.process_time()
        sorted_list = qcks.sort(sub_list, cmpVideosbyName)
        stop_time = time.process_time()

    Tiempo_total = (stop_time-start_time)*1000
    return sorted_list


def categoryTrending(info,category):
    lista=info["videos"]
    categories=info["categorias"]
    category_vids=newCatalog("ARRAY_LIST")
    for i in range(1,lt.size(lista)+1):
        video=lt.getElement(lista,i)
        if video["category_id"]==nameToIdCategory(category,categories):
            addVideo(category_vids,video)
    sortedvids=sortVideosName(category_vids,lt.size(category_vids["videos"]),"Merge")
    most_trending=mostTrending(sortedvids)
    return most_trending
    

        



def sameCountryCategory(info,country,category):
    lista=info["videos"]
    categories=info["categorias"]
    country_vids=newCatalog("ARRAY_LIST")
    for i in range(1,lt.size(lista)+1):
        video=lt.getElement(lista,i)
        if video["country"]==country:
            if video["category_id"]==nameToIdCategory(category,categories):
                addVideo(country_vids,video)
    return country_vids


def sortVideos(catalog, size, tipo):
    try:
        sub_list = lt.subList(catalog["videos"],1,size)
        sub_list = sub_list.copy()
        if tipo == "Insertion":
            start_time = time.process_time()
            sorted_list = ints.sort(sub_list, cmpVideosbyViews)
            stop_time = time.process_time()

        elif tipo == "Selection":
            start_time = time.process_time()
            sorted_list = sets.sort(sub_list, cmpVideosbyViews)
            stop_time = time.process_time()

        elif tipo == "Shell":
            start_time = time.process_time()
            sorted_list = shls.sort(sub_list, cmpVideosbyViews)
            stop_time = time.process_time()
    
        elif tipo == "Merge":
            start_time = time.process_time()
            sorted_list = mrgs.sort(sub_list, cmpVideosbyViews)
            stop_time = time.process_time()

        elif tipo == "Quick":
            start_time = time.process_time()
            sorted_list = qcks.sort(sub_list, cmpVideosbyViews)
            stop_time = time.process_time()

        Tiempo_total = (stop_time-start_time)*1000
        return Tiempo_total, sorted_list

    except IndexError:
        pass

