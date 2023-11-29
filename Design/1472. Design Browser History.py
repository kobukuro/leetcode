class BrowserHistory:

    def __init__(self, homepage: str):
        self.history_stamps = [homepage]
        self.current_step = 0

    def visit(self, url: str) -> None:
        del self.history_stamps[self.current_step + 1:]
        self.history_stamps.append(url)
        self.current_step += 1

    def back(self, steps: int) -> str:
        steps = min(steps, self.current_step)
        self.current_step -= steps
        return self.history_stamps[self.current_step]

    def forward(self, steps: int) -> str:
        steps = min(len(self.history_stamps) - 1 - self.current_step, steps)
        self.current_step += steps
        return self.history_stamps[self.current_step]
