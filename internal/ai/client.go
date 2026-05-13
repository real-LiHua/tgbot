package ai

import (
	"bufio"
	"encoding/json"
	"fmt"
	"net/http"
	"strings"
	"sync"

	"github.com/real-LiHua/tgbot/internal/config"
)

type Client struct {
	baseURL   string
	agentName string
	mu        sync.Mutex
	sessions  map[int64]string
	httpCli   *http.Client
}

func NewClient(cfg *config.Config) *Client {
	return &Client{
		baseURL:   cfg.DockerAgentURL,
		agentName: "agent",
		sessions:  make(map[int64]string),
		httpCli:   &http.Client{},
	}
}

func (c *Client) getSession(chatID int64) (string, error) {
	c.mu.Lock()
	defer c.mu.Unlock()
	if id, ok := c.sessions[chatID]; ok {
		return id, nil
	}
	resp, err := c.httpCli.Post(c.baseURL+"/api/sessions", "application/json", nil)
	if err != nil {
		return "", fmt.Errorf("create session: %w", err)
	}
	defer resp.Body.Close()
	if resp.StatusCode > 299 {
		return "", fmt.Errorf("create session status: %d", resp.StatusCode)
	}
	var data struct {
		ID string `json:"id"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&data); err != nil {
		return "", fmt.Errorf("decode session: %w", err)
	}
	c.sessions[chatID] = data.ID
	return data.ID, nil
}

type SSEEvent struct {
	Type    string `json:"type"`
	Content string `json:"content,omitempty"`
}

type ChatEvent struct {
	Type string `json:"type"`
	Text string `json:"text,omitempty"`
}

func (c *Client) ChatStream(messages []map[string]any, chatID int64) (<-chan ChatEvent, error) {
	sessionID, err := c.getSession(chatID)
	if err != nil {
		return nil, err
	}
	body, err := json.Marshal(messages)
	if err != nil {
		return nil, fmt.Errorf("marshal messages: %w", err)
	}
	req, err := http.NewRequest(http.MethodPost,
		c.baseURL+"/api/sessions/"+sessionID+"/agent/"+c.agentName,
		strings.NewReader(string(body)))
	if err != nil {
		return nil, fmt.Errorf("create request: %w", err)
	}
	req.Header.Set("Content-Type", "application/json")
	resp, err := c.httpCli.Do(req)
	if err != nil {
		return nil, fmt.Errorf("do request: %w", err)
	}
	ch := make(chan ChatEvent)
	go func() {
		defer resp.Body.Close()
		defer close(ch)
		scanner := bufio.NewScanner(resp.Body)
		for scanner.Scan() {
			line := strings.TrimSpace(scanner.Text())
			if !strings.HasPrefix(line, "data: ") {
				continue
			}
			var event SSEEvent
			if err := json.Unmarshal([]byte(line[6:]), &event); err != nil {
				continue
			}
			switch event.Type {
			case "agent_choice":
				ch <- ChatEvent{Type: "delta", Text: event.Content}
			case "tool_call_confirmation":
				resumeBody, _ := json.Marshal(map[string]bool{"approve": true})
				c.httpCli.Post(c.baseURL+"/api/sessions/"+sessionID+"/resume",
					"application/json", strings.NewReader(string(resumeBody)))
			case "stream_stopped":
				ch <- ChatEvent{Type: "done"}
				return
			case "error":
				ch <- ChatEvent{Type: "done"}
				return
			}
		}
	}()
	return ch, nil
}

func (c *Client) ListModels() ([]string, error) {
	resp, err := c.httpCli.Get(c.baseURL + "/api/agents")
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()
	if resp.StatusCode > 299 {
		return nil, fmt.Errorf("status %d", resp.StatusCode)
	}
	return []string{"configured in agent.yaml"}, nil
}


