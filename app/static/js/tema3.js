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
const CAMARA_INICIAL = {
    eye: {x: 1.6,y: 1.6,z: 1.8},
    center: {x: 0,y: 0,z: 0},
    up: {x: 0,y: 0,z: 1  }
};

// Compensa el punto de anclaje del marker "arrow" de Plotly.
const AJUSTE_PUNTA_FLECHA_2D = -0.20;
const LONGITUD_CAMPO_2D = 0.80;
const AJUSTE_PUNTA_CAMPO_2D = -0.20;

const MU_0 = 4 * Math.PI * 1e-7;
/* ============================================================================
 * Variaes Globales
 * ========================================================================== */

let graficoBobina = null;

let sliderN;
let sliderI;
let sliderR;
let btnRestablecer;

let valorN;
let valorI;
let valorR;


/******************************************************************************
 * Funciones auxiliares
 ******************************************************************************/

function formatearCampoMagnetico(campoMagnetico) {

    const partes = campoMagnetico
        .toExponential(3)
        .split("e");

    const mantisa = partes[0];
    const exponente = Number(partes[1]);

    return `${mantisa} × 10<sup>${exponente}</sup>`;

}

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
        scene: {
            aspectmode: "cube",
            camera: CAMARA_INICIAL
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
            ...crearTracesCorriente(),
            ...crearTraceCampo(),
            crearTraceEtiquetaCampo()
        ],

        crearLayout(),
        { responsive: true}
    );
}

/******************************************************************************
 * Gráfico 2D - Ejercicio Resuelto
 ******************************************************************************/

// Geometría
function generarEspira2D() {
    const x = [];
    const y = [];

    for (let i = 0; i <= PUNTOS_ESPIRA; i++) {
        const angulo = (2 * Math.PI * i) / PUNTOS_ESPIRA;
        x.push(RADIO_ESPIRA * Math.cos(angulo));
        y.push(RADIO_ESPIRA * Math.sin(angulo));
    }
    return { x, y };
}

// Trace
function crearTraceEspira2D() {
    const puntos = generarEspira2D();
    return {
        type: "scatter",
        mode: "lines",
        x: puntos.x,
        y: puntos.y,
        line: { color: COLORES.espira, width: 5},
        hoverinfo: "skip",
        showlegend: false
    };
}


// Centro
function crearTraceCentro2D() {
    return {
        type: "scatter",
        mode: "markers",
        x: [0],
        y: [0],
        marker: {size: 8,color: "black"},
        hoverinfo: "skip",
        showlegend: false
    };
}

// Radio
function crearTraceRadio2D() {
    return {
        type: "scatter",
        mode: "lines",
        x: [0, RADIO_ESPIRA],
        y: [0, 0],
        line: {color: COLORES.radio,width: 3,dash: "dash"},
        hoverinfo: "skip",
        showlegend: false
    };
}

// Etiqueta R
function crearTraceEtiquetaRadio2D() {
    return {
        type: "scatter",
        mode: "text",
        x: [RADIO_ESPIRA / 2],
        y: [0.18],
        text: ["R=0.1 m"],
        textfont: {size: 16},
        hoverinfo: "skip",
        showlegend: false
    };
}

function crearTracesCorriente2D() {
    const traces = [];
    const angulos = [ Math.PI / 4,(5 * Math.PI) / 4];

    const longitud = 0.35;

    for (const angulo of angulos) {

        const x = RADIO_ESPIRA * Math.cos(angulo);
        const y = RADIO_ESPIRA * Math.sin(angulo);

        const tx = -Math.sin(angulo);
        const ty =  Math.cos(angulo);

        const x1 = x - (longitud / 2) * tx;
        const y1 = y - (longitud / 2) * ty;

        const x2 = x + (longitud / 2) * tx;
        const y2 = y + (longitud / 2) * ty;

        traces.push({
            type: "scatter",
            mode: "lines",
            x: [x1, x2],
            y: [y1, y2],
            line: {
                color: COLORES.corriente,
                width: 4
            },
            hoverinfo: "skip",
            showlegend: false
        });

        const xm = x2 - AJUSTE_PUNTA_FLECHA_2D * tx;
        const ym = y2 - AJUSTE_PUNTA_FLECHA_2D * ty;

        traces.push({
            type: "scatter",
            mode: "markers",
            x: [xm],
            y: [ym],

            marker: {
                symbol: "arrow",
                size: 14,
                color: COLORES.corriente,
                angle: (Math.atan2(ty, tx) * 180 / Math.PI + 180)

            },
            hoverinfo: "skip",
            showlegend: false
        });
    }
    return traces;
}

// Etiqueta de Corriente
function crearTraceEtiquetaCorriente2D() {
    return {
        type: "scatter",
        mode: "text",
        x: [2],
        y: [1.75],
        text: ["I = 10 A"],
        textfont: {
            size: 18,
            color: COLORES.corriente
        },
        hoverinfo: "skip",
        showlegend: false
    };
}

// Campo
function crearTracesCampo2D() {
    const traces = [];

    const x1 = 0;
    const y1 = 0;

    const x2 = 0;
    const y2 = LONGITUD_CAMPO_2D;

    traces.push({
        type: "scatter",
        mode: "lines",
        x: [x1, x2],
        y: [y1, y2],

        line: {
            color: COLORES.campo,
            width: 4
        },
        hoverinfo: "skip",
        showlegend: false
    });

    const xm = x2;
    const ym = y2 - AJUSTE_PUNTA_CAMPO_2D;

    traces.push({
        type: "scatter",
        mode: "markers",
        x: [xm],
        y: [ym],

        marker: {
            symbol: "arrow",
            size: 16,
            color: COLORES.campo,
            angle: 0
        },

        hoverinfo: "skip",
        showlegend: false
    });

    return traces;
}

