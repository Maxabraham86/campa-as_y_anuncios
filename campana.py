from anuncio import Anuncio, Video, Display, Social
from error import ClassLargoExtendido
#from datetime import date  para poner date como parametro

class Campana():

    def __init__(self, nombre, fecha_inicio, fecha_termino):
        if len(nombre) > 250:
            raise ClassLargoExtendido ('El nombre excede los 250 caracteres')
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.anuncios =[]
    
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

    def crear_video(self, sub_tipo, url_archivo, url_click, duracion):
        v = Video(url_archivo, url_click,sub_tipo, duracion)
        self.__anuncios.append(v)
        
    def crear_display(self, sub_tipo, url_archivo, url_click):
        d = Display(url_archivo, url_click, sub_tipo)
        self.__anunios.append(d)
    def crear_social(self, sub_tipo, url_archivo, url_click):
        s = Social(url_archivo, url_click, sub_tipo)
        self.__anuncios.append(s)
    def __str__(self):
        print (f'Nombre de la campaña {self.nombre}')
        num_videos =0
        num_display = 0
        num_social = 0
        for anuncio in self.__anuncios:
            if isinstance(anuncio, Video):
                num_videos += 1
                
        for anuncio in self.__anuncios:
            if isinstance(anuncio,Display):
                num_display += 1
        for anuncio in self.__anuncios:
            if isinstance(anuncio, Social):
                num_social += 1
                
                print(f' Hay {num_videos} en este anuncio')
                
                
                