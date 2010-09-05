import models
from src.management import initialize

# lambda function for getting location with name
loc = lambda x: models.Location.objects.get(name=x)

LOCATION=[
    dict(name='Sydney')
]
FOOD=[
    dict(name='Apple', type='FRUIT', origin=lambda: loc("Sydney"))
]

initialize(models.Location, LOCATION)
initialize(models.Food, FOOD)