
class ChatHistory:

    def __init__(self):
        self._history = []

    def add(self, question, answer):
        self._history.append((question, answer))

    def clear(self):
        self._history = []

    def get_history(self, n=5):
        return self._history[:n]
