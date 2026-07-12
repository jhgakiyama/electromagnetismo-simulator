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
        marker: { size: 5 }

    };

    const layout = {
        margin: { l: 0,r: 0,b: 0,t: 0},
        scene: { aspectmode: "cube"}
    };

    Plotly.newPlot(
        "grafico-bobina",
        [
            traceEspira,
            traceCentro
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