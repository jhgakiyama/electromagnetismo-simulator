from flask import Flask
import sympy as sp
import plotly.graph_objects as go


def create_app():

    app = Flask(__name__)

    @app.route("/")
    def home():

        I = 10
        r = 0.05

        mu0 = 4 * sp.pi * 10**-7

        B = (mu0 * I) / (2 * sp.pi * r)

        valor = float(B)

        fig = go.Figure()

        fig.add_scatter(
            x=[0, 1],
            y=[0, valor]
        )

        return f"""
        <h1>Primera prueba del proyecto</h1>

        <p>Campo Magnético:</p>

        <p>{valor:.8f} T</p>

        {fig.to_html(full_html=False)}
        """

    return app