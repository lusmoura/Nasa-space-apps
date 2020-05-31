# Covidata

Easily access NASA, ESA and JAXA data

## About

You can use this API to access and see statistics about NASA, JAXA and ESA datasets. Check the available datasets and how to use them bellow.

## Available Datasets
### ESA
    mortality and natality
    coronavirus cases worldwide

### JAXA
    greenhouse gases concentration

### NASA
    landslides
    atmospherical data

## Main Functions
### Constructors
    Initialize an object with the required data

### Describe
    Generete statistics about all the features in the dataset, such as mean, standard deviation and quartiles.

## Examples
```python
from covidata.nasa import Landslides

LS = Landslides(subset=100, verbose=True)

print(LS.summarize())
print(LS.head())
```
