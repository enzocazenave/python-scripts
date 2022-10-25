"""
    DESARROLLAR UN PROGRAMA PARA ELIMINAR TODOS LOS COMENTARIOS DE UN PROGRAMA ESCRITO EN LENGUAJE PYTHON.
    TENER EN CUENTA QUE LOS COMENTARIOS COMIENZAN CON EL SIGNO # (SIEMPRE QUE ESTE NO SE ENCUENTRE ENCERRADO ENTRE COMILLAS SIMPLES O DOBLES)
    Y QUE TAMBIEN SE CONSIDERA COMENTARIO A LAS CADENAS DE DOCUMENTACION (DOCSTRINGS) 
"""

def eliminar_comentario(linea):
    if linea.strip().startswith("#"):
        return ""

    for c in range(len(linea)):
        if linea[c] == '#' and (not linea[c - 1] == '"' and not linea[c - 1] == "'"):
            return linea[:c] + '\n'
            
    return linea        

try:
    entrada = open('archivo.py', 'rt')
    salida = open('archivo_2.py', 'wt')
    linea = entrada.readline()
    docstring = False
    
    while linea:
        linea_limpia = linea.strip()
        condicion_comillas = linea_limpia.startswith('"""') or linea_limpia.startswith("'''")

        if condicion_comillas and not docstring:
            docstring = True
        elif condicion_comillas and docstring:
            docstring = False
        elif not condicion_comillas and not docstring:
            salida.write(eliminar_comentario(linea)) 

        linea = entrada.readline()

except FileNotFoundError:
    print("[ERROR] No se pudo abrir el archivo")
finally:
    try:
        entrada.close()
        salida.close()
    except NameError:
        print("[ERROR] Archivo no encontrado")