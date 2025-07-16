import os, asyncio 
from huggingface_hub import Agent


async def main():
    agent = Agent(
        model="Qwen/Qwen2.5-72B-Instruct",
        provider="nebius",
        servers=[
            {
                "command": "npx",
                "args": [
                    "mcp-remote",
                    "http://localhost:7860/gradio_api/mcp/sse"  # Your Gradio MCP server
                ]
            }
        ],
    )
    async for chunk in agent.run("Salut ca va bien?"):
        if chunk.choices and chunk.choices[0].delta:
            # Extraire le contenu texte du delta
            content = chunk.choices[0].delta.content
            if content: # S'assurer que le contenu n'est pas vide (le dernier chunk est souvent vide)
                print(content, end="", flush=True) # Afficher le morceau de texte
                full_response_content += content # Accumuler le contenu



if __name__ == "__main__":
    asyncio.run(main())