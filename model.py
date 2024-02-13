import numpy as np
import pickle

class Model:
    def __init__(self):
        self.weights = np.random.randn(784, 10)  # Exempelstorlekar
        self.biases = np.zeros(10)
        self.loss_history = []
        self.accuracy_history = []

    def train_on_batch(self, X_batch, y_batch):
        # Antag en enkel träningslogik här
        predictions = np.dot(X_batch, self.weights) + self.biases
        loss = np.mean((predictions - y_batch) ** 2)
        accuracy = np.mean(np.argmax(predictions, axis=1) == np.argmax(y_batch, axis=1))
        
        # Uppdatera historik
        self.loss_history.append(loss)
        self.accuracy_history.append(accuracy)
        
        # Simulera viktuppdatering (ersätt med riktig gradientuppdatering)
        self.weights -= np.random.rand(*self.weights.shape) * 0.01
        self.biases -= np.random.rand(*self.biases.shape) * 0.01
        
        return loss, accuracy

    def generate_drawing(self):
        return np.random.randn(28, 28)

    def save_model(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    def load_model(self, filename):
        with open(filename, 'rb') as file:
            model = pickle.load(file)
        self.weights, self.biases = model.weights, model.biases
        self.loss_history, self.accuracy_history = model.loss_history, model.accuracy_history

    def get_training_history(self):
        return self.loss_history, self.accuracy_history




