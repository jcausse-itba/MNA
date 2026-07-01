# Métodos Numéricos Avanzados

Resúmenes de Métodos Numéricos Avanzados

## Contenido

Importante:
* `Resumen.pdf`: Resumen completo (todos compilados en orden), con índice al principio, listo para imprimir.
* `markdown`: Resúmenes separados, editables en formato `MD`.
* `img`: Imágenes referenciadas desde los `MD`.
* `code_examples`: Algunos ejemplos de código en Python que usé para entender mejor algunos temas de la materia.

> **Nota Importante:** El visualizador de Markdown de GitHub no soporta por completo la sintaxis KaTeX utilizada para las fórmulas matemáticas. Evitar leer directamente o imprimir los Markdown crudos.

Generación del MD compilado:
* `src`: Código fuente para generar el índice y combinar todos los archivos MarkDown.
* `generate`: Script que genera el compilado. Se incluye primero el _heading_, luego el índice, y luego el contenido de cada archivo en la carpeta `markdown` en orden alfabético por nombre de archivo. Solo se incluyen los archivos terminados en `.md`.

### Recomendaciones para exportar a PDF

Se recomienda utilizar Visual Studio Code con las siguientes extensiones para editar y exportar a PDF:
  * `Markdown All in One` para _syntax highlighting_ y _shortcuts_.
  * `Markdown PDF` para exportar a PDF.

## Colaboración

Si hay algo que pueda mejorarse o contenido para agregar, se agradecerá abrir un Pull Request.

### Ejemplo de como insertar una imagen

Se hace embebiendo HTML.

```html
<p align="center">
  <img src="../img/<nombre_archivo>.png" height="<altura_deseada>"/>
</p>
```

donde `<nombre_archivo>` es el nombre del archivo en la carpeta `img` y `<altura_deseada>` es la altura en píxeles deseada.
