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
    "error": "Tiene que estar autenticado para realizar la solicitud"
}
```

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
    email: string
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