# Bemi Django Example

You can find a demo and detailed documentation here https://docs.bemi.io.

## System Dependencies

* Devbox
  * PostgreSQL
  * Python

## Installation

```
make init
make up-services
make create
cp django/.env.sample django/.env
```

## Development

```
make install
make migrate
make up-django
```
