# Pipeline_Project

## La contaminación en Madrid segun el clima


El objetivo de este pipeline es facilitar la visulización del impacto del clima en los niveles de contaminaciónde Madrid. Principalmente se centra en los efectos de la lluvia.

La informacion de la contaminación en Madrid se ha obtenido del dataset [_Air Quality in Madrid (2001-2018)_](https://www.kaggle.com/decide-soluciones/air-quality-madrid)

La cantidad de lluvia se obtiene mediante web scrapin de [_datosclima.es_](https://datosclima.es/Aemethistorico/Lluviasol.php)


Los parametros de entrada son:

- *Fecha Inicio* y *Fecha Fin* (YYYY-MM-DD). Indican el rango de fechas entre los que se quiere reavisar el nivel de contaminante y y las precipitaciones.

- *Contaminante*. Indica el contaminante del que se quiere ver la evolución.
Los posibles valores son:
···BEN - niveles de benceno medidos en μg/m³.
CO - niveles de  mg/m³. 
EBE - niveles de etilbencina medidos en μg/m³.
NMHC - niveles de hidrocarburos en metano (compuestos orgánicos volátiles) medidos en mg/m³
NO - niveles de oxido nitros medidos en μg/m³. 
NO_2 -niveles de dioxido de nitrogeno medidos en μg/m³.
O_3 - niveles de ozon medidos en μg/m³. 
PM10 - nivel de particulas menores de 10μm medido en μg/m³.
PM25 - nivel de particulas menores de 2.5 μm medidod en μg/m³.
SO_2 - nivel de dioxido de azufre medido en μg/m³. 
TCH - nivel de total de hidrocarburos medidos en mg/m³.
TOL - nivel de tolueno (metilbenceno) medido en μg/m³. 