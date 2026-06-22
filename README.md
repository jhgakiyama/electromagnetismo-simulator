# Simulador de Electromagnetismo

Aplicación web educativa desarrollada como apoyo didáctico para la UT 6 Campo de Inducción Magnética de la cátedra de Física II de la Universidad Tecnológica Nacional - Facultad Regional Resistencia.

---

## Objetivo

Facilitar la comprensión de los conceptos fundamentales del electromagnetismo mediante:

* Explicaciones teóricas
* Simulaciones interactivas
* Gráficos dinámicos
* Ejercicios resueltos
* Modos de exploración

El proyecto busca complementar el aprendizaje tradicional permitiendo visualizar fenómenos físicos y experimentar con distintas variables en tiempo real.

---

## Tecnologías Utilizadas

* Python 3
* Flask
* Plotly
* Bootstrap 5
* HTML5
* CSS3
* JavaScript
* Docker
* Docker Compose

---

## Ejecución del Proyecto

### Construir la imagen Docker

```bash
docker-compose build
```

### Iniciar la aplicación

```bash
docker-compose up
```

### Acceder a la aplicación

```text
http://localhost:5000
```

---

## Estructura del Proyecto

```text
electromagnetismo-simulator/

├── app/
│   ├── routes/
│   ├── services/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   └── templates/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run.py
└── README.md
```

---

## Estado Actual del Proyecto

### Tema 1 - Campo Magnético de un Conductor Rectilíneo Infinito

Estado: COMPLETADO

Incluye:

* Introducción al fenómeno físico
* Explicación teórica
* Fórmula fundamental
* Unidades utilizadas
* Simulación interactiva
* Visualización conceptual
* Relación B ∝ I
* Relación B ∝ 1/r
* Ejercicio resuelto paso a paso
* Modo Exploración interactivo
* Conclusiones académicas

---

## Funcionalidades Implementadas

### Modo Aprender

Permite ingresar valores de corriente y distancia para calcular el campo magnético generado por un conductor rectilíneo infinitamente largo.

### Visualización Conceptual

Gráficos que permiten comprender visualmente las relaciones:

* B ∝ I
* B ∝ 1/r

### Ejercicio Resuelto

Desarrollo completo del ejercicio propuesto en Física II:

* Cálculo del campo magnético a 100 cm de un conductor.
* Determinación de la distancia necesaria para obtener un campo magnético específico.

### Modo Exploración

Permite modificar en tiempo real:

* Corriente eléctrica (I)
* Distancia al conductor (r)

Visualizando simultáneamente:

* Valor del campo magnético
* Curva B vs r
* Posición actual de observación
* Representación del conductor

---

## Roadmap

### Tema 1 - Campo Magnético de un Conductor Rectilíneo Infinito

* [x] Implementado

### Tema 2 - Campo Magnético Total de Dos Conductores Paralelos

* [ ] Pendiente

Incluye:

* Superposición de campos magnéticos
* Regla de la mano derecha
* Suma vectorial

### Tema 3 - Campo Magnético de una Bobina Circular

* [ ] Pendiente

Incluye:

* Campo magnético en el centro de una espira

---

## Autor

Proyecto académico orientado al aprendizaje de Física II y al desarrollo de aplicaciones científicas utilizando Python, Flask y Plotly.

Universidad Tecnológica Nacional
Facultad Regional Resistencia
