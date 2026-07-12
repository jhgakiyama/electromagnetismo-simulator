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
const ALTURA_CAMPO = 1.25;
const COLORES = {
    espira: "#0d6efd",
    radio: "#dc3545",
    corriente: "#fd7e14",
    campo: "#198754",
    negro: "#000000"
};
/* ============================================================================
 * Variaes Globales
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

/**
 * Crea una flecha formada por un segmento y un cone.
 */
function crearTraceFlecha(x0, y0, z0, dx, dy, dz, color, nombre = null,mostrarLeyenda = false) {

    const linea = {
        type: "scatter3d",
        mode: "lines",
        x: [x0, x0 + dx],
        y: [y0, y0 + dy],
        z: [z0, z0 + dz],

        line: { width: 5,color: color},
        name: nombre,
        showlegend: mostrarLeyenda
    };

    const punta = {
        type: "cone",
        x: [x0 + dx],
        y: [y0 + dy],
        z: [z0 + dz],
        u: [dx],
        v: [dy],
        w: [dz],
        sizemode: "absolute",
        sizeref: 0.18,
        colorscale: [ [0, color],[1, color]],
        showscale: false,
        hoverinfo: "skip"
    };

    return [linea, punta];

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

        line: { width: 6}
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
        marker: { size: 5, color: COLORES.negro,}
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
            color: COLORES.radio,
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
    const longitud = 0.45;
    const traces = [];
    const angulos = [
        0,
        Math.PI / 2,
        Math.PI,
        (3 * Math.PI) / 2
    ];

    for (let i = 0; i < angulos.length; i++) {
        const angulo = angulos[i];
        const x = RADIO_ESPIRA * Math.cos(angulo);
        const y = RADIO_ESPIRA * Math.sin(angulo);
        const tx = -Math.sin(angulo);
        const ty = Math.cos(angulo);

        traces.push(
            ...crearTraceFlecha(
                x,
                y,
                0,
                longitud * tx,
                longitud * ty,
                0,
                COLORES.corriente,
                "Corriente",
                i === 0
            )
        );
    }
    return traces;
}


/**
 * Trace del campo B
 */
function crearTraceCampo() {
    return crearTraceFlecha(0,0,0,0,0,ALTURA_CAMPO,COLORES.campo,"Campo B",true);
}

/**
 * Etiqueta del Campo B.
 */
function crearTraceEtiquetaCampo() {
    return {
        type: "scatter3d",
        mode: "text",
        x: [0],
        y: [0],
        z: [ALTURA_CAMPO + 0.15],
        text: ["B"],
        showlegend: false
    };
}

/* ============================================================================
 * Layout
 * ========================================================================== */

function crearLayout() {
    return {
        margin: {l: 0,r: 0,b: 0,t: 0},
        scene: {aspectmode: "cube"}
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
            ...crearTracesCorriente(),
            ...crearTraceCampo(),
            crearTraceEtiquetaCampo()
        ],

        crearLayout(),
        { responsive: true}
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