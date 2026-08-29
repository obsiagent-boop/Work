import os
import json
import logging
from typing import Dict, Any, List, Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")

EXA_MCP_URL = "https://mcp.exa.ai/mcp?tools=web_search_exa,web_fetch_exa,agent_run,web_search_advanced_exa"

class ExaMCPIntegrationEngine:
    """
    Exa MCP Integration Engine supporting web_search_exa, web_fetch_exa,
    agent_run (Exa Agent), and web_search_advanced_exa.
    """

    def __init__(self, mcp_url: str = EXA_MCP_URL):
        self.mcp_url = mcp_url

    def get_mcp_config(self) -> Dict[str, Any]:
        return {
            "mcpServers": {
                "exa": {
                    "url": self.mcp_url
                }
            }
        }

if __name__ == "__main__":
    engine = ExaMCPIntegrationEngine()
    print("=== EXA MCP CONFIGURATION ===")
    print(json.dumps(engine.get_mcp_config(), indent=2))
