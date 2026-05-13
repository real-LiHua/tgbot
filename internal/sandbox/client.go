package sandbox

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"time"

	"github.com/real-LiHua/tgbot/internal/config"
)

type Client struct {
	baseURL    string
	apiKey     string
	httpClient *http.Client
}

func NewClient(cfg *config.Config) *Client {
	return &Client{
		baseURL:    cfg.SandboxURL,
		apiKey:     cfg.SandboxAPIKey,
		httpClient: &http.Client{Timeout: 120 * time.Second},
	}
}

type CreateRequest struct {
	Timeout int `json:"timeout"`
}

type CreateResponse struct {
	SandboxID string `json:"sandbox_id"`
}

type RunRequest struct {
	SandboxID string            `json:"sandbox_id"`
	Cmd       string            `json:"cmd"`
	Args      []string          `json:"args"`
	Cwd       string            `json:"cwd,omitempty"`
	Env       map[string]string `json:"env,omitempty"`
}

type RunResponse struct {
	ExitCode int    `json:"exit_code"`
	Stdout   string `json:"stdout"`
	Stderr   string `json:"stderr"`
	TimedOut bool   `json:"timed_out"`
}

type ReadRequest struct {
	SandboxID string `json:"sandbox_id"`
	Path      string `json:"path"`
}

type ReadResponse struct {
	Data *string `json:"data"`
}

type WriteFileEntry struct {
	Path    string `json:"path"`
	Content string `json:"content"`
}

type WriteRequest struct {
	SandboxID string          `json:"sandbox_id"`
	Files     []WriteFileEntry `json:"files"`
}

func (c *Client) headers() map[string]string {
	if c.apiKey != "" {
		return map[string]string{"X-Api-Key": c.apiKey}
	}
	return nil
}

func (c *Client) do(method, url string, body, resp any) error {
	var reqBody io.Reader
	if body != nil {
		b, err := json.Marshal(body)
		if err != nil {
			return fmt.Errorf("marshal request: %w", err)
		}
		reqBody = bytes.NewReader(b)
	}
	req, err := http.NewRequest(method, url, reqBody)
	if err != nil {
		return fmt.Errorf("create request: %w", err)
	}
	req.Header.Set("Content-Type", "application/json")
	for k, v := range c.headers() {
		req.Header.Set(k, v)
	}
	r, err := c.httpClient.Do(req)
	if err != nil {
		return fmt.Errorf("do request: %w", err)
	}
	defer r.Body.Close()
	if r.StatusCode > 299 {
		rb, _ := io.ReadAll(r.Body)
		return fmt.Errorf("status %d: %s", r.StatusCode, string(rb))
	}
	if resp != nil {
		return json.NewDecoder(r.Body).Decode(resp)
	}
	return nil
}

func (c *Client) Create(timeout int) (*CreateResponse, error) {
	var resp CreateResponse
	err := c.do(http.MethodPost, c.baseURL+"/create", &CreateRequest{Timeout: timeout}, &resp)
	if err != nil {
		return nil, err
	}
	return &resp, nil
}

func (c *Client) Run(sandboxID, cmd string, args []string, env map[string]string) (*RunResponse, error) {
	var resp RunResponse
	err := c.do(http.MethodPost, c.baseURL+"/run", &RunRequest{
		SandboxID: sandboxID,
		Cmd:       cmd,
		Args:      args,
		Env:       env,
	}, &resp)
	if err != nil {
		return nil, err
	}
	return &resp, nil
}

func (c *Client) ReadFile(sandboxID, path string) (*string, error) {
	var resp ReadResponse
	err := c.do(http.MethodPost, c.baseURL+"/read", &ReadRequest{
		SandboxID: sandboxID,
		Path:      path,
	}, &resp)
	if err != nil {
		return nil, err
	}
	return resp.Data, nil
}

func (c *Client) WriteFiles(sandboxID string, files []WriteFileEntry) error {
	return c.do(http.MethodPost, c.baseURL+"/write", &WriteRequest{
		SandboxID: sandboxID,
		Files:     files,
	}, nil)
}

func (c *Client) Stop(sandboxID string) error {
	return c.do(http.MethodPost, c.baseURL+"/stop/"+sandboxID, nil, nil)
}
