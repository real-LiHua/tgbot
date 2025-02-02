## Telegram Bot

This repository contains a Telegram bot built using the Telethon library. The bot is designed to handle various commands and events, including AI responses, message logging, and more.

### Prerequisites

- Python 3.10+
- A Telegram bot token (obtainable from [BotFather](https://t.me/botfather))
- `pip` for installing Python packages

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/real-LiHua/tgbot
    cd tgbot
    ```

2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```sh
    pip install -r .
    ```

4. Create a `.env` file in the root directory and add your bot token and other environment variables:

    ```env
    BOT_TOKEN=your_bot_token
    SECRET=your_secret
    ```

5. Create a `config.yaml` file in the root directory with the necessary configuration for AI models:

    ```yaml
    chat_completion:
      - type: ollama
        host: your_host
        model: your_model
      - base_url: https://api.openai.com/v1
        api_key: your_openai_api_key
        model: your_openai_model
    ```

### Usage

1. Run the bot:

    ```sh
    python -m tgbot
    ```

2. The bot will start and connect to Telegram. You can interact with it using the following commands:

    - `/ai`: Invoke the AI model to respond to messages.
    - `/ping`: Check the bot's response time.
    - `/reset`: Clear the chat data.
    - `/import_history`: Import message history from a file.

### Project Structure

- `src/tgbot/core/ai.py`: Handles AI model invocations and responses.
- `src/tgbot/core/data.py`: Manages chat data and system messages.
- `src/tgbot/core/history.py`: Logs message history and handles raw events.
- `src/tgbot/core/inline.py`: Handles inline queries and callback queries.
- `src/tgbot/core/ping.py`: Implements the `/ping` command.
- `src/tgbot/core/reset.py`: Implements the `/reset` command.
- `src/tgbot/core/tools/`: Contains various tools and request models.
- `src/tgbot/__main__.py`: Main entry point for running the bot.
- `src/tgbot/plugins/`: Directory for additional plugins.

### Configuration

- **Environment Variables**:
  - `BOT_TOKEN`: Your Telegram bot token.
  - `SECRET`: A secret value used in system messages.

- **config.yaml**:
  - `chat_completion`: Configuration for AI models, including type, host, base URL, API key, and model name.

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

### Contact

For any questions or issues, please open an issue on GitHub or contact the repository owner.
