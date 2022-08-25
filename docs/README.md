# Prototipo Practica "Trivia Guatemala"

Este es un prototipo basado en la información disponible hasta la unidad 3 de
el curso de "Practica del desarrollo de software"

## Desarrollo

Necesita [`python`](https://www.python.org/) (para el backend) y
[`nodejs`](https://nodejs.org/es/) (para compilar el frontend).

### Servidor

Instale los paquetes listados en `api/requirements.txt` (preferiblemente en un
entorno virtual)

```
pip -r ./api/requirements.txt
```

Puede correr el servidor con el siguiente comando (dentro del directorio `api`):

```
python app.py
```

### Frontend

Dentro del directorio `webapp` corra el comando:

```
npm install
```

Puede correr el servidor de desarrollo con `npm run dev`

**Nota:** Ambos servidores tienen que correr a la vez. El servidor de python
corre por default en `http://localhost:5000`, en caso de correr en otra url
tiene que colocarla en `webapp/nuxt.config.js` reemplazando el default de
`axios.baseURL`.

## Producción

Corra el comando:

```
npm run build
```

Para obtener los archivos estáticos. Tiene que definir la variable de entorno
`HOST_URL` con la URL en la que se va a hostear el sitio.

Configure el servidor para que sirva los assets estáticos, y que todas las
solicitudes que vayan a las rutas de `/api` las redirija al servidor de python.
