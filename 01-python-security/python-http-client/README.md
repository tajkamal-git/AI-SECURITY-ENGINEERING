# Day 3 – Python HTTP Client

## Objective
Build a Python HTTP client using the Requests library to send GET, POST, PUT, PATCH and DELETE requests and analyse HTTP responses.

## Technologies
- Python
- Requests
- HTTP
- JSON
- PowerShell

## Features
- Supports GET, POST, PUT, PATCH and DELETE.
- Sends query parameters.
- Sends JSON payloads.
- Custom request headers.
- Displays response status codes.
- Displays response headers.
- Displays response body.
- Displays response time.
- Handles connection errors.
- Handles timeout errors.
- Handles general request exceptions.

## Project Structure

```text
python-http-client/
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

## Test Environment

The client uses the HTTPBin public test service.

https://httpbin.org/

## HTTP Methods

| Method | Purpose |
|---|---|
| GET | Retrieve data |
| POST | Submit data |
| PUT | Replace data |
| PATCH | Partially modify data |
| DELETE | Request deletion |

## Security Concepts Learned
- HTTP request and response handling
- HTTP status codes
- Headers
- Query parameters
- JSON payloads
- Timeout handling
- Exception handling
- HTTP methods
- Basic HTTP client security considerations
- SSRF concept

## Limitations
This is an educational HTTP client. It is not a production-grade security testing tool. It does not implement authentication, URL validation, retry controls, comprehensive response processing, or SSRF protections.

## Day 3 Status
Completed after testing all five HTTP methods, reviewing responses, documenting findings and understanding the code.
