from abc import ABC, abstractmethod
from error import SubTipoInvalidoError



class Anuncio(ABC):
    sub_tipos=()
    
    @staticmethod
    def mostrar_formatos():
        pass
    '''
        print('formato video')
        for x in Video.SUB_TIPOS:
            print (f'-{x}')
            
        print('formato Display')
        for d in Display.SUB_TIPOS:
            print (f'-{d}')
            
        print('formato Social')
        for s in Social.SUB_TIPOS:
            print (f'-{s}')
    '''     
    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimiencionar_anuncion(self):
        pass
    
    
    def __init__(self, alto, ancho, url_archivo, url_click, sub_tipo):
        self.__alto = alto
        self.__ancho= ancho
        self.__url_archivo = url_archivo
        self.__url_click = url_click
        self.__sub_tipo = sub_tipo
        
    
    
    
        if  sub_tipo not in Anuncio.sub_tipos:
            print('Ese subtipo, no existe')
        
    @property 
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho if ancho > 0 else 1            
        
        
    @property 
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, alto):
        self.__alto = alto if alto > 0 else 1  
        
        
    @property
    def url_archivo(self):
        return self.__url_archivo
    
    @url_archivo.setter
    def url_archivo(self, value):
        self.__url_archivo = value
        
    @property
    def url_click(self):
        return self.__url_click
    
    @url_click.setter
    def url_click(self, value):
        self.__url_archivo = value
        
    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo):
        pass
        '''
        if (isinstance(self,Video) and sub_tipo not in Video.SUB_TIPOS
        or isinstance(self,Display) and sub_tipo not in Display.SUB_TIPOS
        or isinstance(self, Social) and sub_tipo not in Social.SUB_TIPOS):
            raise SubTipoInvalidoError('El subtipo indicado no está permitido para este formato')
        else:
            self.__sub_tipo = sub_tipo
        '''
        
        
class Video(Anuncio):
    
    FORMATO = "Video"
    
    SUB_TIPOS = ("instream", "outstream")
    
    def __init__(self, url_archivo, url_click, sub_tipo, duracion):
        super().__init__(1,1,url_archivo, url_click, sub_tipo)
        self.__duracion = duracion if duracion > 0 else 5
        
    @property
    def ancho (self):
        return self.__ancho
    @ancho.setter
    def ancho(self, ancho):
        pass
    
    @property
    def alto (self):
        return self.__alto
    @alto.setter
    def alto(self, alto):
        pass
    
    @property
    def duracion(self):
        return self.__duracion
    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = duracion if duracion > 0 else 5
    
    def comprimir_anuncio(self):
        print ('Compresión de vídeo no implementada aún')
        
    def redimensionar_anuncio(self):
        print ('Recorte de vídeo no implementado aún')
        
        
class Display(Anuncio):
    FORMATO = "Display"
    
    SUB_TIPOS = ("tradicional", "native")
    
    
class Social(Anuncio):
    
    FORMATO = "Social"
    
    SUB_TIPOS = ("facebook", "linkedin")
    