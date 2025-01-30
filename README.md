# lambda_helper_util

`lambda_helper_util` is a utility module designed to simplify common tasks in AWS Lambda functions. It provides helper functions for handling HTTP responses, checking the execution environment, and parsing event request data.

## Installation

Ensure that `lambda_helper_util` is available in your Lambda function's environment. You can include it in your deployment package or add it as a layer.

## Features

- **`create_response_object(status_code: int, body: str, enable_cors: bool) -> dict`**: Creates a properly formatted HTTP response object.
- **`is_dev(event: dict) -> bool`**: Determines if the current execution environment is in development mode.
- **`get_header_object(event: dict) -> dict`**: Extracts headers from the incoming request event.
- **`get_last_path_value(url_path: str) -> str`**: Retrieves the last segment of the URL path.
- **`get_request_context(event: dict) -> dict`**: Extracts the request context, including HTTP method and URL path.

## Usage Example

```python
import json
from lambda_helper_util import create_response_object, is_dev, get_header_object, get_last_path_value, get_request_context

def lambda_handler(event, context):
    # Initialize variable
    enable_cors = True
    headers = get_header_object(event)
    request_context = get_request_context(event)

    if is_dev(event):
        return create_response_object(200, json.dumps(event), enable_cors)

    if get_last_path_value(request_context["UrlPath"]) != "token":
        return create_response_object(200, json.dumps({"message": "invalid path."}), enable_cors)

    if 'grant_type' not in headers or 'scope' not in headers:
        return create_response_object(200, json.dumps({"message": "headers not complete."}), enable_cors)
    
    if request_context["HttpMethod"] != 'POST':
        return create_response_object(200, json.dumps({"message": "invalid http method."}), enable_cors)

    return create_response_object(200, json.dumps({"message": "request processed successfully."}), enable_cors)
```

## License

This module is open-source and can be modified as needed for your AWS Lambda functions.

