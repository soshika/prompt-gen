# OpenAI API Prompt Generator

This is a Flask application that generates prompts using the OpenAI API. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- Flask
- An OpenAI API key

### Installing

1. Clone the repository:
    ```
    git clone https://github.com/<your-github-username>/openai-prompt-generator.git
    ```
2. Navigate to the project directory:
    ```
    cd openai-prompt-generator
    ```
3. Create a virtual environment:
    ```
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```
        .\venv\Scripts\activate
        ```
    - On Unix or MacOS:
        ```
        source venv/bin/activate
        ```
5. Install the required packages:
    ```
    pip install -r requirements.txt
    ```
6. Create a `.env` file in the root directory and add your OpenAI API key:
    ```
    OPENAI_API_KEY='your-api-key-here'
    ```
7. Run the Flask application:
    ```
    flask run
    ```

The application should now be running at http://127.0.0.1:5000.

## Usage

Visit the application URL in your web browser to use the prompt generator.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
