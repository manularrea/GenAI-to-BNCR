# Lab 05: First Steps with Azure OpenAI

**Duration:** 3 hours  
**Difficulty:** Beginner  
**Prerequisites:** Basic Python knowledge

## Overview

This lab introduces you to Azure OpenAI Service through hands-on exercises. You'll learn how to make API calls, manage conversations, handle errors, and optimize costs for banking applications.

## Learning Objectives

By completing this lab, you will:

- Understand Azure OpenAI Service architecture and authentication
- Make your first API calls to GPT-3.5 and GPT-4 models
- Explore different parameters (temperature, max_tokens, top_p)
- Build a simple banking assistant chatbot
- Handle errors and implement retry logic
- Understand token usage and cost optimization

## Lab Structure

### Part 1: Environment Setup (15 minutes)
- Install required packages
- Configure environment variables
- Initialize Azure OpenAI client

### Part 2-3: Basic API Calls (30 minutes)
- Your first chat completion
- Understanding message roles (system, user, assistant)
- Testing different system prompts

### Part 4-5: Parameter Exploration (30 minutes)
- Temperature parameter and its effects
- Max tokens and output control
- Finding the right balance for banking applications

### Part 6: Conversational AI (45 minutes)
- Building a banking assistant class
- Managing conversation history
- Context-aware responses

### Part 7: Error Handling (30 minutes)
- Common API errors
- Implementing retry logic with exponential backoff
- Production-ready error handling

### Part 8-9: Cost Optimization (30 minutes)
- Understanding token usage
- Calculating API costs
- Comparing GPT-3.5 vs GPT-4
- Cost optimization strategies

### Practical Exercises (60 minutes)
- Exercise 1: Product recommendation system
- Exercise 2: Multi-language support
- Exercise 3: Cost optimization challenge

## Prerequisites

Before starting this lab, ensure you have:

1. **Azure OpenAI Access**: Your instructor will provide credentials
2. **Python Environment**: Python 3.11+ with pip
3. **Required Packages**: Listed in `requirements.txt`
4. **Environment Variables**: Configured in `.env` file

## Setup Instructions

1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/manularrea/azure-genai-labs.git
   cd azure-genai-labs
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your Azure credentials
   ```

4. **Launch Jupyter**:
   ```bash
   jupyter lab
   ```

5. **Open the notebook**:
   Navigate to `labs/lab05/lab05_azure_openai_basics.ipynb`

## Azure Resources Used

This lab uses the following Azure resources:

- **Azure OpenAI Service**
  - GPT-3.5 Turbo deployment (60K TPM)
  - GPT-4 deployment (10K TPM) - optional
  - Region: East US 2

**Estimated Cost:** ~$0.50 per lab session

## Key Concepts

### Message Roles
- **System**: Defines the AI's behavior and context
- **User**: The user's input or question
- **Assistant**: The AI's previous responses

### Temperature Parameter
- **0.0**: Deterministic, consistent responses
- **0.7**: Balanced (recommended for banking)
- **1.0+**: Creative, varied responses

### Token Usage
- Input tokens: Your prompt and conversation history
- Output tokens: The AI's response
- Total tokens: Input + Output (affects cost)

## Practical Exercises

### Exercise 1: Product Recommendation System
Build a system that recommends banking products based on customer needs using the provided dataset.

**Skills practiced:**
- System prompt engineering
- Data integration
- Structured responses

### Exercise 2: Multi-language Support
Create a bilingual assistant that handles Spanish and English conversations seamlessly.

**Skills practiced:**
- Language detection
- Context management
- Multilingual prompts

### Exercise 3: Cost Optimization
Optimize API usage to stay within a $10/day budget while maintaining quality.

**Skills practiced:**
- Token counting
- Cost calculation
- Model selection
- Prompt optimization

## Expected Outcomes

After completing this lab, you should be able to:

✅ Initialize and authenticate with Azure OpenAI Service  
✅ Create effective system prompts for banking scenarios  
✅ Manage multi-turn conversations with context  
✅ Handle API errors gracefully with retry logic  
✅ Calculate and optimize API costs  
✅ Choose between GPT-3.5 and GPT-4 based on requirements  

## Troubleshooting

### Common Issues

**Issue:** `AuthenticationError: Incorrect API key`
- **Solution**: Verify your `.env` file has the correct `AZURE_OPENAI_API_KEY`

**Issue:** `RateLimitError: Rate limit exceeded`
- **Solution**: The retry logic will handle this automatically. If persistent, contact your instructor.

**Issue:** `DeploymentNotFound: The API deployment was not found`
- **Solution**: Check your deployment names in `.env` match those in Azure

**Issue:** High token usage
- **Solution**: Reduce `max_tokens`, optimize system prompt, or use GPT-3.5 instead of GPT-4

## Additional Resources

- [Azure OpenAI Documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Best Practices for Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)

## Next Lab

**Lab 06: Prompt Engineering Fundamentals**  
Learn advanced techniques for crafting effective prompts that produce consistent, high-quality results for banking applications.

---

**Instructor:** Manuela Larrea  
**Contact:** manuela.larrea@idataglobal.com  
**Course:** Generative AI for Banking Sector - BNCR

