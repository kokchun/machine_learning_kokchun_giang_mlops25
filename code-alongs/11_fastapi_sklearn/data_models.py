from pydantic import BaseModel, Field


class IrisInput(BaseModel):
    sepal_length: float = Field(ge=3.8, le=8.4)
    sepal_width: float = Field(ge=1.5, le=4.9)
    petal_length: float = Field(ge=0.5, le=7.4)
    petal_width: float = Field(ge=0.1, le=3.0)

class PredictionOutput(BaseModel):
    predicted_flower: str
