# Telegram 机器人项目

该项目是一个使用 Python 构建的 Telegram 机器人。该机器人旨在处理各种命令和事件，与用户交互，并使用 AI 模型和工具执行任务。

## 配置

该机器人的配置使用 YAML 文件完成。以下是一个示例配置文件 (`config.yaml`) 以及每个部分及其参数的详细说明。

### 示例配置 (`config.yaml`)

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

### 配置部分

#### `tor`

- **proxy**: TOR 的代理 URL。用于通过 TOR 网络路由请求。

#### `auth`

不同 AI 服务的身份验证配置列表。每个条目包含：

- **base_url**: AI 服务的基本 URL。
- **api_key**: 访问 AI 服务的 API 密钥。

#### `completions`

用于生成文本补全的 AI 模型列表。每个条目包含：

- **model**: AI 模型的名称。
- **auth**: 引用 `auth` 部分中定义的身份验证配置。
- **tool**: 一个布尔值，指示模型是否使用工具。

#### `images`

用于生成图像的 AI 模型列表。每个条目包含：

- **model**: AI 模型的名称。
- **auth**: 引用 `auth` 部分中定义的身份验证配置。

## 依赖项

项目依赖项在 `pyproject.toml` 文件中指定。以下是主要依赖项列表：

- `aiohttp`: 异步 HTTP 客户端。
- `hachoir`: 用于解析二进制文件的库。
- `openai`: OpenAI API 客户端。
- `pillow`: Python 图像库。
- `portalocker`: 文件锁定库。
- `python-dotenv`: 从 `.env` 文件加载环境变量的库。
- `regex`: 正则表达式库。
- `ruamel-yaml`: Python 的 YAML 解析器和发射器。
- `singleton-decorator`: 单例模式装饰器。
- `telethon`: Telegram 客户端库。

## 运行机器人

要运行机器人，请按照以下步骤操作：

1. 安装依赖项：
   ```sh
   pip install -r .
   ```

2. 创建一个 `.env` 文件，包含以下环境变量：
   ```env
   BOT_TOKEN=your-telegram-bot-token
   SECRET=your-secret
   ```

3. 根据上面提供的示例创建一个 `config.yaml` 文件。

4. 运行机器人：
   ```sh
   python -m tgbot
   ```

机器人将启动并使用提供的机器人令牌连接到 Telegram。它将处理源代码中定义的命令和事件。
