# Covidata

Easily access NASA, ESA and JAXA data

## Datasets
### ESA
    mortality and natality
    coronavirus cases worldwide

### JAXA
    greenhouse gases concentration

### NASA
    landslides
    atmospherical data

## Example
```python
import covidata
os = covidata.esa.opendata
df = os.get()
print(df.head())
```
