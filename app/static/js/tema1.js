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
        title: "Representación tridimensional",
        scene: {
            aspectmode: "cube",
            xaxis: { title: "X",range: [-3,3]},
            yaxis: { title: "Y", range: [-3,3]},
            zaxis: { title: "Z", range: [-3,3] },
            camera: {
                eye: { x: 1.7,y: 1.5,z: 1.3}
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
        y: [0],
        z: [2],

        marker: { color: "blue", size: 6 },
        text: ["P"],
        textposition: "top center"
    };

    const data = [ conductor, punto];

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