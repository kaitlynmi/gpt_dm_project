from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Print environment variables for testing
for key, value in os.environ.items():
    print(f'{key}: {value}')