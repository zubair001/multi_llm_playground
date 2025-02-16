# **Multi-LLM Backend with FastAPI**

This is a FastAPI backend application that supports multi-LLM (Large Language Model) communication using OpenRouter API. It is designed to allow interaction with multiple models such as **Mistral**, **Claude**, and others. The backend also supports **streaming responses** for generating long texts.

## **Features**
- **Multi-LLM Support**: Integrates with various models via the OpenRouter API.
- **Text Generation**: Provides endpoints to generate text using different models.
- **Streaming Responses**: Returns streaming responses for long texts, enabling real-time interaction with large language models.
- **Configurable**: Easily switch between different models and configuration settings.

## **Tech Stack**
- **Backend**: FastAPI
- **API Client**: OpenAI Python client for OpenRouter
- **Environment Management**: `.env` for sensitive data and configuration
- **Data Validation**: Pydantic models
- **Streaming**: Supports streaming API responses for large text generation
- **Deployment**: Can be deployed on any cloud platform that supports FastAPI (e.g., AWS, Azure, GCP)

## **Installation & Setup**

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/fastapi-llm-backend.git
cd fastapi-llm-backend



