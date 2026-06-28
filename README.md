# Métodos Numéricos Avanzados

Resúmenes de Métodos Numéricos Avanzados

## Contenido

Importante:
* `Resumen.pdf`: Resumen completo (todos compilados en orden), con índice al principio, listo para imprimir.
* `markdown`: Resúmenes separados, editables en formato `MD`.
* `img`: Imágenes referenciadas desde los `MD`.

> **Nota Importante:** El visualizador de Markdown de GitHub no soporta por completo la sintaxis KaTeX utilizada para las fórmulas matemáticas. Evitar leer directamente o imprimir los Markdown crudos.

Cosas que uno hace cuando está aburrido:
* `src`: Código fuente para generar el índice y combinar todos los archivos MarkDown. Estaba bastante aburrido asique hice un mini-proyecto dentro de este repo.
* `generate`: Script que genera el compilado. Se incluye primero el heading, luego el índice, y luego el contenido de cada archivo en la carpeta `markdown` en orden alfabético por nombre de archivo. Solo se incluyen los archivos terminados en `.md`.

### Recomendaciones para exportar

Se recomienda utilizar Visual Studio Code con las siguientes extensiones para editar y exportar:
  * `Markdown All in One` para _syntax highlighting_ y _shortcuts_.
  * `Markdown PDF` para exportar a PDF.

## Colaboración

Si hay algo que pueda mejorarse o contenido para agregar, se agradecerá abrir un Pull Request.

### Ejemplo de como insertar una imagen

Se hace embebiendo HTML.

```html
<p align="center">
  <img src="../img/sarrus.png" height="120"/>
</p>
```
