from src.analyze.analyzer import Analyzer


class Raw_Analyzer(Analyzer):
    def __init__(self, read_file):
        super().__init__(read_file)
    
    def _analyze_except(self, err):
        return super()._analyze_except(err)

    def analyze(self):
        return self.metadata