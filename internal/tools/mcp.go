package tools

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"sync"

	"github.com/modelcontextprotocol/go-sdk/mcp"
	"github.com/real-LiHua/tgbot/internal/config"
)

type MCPServer struct {
	server  *mcp.Server
	actions *TelegramActions
	apiKey  string
	mu      sync.Mutex
	pending map[string]map[string]any
	httpSrv *http.Server
}

func NewMCPServer(cfg *config.Config) *MCPServer {
	return &MCPServer{
		apiKey:  cfg.BotToolAPIKey,
		pending: make(map[string]map[string]any),
	}
}

func (m *MCPServer) SetActions(a *TelegramActions) {
	m.actions = a
}

func (m *MCPServer) Start(ctx context.Context, addr string) error {
	impl := &mcp.Implementation{Name: "tgbot", Version: "1.0.0"}
	m.server = mcp.NewServer(impl, &mcp.ServerOptions{
		Capabilities: &mcp.ServerCapabilities{
			Tools: &mcp.ToolCapabilities{ListChanged: false},
		},
	})

	m.registerTools()

	mux := http.NewServeMux()
	mux.HandleFunc("/mcp", func(w http.ResponseWriter, r *http.Request) {
		if m.apiKey != "" && r.Header.Get("X-Api-Key") != m.apiKey {
			http.Error(w, "unauthorized", http.StatusForbidden)
			return
		}
		m.handleSSETransport(w, r)
	})
	mux.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		w.Write([]byte(`{"status":"ok"}`))
	})
	mux.HandleFunc("/api/openapi.json", m.handleOpenAPI)

	m.httpSrv = &http.Server{
		Addr:    addr,
		Handler: mux,
	}
	return m.httpSrv.ListenAndServe()
}

func (m *MCPServer) Shutdown(ctx context.Context) error {
	if m.httpSrv != nil {
		return m.httpSrv.Shutdown(ctx)
	}
	return nil
}

