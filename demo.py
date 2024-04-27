from error import SubTipoInvalidoError
from campana import Campana

arch = open('error.log', 'a')

c = Campana('ricomida', '2024-03-15', '2024-03-24')

try:

    c.crear_video('htpps://www.tupruebam4.cl' ,' htpps://www.tupruebam4.cl','instream' ,5  )
except SubTipoInvalidoError as e:
    print (f'Error al agregar un video {e}')
    arch.write(f'Error al agregar un video {e}')


try:
    c.crear_display(20,20 ,'htpps://www.tupruebam4.cl' ,' htpps://www.tupruebam4.cl','native')
except SubTipoInvalidoError as e:
    print (f'Error al agregar un display {e}')
    arch.write(f'Error al agregar un display {e}')
    
try:
    c.crear_social(15,24,'htpps://www.tupruebam4.cl' ,' htpps://www.tupruebam4.cl', 'facebook')
except SubTipoInvalidoError as e:
    print (f'Error al agregar un display {e}')
    arch.write(f'Error al agregar un display {e}')
# Imrpimimos el detalle de nuestea campaña
print (c)
# Cerramos el archivo
arch.close()





