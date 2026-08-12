document.addEventListener("DOMContentLoaded", function () {

    const collapse = document.getElementById("solucionP2");

    if (collapse) {
        collapse.addEventListener("shown.bs.collapse", function () {

            const graficos = collapse.querySelectorAll(".js-plotly-plot");

            graficos.forEach(function (grafico) {
                Plotly.Plots.resize(grafico);
            });

        });
    }

});