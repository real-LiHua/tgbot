# Telegram Bot Project

This project is a Telegram bot built using Python. The bot is designed to handle various commands and events, interact with users, and perform tasks using AI models and tools.

## Configuration

The configuration for this bot is done using a YAML file. Below is an example configuration file (`config.yaml`) and a detailed explanation of each section and its parameters.

### Example Configuration (`config.yaml`)

```yaml
tor:
  proxy: socks5://127.0.0.1:9050

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
```

### Configuration Sections

#### `tor`

- **proxy**: The proxy URL for TOR. This is used to route requests through the TOR network.

#### `auth`

A list of authentication configurations for different AI services. Each entry contains:

- **base_url**: The base URL of the AI service.
- **api_key**: The API key for accessing the AI service.

#### `completions`

A list of AI models used for generating text completions. Each entry contains:

- **model**: The name of the AI model.
- **auth**: A reference to the authentication configurations defined in the `auth` section.
- **tool**: A boolean indicating whether the model uses tools.

#### `images`

A list of AI models used for generating images. Each entry contains:

- **model**: The name of the AI model.
- **auth**: A reference to the authentication configurations defined in the `auth` section.

## Dependencies

The project dependencies are specified in the `pyproject.toml` file. Here is a list of the main dependencies:

- `aiohttp`: Asynchronous HTTP client.
- `hachoir`: Library for parsing binary files.
- `openai`: OpenAI API client.
- `pillow`: Python Imaging Library.
- `portalocker`: File locking library.
- `python-dotenv`: Library for loading environment variables from a `.env` file.
- `regex`: Regular expression library.
- `ruamel-yaml`: YAML parser and emitter for Python.
- `singleton-decorator`: Singleton pattern decorator.
- `telethon`: Telegram client library.

## Running the Bot

To run the bot, follow these steps:

1. Install the dependencies:
   ```sh
   pip install -r .
   ```

2. Create a `.env` file with the following environment variables:
   ```env
   BOT_TOKEN=your-telegram-bot-token
   SECRET=your-secret
   ```

3. Create a `config.yaml` file based on the example provided above.

4. Run the bot:
   ```sh
   python -m tgbot
   ```

The bot will start and connect to Telegram using the provided bot token. It will handle commands and events as defined in the source code.
