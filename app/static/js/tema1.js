const MU0 = 4 * Math.PI * 1e-7;

const sliderCorriente =
    document.getElementById(
        "slider-corriente"
    );

const sliderDistancia =
    document.getElementById(
        "slider-distancia"
    );

const valorCorriente =
    document.getElementById(
        "valor-corriente"
    );

const valorDistancia =
    document.getElementById(
        "valor-distancia"
    );

const resultadoCampo =
    document.getElementById(
        "resultado-campo"
    );


function actualizarExploracion() {

    const I =
        parseFloat(
            sliderCorriente.value
        );

    const r =
        parseFloat(
            sliderDistancia.value
        );

    valorCorriente.textContent =
        `${I.toFixed(1)} A`;

    valorDistancia.textContent =
        `${r.toFixed(2)} m`;

    const B =
        (MU0 * I) /
        (2 * Math.PI * r);

    const microTesla =
        B * 1e6;

    resultadoCampo.textContent =
        `${microTesla.toFixed(2)} μT`;

    generarGraficoExploracion(I,r);
}

// ==========================================
// Gráfico 1
// Campo Magnético vs Distancia
// ==========================================
function generarGraficoExploracion(corriente,distanciaActual) {

    const distancias = [];
    const campos = [];

    for (let r = 0.01;r <= 2;r += 0.01) 
        {
            const B = (MU0 * corriente)/(2 * Math.PI * r);
            distancias.push(Number(r.toFixed(2)));
            campos.push(B * 1e6);
    }

    const campoActual = ( (MU0 * corriente)/(2 * Math.PI * distanciaActual) ) * 1e6;

    const curva = {x: distancias,y: campos,mode: "lines",name: "B vs r"};

    const puntoActual = { 
        x: [distanciaActual],
        y: [campoActual],
        mode: "markers",
        name: "B",  
        text: [ `r = ${distanciaActual.toFixed(2)} m B = ${campoActual.toFixed(2)} μT`],
        hoverinfo: "text",
        marker: {size: 12} };
    
    const conductor = {
        textposition: "top center",
        x: [0, 0],
        y: [0, Math.max(...campos) * 1.3],
        mode: "lines+text",
        name: "Conductor rectilíneo ∞",
        line: { 
            dash: "dash",
            width: 4
        }        
    };

    const data = [ curva, puntoActual,conductor];

    const layout = {
        title: {text:"Campo Magnético vs Distancia"},
        xaxis: { title: { text: "Distancia (m)"}}, 
        yaxis: { title: { text:"Campo Magnético (μT)"}}, 
        legend: {
            orientation: "h",
            yanchor:"top",
            y:-0.25,
            xanchor:"center",
            x:0.5
        }
    };
    
    Plotly.newPlot( "grafico-exploracion", data, layout, {responsive: true});
}

sliderCorriente.addEventListener(
    "input",
    actualizarExploracion
);

sliderDistancia.addEventListener(
    "input",
    actualizarExploracion
);


// ==========================================
// Gráfico 2
// Geometría del Campo Magnético
// ==========================================

function generarGraficoGeometrico() {

   const layout = {
        scene: {
            aspectmode: "cube",
            xaxis: { title: "X",range: [-3,3], nticks:7},
            yaxis: { title: "Y", range: [-3,3], nticks:7},
            zaxis: { title: "Z", range: [-3,3], nticks:7},
            
            camera: {
                eye: { x: 1.35, y: 1.35, z: 1.10 },
                center: { x: 0, y: 0, z: 0},
                up: { x: 0, y: 0, z: 1}
            }
        }
    };

    const conductor = {
        type: "scatter3d",
        mode: "lines",
        name: "Conductor",

        x: [0, 0],
        y: [0, 0],
        z: [-3, 3],

        line: { color: "red", width: 8 }
    };

    const punto = {
        type: "scatter3d",
        mode: "markers+text",
        name: "P",

        x: [2],
        y: [1],
        z: [1],

        marker: { color: "blue", size: 6 },
        text: ["P"],
        textposition: "top center"
    };

    const distancia = {
        type: "scatter3d",
        mode: "lines+text",
        name: "r",

        x: [0, 2],
        y: [0, 1],
        z: [1, 1],

        line: {
            color: "#6c757d",
            width: 4,
            dash: "dash"
        },

        text: ["", "r"],
        textposition: "middle center"
    };

    const corriente = {
        type: "scatter3d",
        mode: "lines+text",
        name: "Corriente",

        x: [0, 0],
        y: [0, 0],
        z: [2.0, 2.8],

        line: {
            color: "orange",
            width: 6
        },

        text: ["", "I"],
        textposition: "top center"
    };

    const flechaCorriente = {
        type: "cone",

        x: [0],
        y: [0],
        z: [2.8],

        u: [0],
        v: [0],
        w: [1],

        sizemode: "absolute",
        sizeref: 0.35,

        colorscale: [
            [0, "orange"],
            [1, "orange"]
        ],

        showscale: false,
        name: "I"
    };

    const plano = {
        type: "mesh3d",

        x: [-3, -3, 3, 3],
        y: [-1.5, -1.5, 1.5, 1.5],
        z: [-3, 3, 3, -3],

        i: [0, 0],
        j: [1, 2],
        k: [2, 3],

        opacity: 0.08,
        color: "#4A90E2",

        hoverinfo: "skip",
        showscale: false,
        name: 'Plano',
        showlegend: true
    };

    const r = {x: 2,y: 1,z: 0};
    const I = {x: 0,y: 0,z: 1};
    const B = {
        x: I.y * r.z - I.z * r.y,
        y: I.z * r.x - I.x * r.z,
        z: I.x * r.y - I.y * r.x
    };

    const modulo = Math.sqrt(B.x**2 + B.y**2 + B.z**2);

    B.x /= modulo;
    B.y /= modulo;
    B.z /= modulo;

    const longitud = 1.6;

    const lineaB = {
        type: "scatter3d",
        mode: "lines",
        name: "Campo B",

        x: [2, 2 + B.x * longitud],
        y: [1, 1 + B.y * longitud],
        z: [1, 1 + B.z * longitud],

        line: {
            color: "green",
            width: 8
        }
    };

    const vectorB = {
        type: "cone",

        x: [2 + B.x * longitud],
        y: [1 + B.y * longitud],
        z: [1 + B.z * longitud],

        u: [B.x],
        v: [B.y],
        w: [B.z],

        sizemode: "absolute",
        sizeref: 0.28,

        anchor: "tip",

        colorscale: [
            [0, "green"],
            [1, "green"]
        ],

        showscale: false,
        name: "Campo B"
    };

    const data = [
        plano,
        conductor,
        corriente,
        flechaCorriente,
        distancia,
        punto,
        lineaB,
        vectorB
    ];

    Plotly.newPlot(
        "grafico-geometria",
        data,
        layout,
        {
            displaylogo: false,
            responsive: true
        }
    );

}


actualizarExploracion();

generarGraficoGeometrico();