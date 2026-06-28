# Sistema de Visión Artificial para Reconocimiento de Dígitos

Este repositorio contiene el desarrollo del **Proyecto 2** para el curso **CS6001 Introducción a las Ciencias de la Computación** en la **Universidad de Ingeniería y Tecnología (UTEC)**. El sistema implementa un clasificador de dígitos manuscritos basado en similitud matemática utilizando el algoritmo de Vecinos Más Cercanos ($k$-NN) desarrollado desde cero.

## Fundamento Teórico

### 1. Representación de Imágenes y Distancia Euclidiana
Cada imagen manuscrita preprocesada de $8\times8$ píxeles se transforma mediante un aplanamiento (*flattening*) en un vector de 64 componentes, donde cada posición corresponde a la intensidad en escala de grises de un píxel. La similitud entre una imagen de prueba ($x$) y una de referencia ($y$) se calcula mediante la fórmula de la distancia euclidiana:

$$d(x,y)=\sqrt{\sum_{i=1}^{64}(x_{i}-y_{i})^{2}}$$

### 2. Algoritmo de Clasificación ($k$-NN)
Se evalúa la distancia euclidiana entre la muestra y los 1797 registros del dataset `digits` de *scikit-learn*. El sistema extrae los 3 vecinos más cercanos ($k=3$) y asigna por mayoría de votos la clase predominante. En caso de empate absoluto (3 clases distintas), se activa una heurística que analiza los 10 vecinos más cercanos para tomar una decisión consistente.

---

## Flujo de Procesamiento (Pipeline)
El script desarrollado en Python realiza los siguientes pasos secuenciales sobre cada archivo de imagen:
1. **Carga de Datos:** Importación de los 1797 números de la colección `datasets.load_digits()`.
2. **Interpolación Espacial:** Reducción de dimensiones espaciales a una matriz de $8\times8$ píxeles.
3. **Inversión Cromática:** Ajuste para obtener fondo oscuro con trazo claro, emparejando el formato original del dataset.
4. **Normalización:** Mapeo de los rangos de intensidad de píxeles a valores enteros discretos en el intervalo $[0, 16]$.

## Conclusiones Clave

**Sensibilidad al Preprocesamiento:** El cálculo basado exclusivamente en distancia euclidiana es altamente sensible a la variabilidad geométrica. Un mal recorte periférico o un exceso de márgenes blancos altera drásticamente las distancias multidimensionales imposibilitando el acierto.
**Compresión Espacial de Información:** Reducir las dimensiones a matrices de $8\times8$ actúa como un filtro suavizador que elimina las frecuencias altas del trazo (imperfecciones del lapicero), pero remueve detalles morfológicos esenciales para diferenciar dígitos complejos.
**Discrepancia de Datos (*Data Mismatch*):** El bajo rendimiento no responde a un error procedimental de lógica de programación en el código, sino a las marcadas diferencias estilísticas y estructurales entre las muestras caligráficas tomadas por el equipo y los patrones del dataset de referencia de scikit-learn.

---
"Dota es mejor que LOL (Yarasca, 2026)".
