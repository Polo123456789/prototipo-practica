# Rutas del sitio

El siguiente diagrama de estado de una dia del flujo que seguirira un usuario
del sitio:

![](./img/estados.png)

Todas las rutas de la API reciben y contestan con objetos JSON. Excepto a que se
mencione explicitamente, todas las rutas `/api/*` reciben sus datos con un
`POST`.

Todas las rutas a excepcion de `/`, `/inicio-sesion` y `/registrarse` requieren
que el usuario este autenticado. De no estar autenticado se le redireccionara a
`inicio-sesion`.

De no estar autenticado, las rutas `/api/*` responderan con:

```JSON
{
    "error": {
        "detail": "Tiene que estar autenticado para iniciar sesion"
    }
}
```

<!-- Revisar para que se ajuten medianamente a:

https://jsonapi.org/format/

Al menos que tome la parte de que la respuesta tiene `data` o `error`

Los objetos que devueve ya estan bien para ser la data, solo hay que definir
que es lo que tendran los de error.

-->

# Index

## `/`

No tiene nada, unicamente refiere al usuario a que inice sesion o que se
registre.

# Inicio de Sesion

## `/inicio-sesion`

Le solicita al usuario su correo y contraseña. De ser correctos, lo redirije a
`/dashboard`. De otro modo, se lo indica al usuario.

## `/api/inicio-sesion`

Recibe un objeto en la siguiente forma:

```typescript
{
    email: string,
    password: string
}
```

Valida las credenciales, y responde con un objeto en la forma:

```typescript
{
    valid: boolean
}
```

Guarda en una sesion en el servidor del usuario.

# Registro

## `/registrarse`

Le solicita al usuario:

* Nombres
* Apellidos
* Fecha de nacimiento
* Correo electronico
* Contraseña
* Si acepta recibir correos

**Nota:** Refierase a el documento de requerimientos para ver las restricciones
en las entradas del usuario

De registrarse exitosamente se le redirige a `/inicio-sesion`.

## `/api/registrarse`

Recibe un objeto en la siguiente forma:

```typescript
{
    name: string,
    surname: string,
    birthDate: string,
    email: string, 
    password: string,
    wantsEmails: boolean
}
```

Donde `birthDate` se obtuvo de un objeto `Date` usando el metodo
`toUTCString` [^1].

[^1]: Para que sea mas sencillo obtener la fecha desde python.
[Referencia](https://stackoverflow.com/questions/8153631/js-date-object-to-python-datetime).

De registrar exitosamente al usuario el servidor respondera un objeto en la
forma:

```typescript
{
    error?: string,
    registered: boolean
}
```

Donde `error` solo estara definido en caso de que `registered` sea falso.

# Dashboard

## `/dashboard`

Le al usuario ir a:

* Su pagina de perfil (`/profile`).
* La seccion de trivia (`/trivia`).
* Agregar amigos (`/add-friend`).

Tambien le mostrara al usuario:

* Su puntaje y nivel.
* Las solicitudes de amistad que tenga pendientes.

## `/api/dasboard-data`

**Metodo:** `GET`

Responde con un objeto en la forma:

```typescript
{
    name: string,
    surname: string,
    score: number,
    level: number,
    avatar: string,
    friendRequests: FriendRequest[]
}
```

Donde `FriendRequest` se define como:

```typescript
{
    senderId: number,
    name: string,
    surname: string,
    avatar: string
}
```
## `/api/process-friend-request`

Recibe un objeto en la forma:

```typescript
{
    accepted: boolean,
    senderId: number
}
```