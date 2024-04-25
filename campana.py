from anuncio import Anuncio
from error import ClassLargoExtendido


class Campana(Anuncio):


    def __init__(self, nombre, fecha_inicio, fecha_termino):
        if len(nombre) > 250:
            raise ClassLargoExtendido ('El nombre excede los 250 caracteres')
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self__nombre = nombre    
        
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self__fecha_inicio = fecha_inicio    
        
    def fecha_termino(self):
        return self.__fecha_termino
    @fecha_termino.setter
    def fecha_termino(self, fecha_termino):
        self__fecha_termino = fecha_termino 
        
    def __str__(self):
        return f'Nombre de la campaña {self.nombre}, Feecha de incio {self.fecha_inicio} Fecha de termino {self.fecha_termino}'