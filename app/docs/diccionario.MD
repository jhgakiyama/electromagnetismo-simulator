# Convención de Nombres - Símbolos, Fórmulas y Subíndices

**Versión:** 1.0  
**Proyecto:** Simulador de Electromagnetismo - Física II (UTN)

---

# Objetivo

Definir una nomenclatura uniforme para todo el proyecto, incluyendo:

- Código Python
- Templates HTML
- Gráficos Plotly
- Explicaciones teóricas
- Variables matemáticas
- Documentación

El objetivo es que el alumno encuentre siempre la misma notación durante todo el recorrido.

---

# Regla General

Se utilizará la siguiente convención:

- Símbolos matemáticos → Notación física estándar.
- Variables Python → snake_case descriptivo.
- Variables HTML → mismo nombre utilizado en Python.
- Textos visibles → utilizar subíndices reales (₁, ₂).

---

# Conductores

| Símbolo | Nombre | Descripción |
|----------|---------|-------------|
| I₁ | Conductor 1 | Primer conductor rectilíneo |
| I₂ | Conductor 2 | Segundo conductor rectilíneo |

Variables Python:

```python
conductor1
conductor2
corriente1
corriente2
```

---

# Puntos de observación

| Símbolo | Nombre | Descripción |
|----------|---------|-------------|
| P₁ | Punto de observación 1 | Punto resuelto paso a paso |
| P₂ | Punto de observación 2 | Punto utilizado como ejercicio del alumno |

Variables Python:

```python
p1
p2
```

---

# Vector radio

Representa la distancia entre un conductor y el punto de observación.

| Símbolo | Nombre | Descripción |
|----------|---------|-------------|
| r₁ | Vector radio desde I₁ hasta P |
| r₂ | Vector radio desde I₂ hasta P |

Variables Python:

```python
r1
r2
```

---

# Diferencias cartesianas

| Símbolo | Nombre |
|----------|---------|
| Δx | Diferencia sobre el eje X |
| Δy | Diferencia sobre el eje Y |

Variables Python:

```python
dx
dy
```

Para el segundo conductor:

```python
dx1
dy1

dx2
dy2
```

---

# Campo magnético

| Símbolo | Nombre | Descripción |
|----------|---------|-------------|
| B₁ | Campo producido por I₁ |
| B₂ | Campo producido por I₂ |
| B | Campo magnético total |

Variables Python:

```python
b1
b2
b_total
```

---

# Componentes cartesianas

## Campo B₁

| Símbolo | Nombre |
|----------|---------|
| Bx₁ | Componente horizontal |
| By₁ | Componente vertical |

Variables:

```python
bx1
by1
```

---

## Campo B₂

| Símbolo | Nombre |
|----------|---------|
| Bx₂ | Componente horizontal |
| By₂ | Componente vertical |

Variables:

```python
bx2
by2
```

---

## Campo total

| Símbolo | Nombre |
|----------|---------|
| Bx | Componente horizontal total |
| By | Componente vertical total |

Variables:

```python
bx_total
by_total
```

---

# Constantes físicas

| Símbolo | Nombre |
|----------|---------|
| μ₀ | Permeabilidad magnética del vacío |

Variables Python:

```python
MU0
```

---

# Fórmulas utilizadas

## Distancia (Vector radio)
```
r = √(Δx² + Δy²)
```
---

## Campo magnético de un conductor rectilíneo infinito

```
       μ₀ · I
B = ───────────
      2π · r
```

---

## Componentes cartesianas

```
Bx = B · cos(θ)

By = B · sin(θ)
```

**Nota:** En la implementación del proyecto no se calcula el ángulo. Las componentes se obtienen utilizando el vector perpendicular asociado al vector radio.

---

## Principio de superposición

```
Bx = Bx₁ + Bx₂

By = By₁ + By₂
```

---

## Magnitud del campo resultante

```
|B| = √(Bx² + By²)
```
---

# Convención para textos del simulador

En todas las explicaciones visibles al alumno se utilizarán subíndices reales.

Correcto:

```
P₁
P₂
I₁
I₂
B₁
B₂
Bx₁
By₁
Bx₂
By₂
r₁
r₂
```

Evitar:

```
P1
P2
I1
I2
B1
B2
r1
r2
```

---

# Convención para el código Python

En Python se utilizará siempre `snake_case`.

Ejemplos:

```python
corriente1
corriente2

r1
r2

b1
b2

bx1
by1

bx2
by2

bx_total
by_total

b_total
```

---

# Beneficios

Esta convención garantiza que:

- El alumno vea siempre la misma notación en todo el material.
- El código sea consistente y fácil de mantener.
- Los gráficos, explicaciones y cálculos utilicen exactamente los mismos símbolos.
- La documentación técnica y académica permanezca sincronizada.