from error import SubTipoInvalidoError
from campana import Campana

arch = open('error.log', 'a')

c = Campana('ricomida', '2024-03-15', '2024-03-24')

try:

    c.crear_video('instream' , 'htpps://www.tupruebam4.cl' ,' htpps://www.tupruebam4.cl',05  )
except SubTipoInvalidoError as e:
    print (f'Error al agregar un video {e}')
    arch.write(f'Error al agregar un video {e}')


try:
    c.crear_display('native','htpps://www.tupruebam4.cl' ,' htpps://www.tupruebam4.cl')
except SubTipoInvalidoError as e:
    print (f'Error al agregar un display {e}')
    arch.write(f'Error al agregar un display {e}')
    
try:
    c.crear_social('facebook','htpps://www.tupruebam4.cl' ,' htpps://www.tupruebam4.cl')
except SubTipoInvalidoError as e:
    print (f'Error al agregar un display {e}')
    arch.write(f'Error al agregar un display {e}')
# Imrpimimos el detalle de nuestea campaña
print (c)
# Cerramos el archivo
arch.close()




