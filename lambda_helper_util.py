def get_request_context(event):
    """
    Extracts the request context information from the event object.
    """
    request_context = {
        "HttpMethod": "",
        "UrlPath": "",
        "UsingFunctionUrl": False
    }

    # Check for request context details
    if 'requestContext' in event:
        if 'http' in event['requestContext']:
            request_context["HttpMethod"] = event['requestContext']['http']['method']
            request_context["UsingFunctionUrl"] = True

    # Fallback to 'httpMethod' if available
    if 'httpMethod' in event:
        request_context["HttpMethod"] = event['httpMethod']

    # Determine the URL path
    if 'rawPath' in event:
        request_context["UrlPath"] = event['rawPath']
        request_context["UsingFunctionUrl"] = True
    elif 'path' in event:
        request_context["UrlPath"] = event['path']

    return request_context


def get_path_value(raw_path, path_index):
    """
    Returns the specific segment of the path by index.
    """
    path_segments = raw_path.split('?')[0].split('/')
    return path_segments[path_index]


def get_last_path_value(raw_path):
    """
    Returns the last segment of the path.
    """
    path_segments = raw_path.split('?')[0].split('/')
    return path_segments[-1]


def get_header_object(event):
    """
    Converts the headers in the event object to a case-insensitive dictionary.
    """
    headers = {}

    if 'headers' in event and event['headers']:
        for header_name, header_value in event['headers'].items():
            headers[header_name.lower()] = header_value

    return headers


def create_response_object(status_code, response_body, enable_cors):
    """
    Creates a response object with optional CORS headers.
    """
    response = {
        'statusCode': status_code,
        'body': response_body
    }

    if enable_cors:
        response['headers'] = {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Origin': '*'
        }

    return response


def create_authorizer_response(is_authorized, error_message):
    """
    Creates an authorizer response with a policy document.
    """
    effect = "Allow" if is_authorized else "Deny"

    return {
        "principalId": "user",
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": effect,
                    "Resource": "*"
                }
            ]
        },
        "context": {
            "errorMessage": f"\"{error_message}\""
        }
    }
