from abc import abstractmethod


class Pipeline:
    @abstractmethod
    def data_prep(self, x, y):
        raise NotImplementedError

    @abstractmethod
    def train(self, x, y):
        raise NotImplementedError

    @abstractmethod
    def predict(self, x):
        raise NotImplementedError

    @abstractmethod
    def deploy(self):
        print("deployando modelo de forma default")

    @abstractmethod
    def should_deploy(self):
        return False

    def run(self, x, y):
        self.data_prep(x, y)
        self.train(x, y)
        self.predict(x)
        if self.should_deploy():
            self.deploy()


class PipelineSklearn(Pipeline):
    def __init__(self, random_state=42):
        self.random_state = random_state

    def data_prep(self, x, y):
        print("Data Prep Scikit")

    def train(self, x, y):
        print("Treinando modelo com scikit")

    def predict(self, x):
        print("Fazendo predição com scikit")

    def should_deploy(self):
        return True


class PipelineTensorflow(Pipeline):
    def data_prep(self, x, y):
        print("Data Prep tensorflow")

    def train(self, x, y):
        print("Treinando modelo com tensorflow")

    def predict(self, x):
        print("Fazendo predição com tensorflow")

    def deploy(self):
        print("deployando modelo com tensorflow")

    def should_deploy(self):
        return True


pipesk = PipelineSklearn(random_state=123)
pipesk.run(1, 2)
pipetf = PipelineTensorflow()
pipetf.run(1, 2)
