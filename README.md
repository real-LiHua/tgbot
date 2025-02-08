## Overview

This project is a Telegram bot built using the Telethon library. The bot provides various functionalities such as AI responses, message handling, and administrative tools. The configuration is managed using a YAML file.

## Features

- **AI Responses**: The bot can invoke AI models to generate responses to user messages.
- **Message Handling**: The bot can handle new messages, edit messages, and forward messages.
- **Administrative Tools**: The bot provides tools for managing chat participants, such as kicking participants, pinning/unpinning messages, and editing admin permissions.
- **History Import**: The bot can import message history from a file.
- **Inline Queries**: The bot supports inline queries to provide AI-generated responses.

## Configuration

The configuration is managed using a YAML file (`config.yaml`). The configuration file follows the YAML 1.2 specification.

### Configuration Structure

```yaml
telegram:
  app_id: 611335
  app_hash: "d524b414d21f4d37f08684c1df41ac9c"
  bot_token: "********:********************************"

auth: &auth
  - base_url: "https://api.siliconflow.cn/v1"
    api_key: "sk-**************************************"
  - base_url: "https://huggingface.co/api/inference-proxy/together"
    api_key: "hf_**************************************"
  - base_url: "https://integrate.api.nvidia.com/v1"
    api_key: "nvapi-***********************************"
  - base_url: "https://openrouter.ai/api/v1"
    api_key: "sk-or-v1-********************************"

completions:
  - model: "Qwen/Qwen2.5-Coder-32B-Instruct"
    auth: *auth
    tool: true
  - model: "Qwen/Qwen2.5-72B-Instruct"
    auth: *auth
    tool: true
  - model: "meta-llama/Llama-3.3-70B-Instruct"
    auth: *auth
    tool: true
  - model: "deepseek-r1"
    auth: *auth

images:
  - model: "black-forest-labs/FLUX.1-dev"
    auth: *auth
  - model: "stabilityai/stable-diffusion-3.5-large"
    auth: *auth
  - model: "stabilityai/stable-diffusion-3-medium"
    auth: *auth
  - model: "stabilityai/stable-diffusion-xl-base-1.0"
    auth: *auth

tor:
  proxy: socks5://127.0.0.1:9050
```

### Configuration Fields

- **telegram**: Telegram bot configuration.
  - `app_id` (int): The app ID for the Telegram API.
  - `app_hash` (string): The app hash for the Telegram API.
  - `bot_token` (string): The bot token for the Telegram bot.

- **auth**: A list of authentication configurations.
  - `base_url` (string): The base URL for the API.
  - `api_key` (string): The API key for authentication.

- **completions**: A list of AI model configurations for generating completions.
  - `model` (string): The name of the AI model.
  - `auth` (list): A reference to the authentication configurations.
  - `tool` (boolean): Indicates whether the model uses tools.

- **images**: A list of AI model configurations for generating images.
  - `model` (string): The name of the AI model.
  - `auth` (list): A reference to the authentication configurations.

- **tor**: Configuration for the Tor proxy.
  - `proxy` (string): The Tor proxy URL.

## Setup

1. **Install Dependencies**: Use the following command to install them:
   ```sh
   pip install git+https://github.com/real-LiHua/tgbot
   ```

2. **Run the Bot**: Use the following command to run the bot:
   ```sh
   python -m tgbot
   ```

## TODO

- Implement the `UploadProfilePhotoRequest` tool.
- Implement the `SearXNG` tool.
- Add more AI models and tools as needed.
- Improve error handling and logging.
