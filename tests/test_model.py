import unittest
import torch
from src.models.model import FraudDetectionModel
from src.models.train import train_model

class TestModel(unittest.TestCase):
    def setUp(self):
        # Initialize model parameters
        self.input_size = 128
        self.hidden_size = 64
        self.output_size = 1
        self.model = FraudDetectionModel(self.input_size, self.hidden_size, self.output_size)

    def test_model_architecture(self):
        # Test if the model architecture is correctly initialized
        self.assertEqual(self.model.fc1.in_features, self.input_size)
        self.assertEqual(self.model.fc2.out_features, self.output_size)

    def test_train_model(self):
        # Test the training routine with mock data
        mock_data = torch.randn(10, self.input_size)
        mock_labels = torch.randint(0, 2, (10, 1)).float()
        config = {
            'input_size': self.input_size,
            'hidden_size': self.hidden_size,
            'output_size': self.output_size,
            'learning_rate': 0.001,
            'epochs': 1
        }
        trained_model = train_model((mock_data, mock_labels), config)
        self.assertIsInstance(trained_model, FraudDetectionModel)

if __name__ == '__main__':
    unittest.main()
