import logging.config
import yaml
from data.data_loader import load_data
from models.train import train_model
from utils.helpers import preprocess_data

def main():
    # Load configuration
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    # Set up logging
    logging.config.fileConfig(config['logging']['config_file'])
    logger = logging.getLogger('appLogger')

    logger.info('Starting Lumen AI application')

    # Load and preprocess data
    data = load_data(config['data']['source'])
    processed_data = preprocess_data(data)

    # Train model
    model = train_model(processed_data, config['model'])

    logger.info('Lumen AI application finished successfully')

if __name__ == "__main__":
    main()
