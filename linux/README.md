
# Comandos Linux

## Comandos para trabajar desde la ubicaciòn.
- **man** Comando permite invocar los manuales en los    diferentes comandos.
    ```bash
    $ man date 
    ```
- **ls -a** Listar todos los directorios incluyendo los ocultos.
    ```bash
    $ ls -a 
    ```
- **ls -t** Ordena archivos por fecha de modificaciòn.
    ```bash
    $ ls -t 
    ```
- **ls -x** Ordena archivos por nombre (1) y extenciòn (2).
    ```bash
    $ ls -x 
    ```
- **ls -R** Muestra directorios de forma recursiva.
    ```bash
    $ ls -R 
    ```
## Comandos para mover o copiar

- **cp** Copia un archivo a un directorio.
    ```bash
    $ cp [archivo a copiar] [/ruta directorio a copiar]
    ```
- **mv** Mueve un archivo de ruta.
    ```bash
    $ mv [archivo a mover ] [/ruta directorio a mover]
    ```
- **rmdir** Elimina un directorio
    ```bash
    $ rmdir [ruta / directorio a eliminar]
    ```
- **ln -s** Comando para crear un acceso directo en la terminal
    ```bash
    $ ln -s [target_directory_path] [linked_directory_name_path]
    ```
___

## Utilizades batch 

- **cat** Muestra el contenido completo de un archivo.
    ```bash
    $ cat texto.txt
    ```
- **head** Muestra las primeras lienas del archivo o limitarlas con [-n#]
    ```bash
    $ head texto.txt
    $ head -n 5 texto.txt
    ```
- **tail** Muestra las ultimas lienas del archivo o limitarlas con [-n#].
    ```bash
    $ tail texto.txt
    $ tail -n 5 texto.txt
    ```
- **grep** Permite hacer busquedas con expresiones regulares.
    ```bash
    $ grep palabra clave archivo.txt
    $ grep -i pAlaBra cLaVe archivo.txt
    $ grep palabra clave$ archivo.txt
    $ grep ^palabra clave archivo.txt
    ```

