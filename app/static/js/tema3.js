/******************************************************************************
 * Tema 3 - Bobina Circular
 * Laboratorio Virtual de Física II
 *
 * Este módulo contiene la representación 3D de una bobina circular,
 * el ejercicio resuelto y el laboratorio interactivo.
 ******************************************************************************/

/* ============================================================================
 * Constantes
 * ========================================================================== */

const RADIO_ESPIRA = 2;
const PUNTOS_ESPIRA = 100;


/* ============================================================================
 * Variables Globales
 * ========================================================================== */

// Se utilizarán más adelante para actualizar el gráfico sin recrearlo.
let graficoBobina = null;


/* ============================================================================
 * Funciones Auxiliares
 * ========================================================================== */

/**
 * Genera los puntos de una espira circular en el plano XY.
 */
function generarEspira() {
    const x = [];
    const y = [];
    const z = [];

    for (let i = 0; i <= PUNTOS_ESPIRA; i++) {

        const angulo = (2 * Math.PI * i) / PUNTOS_ESPIRA;

        x.push(RADIO_ESPIRA * Math.cos(angulo));
        y.push(RADIO_ESPIRA * Math.sin(angulo));
        z.push(0);

    }

    return { x, y, z };
    
}

/**
 * Genera los segmentos que representan el sentido
 * de circulación de la corriente sobre la espira.
 */
function generarFlechasCorriente() {

   const flechas = [];

    // Cuatro posiciones sobre la espira
    const angulos = [
        0,
        Math.PI / 2,
        Math.PI,
        3 * Math.PI / 2
    ];

    const longitud = 0.45;

    for (const angulo of angulos) {

        // Punto sobre la espira
        const x = RADIO_ESPIRA * Math.cos(angulo);
        const y = RADIO_ESPIRA * Math.sin(angulo);

        // Vector tangente (sentido antihorario)
        const tx = -Math.sin(angulo);
        const ty =  Math.cos(angulo);

        flechas.push({
            type: "scatter3d",
            mode: "lines",
            x: [x, x + longitud * tx],
            y: [y, y + longitud * ty],
            z: [0, 0],
            line: { width: 5, color: "orange"},
            showlegend: false
        });
    }
    return flechas;
}
/* ============================================================================
 * Construcción del Gráfico
 * ========================================================================== */

/**
 * Crea el gráfico 3D inicial.
 */
function crearGraficoBobina() {
    
    const puntosEspira = generarEspira();

    const traceEspira = {
        type: "scatter3d",
        mode: "lines",
        x: puntosEspira.x,
        y: puntosEspira.y,
        z: puntosEspira.z,

        name: "Espira",
        line: { width: 6 }
    };

     // ============================================
    // Centro de la espira
    // ============================================

    const traceCentro = {
        type: "scatter3d",
        mode: "markers",
        x: [0],
        y: [0],
        z: [0],
        name: "Centro",
        marker: { size: 5 }
    };

    // ============================================
    // Radio de la espira
    // ============================================

    const traceRadio = {
        type: "scatter3d",
        mode: "lines",
        x: [0, RADIO_ESPIRA],
        y: [0, 0],
        z: [0, 0],

        line: {
            width: 5,
            color: "red",
            dash: "dash"
        },

        name: "Radio R",
        showlegend: true
    };

    const traceEtiquetaRadio = {
        type: "scatter3d",
        mode: "text",
        x: [RADIO_ESPIRA / 2],
        y: [0],
        z: [0],
        text: ["R"],
        showlegend: false
    };

    const flechasCorriente = generarFlechasCorriente();

    const layout = {
        margin: { l: 0,r: 0,b: 0,t: 0},
        scene: { aspectmode: "cube"}
    };

    Plotly.newPlot(
        "grafico-bobina",
        [
            traceEspira,
            traceCentro,
            traceRadio,
            traceEtiquetaRadio ,
            ...flechasCorriente
        ],
        layout,
        { responsive: true}
    );
}


/* ============================================================================
 * Actualización del Gráfico
 * ========================================================================== */

/**
 * Actualiza el gráfico cuando cambian los parámetros.
 *
 * (Corriente, radio, número de espiras, etc.)
 */
function actualizarGraficoBobina() {

    // Implementar en el laboratorio

}


/* ============================================================================
 * Laboratorio Virtual
 * ========================================================================== */

/**
 * Inicializa los controles del laboratorio.
 */
function inicializarLaboratorio() {

    // Implementar en T3-05

}


/**
 * Recalcula resultados numéricos.
 */
function actualizarResultados() {

    // Implementar en T3-05

}


/* ============================================================================
 * Inicialización
 * ========================================================================== */

document.addEventListener("DOMContentLoaded", () => {

    crearGraficoBobina();

});