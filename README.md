Se necesita tener previamente instalado las siguientes dependencias:
- FastAPI
- uvicorn
- numpy
- pandas

# Desarrollo y despliegue de API

# URL pública
La API está desplegada en Render y disponible en:
https://desarrollo-y-despliegue-de-api-deploy.onrender.com

# Descripción
Esta API expone un modelo de regresión basado en el dataset 'real_state_ecuador_dataset'
Permite predecir el precio de alquiler de una vivienda en función de sus características.

# Instrucciones de uso
Clonar el repositorio:
   git clone https://github.com/angelariasparedes-png/Notebook-de-an-lisis-de-datos-1.-Procesamiento-y-an-lisis-de-datos-.git
   cd api

# Justificación del modelo elegido
Se utilizó un modelo de regresión lineal porque es un método sencillo, interpretable y adecuado como punto de partida para analizar la relación entre las característica>

El desempeño del modelo evaluó las métricas MAE, RMSE y R². El MAE y el RMSE muestran el error promedio y típico de las predicciones, mientras que el R² indica el grado>

# Ejemplo de la API
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{"provincia":"Pichincha","lugar":"Quito","num_dormitorios":2,"num_banos":3,"area":120,"num_garages":1}'


