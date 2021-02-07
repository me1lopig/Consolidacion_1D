
# librerias de creación de archivos de salida de resultados y de cálculos



def archivo_datos(espesor,carga,coefConso,coefComp,permeabilidad,x,t,alfa,tipoContorno):
    # imprime los datos de entrada para los cálculos del problema

    f = open ('datos.txt','w')
    f.write('Datos del modelo \n\n')

    f.write('Datos de contorno\n')
    f.write('Espesor del estrato % .2f [m] \n'%espesor)
    f.write('Carga exterior %.2f [kPa] \n'%carga)

    f.write('\nParámetros del terreno\n')
    f.write('Coeficiente de consolidacion %.5g [m2/dia]\n'%coefConso)
    f.write('Coeficiente de compresibilidad volumetrico %.5g [m2/kN]\n'%coefComp)
    f.write('Permeabiidad %.5g [m/dia]\n'%permeabilidad)

    f.write('\nParámetros geométricos y de convergencia del modelo\n')
    f.write('El valor del intervalo en x [m]= %.2f\n'%x)
    f.write('El valor del intervalo en t [dias]= %.2f\n'%t)
    f.write('El valor del coeficiente de convergencia [alfa]= %.5f\n'%alfa)
    f.write('El tipo de contorno seleccionado es %s '%tipoContorno)
    f.close() # cerramos el archivo creado