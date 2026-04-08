# Censys Queries for AI/ML Infrastructure

> Censys found 25%+ of Ollama instances on non-default ports (443, 80, 8080). Port-only scanning misses a significant fraction.

## Self-Hosted LLMs
```
services.port=11434 AND services.http.response.body:"Ollama"
services.port=11434 AND services.http.response.html_title:"Ollama"
services.port=8000 AND services.http.response.body:"v1/models"
services.port=1234 AND services.http.response.body:"lmstudio"
services.port=8080 AND services.http.response.body:"llama"
```

## AI Agents
```
services.port=18789 AND services.http.response.body:"Clawdbot"
services.port=18789 AND services.http.response.body:"OpenClaw"
services.port=18789 AND services.http.response.body:"auth_mode"
```

## Web UIs
```
services.port=7860 AND services.http.response.html_title:"Gradio"
services.port=8501 AND services.http.response.html_title:"Streamlit"
services.http.response.html_title:"Stable Diffusion"
services.http.response.html_title:"ComfyUI"
```

## Vector Databases
```
services.port=6333 AND services.http.response.body:"qdrant"
services.port=6333 AND services.http.response.body:"collections"
services.port=8080 AND services.http.response.body:"weaviate"
services.port=19530
services.port=9091 AND services.http.response.body:"milvus"
```

## MLOps
```
services.port=5000 AND services.http.response.html_title:"MLflow"
services.port=8888 AND services.http.response.html_title:"Jupyter"
services.port=8888 AND services.http.response.html_title:"JupyterLab"
services.http.response.html_title:"Kubeflow"
services.http.response.html_title:"Label Studio"
services.port=6006 AND services.http.response.html_title:"TensorBoard"
```

## By Cloud Provider
```
services.port=11434 AND autonomous_system.name:"AMAZON"
services.port=11434 AND autonomous_system.name:"HETZNER"
services.port=11434 AND autonomous_system.name:"DIGITALOCEAN"
services.port=11434 AND autonomous_system.name:"GOOGLE"
services.port=11434 AND autonomous_system.name:"MICROSOFT"
```