func (m *MCPServer) registerTools() {
	type sendMsgInput struct {
		ChatID int64  `json:"chat_id" jsonschema:"Chat ID to send to"`
		Text   string `json:"text" jsonschema:"Message text"`
	}
	type sendMsgOutput struct {
		Result string `json:"result"`
	}
	mcp.AddTool(m.server, &mcp.Tool{
		Name:        "send_message",
		Description: "Send a text message to a chat or group",
	}, func(ctx context.Context, req *mcp.CallToolRequest, input sendMsgInput) (*mcp.CallToolResult, sendMsgOutput, error) {
		r, err := m.actions.SendMessage(input.ChatID, input.Text)
		if err != nil {
			return nil, sendMsgOutput{}, err
		}
		return nil, sendMsgOutput{Result: r}, nil
	})

	type getChatInput struct {
		ChatID int64 `json:"chat_id" jsonschema:"Chat ID"`
	}
	type getChatOutput struct {
		Result string `json:"result"`
	}
	mcp.AddTool(m.server, &mcp.Tool{
		Name:        "get_chat_info",
		Description: "Get detailed information about a chat or group",
	}, func(ctx context.Context, req *mcp.CallToolRequest, input getChatInput) (*mcp.CallToolResult, getChatOutput, error) {
		r, err := m.actions.GetChatInfo(input.ChatID)
		if err != nil {
			return nil, getChatOutput{}, err
		}
		return nil, getChatOutput{Result: r}, nil
	})

	type getMemberCountOutput struct {
		Count int `json:"count"`
	}
	mcp.AddTool(m.server, &mcp.Tool{
		Name:        "get_chat_member_count",
		Description: "Get the number of members in a chat or group",
	}, func(ctx context.Context, req *mcp.CallToolRequest, input getChatInput) (*mcp.CallToolResult, getMemberCountOutput, error) {
		count, err := m.actions.GetChatMemberCount(input.ChatID)
		if err != nil {
			return nil, getMemberCountOutput{}, err
		}
		return nil, getMemberCountOutput{Count: count}, nil
	})

	type banInput struct {
		ChatID int64 `json:"chat_id" jsonschema:"Chat ID"`
		UserID int64 `json:"user_id" jsonschema:"User ID to ban"`
	}
	type actionOutput struct {
		Result string `json:"result"`
	}
	mcp.AddTool(m.server, &mcp.Tool{
		Name:        "ban_chat_member",
		Description: "Ban a user from a chat or group",
	}, func(ctx context.Context, req *mcp.CallToolRequest, input banInput) (*mcp.CallToolResult, actionOutput, error) {
		r, err := m.actions.BanChatMember(input.ChatID, input.UserID)
		if err != nil {
			return nil, actionOutput{}, err
		}
		return nil, actionOutput{Result: r}, nil
	})

	mcp.AddTool(m.server, &mcp.Tool{
		Name:        "unban_chat_member",
		Description: "Unban a user from a chat or group",
	}, func(ctx context.Context, req *mcp.CallToolRequest, input banInput) (*mcp.CallToolResult, actionOutput, error) {
		r, err := m.actions.UnbanChatMember(input.ChatID, input.UserID)
		if err != nil {
			return nil, actionOutput{}, err
		}
		return nil, actionOutput{Result: r}, nil
	})

	type promoteInput struct {
		ChatID int64 `json:"chat_id" jsonschema:"Chat ID"`
		UserID int64 `json:"user_id" jsonschema:"User ID to promote"`
	}
	mcp.AddTool(m.server, &mcp.Tool{
		Name:        "promote_chat_member",
		Description: "Promote a user to admin in a chat",
	}, func(ctx context.Context, req *mcp.CallToolRequest, input promoteInput) (*mcp.CallToolResult, actionOutput, error) {
		r, err := m.actions.PromoteChatMember(input.ChatID, input.UserID)
		if err != nil {
			return nil, actionOutput{}, err
		}
		return nil, actionOutput{Result: r}, nil
	})

	type pinInput struct {
		ChatID    int64 `json:"chat_id" jsonschema:"Chat ID"`
		MessageID int   `json:"message_id" jsonschema:"Message ID to pin"`
	}
	mcp.AddTool(m.server, &mcp.Tool{
		Name:        "pin_message",
		Description: "Pin a message in a chat",
	}, func(ctx context.Context, req *mcp.CallToolRequest, input pinInput) (*mcp.CallToolResult, actionOutput, error) {
		r, err := m.actions.PinMessage(input.ChatID, input.MessageID)
		if err != nil {
			return nil, actionOutput{}, err
		}
		return nil, actionOutput{Result: r}, nil
	})

	type leaveInput struct {
		ChatID int64 `json:"chat_id" jsonschema:"Chat ID to leave"`
	}
	mcp.AddTool(m.server, &mcp.Tool{
		Name:        "leave_chat",
		Description: "Leave a chat or group",
	}, func(ctx context.Context, req *mcp.CallToolRequest, input leaveInput) (*mcp.CallToolResult, actionOutput, error) {
		r, err := m.actions.LeaveChat(input.ChatID)
		if err != nil {
			return nil, actionOutput{}, err
		}
		return nil, actionOutput{Result: r}, nil
	})

	type setTitleInput struct {
		ChatID int64  `json:"chat_id" jsonschema:"Chat ID"`
		Title  string `json:"title" jsonschema:"New chat title"`
	}
	mcp.AddTool(m.server, &mcp.Tool{
		Name:        "set_chat_title",
		Description: "Change the title of a chat or group",
	}, func(ctx context.Context, req *mcp.CallToolRequest, input setTitleInput) (*mcp.CallToolResult, actionOutput, error) {
		r, err := m.actions.SetChatTitle(input.ChatID, input.Title)
		if err != nil {
			return nil, actionOutput{}, err
		}
		return nil, actionOutput{Result: r}, nil
	})

	type setDescInput struct {
		ChatID      int64  `json:"chat_id" jsonschema:"Chat ID"`
		Description string `json:"description" jsonschema:"New chat description"`
	}
	mcp.AddTool(m.server, &mcp.Tool{
		Name:        "set_chat_description",
		Description: "Change the description of a chat or group",
	}, func(ctx context.Context, req *mcp.CallToolRequest, input setDescInput) (*mcp.CallToolResult, actionOutput, error) {
		r, err := m.actions.SetChatDescription(input.ChatID, input.Description)
		if err != nil {
			return nil, actionOutput{}, err
		}
		return nil, actionOutput{Result: r}, nil
	})
}

