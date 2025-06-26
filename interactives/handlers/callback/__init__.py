from interactives.handlers.callback.gavrikov import router as gavrikov_callback_router
from interactives.handlers.callback.belozyortseva import router as belozyortseva_callback_router
from interactives.handlers.callback.mendubaev import router as mendubaev_callback_router
from interactives.handlers.callback.speaker_sadriev import router as sadriev_router
from interactives.handlers.callback.speaker_gilmanova import router as gilmanova_router
from interactives.handlers.callback.speaker_horoshutina import router as horoshine_router
from interactives.handlers.callback.zabegayev import router as zabegayev_callback_router
from interactives.handlers.callback.zargaryan import router as zargaryan_callback_router

from interactives.handlers.callback.ending import router as ending
from interactives.handlers.state.zargaryan import router as zargaryan_state_router


callback_routers = [
    gavrikov_callback_router,
    belozyortseva_callback_router,
    mendubaev_callback_router,
    sadriev_router,
    gilmanova_router,
    horoshine_router,
    ending,
    zabegayev_callback_router,
    zargaryan_callback_router,
    zargaryan_state_router
]
