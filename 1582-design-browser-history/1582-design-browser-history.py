class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.history.append(homepage)
        self.index = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.index+1]
        self.history.append(url)
        self.index+=1

    def back(self, steps: int) -> str:
        if self.index < steps:
            steps = self.index
        self.index-=steps
        return self.history[self.index]

    def forward(self, steps: int) -> str:
        if (len(self.history) - 1 - self.index) < steps:
            steps = len(self.history) - 1 - self.index
        self.index+=steps
        return self.history[self.index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)