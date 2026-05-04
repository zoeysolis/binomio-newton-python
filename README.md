# binomio-newton-python
Desarrollo paso a paso de binomios de Newton (a + b)^n usando combinatoria y lógica algorítmica

# Desarrollo de Binomios de Newton 
Este proyecto fue desarrollado para la materia **Matemática Discreta**. Es una herramienta en Python que calcula el desarrollo completo de un binomio del tipo $(a + b)^n$ aplicando el Teorema del Binomio y combinatoria.

##  Características
- **Cálculo de Coeficientes:** Utiliza la fórmula de combinatoria $C(n, k) = \frac{n!}{k!(n-k)!}$.
- **Paso a Paso:** Muestra el desarrollo desglosado antes de la simplificación.
- **Manejo de Variables:** Capaz de procesar términos con coeficientes numéricos y variables (ej: `2x`, `-3y`).
- **Simplificación:** Agrupa y ordena las potencias de forma automática.

##  Lógica Matemática
El programa se basa en la fórmula:
$$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$$

##  Cómo usarlo
1. Ejecuta el script: `python binomio.py`
2. Ingresa el primer término (ej: `x`).
3. Ingresa el segundo término (ej: `2y`).
4. Ingresa el exponente (ej: `3`).
5. El programa devolverá: `x^3 + 6x^2y + 12xy^2 + 8y^3`.

---
*Proyecto de lógica aplicada - Tecnicatura en Desarrollo de Software*