// Etiqueta B
function crearTraceEtiquetaCampo2D() {

    return {
        type: "scatter",
        mode: "text",
        x: [0],
        y: [LONGITUD_CAMPO_2D + 0.25],
        text: ["B"],

        textfont: {size: 18,color: COLORES.campo},
        hoverinfo: "skip",
        showlegend: false
    };

}

function crearTraceCampoTemporal() {
    return {
        type: "scatter",
        mode: "text",
        x: [0],
        y: [0],
        text: ["⊙"],
        textfont: {
            size: 34,
            color: COLORES.campo,
            family: "Arial Black"
        },

        hoverinfo: "skip",
        showlegend: false
    };
}

// Layout
function crearLayout2D() {
    return {
        margin: {l: 10,r: 10,t: 10,b: 10},
        xaxis: {visible: false,scaleanchor: "y",range: [-2.6, 2.6]},
        yaxis: {visible: false,range: [-2.6, 2.6]},
        plot_bgcolor: "white",
        paper_bgcolor: "white"
    };

}

// Crear Grafico
function crearGraficoEjercicio2D() {
    Plotly.newPlot(
        "grafico-ejercicio-bobina",
        [
            crearTraceEspira2D(),
            // crearTraceCentro2D(),
            crearTraceRadio2D(),
            crearTraceEtiquetaRadio2D(),
            ...crearTracesCorriente2D(),
            crearTraceCampoTemporal(),
            crearTraceEtiquetaCorriente2D()
            // ...crearTracesCampo2D(),
            // crearTraceEtiquetaCampo2D()
        ],
        crearLayout2D(),
        { responsive: true,displayModeBar: false,staticPlot: true}
    );
}


/******************************************************************************
 * LABORATORIO VIRTUAL
 ******************************************************************************/


function crearGraficoLaboratorio() {

    Plotly.newPlot(
        "grafico-laboratorio-bobina",

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

        {
            responsive: true
        }

    );

}

function leerParametrosLaboratorio() {
    // Leer el estado actual del experimento.
    return {
        numeroEspiras: Number(sliderN.value),
        corriente: Number(sliderI.value),
        radio: Number(sliderR.value),
        sentidoCorriente: radioAntihorario.checked ? 1 : -1
    };

}


function calcularCampoMagnetico(parametrosLaboratorio) {
    return (
        MU_0 * parametrosLaboratorio.numeroEspiras * parametrosLaboratorio.corriente
    ) / ( 2 * parametrosLaboratorio.radio);
}


function actualizarValoresParametros() {
// Actualizar los textos debajo de los controles.
    
    // actualizo los texto
    valorN.textContent = `${sliderN.value} espiras`;
    valorI.textContent = `${sliderI.value} A`;
    valorR.textContent = `${Number(sliderR.value).toFixed(2)} m`;
}


function actualizarResultados(campoMagnetico,sentidoCorriente) {
    const resultadoB = document.getElementById("resultado-b");
    const resultadoMicroTesla = document.getElementById("resultado-b-ut");
    const direccionCampo = document.getElementById("direccion-campo");

    resultadoB.innerHTML = `${formatearCampoMagnetico(campoMagnetico)} T`;
    resultadoMicroTesla.textContent = `${(campoMagnetico * 1e6).toFixed(0)} μT`;

    if (sentidoCorriente ===  1) {
        direccionCampo.textContent = "⬆ Saliente (+Z)";
    } else {
        direccionCampo.textContent = "⬇ Entrante (−Z)";
    }
}

function actualizarLaboratorio() {

    actualizarValoresParametros();
    const parametrosLaboratorio  = leerParametrosLaboratorio();
    const campoMagnetico = calcularCampoMagnetico(parametrosLaboratorio);

    actualizarResultados(campoMagnetico,parametrosLaboratorio.sentidoCorriente);
}

function restablecerValores() {
    sliderN.value = 48;
    sliderI.value = 10;
    sliderR.value = 0.10;

    document.getElementById("corriente-antihoraria").checked = true;
    actualizarLaboratorio();
}

function inicializarLaboratorio() {

    sliderN = document.getElementById("slider-n");
    sliderI = document.getElementById("slider-i");
    sliderR = document.getElementById("slider-r");

    radioAntihorario = document.getElementById("corriente-antihoraria");
    radioHorario = document.getElementById("corriente-horaria");

    btnRestablecer = document.getElementById("btn-restablecer");

    valorN = document.getElementById("valor-n");
    valorI = document.getElementById("valor-i");
    valorR = document.getElementById("valor-r");

    sliderN.addEventListener("input",actualizarLaboratorio);
    sliderI.addEventListener("input",actualizarLaboratorio);
    sliderR.addEventListener("input",actualizarLaboratorio);

    radioAntihorario.addEventListener("change", actualizarLaboratorio);
    radioHorario.addEventListener("change", actualizarLaboratorio);

    btnRestablecer.addEventListener("click",restablecerValores);
    actualizarLaboratorio();
}


/* ============================================================================
 * Inicialización
 * ========================================================================== */

document.addEventListener("DOMContentLoaded", () => {

    crearGraficoBobina();

    crearGraficoEjercicio2D();

    crearGraficoLaboratorio();
    inicializarLaboratorio();
});