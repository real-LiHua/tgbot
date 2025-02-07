# tgbot

A Telegram bot project.

## Description

This project is a Telegram bot that utilizes various AI models and tools to interact with users. The bot is built using Python and leverages several libraries and APIs to provide its functionality.

## Configuration

The configuration for the bot is done using a YAML file. Below is an example configuration file (`config.yaml`) and a detailed explanation of each section and its parameters.

### Example Configuration (`config.yaml`)

```yaml
tor:
  ip: 127.0.0.1
  port: 9050

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
  - model: "Qwen/Qwen2.5-72B-Instruct"
    auth: *auth
  - model: "meta-llama/Llama-3.3-70B-Instruct"
    auth: *auth
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

This section configures the Tor proxy settings.

- `ip` (string): The IP address of the Tor proxy. Default is `127.0.0.1`.
- `port` (integer): The port number of the Tor proxy. Default is `9050`.

#### `auth`

This section defines the authentication details for various AI model APIs. It uses YAML anchors (`&auth`) and aliases (`*auth`) to reuse the same authentication details across multiple models.

- `base_url` (string): The base URL of the API.
- `api_key` (string): The API key for authentication.

#### `completions`

This section lists the AI models used for text completions.

- `model` (string): The name of the AI model.
- `auth` (list): A list of authentication details, referenced from the `auth` section.

#### `images`

This section lists the AI models used for image generation.

- `model` (string): The name of the AI model.
- `auth` (list): A list of authentication details, referenced from the `auth` section.

## Dependencies

The project uses the following dependencies, specified in the `pyproject.toml` file:

- `aiohttp>=3.11.11`
- `hachoir>=3.3.0`
- `openai>=1.61.0`
- `pillow>=11.1.0`
- `portalocker>=3.0.0`
- `python-dotenv>=1.0.1`
- `regex>=2024.11.6`
- `ruamel-yaml>=0.18.10`
- `singleton-decorator>=1.0.0`
- `telethon>=1.38.1`

## Usage

To run the bot, follow these steps:

1. Install the dependencies:
   ```sh
   pip install -r .
   ```

2. Create a `.env` file with your environment variables:
   ```env
   BOT_TOKEN=your_bot_token
   SECRET=your_secret
   ```

3. Create a `config.yaml` file with your configuration.

4. Run the bot:
   ```sh
   python -m tgbot
   ```
# TODO

- [ ] Import message history
- [ ] Inline AI assistant
- [ ] Plugin management
- [ ] UserBot
- [ ] Web penetration testing
- [ ] Web search
