from interactives.handlers.state.ending import router as ending_state
from interactives.handlers.state.gilmanova import router as gilmanova_state
from interactives.handlers.state.ask_speaker import router as ask_speaker_state


state_routers = [
    gilmanova_state,
    ending_state,
    ask_speaker_state
]