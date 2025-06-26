from interactives.handlers.callback.gavrikov import router as gavrikov_router
from interactives.handlers.callback.belozyortseva import router as belozyortseva_router
from interactives.handlers.callback.mendubaev import router as mendubaev_router
from interactives.handlers.callback.speaker_sadriev import router as sadriev_router
from interactives.handlers.callback.speaker_gilmanova import router as gilmanova_router
from interactives.handlers.callback.speaker_horoshutina import router as horoshine_router

from interactives.handlers.callback.ending import router as ending


callback_routers = [
    gavrikov_router,
    belozyortseva_router,
    mendubaev_router,
    sadriev_router,
    gilmanova_router,
    horoshine_router,
    ending
]
