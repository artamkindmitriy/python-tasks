class LogIterator:
    def __init__(self, logs: list[str]):
        self.logs = logs
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.logs):
            log = self.logs[self.index]
            self.index += 1

            if "ERROR" in log:
                return log

        raise StopIteration