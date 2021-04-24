
# Indice Linux
_____
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
_____
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
_____
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
_____
## Monitoreo de recursos del sistema
- **&** Sirve para enviar el proceso a un segundo plano.
    ```bash
    $ mysql -h 127.0.0.1 -u root -p1234 < dump-sql &
    ```
- **ctrl z** Sirve para enviar un proceso al background del sistema.
- **fg** Sirve para retomar el proceso enviado a background.
- **ps** permite revisar los procesos del sistema.
- **ps ax** permite ver los procesos activos del sistema.
- **top** muestra el estado del sistema.
- **kill** Envia señales a los procesos para terminarlos.
- **kill -9** Envia señal de cortar inmediatamente.
- **killall archivoejecutable** Envia señal de cortar inmediatamente.
- **nohub** Genera un archivo de nombre nohub.out que almacena la información del proceso.
- **./** Ejecuta un proceso.
- **ps auxf | sort -nr -k 3 | head -5** Comando para conocer los procesos que mas CPU consume el S.O
- **ps auxf | sort -nr -k 4 | head -5** Comando para conocer los procesos que mas RAM consume el S.O
_____
## Permisos y Modificaciones
- **ls -l** Comando que permite visualizar los privigelios de los archivos.
<p align="center"> <img src ="./images/permisos.png"></p>

- Dueño {rwx} Grupos {rwx} Otros {rwx}
    - r=Lectura
    - w=Escritura
    - x=Ejecucion

    ```bash
        $ rw-rw-r-- 1 usuario usuario 2318 feb 26 17:45 README.md
    ```
- **chmod** Cambia permisos de lectura escritura y ejecucion al archivo teniendo en cuenta el usuario - grupo y otros.
    ```bash
        # Añadir permisos de ejecucion al usuario 
        $ chmod u+x nuevo.txt
        # Añadir permisos de escritura al grupo.
        $ chmod g+w nuevo.txt
        # Añadir permisos de escritura a otros.
        $ chmod o+w nuevo.txt
        # Añadir permisos de ejecucion a todos (cualquier usuario).
        $ chmod a+x nuevo.txt
        # Añadir permisos usando el esquema binario(-=0 x=1 w=2 r=4).
            # Permisos del usuario propietario: r (4) + w (2) + x (1) = 7.
            # Permisos del grupo al que pertenece el archivo: r (4) + x (1) = 5.
            #Permisos del grupo al que pertenece el archivo: r (4) = 4.
        $ chmod 754 hello.php
    ```
- **chown** Cambia quien el es usuario propietario del archivo.
    ```bash
            # Cambiando el usuario propietario
            $ sudo chown nuevo-usuario archivo.txt
            # Cambiando el grupo propietario
            $ sudo chown nuevo-grupo archivo.txt
            # Cambiando el usuario y grupo propietario
            $ sudo chown nuevo-usuario:nuevo-grupo archivo.txt
        ```
- **chgrp** Cambia quien es el grupo de usuarios que puede acceder 
_____
## Compresion de Archivos.
- **gizp** Comando para comprimir los archivos.
    ```bash
            # Comprimiendo el archivo.
            $ gzip archivo.txt
            # Descomprimiendo el archivo.
            $ gzip -d archivo.txt.gz
    ```
- **tar** permite agrupar varios archivos en un grupo 
    ```bash
            # Agrupando archivos de la carpeta backup
            $ tar cf backup.tar backup/*
            # Revisando el contenido de backup.tar
            $ tar tf backup.tar
            # Descomprimir el contenido de backup.tar
            $ tar xf backup.tar
            # agrupar y comprimir todos los archivos de la carpeta backup.
            $ tar czf backup.tgz backup/*
            # Des-agrupar y des-comprimir todos los archivos de la carpeta backup.
            $ tar xzf backup.tgz
    ```
_____
## Busquedas.
- **locate** Permite hacer una busqueda de un archivo en todo el sistema.
    ```bash
            # Buscarndo archivo en el sistema
            $ locate hello.php
    ```
- **find** Busca archivos en el sistema con diferentes argumentos
    ```bash
            # Buscarndo un archivo con usuario y permisos 644
            $ find . -user usuario -perm 644
            # Buscarndo solo archivos modificados (-type) en un tiempo mayor a 7 dias.
            $ find . -type f -mtime +7
            # Buscarndo archivos modificados (-type) en un tiempo mayor a 7 dias y moviendo el resultado a una carpeta backup.
            $ find . -type f -mtime +7 -exec cp {} ./backup/ \;
    ```
_____
## Comandos HTTP
- **curl** Se usa para hacer pedidos hacia un servidor y se genera una respuesta.
    ```bash
            # Realizando peticion a url
            $ curl https://platzi.com
            # Realizando peticion a url con la opcion -v muestra toda a comunicacion http
            $ curl -v https://platzi.com
            # Realizando peticion a url con opcion -v muestra toda la comunicacion http y solo encabezados redireccionando la salida estandard a un espacio null
            $ curl -v https://platzi.com > /dev/null
    ```
- **wget** Se usa para hacer pedidos hacia un servidor y se genera una respuesta adicionalmente esta peticion permite hacer descargas.
    ```bash
            # Realizando una descarga del producto elasticsearch usan wget.
            $ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.11.1-linux-x86_64.tar.gz
    ```
_____
## Que son y como se utilizan las variables de entorno.
- Es una definicion global de variable que le brinda acceso a uno o todos los procesos.
    ```bash
            # ejemplo con variable PATH
            $ echo $PATH
            # Ejemplo de respuesta.
            /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
    ```
- **export** Asigna una variable global para toda la sesion.
    ```bash
            # ejemplo de asignacion.
            $ export MI_VARIBLE=nombre_variable
            # Invocando la variable
            $ echo $MI_VARIBLE
    ```
- **VAR=** Asigna una variable global unicamente para comandos especiales No sobre escribe la variable global.
    ```bash
            # ejemplo de asignacion.
            $ MI_VARIBLE=/home php ejemplo.php
    ```
_____
## Como dejar tareas programadas.
- **at**
    ```bash
            # ejemplo de asignacion.
            $ at now +2 minutes
            at> echo "Hola mundo" > /home/usuario/hola.txt
            at> <EOT>
            # Control E para salir
    ```
- **cron** Utiliza un archivo crontab para programar las tareas.
    ```bash
            # ver y editar las tareas del archivo
            $ crontab -e
            # Ejemlo de edicion del archivo.
            # 45 12 * * * echo "Hola" > hola.txt
    ```
_____
## Analisis de parametros de red
- **ifconfig** Lista las tarjetas con las direcciones asignadas.
- **ip a** Lista las direcciones ip de la maquina
- **hostname** Lista el nombre del host
- **route -n** Lista la puerta de enlace predeterminada o dispositivo que permite la conexion a internet.
- **nslookup** Permite validar cuales son las IP de ciertos dominios.
- **curl** Permite realizar simulaciones a peticiones como lo hace postman.
- **wget** Permite realizar descarga de paquetes
_____
## Manejo de paquetes basados en Debian
- **sudo apt-get update** Actualiza la información local de los repositorios ubuntu
- **sudo apt-get upgrade** Actualiza todos los programas instalados en la maquina.
- **sudo apt search paquete** Realiza busqueda de paquetes
- **sudo apt-cache search paquete** Realiza busqueda de paquetes
- **dpkg -l** Muestra los paquetes instalados.
- **sudo dpkg-reconfigure tzdata** Realiza una nueva configuracion de la zona horaria.
- **sudo snap install canonical-livepatch** Paquete para realizar instalaciones sin necesidad de reiniciar el host.
_____
## Desempaquetado, descompresión, compilación e instalación de paquetes
- **sudo apt install {librerias}** Descarga las librerias que son necesarias para el proyecto.
- c**wget {url con el archivo comprimido}** Descarga las librerias que son necesarias para el proyecto.
- **tar xvzf {libreria}.tar.gz** Descomprime el archivo descargado en el punto anterior.

_____
## Usuarios administracion del sistema operativo
- **id** Muestra el identificador del usuario.
- **whoami** Muestra el nombre del usuario.
- **cat /etc/passwd** Ruta donde se encuentra ubicado el registro de los usuarios.
- **cat /etc/shadow** Ruta donde se encuentra ubicado el archivo de contraseñas.
- **passwd** Comando para modificar contraseñas.
- **sudo useradd {usuario}** Comando para crear usuarios al sisitema -- NO Crea el Home --.
- **sudo adduser {usuario}** Comando para crear usuarios configurando contraseña -- Crea el Home --.
- **sudo userdel {usuario}** Comando para eliminar usuarios al sisitema.
- **cat /usr/sbin/adduser** Permite ver el contenido de la estructura de creacion de usuarios.
- **su - {usuario}** Comando para cambiar de usuario en la consola.
- **groups {usuario}** Comando para validar grupo al que pertenece el usuario.
- **sudo gpasswd -a {usuario}{grupo}** Comando para agregar usuarios a un grupo.
- **sudo gpasswd -d {usuario}{grupo}**Comando para remover usuarios de un grupo.
- **usermod -aG {grupo} {usuario}** Comando para agregar usuarios a un grupo.
- **sudo -l** Comando para revisar los permisos de usuario.
_____
## PAM para el control de acceso de usuarios
- **/etc/pam.d** Ruta donde se valida archivos de configuracion respecto a PAM.
- **/lib64/security** Ruta de acceso a las librerias de seguridad.
- **pwscore** Comando que valida la seguridad de una contrseña.
- **ulimit -a** Comando para listar los permisos que tiene el usuario para ejecutar.
- **/etc/security/time.conf** Archivo de configuracion para limitar el acceso SSH de usuarios
____
## Autenticacion de clientes y servidores sobre SSH.
- **ssh** Es un comando que permite conectar en forma segura a otra terminal, los parametros son los siguientes ssh {usuario}@{host destino}
- **sudo vi /etc/ssh/sshd_config** Archivo de configuracion reglas ssh
- **ssh-keygen** Commando para generar las llaves publicas y privadas.
- **ls .ssh** Comando para listar los archivos llaves.
- **ssh-copy-id -i ~/.ssh/id_rsa.pub {usuario}@{ip_servidor}** Comando para copiar llave publica a un servidor.
- **ssh {usuario}@{servidor}** Comando para conectar por ssh al servidor una vez realizado punto anterior.
- **ssh -vvvv {usuario}@{servidor}** Comando para revisar fallas de conexion al servidor. Entre mas vvv tenga mayor es el detalle.
_____


### Trucos.
- **Enviar correos @ a traves de la consola**
    ```bash
            # Enviando un mensaje de correo por consola
            $ echo "probando" | mail -s "Probando mensaje" destinatario@correo.com
    ```

---
Author
- Oscar Giovanni Bocanegra
- https://www.linkedin.com/in/oscarbocanegra/

___
Fuentes.
- [Platzi](https://platzi.com/)
    - Curso Intoduccion linea de comandos 
    - [Curso Administración de Servidores Linux](https://platzi.com/clases/1667-linux/22840-autenticacion-de-clientes-y-servidores-sobre-ssh/)
    - [Blog Domina la Administración de Usuarios y Permisos en Servidores Linux](https://platzi.com/blog/administracion-usuarios-servidores-linux/)
    - [Blog - Mas de 400 comandos linux](https://blog.desdelinux.net/mas-de-400-comandos-para-gnulinux-que-deberias-conocer/)
