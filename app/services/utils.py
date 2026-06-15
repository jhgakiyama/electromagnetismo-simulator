SUPERSCRIPTS = {
    "0": "⁰",
    "1": "¹",
    "2": "²",
    "3": "³",
    "4": "⁴",
    "5": "⁵",
    "6": "⁶",
    "7": "⁷",
    "8": "⁸",
    "9": "⁹",
    "-": "⁻"
}


def exponente_a_superindice(exponente):

    return "".join(
        SUPERSCRIPTS[c]
        for c in str(exponente)
    )


def formatear_cientifico(valor):

    mantisa, exponente = f"{valor:.2e}".split("e")

    exponente = int(exponente)

    return (
        f"{mantisa} × 10"
        f"{exponente_a_superindice(exponente)}"
    )