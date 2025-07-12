# Configuration pour Pylance/Pyright
# Ce fichier aide l'analyseur de code à comprendre les imports

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Ces imports ne sont utilisés que pour l'analyse statique
    from cs_manim import (
        CLIENT_COLOR,
        FONT_NAME,
        REQUEST_COLOR,
        RESPONSE_COLOR,
        SERVER_COLOR,
        MobilePhone,
        Server,
    )

    __all__ = [
        "CLIENT_COLOR",
        "FONT_NAME",
        "REQUEST_COLOR",
        "RESPONSE_COLOR",
        "SERVER_COLOR",
        "MobilePhone",
        "Server",
    ]
