import unittest
import pandas as pd
from src.data.data_loader import load_data

class TestDataLoader(unittest.TestCase):
    def setUp(self):
        # Setup code to create a sample CSV file or mock data
        self.sample_data = pd.DataFrame({
            'column1': [1, 2, 3],
            'column2': ['a', 'b', 'c']
        })
        self.sample_data.to_csv('sample_data.csv', index=False)

    def tearDown(self):
        # Cleanup code to remove the sample CSV file
        import os
        os.remove('sample_data.csv')

    def test_load_data(self):
        # Test loading data from a CSV file
        data = load_data('sample_data.csv')
        pd.testing.assert_frame_equal(data, self.sample_data)

if __name__ == '__main__':
    unittest.main()
