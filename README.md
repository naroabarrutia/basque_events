# Event data from the Basque Country

This package has been developed using event data from the Open Data Euskadi api. Several functions have been created to facilitate users the interpretation of the data. The following variables have been used: 

-	Event type
-	Name of the event
-	Municipality
-	Establishment
-	Opening/Closing hours
-	Price
-	URL

## Functions

| Function | Description | Inputs |
| ------ | ------ | ------ |
| data_api | Used by other functions to obtain data from the api | Api URL |
| info_events | Gets event data from an specific month in  | Month, year & language (basque or spanish)  |
| year_data | Displays two barplots | Year and boolean value (True or False) |
| download | Downloads the data | Month, year and format (csv or json) |

## File structure
```sh
examples 
    datos_año.JPG
```

```sh
basque_events
    basque_events.py
    __init__.py
```

```sh
LICENSE.txt
```

```sh
README.md
```

```sh
setup.cfg
```

```sh
setup.py
```
## Dependencies
- [Pandas] - Tools for manipulating different data types.
- [Matplotlib] - Graph creation.
- [Request] - Obtain requested data from the api.
- [Seaborn] - Easy to use data visualization.

## Installation
```python
pip install basque_events

```

## Use case
```python
import basque_events as be

# Event info from 2021/01
be.events_info(2021, 1, 'eus')

# Download data from 2021/05 in csv format
be.download(2021, 5, 'es', 'csv')

# Display two barplots with event data from 2021 
be.year_data(2021, True)
```

![Graph](https://raw.githubusercontent.com/naroabarrutia/basque_events/main/examples/datos_a%C3%B1o.JPG)

## License
[MIT]

## Authors
>Mikel Madariaga & Naroa Barrutia 

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen)

[Pandas]: <https://pandas.pydata.org/>
[Matplotlib]: <https://matplotlib.org/>
[Request]: <https://pypi.org/project/requests/>
[Seaborn]: <https://seaborn.pydata.org/>
[MIT]: <https://choosealicense.com/licenses/mit/>