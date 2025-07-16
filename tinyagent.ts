import { Agent } from "@huggingface/tiny-agents"; // Ou le chemin correct vers le module Agent

const agent = new Agent({
    provider: process.env.PROVIDER ?? "nebius",
    model: process.env.MODEL_ID ?? "Qwen/Qwen2.5-72B-Instruct",
    apiKey: process.env.HF_TOKEN,
    servers: [
        // ... existing servers ...
        {
            command: "npx",
            args: [
                "mcp-remote",
                "http://localhost:7860/gradio_api/mcp/sse"  // Your Gradio MCP server
            ]
        }
    ],
});

// Le reste de votre code qui utilise 'agent'