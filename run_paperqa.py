from paperqa import Settings, ask
from paperqa.settings import AgentSettings
import litellm
#litellm.api_timeout = 500 

class EnvironmentState:
    def __init__(self, *args, **kwargs):
        pass

Settings.model_rebuild()

local_llm_config = {
    "model_list": [
        {
            "model_name": "ollama/llama3",
            "litellm_params": {
                "model": "ollama/llama3",
                "api_base": "http://localhost:11434", 
                "timeout" : 1000
            },
        }
    ]
}
# local_llm_config = {
#     "model_list": [
#         {
#             "model_name": "ollama/llama3",
#             "litellm_params": {
#                 "model": "ollama/llama3",
#                 "api_base": "http://localhost:11434",
#                 "timeout": 1000,
#                 "litellm_params": {"gpu": True}  # Force GPU usage
#             },
#         }
#     ]
# }


# PaperQA Settings
settings = Settings(
    llm="ollama/llama3",
    llm_config=local_llm_config,
    summary_llm="ollama/llama3",
    summary_llm_config=local_llm_config,
    embedding="ollama/nomic-embed-text",
    agent=AgentSettings(agent_llm="ollama/llama3", agent_llm_config=local_llm_config),
    paper_directory="papers", 
    async_processing=False
)


answer = ask(
    "What machine learning algorithms can classify heart failure?",
    settings=settings
)

print(answer)
