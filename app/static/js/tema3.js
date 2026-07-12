/******************************************************************************
 * Tema 3 - Bobina Circular
 * Laboratorio Virtual de Física II
 *
 * Representación 3D de una bobina circular utilizando Plotly.js
 ******************************************************************************/

/* ============================================================================
 * Configuración
 * ========================================================================== */

const RADIO_ESPIRA = 2;
const PUNTOS_ESPIRA = 100;


/* ============================================================================
 * Variables Globales
 * ========================================================================== */

let graficoBobina = null;


/* ============================================================================
 * Geometría
 * ========================================================================== */

/**
 * Genera los puntos de una espira circular sobre el plano XY.
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
 * Traces Plotly
 * ========================================================================== */

/**
 * Espira circular.
 */
function crearTraceEspira() {

    const puntos = generarEspira();

    return {

        type: "scatter3d",

        mode: "lines",

        x: puntos.x,

        y: puntos.y,

        z: puntos.z,

        name: "Espira",

        line: {

            width: 6

        }

    };

}


/**
 * Centro de la espira.
 */
function crearTraceCentro() {

    return {

        type: "scatter3d",

        mode: "markers",

        x: [0],

        y: [0],

        z: [0],

        name: "Centro",

        marker: {

            size: 5

        }

    };

}


/**
 * Radio R.
 */
function crearTraceRadio() {

    return {

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

}


/**
 * Etiqueta del radio.
 */
function crearTraceEtiquetaRadio() {

    return {

        type: "scatter3d",

        mode: "text",

        x: [RADIO_ESPIRA / 2],

        y: [0],

        z: [0],

        text: ["R"],

        showlegend: false

    };

}


/**
 * Flechas que indican el sentido de circulación
 * de la corriente eléctrica.
 */
function crearTracesCorriente() {

    const flechas = [];

    const angulos = [

        0,

        Math.PI / 2,

        Math.PI,

        (3 * Math.PI) / 2

    ];

    const longitud = 0.45;

    for (const angulo of angulos) {

        const x = RADIO_ESPIRA * Math.cos(angulo);
        const y = RADIO_ESPIRA * Math.sin(angulo);

        const tx = -Math.sin(angulo);
        const ty = Math.cos(angulo);

        flechas.push({

            type: "scatter3d",

            mode: "lines",

            x: [x, x + longitud * tx],

            y: [y, y + longitud * ty],

            z: [0, 0],

            line: {

                width: 5,

                color: "orange"

            },

            showlegend: false

        });

    }

    return flechas;

}


/* ============================================================================
 * Layout
 * ========================================================================== */

function crearLayout() {

    return {

        margin: {

            l: 0,

            r: 0,

            b: 0,

            t: 0

        },

        scene: {

            aspectmode: "cube"

        }

    };

}


/* ============================================================================
 * Construcción del gráfico
 * ========================================================================== */

function crearGraficoBobina() {

    graficoBobina = Plotly.newPlot(

        "grafico-bobina",

        [

            crearTraceEspira(),

            crearTraceCentro(),

            crearTraceRadio(),

            crearTraceEtiquetaRadio(),

            ...crearTracesCorriente()

        ],

        crearLayout(),

        {

            responsive: true

        }

    );

}


/* ============================================================================
 * Actualización del gráfico
 * ========================================================================== */

function actualizarGraficoBobina() {

    // Implementar en el laboratorio.

}


/* ============================================================================
 * Laboratorio Virtual
 * ========================================================================== */

function inicializarLaboratorio() {

    // Implementar en T3-05

}


function actualizarResultados() {

    // Implementar en T3-05

}


/* ============================================================================
 * Inicialización
 * ========================================================================== */

document.addEventListener("DOMContentLoaded", () => {

    crearGraficoBobina();

});