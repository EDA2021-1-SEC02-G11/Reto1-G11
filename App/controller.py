﻿"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog(tipo):
    catalog = model.newCatalog(tipo)
    return catalog

# Funciones para la carga de datos

def loadData(catalog):

    loadVideos(catalog)
    loadCategoria(catalog)
    loadCountrys(catalog)

def loadCategoria(catalog):

    categoriafile = cf.data_dir + "category-id.csv"

    input_file = csv.DictReader(open(categoriafile, encoding='utf-8'),delimiter='\t')
    for categoria in input_file:
        model.addCategoria(catalog,categoria)

def loadVideos(catalog):
    
    videosfile = cf.data_dir + "videos-small.csv"
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def loadCountrys(catalog):
    
    videosfile = cf.data_dir + "videos-small.csv"
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addCountry(catalog, video)
# Funciones de ordenamiento

def sameCountryCategory(lista,country,category):
    return model.sameCountryCategory(lista,country,category)

def sortVideos(catalog, size, tipo):
    return model.sortVideos(catalog, size, tipo)

def categoryTrending(info,category):
    return model.categoryTrending(info,category)

# Funciones de consulta sobre el catálogo

def nameToIdCategory(category_name,categories):
    return model.nameToIdCategory(category_name,categories)

def llamar_Trending(catalog,country):
    return model.Trending(catalog,country)

def videos_mas_likes(catalog,country,cant_videos,tag):
    return model.videos_mas_likes(catalog,country,cant_videos,tag)
