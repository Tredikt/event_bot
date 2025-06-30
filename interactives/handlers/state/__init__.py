from interactives.handlers.state.ending import router as ending_state
from interactives.handlers.state.gilmanova import router as gilmanova_state
from interactives.handlers.state.ask_question import router as ask_question_state


state_routers = [
    ending_state,
    gilmanova_state,
    ask_speaker_state
]