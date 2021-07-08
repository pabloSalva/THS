# Tu Hogar Sustentable (THS)

# pasos a seguir para correr la api

# 1 clonar el repositorio localmente

# 2 asegurarse de tener instalado python3 en el sistema. para eso en una terminal tipear: python3 --version

# 2.1 si no está instalado instalar una versión > 3

# 3 instalado todo crear un entorno virtual:

    virtualenv venv

# 4 luego activar el entorno virtual:

    source venv/bin/activate

# 5 una vez activado el entorno instalar todos los requerimientos del archivo requirements.txt:

    pip install -r requirements.txt

# Si todo sale bien les va a empezar a instalar un monton de dependencias y librerías

# 6 cuando termine todo corremos las migraciones iniciales:

    python manage.py migrate

# para que el comando anterior se ejecute tenemos que estar posicionados en el mismo directorio que el

# archivo manage.py. si no, va a largar un error

# 7 una vez ejecutadas exitosamente las migraciones creamos un super usuario:

    python manage.py createsuperuser

# seguimos las instrucciones y se crea solo

# 8 finalmente levantamos el servidor para asegurarnos que está todo manso:

    python manage.py runserver

# nos va a mostrar algo como esto:

    System check identified 3 issues (0 silenced).
    July 07, 2021 - 23:48:04
    Django version 3.0.8, using settings 'api_cheap_heat.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

# vamos al navegador y abrimos en la url de arriba y listo.
