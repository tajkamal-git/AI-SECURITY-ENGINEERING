# Day 2 – HTTP Request Inspector

## Overview
A Python-based HTTP inspection exercise that sends test GET requests and analyses HTTP request and response information.

## Learning Objectives
- Understand HTTP request and response structures.
- Learn HTTP methods and status codes.
- Inspect request and response headers.
- Understand cookies and sessions.
- Use Python Requests to inspect HTTP traffic.

## Technologies
- Python
- Requests library
- HTTP
- JSON

## Project Structure
```text
http-inspector/
├── main.py
├── requirements.txt
└── README.md
```

## Installation
```powershell
python -m pip install -r requirements.txt
```

## Execution
```powershell
python main.py
```

## Practical Work
- Sent a GET request to a public HTTP testing endpoint.
- Inspected outgoing request headers.
- Analysed response status and headers.
- Examined JSON response data.
- Tested cookie persistence using a Python session.

## Security Concepts
- HTTPS
- HTTP methods
- Cookie security
- Session management
- Authorization headers
- HTTP error responses

## Learning Outcome
Learned how HTTP communication works and how Python can be used to inspect request and response details.

## Limitations
This is a learning exercise using a public test endpoint. It is not a production-grade HTTP security scanner.
