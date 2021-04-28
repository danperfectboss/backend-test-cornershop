Este es un repositorio para prueba tecnica para posición backend de cornershop

- [Canal de Slack](https://compaiaprueba.slack.com/archives/C020235MGCW)

El token de Slack que va en el código se envió por correo.

El token se tiene que insertar en la linea 21 del archivo bot.py para que pueda enviar mensajes por medio de Slack, el archivo bot.py se encuenra ubicado en "app_delivery/complements/bot.py"

Para que el projecto funcione correctamente se tiene que instalar los requerimentos que vienen el el archivo "requirements.py"  ubicado en "backend-test-cornershop/backendTest/requirements.txt"
Usamos el comando:
$ pip install -r requirements.txt

Se necesitaran tener 2 terminales abiertas una para correr celery y el otro para correr el projecto Django
Se ejecuta este comando al nivel del archivo "manage.py"

Cerely:
$ celery -A backendTest worker -l info

en la otra termina se ejecuta el comando
$ python3 manage.py runserver

Rutas:
Para navegar por el sistema nos posicionamos en el navegador en la siguiente ruta, la cual mostrara los elementos registrados hasta el momento en la base
[http://127.0.0.1:8000/allRecipes/](http://127.0.0.1:8000/allRecipes/)
Y para mostrar unicamente el menu del día es:
[http://127.0.0.1:8000/menu/<int<](http://127.0.0.1:8000/menu/1)

Este link es el que se mandará al canal de Slack

Se uso una app de Heroku con Redis para hacer funcionar Celery

Buena Suerte!
  



