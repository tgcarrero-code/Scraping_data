## API REST: RAWG Video Games Database

### ¿Qué hace esta sección?
En esta sección se hacen requests para analizar, extraer y comparar datos de diversos videojuegos en la plataforma RAWG por medio de un API Key. Se exploraron estadísticas generales, rankings, comparaciones y, finalmente, se exporta un top 20 de los mejores juegos a todo nivel.

### ¿Cómo obtener la API Key?
1. Crear una cuenta en https://rawg.io
2. Ir a https://rawg.io/apidocs
3. Hacer clic en "Get API Key"
4. Copiar la key y pegarla en el notebook como variable local

### ¿Cómo correr el notebook?
1. Abrir `api/tarea_rawg_api.ipynb` en Jupyter
2. Reemplazar `API_KEY` con tu key personal
3. Ejecutar todas las celdas en orden

### ¿Qué contiene el output?
Contiene los 20 mejores juegos de todos los tiempos según RAWG, con las columnas: nombre, rating, metacritic, fecha de lanzamiento y género principal.
