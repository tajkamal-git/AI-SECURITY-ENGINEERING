
import json


ALLOWED_METHODS = {
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "HEAD",
    "OPTIONS"
}


def load_request(file_path):
    """Load request information from a JSON file."""

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("[ERROR] Request file not found.")

    except json.JSONDecodeError:
        print("[ERROR] Invalid JSON format.")

    return None


def validate_request(request):
    """Validate the structure of request data."""

    if not isinstance(request, dict):
        return False, "Request must be a JSON object."

    required_fields = ["method", "url", "headers", "body"]

    for field in required_fields:
        if field not in request:
            return False, f"Missing field: {field}"

    if not isinstance(request["method"], str):
        return False, "Method must be a string."

    if request["method"].upper() not in ALLOWED_METHODS:
        return False, "Unsupported HTTP method."

    if not isinstance(request["url"], str) or not request["url"].startswith("/"):
        return False, "URL must be a relative request path."

    if not isinstance(request["headers"], dict):
        return False, "Headers must be a JSON object."

    if not isinstance(request["body"], dict):
        return False, "Body must be a JSON object."

    return True, "Request structure is valid."


def analyse_request(request):
    """Analyse HTTP request information."""

    print("\n========== HTTP REQUEST ANALYSIS ==========")

    print("Method:", request["method"].upper())
    print("URL:", request["url"])

    print("\nHeaders:")

    for key, value in request["headers"].items():
        print(f"{key}: {value}")

    print("\nBody fields:")

    for key in request["body"]:
        print(key)

    print("\nTotal headers:", len(request["headers"]))
    print("Total body fields:", len(request["body"]))

    print("\n===========================================")


def main():

    request = load_request("request.json")

    if request is None:
        return

    valid, message = validate_request(request)

    print("\nValidation:", message)

    if not valid:
        print("[ERROR] Request analysis stopped.")
        return

    analyse_request(request)


if __name__ == "__main__":
    main()
