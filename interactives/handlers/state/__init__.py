from interactives.handlers.state.ending import router as ending_state
from interactives.handlers.state.ask_question import router as ask_question_state


state_routers = [
    ending_state,
    ask_speaker_state
]