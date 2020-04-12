# Como subir tu trabajo de Colab a Git
A continuación se comentara los pasos a tener en cuenta para realizar modificaciones en tus repositorios de git desde git hub


1.   El primer paso a tener en cuenta es clonar tu repositorio de git en nuestro colab para lo que utilizaremos el siguiente codigo:


```
!git clone https://github.com/psariasz/*<name-repository>*.git

#Es importante no olvidar el ! ya que colab entiende que es un formato bash
```
obtendremos un output como el que se muestra a continuación:

```
Cloning into 'cloud-repository'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (4/4), done.
```
2.  Recuerda que es importante recordar en que carpeta te encuentras, para la edicion del repositorio. Para esto utilizaremos los siguientes comandos a continuación:

```
pwd 
#Me muestra en que carpeta me encuentro ubicado en el momento
cd <DirectoryName>
#cambiamos de directorio hacia adelante
cd ..
#si me quiero salir de directorio
!ls
#se encarga de listarme los directorios o el contenido de estos
!cat <FileName>
#Se encarga de leerme o mostrarme que contiene el archivo
```
3. Podemos realizar cambios bien sea en el codigo o utilizando caracteres como # %%writefile <FileName> y correrlos en una celda de colab
4. Ahora para guardar los cambios realizados correremos los siguientes codigos:

```
!git add . 

!git init

!git config --global user.email "<Correo electronico>"

!git config --global user.name "<UserName>"

!git add .

!git commit -m "<NombreDelCambio>"

!git remote add origin https://<UserName>:<Password>@github.com/<UserName>/<Name-Repository>.git

!git push -u origin master

#si no funciona, se debe utilizar la siguiente función para eliminar los ya creados
!git remote rm origin
```
Estos son los pasos para hacer cambios en nuestro repositorio de GitHub desde Colab.

Ahora bien es importante relatar los pasos para crear un nuevo script desde colab y subirlo a nuestro repositorio

1. observamos si lacarpeta donde nos encontramos es el desado para crear nuestra nueva carpeta recuerda utilizar la funcion #pwd
2. luego de encontrarnos donde queremos vamos a utilizar el siguiente codigo

```
!mkdir <FileName>      #crea la nueva carpeta
cd <FileName>          #nos lleva directamente al archivo creado
!touch <FileName>.xx   #esta funcion crea el archivo de codigo y nuestras "xx" recuerda que el archivo puede estar en .py  de python o .sh de bash, etc.
!cat <FileName>        #Se encarga de leerme o mostrarme que contiene el archivo
```
3. sigues todos los puntos realizados anteriormente para poder subir el archivo a tu repositorio en GitHub.Recuerda regresar al directorio
donde se estaba creando todo ``` cd .. ```
