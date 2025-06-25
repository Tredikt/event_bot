from interactives.handlers.callback import tests_callback_router
from interactives.handlers.callback.speaker_horoshutina import router as horoshutina_router
from interactives.handlers.callback.speaker_gilmanova import router as gilmanova_router
from interactives.handlers.callback.speaker_sadriev import router as sadriev_router


interactive_routers = [
    tests_callback_router,
    horoshutina_router,
    gilmanova_router,
    sadriev_router,
]