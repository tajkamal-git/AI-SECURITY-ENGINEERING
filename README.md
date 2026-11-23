# Python HTTP Request Parser

## Overview

A Python-based HTTP Request Parser developed as part of my six-month AI Security Engineering and Application Security Engineering preparation.

The project reads HTTP request information stored in JSON format, validates its structure and analyses request components.

## Features

- JSON file parsing
- HTTP method validation
- Request structure validation
- Header analysis
- Request body field analysis
- Exception handling
- Invalid input detection

## Technologies

- Python
- JSON
- VS Code
- Git and GitHub

## Project Structure

```text
api-request-analyser/
├── main.py
├── request.json
├── README.md
└── .gitignore
```

## Execution

```bash
python main.py
```

## Security Concepts Practised

- Input validation
- Allowlist validation
- JSON parsing
- Exception handling
- HTTP request structure

## Testing

Tested normal request data, unsupported HTTP methods, missing fields, invalid headers and malformed JSON.

## Learning Outcome

Learned how Python handles structured HTTP request information and how validation and exception handling can be applied when developing security-related tools.

## Future Improvements

- HTTP response analysis
- Request and response logging
- Security header analysis
- URL validation
- Automated API security checks