# 🐍 Python Mini Debugger (AI-Powered)

An AI-powered Python debugging assistant that automatically analyzes buggy code, generates multiple fixes using an LLM, tests them inside a sandboxed environment, and returns the best working solution.

This project demonstrates LLM-powered debugging, agent orchestration, secure code execution, and automated fix evaluation.

## 🚀 Features

#### 🔍 Automated Code Debugging

  Detects runtime errors and code issues

  Generates fixes using an LLM

  Explains the problem and solution

#### 🤖 AI Debug Agent

  Uses an LLM to analyze errors

  Produces multiple candidate fixes

#### ⚡ Parallel Fix Testing

  Runs candidate fixes concurrently

  Selects the best working result automatically

#### 🐳 Secure Code Execution

  Executes user code inside Docker sandbox

  Prevents unsafe execution

#### 📊 Code Quality Checks

  Integrates flake8 linting

  Detects style issues and potential bugs

#### 🧠 Intelligent Orchestration

  Coordinates debugging workflow

  Performs early stopping when a successful fix is found

#### 📡 REST API

  Built using FastAPI for easy integration.

## 🏗 System Architecture


    User Code
    │
    ▼
    FastAPI Endpoint
    │
    ▼
    Code Orchestrator
    │
    ├── Initial Code Execution
    │
    ├── Debug Agent (LLM)
    │ │
    │ └── Generate Multiple Fixes
    │
    ├── Parallel Execution Engine
    │ │
    │ └── Test Fixes in Docker Sandbox
    │
    └── Best Fix Selection
    │
    ▼
    Return Working Code

## 📂 Project Structure

    python_debugger
    │
    ├── agents
    │   └── debug_agent.py
    │
    ├── sandbox
    │   └── executor.py
    │
    ├── core
    │   ├── logger.py
    │   ├── middleware.py
    │   ├── exception_handler.py
    │   └── config.py
    │
    ├── db
    │   ├── database.py
    │   └── models.py
    │
    ├── schemas
    │   ├── request.py
    │   └── response.py
    │
    ├── llm
    │   └── llm_wrapper.py
    │
    ├── orchestrator.py
    ├── main.py
    ├── requirements.txt
    └── README.md

## ⚙️ How It Works
#### 1️⃣ User Submits Buggy Code

Example:

    print(x)

#### 2️⃣ Code Execution

The system runs the code and captures:

    runtime errors
    stdout
    stderr
    lint issues

**Example error:**
NameError: name 'x' is not defined

#### 3️⃣ AI Debugging

The Debug Agent sends the error and code context to the LLM which generates candidate fixes.

Example fix:

    x = "Hello World"
    print(x)

#### 4️⃣ Parallel Fix Evaluation

Multiple fixes are tested concurrently using:
ThreadPoolExecutor

#### 5️⃣ Best Fix Selection

The system chooses the fix that:
  executes successfully
  has minimal lint issues
  produces correct output

#### 6️⃣ Final Response

  Example response:
  
    {
    
      "status": "success",
      
      "final_code": "x = 'Hello World'\nprint(x)",
      
      "result": {
      
        "stdout": "Hello World",
        
        "stderr": "",
        
        "success": true
        
      }
      
    }


## 🧪 API Usage

    Start the server
    uvicorn main:app --reload
    Endpoint
    POST /review_debug
    Request
    {
      "code": "print(x)"
    }
    Response
    {
      "status": "success",
      "final_code": "x = 'Hello World'\nprint(x)"
    }

## 🐳 Docker Sandbox

The debugger executes code inside a Docker container to isolate execution.
Build image:
    docker build -t python-runner .
#### 📦 Installation

**1** Install dependencies

    pip install -r requirements.txt
    
**2** Create environment variables

    Create .env
    OPENAI_API_KEY=your_api_key

**3** Run server
    uvicorn main:app --reload


## 🧰 Tech Stack

#### Backend
  Python
  FastAPI
  Pydantic
#### AI / LLM
  OpenAI API
  Prompt Engineering
#### Execution
  Docker
  Subprocess
#### Code Analysis
  flake8
#### Database
  SQLAlchemy
#### DevOps
  Git
  CI/CD ready

## 📈 Future Improvements

Multi-language debugging support

AST-based static analysis

Improved sandbox security

UI dashboard for debugging sessions

Memory-enabled AI debugging agent

## 👩‍💻 Author

Zainab Waseem

GitHub
https://github.com/ZainabWaseemQazi

LinkedIn
https://linkedin.com/in/zainab-waseem


