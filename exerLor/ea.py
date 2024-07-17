class TransitionPhase:
    def __init__(self, current_state, target_state, transition_reason, transition_operation):
        self.current_state = current_state
        self.target_state = target_state
        self.transition_reason = transition_reason
        self.transition_operation = transition_operation