func (m *MCPServer) handleSSETransport(w http.ResponseWriter, r *http.Request) {
	flusher, ok := w.(http.Flusher)
	if !ok {
		http.Error(w, "streaming not supported", http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-Type", "text/event-stream")
	w.Header().Set("Cache-Control", "no-cache")
	w.Header().Set("Connection", "keep-alive")

	switch r.Method {
	case http.MethodGet:
		log.Printf("MCP SSE client connected")
		<-r.Context().Done()
		log.Printf("MCP SSE client disconnected")

	case http.MethodPost:
		var req struct {
			Method string          `json:"method"`
			Params json.RawMessage `json:"params"`
			ID     any             `json:"id"`
		}
		if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
			sendSSEError(w, flusher, req.ID, err)
			return
		}
		m.handleMCPRequest(w, flusher, &req)

	default:
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
	}
}

func (m *MCPServer) handleMCPRequest(w http.ResponseWriter, flusher http.Flusher, req *struct {
	Method string          `json:"method"`
	Params json.RawMessage `json:"params"`
	ID     any             `json:"id"`
}) {
	switch req.Method {
	case "initialize":
		resp := map[string]any{
			"jsonrpc": "2.0",
			"id":      req.ID,
			"result": map[string]any{
				"protocolVersion": "1.0",
				"capabilities": map[string]any{
					"tools": map[string]any{},
				},
				"serverInfo": map[string]string{
					"name":    "tgbot",
					"version": "1.0.0",
				},
			},
		}
		sendSSEJSON(w, flusher, resp)

	case "tools/list":
		tools := []map[string]any{
			{"name": "send_message", "description": "Send a text message", "inputSchema": map[string]any{
				"type": "object", "properties": map[string]any{
					"chat_id": map[string]any{"type": "integer", "description": "Chat ID"},
					"text":    map[string]any{"type": "string", "description": "Message text"},
				}, "required": []string{"chat_id", "text"},
			}},
			{"name": "get_chat_info", "description": "Get chat information", "inputSchema": map[string]any{
				"type": "object", "properties": map[string]any{
					"chat_id": map[string]any{"type": "integer", "description": "Chat ID"},
				}, "required": []string{"chat_id"},
			}},
			{"name": "get_chat_member_count", "description": "Get member count", "inputSchema": map[string]any{
				"type": "object", "properties": map[string]any{
					"chat_id": map[string]any{"type": "integer", "description": "Chat ID"},
				}, "required": []string{"chat_id"},
			}},
			{"name": "ban_chat_member", "description": "Ban a user", "inputSchema": map[string]any{
				"type": "object", "properties": map[string]any{
					"chat_id": map[string]any{"type": "integer"},
					"user_id": map[string]any{"type": "integer"},
				}, "required": []string{"chat_id", "user_id"},
			}},
			{"name": "unban_chat_member", "description": "Unban a user", "inputSchema": map[string]any{
				"type": "object", "properties": map[string]any{
					"chat_id": map[string]any{"type": "integer"},
					"user_id": map[string]any{"type": "integer"},
				}, "required": []string{"chat_id", "user_id"},
			}},
			{"name": "promote_chat_member", "description": "Promote a user to admin", "inputSchema": map[string]any{
				"type": "object", "properties": map[string]any{
					"chat_id": map[string]any{"type": "integer"},
					"user_id": map[string]any{"type": "integer"},
				}, "required": []string{"chat_id", "user_id"},
			}},
			{"name": "pin_message", "description": "Pin a message", "inputSchema": map[string]any{
				"type": "object", "properties": map[string]any{
					"chat_id":    map[string]any{"type": "integer"},
					"message_id": map[string]any{"type": "integer"},
				}, "required": []string{"chat_id", "message_id"},
			}},
			{"name": "leave_chat", "description": "Leave a chat", "inputSchema": map[string]any{
				"type": "object", "properties": map[string]any{
					"chat_id": map[string]any{"type": "integer"},
				}, "required": []string{"chat_id"},
			}},
			{"name": "set_chat_title", "description": "Set chat title", "inputSchema": map[string]any{
				"type": "object", "properties": map[string]any{
					"chat_id": map[string]any{"type": "integer"},
					"title":   map[string]any{"type": "string"},
				}, "required": []string{"chat_id", "title"},
			}},
			{"name": "set_chat_description", "description": "Set chat description", "inputSchema": map[string]any{
				"type": "object", "properties": map[string]any{
					"chat_id":     map[string]any{"type": "integer"},
					"description": map[string]any{"type": "string"},
				}, "required": []string{"chat_id", "description"},
			}},
		}
		resp := map[string]any{
			"jsonrpc": "2.0",
			"id":      req.ID,
			"result":  map[string]any{"tools": tools},
		}
		sendSSEJSON(w, flusher, resp)

	case "tools/call":
		var params struct {
			Name      string         `json:"name"`
			Arguments map[string]any `json:"arguments"`
		}
		if err := json.Unmarshal(req.Params, &params); err != nil {
			sendSSEError(w, flusher, req.ID, err)
			return
		}
		result, err := m.executeTool(params.Name, params.Arguments)
		resp := map[string]any{
			"jsonrpc": "2.0",
			"id":      req.ID,
		}
		if err != nil {
			resp["error"] = map[string]any{"code": -32000, "message": err.Error()}
		} else {
			resp["result"] = map[string]any{
				"content": []map[string]any{{"type": "text", "text": result}},
			}
		}
		sendSSEJSON(w, flusher, resp)

	default:
		sendSSEError(w, flusher, req.ID, fmt.Errorf("unknown method: %s", req.Method))
	}
}

func (m *MCPServer) executeTool(name string, args map[string]any) (string, error) {
	if m.actions == nil {
		return "", fmt.Errorf("telegram actions not initialized")
	}
	switch name {
	case "send_message":
		chatID := int64(args["chat_id"].(float64))
		text := args["text"].(string)
		return m.actions.SendMessage(chatID, text)
	case "get_chat_info":
		chatID := int64(args["chat_id"].(float64))
		return m.actions.GetChatInfo(chatID)
	case "get_chat_member_count":
		chatID := int64(args["chat_id"].(float64))
		count, err := m.actions.GetChatMemberCount(chatID)
		if err != nil {
			return "", err
		}
		return fmt.Sprintf("%d", count), nil
	case "ban_chat_member":
		chatID := int64(args["chat_id"].(float64))
		userID := int64(args["user_id"].(float64))
		return m.actions.BanChatMember(chatID, userID)
	case "unban_chat_member":
		chatID := int64(args["chat_id"].(float64))
		userID := int64(args["user_id"].(float64))
		return m.actions.UnbanChatMember(chatID, userID)
	case "promote_chat_member":
		chatID := int64(args["chat_id"].(float64))
		userID := int64(args["user_id"].(float64))
		return m.actions.PromoteChatMember(chatID, userID)
	case "pin_message":
		chatID := int64(args["chat_id"].(float64))
		msgID := int(args["message_id"].(float64))
		return m.actions.PinMessage(chatID, msgID)
	case "leave_chat":
		chatID := int64(args["chat_id"].(float64))
		return m.actions.LeaveChat(chatID)
	case "set_chat_title":
		chatID := int64(args["chat_id"].(float64))
		title := args["title"].(string)
		return m.actions.SetChatTitle(chatID, title)
	case "set_chat_description":
		chatID := int64(args["chat_id"].(float64))
		desc := args["description"].(string)
		return m.actions.SetChatDescription(chatID, desc)
	default:
		return "", fmt.Errorf("unknown tool: %s", name)
	}
}

func (m *MCPServer) handleOpenAPI(w http.ResponseWriter, r *http.Request) {
	spec := map[string]any{
		"openapi": "3.0.0",
		"info": map[string]any{
			"title":   "Telegram Bot Tools",
			"version": "1.0.0",
		},
		"servers": []map[string]any{{"url": "/"}},
		"paths": map[string]any{
			"/api/tools/send_message": map[string]any{
				"post": map[string]any{
					"operationId": "send_message",
					"requestBody": map[string]any{
						"required": true,
						"content": map[string]any{
							"application/json": map[string]any{
								"schema": map[string]any{
									"type": "object",
									"properties": map[string]any{
										"chat_id": map[string]any{"type": "integer"},
										"text":    map[string]any{"type": "string"},
									},
									"required": []string{"chat_id", "text"},
								},
							},
						},
					},
					"responses": map[string]any{
						"200": map[string]any{
							"description": "OK",
							"content": map[string]any{
								"application/json": map[string]any{
									"schema": map[string]any{
										"type": "object",
										"properties": map[string]any{
											"result": map[string]any{"type": "string"},
										},
									},
								},
							},
						},
					},
				},
			},
			"/api/tools/ban_chat_member": map[string]any{
				"post": map[string]any{
					"operationId": "ban_chat_member",
					"requestBody": map[string]any{
						"required": true,
						"content": map[string]any{
							"application/json": map[string]any{
								"schema": map[string]any{
									"type": "object",
									"properties": map[string]any{
										"chat_id": map[string]any{"type": "integer"},
										"user_id": map[string]any{"type": "integer"},
									},
									"required": []string{"chat_id", "user_id"},
								},
							},
						},
					},
					"responses": map[string]any{
						"200": map[string]any{"description": "OK"},
					},
				},
			},
		},
	}
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(spec)
}

func sendSSEJSON(w http.ResponseWriter, flusher http.Flusher, data any) {
	b, _ := json.Marshal(data)
	fmt.Fprintf(w, "data: %s\n\n", b)
	flusher.Flush()
}

func sendSSEError(w http.ResponseWriter, flusher http.Flusher, id any, err error) {
	resp := map[string]any{
		"jsonrpc": "2.0",
		"id":      id,
		"error":   map[string]any{"code": -32603, "message": err.Error()},
	}
	sendSSEJSON(w, flusher, resp)
}
