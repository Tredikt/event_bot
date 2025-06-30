from interactives.handlers.callback.gavrikov import router as gavrikov_callback_router
from interactives.handlers.callback.belozyortseva import router as belozyortseva_callback_router
from interactives.handlers.callback.speaker_sadriev import router as sadriev_router
from interactives.handlers.callback.speaker_horoshutina import router as horoshine_router
from interactives.handlers.callback.zabegayev import router as zabegayev_callback_router
from interactives.handlers.callback.nurkhametova import router as nurkhametova_callback_router

from interactives.handlers.callback.ending import router as ending



callback_routers = [
    gavrikov_callback_router,
    belozyortseva_callback_router,
    sadriev_router,
    horoshine_router,
    ending,
    zabegayev_callback_router,
    nurkhametova_callback_router
]
