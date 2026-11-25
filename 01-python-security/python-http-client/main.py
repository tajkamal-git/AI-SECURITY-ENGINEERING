import requests


BASE_URL = "https://httpbin.org"


def display_response(response):
    """Display HTTP response information."""

    print("\n========== RESPONSE ==========")
    print("Status Code:", response.status_code)
    print("URL:", response.url)
    print("Response Time:", response.elapsed.total_seconds(), "seconds")

    print("\nResponse Headers:")
    for name, value in response.headers.items():
        print(f"{name}: {value}")

    print("\nResponse Body:")
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print(response.text[:1000])


def send_request(method, endpoint):
    """Send an HTTP request using the selected method."""

    url = BASE_URL + endpoint

    headers = {
        "User-Agent": "Python-Security-Client/1.0",
        "Accept": "application/json"
    }

    payload = {
        "username": "security_student",
        "purpose": "HTTP client learning"
    }

    try:
        if method == "GET":
            response = requests.get(
                url,
                params={"course": "application-security"},
                headers=headers,
                timeout=10
            )

        elif method == "POST":
            response = requests.post(
                url,
                json=payload,
                headers=headers,
                timeout=10
            )

        elif method == "PUT":
            response = requests.put(
                url,
                json=payload,
                headers=headers,
                timeout=10
            )

        elif method == "PATCH":
            response = requests.patch(
                url,
                json={"username": "updated_student"},
                headers=headers,
                timeout=10
            )

        elif method == "DELETE":
            response = requests.delete(
                url,
                headers=headers,
                timeout=10
            )

        else:
            print("[ERROR] Unsupported method.")
            return

        display_response(response)

    except requests.exceptions.Timeout:
        print("[ERROR] Request timed out.")

    except requests.exceptions.ConnectionError:
        print("[ERROR] Unable to connect to server.")

    except requests.exceptions.RequestException as error:
        print("[ERROR] Request failed:", error)


def main():
    print("===== PYTHON HTTP CLIENT =====")
    print("1. GET")
    print("2. POST")
    print("3. PUT")
    print("4. PATCH")
    print("5. DELETE")

    choice = input("\nChoose method: ").strip()

    method_map = {
        "1": "GET",
        "2": "POST",
        "3": "PUT",
        "4": "PATCH",
        "5": "DELETE"
    }

    method = method_map.get(choice)

    if method is None:
        print("[ERROR] Invalid selection.")
        return

    send_request(method, "/anything")


if __name__ == "__main__":
    main()