# 说明

## 概述

该项目是一个使用 Telethon 库构建的 Telegram 机器人。该机器人提供各种功能，如 AI 响应、消息处理和管理工具。配置使用 YAML 文件进行管理。

## 功能

- **AI 响应**：机器人可以调用 AI 模型生成用户消息的响应。
- **消息处理**：机器人可以处理新消息、编辑消息和转发消息。
- **管理工具**：机器人提供管理聊天参与者的工具，如踢出参与者、置顶/取消置顶消息和编辑管理员权限。
- **历史导入**：机器人可以从文件中导入消息历史。
- **内联查询**：机器人支持内联查询以提供 AI 生成的响应。

## 配置

配置使用 YAML 文件 (`config.yaml`) 进行管理。配置文件遵循 YAML 1.2 规范。

### 配置结构

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

### 配置字段

- **tor**：Tor 代理的配置。
  - `proxy` (字符串)：Tor 代理 URL。

- **auth**：认证配置列表。
  - `base_url` (字符串)：OpenAI API 的基础 URL。
  - `api_key` (字符串)：认证的 API 密钥。

- **completions**：生成补全的 AI 模型配置列表。
  - `model` (字符串)：AI 模型的名称。
  - `auth` (列表)：认证配置的引用。
  - `tool` (布尔值)：指示模型是否使用工具。

- **images**：生成图像的 AI 模型配置列表。
  - `model` (字符串)：AI 模型的名称。
  - `auth` (列表)：认证配置的引用。

## 设置

1. **安装依赖** 使用以下命令安装它们：
   ```sh
   pip install -r .
   ```

2. **环境变量**：在项目根目录创建 `.env` 文件，并添加以下环境变量：
   ```env
   BOT_TOKEN=<你的 telegram 机器人令牌>
   SECRET=<要让机器人保密的内容>
   ```

3. **运行机器人**：使用以下命令运行机器人：
   ```sh
   python -m tgbot
   ```

## 待办事项

- 实现 `UploadProfilePhotoRequest` 工具。
- 实现 `SearXNG` 工具。
- 根据需要添加更多 AI 模型和工具。
- 改进错误处理和日志记录。
