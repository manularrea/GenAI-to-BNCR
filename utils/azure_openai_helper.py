"""
Azure OpenAI Helper Functions
Provides reusable utilities for interacting with Azure OpenAI Service
"""

import os
import time
from typing import List, Dict, Optional
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class AzureOpenAIClient:
    """Wrapper class for Azure OpenAI operations"""
    
    def __init__(self):
        """Initialize Azure OpenAI client with environment variables"""
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )
        
        self.gpt4_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_GPT4", "gpt-4")
        self.gpt35_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_GPT35", "gpt-35-turbo")
        self.embedding_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_EMBEDDING", "text-embedding-ada-002")
    
    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "gpt-35-turbo",
        temperature: float = 0.7,
        max_tokens: int = 800,
        **kwargs
    ) -> str:
        """
        Generate a chat completion
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            model: Model to use ('gpt-4' or 'gpt-35-turbo')
            temperature: Sampling temperature (0-2)
            max_tokens: Maximum tokens to generate
            **kwargs: Additional parameters for the API
            
        Returns:
            Generated text response
        """
        deployment = self.gpt4_deployment if model == "gpt-4" else self.gpt35_deployment
        
        try:
            response = self.client.chat.completions.create(
                model=deployment,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                **kwargs
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in chat completion: {str(e)}")
            raise
    
    def chat_completion_with_retry(
        self,
        messages: List[Dict[str, str]],
        max_retries: int = 3,
        **kwargs
    ) -> str:
        """
        Generate chat completion with exponential backoff retry
        
        Args:
            messages: List of message dictionaries
            max_retries: Maximum number of retry attempts
            **kwargs: Additional parameters for chat_completion
            
        Returns:
            Generated text response
        """
        for attempt in range(max_retries):
            try:
                return self.chat_completion(messages, **kwargs)
            except Exception as e:
                if attempt == max_retries - 1:
                    raise
                wait_time = 2 ** attempt
                print(f"Attempt {attempt + 1} failed. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
    
    def get_embedding(self, text: str) -> List[float]:
        """
        Generate embedding vector for text
        
        Args:
            text: Input text to embed
            
        Returns:
            Embedding vector as list of floats
        """
        try:
            response = self.client.embeddings.create(
                model=self.embedding_deployment,
                input=text
            )
            return response.data[0].embedding
        except Exception as e:
            print(f"Error generating embedding: {str(e)}")
            raise
    
    def get_embeddings_batch(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for multiple texts
        
        Args:
            texts: List of input texts
            
        Returns:
            List of embedding vectors
        """
        try:
            response = self.client.embeddings.create(
                model=self.embedding_deployment,
                input=texts
            )
            return [item.embedding for item in response.data]
        except Exception as e:
            print(f"Error generating batch embeddings: {str(e)}")
            raise
    
    def stream_chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "gpt-35-turbo",
        **kwargs
    ):
        """
        Stream chat completion responses
        
        Args:
            messages: List of message dictionaries
            model: Model to use
            **kwargs: Additional parameters
            
        Yields:
            Chunks of generated text
        """
        deployment = self.gpt4_deployment if model == "gpt-4" else self.gpt35_deployment
        
        try:
            response = self.client.chat.completions.create(
                model=deployment,
                messages=messages,
                stream=True,
                **kwargs
            )
            
            for chunk in response:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            print(f"Error in streaming completion: {str(e)}")
            raise


def count_tokens(text: str, model: str = "gpt-35-turbo") -> int:
    """
    Estimate token count for text
    
    Args:
        text: Input text
        model: Model name for tokenization
        
    Returns:
        Estimated token count
    """
    # Simple estimation: ~4 characters per token
    return len(text) // 4


def format_messages(system_prompt: str, user_message: str) -> List[Dict[str, str]]:
    """
    Format messages for chat completion
    
    Args:
        system_prompt: System instruction
        user_message: User query
        
    Returns:
        Formatted message list
    """
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]


def add_message_to_history(
    history: List[Dict[str, str]],
    role: str,
    content: str
) -> List[Dict[str, str]]:
    """
    Add a message to conversation history
    
    Args:
        history: Existing message history
        role: Message role ('user', 'assistant', or 'system')
        content: Message content
        
    Returns:
        Updated message history
    """
    history.append({"role": role, "content": content})
    return history


# Example usage
if __name__ == "__main__":
    # Initialize client
    client = AzureOpenAIClient()
    
    # Simple chat completion
    messages = format_messages(
        system_prompt="You are a helpful banking assistant.",
        user_message="What is a credit score?"
    )
    
    response = client.chat_completion(messages, model="gpt-35-turbo")
    print(f"Response: {response}")
    
    # Generate embedding
    embedding = client.get_embedding("What is a credit score?")
    print(f"Embedding dimension: {len(embedding)}")

