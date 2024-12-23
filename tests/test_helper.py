import unittest
import pandas as pd
from src.utils.helpers import preprocess_data

class TestHelpers(unittest.TestCase):
    def setUp(self):
        # Setup code to create sample data
        self.raw_data = pd.DataFrame({
            'column1': [1, None, 3],
            'column2': ['a', 'b', None]
        })
        self.expected_data = pd.DataFrame({
            'column1': [1, 3],
            'column2': ['a', 'b']
        })

    def test_preprocess_data(self):
        # Test the preprocess_data function
        processed_data = preprocess_data(self.raw_data)
        pd.testing.assert_frame_equal(processed_data, self.expected_data)

if __name__ == '__main__':
    unittest.main()
