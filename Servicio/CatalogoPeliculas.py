#!/usr/bin/python3
# -*- coding: utf-8 -*-
# github.com/JuanPerdomo00
#
#  create by: jakepy Perdomo <j4kyjak3@protonmail.com>
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; version 2 of the License.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA


import os


class CatalogoPeliculas:
    def __init__(self, archivo):
        self.ruta = archivo

    def agregar_pelicula(self, pelicula):
        try:
            with open(self.ruta, "a") as archivo:
                archivo.write(f"{pelicula.nombre}\n")
                print(f"La pelicula {pelicula.nombre} fue agregada correctamente \n")

        except Exception as e:
            print("Error: ", e)

    def listar_peliculas(self):
        try:
            i = 0
            with open(self.ruta, "r", encoding="utf8") as archivo:
                print("Lista de Peliculas".center(50, "-"))
                for lista in archivo.readlines():
                    i += 1
                    print(f"ID: [{i}] Pelicula: {lista}")
        except FileNotFoundError as e:
            print(f"Error al listar, El archivo {self.ruta} no existe", e)

    def eliminar_peliculas(self):
        ruta = self.ruta
        try:
            if os.path.exists(ruta):
                os.remove(ruta)
                print(f"El erchivo {ruta} fue eliminado correctamente en la ruta")
                os.system(f"echo $('pwd')/{ruta}")
            else:
                print(f"El archivo {ruta} no existe posiblemente ya fue eliminado")
        except FileNotFoundError as e:
            print("Error: ", e)
