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
}


sliderCorriente.addEventListener(
    "input",
    actualizarExploracion
);

sliderDistancia.addEventListener(
    "input",
    actualizarExploracion
);


actualizarExploracion();