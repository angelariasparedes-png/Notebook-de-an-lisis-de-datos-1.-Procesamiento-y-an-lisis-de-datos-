from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd

# iniciar la app FastAPI
app = FastAPI()

# definimos la entrada
class InputData(BaseModel):
    provincia: str
    lugar: str
    num_dormitorios: int
    num_banos: int
    area: float
    num_garages: int

# Supongamos que ya entrenaste tu modelo y tienes los coeficientes
# Aquí pondrías los coeficientes obtenidos con numpy.linalg.pinv
coef = np.array([100.0, 20.0, 30.0, 50.0, 5.0, 10.0])  # ejemplo
# Nota: el primer valor es el intercepto

@app.post("/predict")
def predict(data: InputData):
    # Convertir entrada a vector
    X = np.array([
        1,  # intercepto
        data.num_dormitorios,
        data.num_banos,
        data.area,
        data.num_garages,
        # Aquí deberías añadir las variables dummy de provincia y lugar
        # según cómo entrenaste tu modelo
    ])

    # Calcular predicción
    y_pred = float(X @ coef[:len(X)])  # producto matricial

    return {"prediction": y_pred}
