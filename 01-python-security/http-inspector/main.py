
import requests


def inspect_request(response):
    """Display information about the outgoing HTTP request."""
    request = response.request

    print("\n========== REQUEST DETAILS ==========")
    print("Method:", request.method)
    print("URL:", request.url)

    print("\nRequest Headers:")
    for name, value in request.headers.items():
        print(f"{name}: {value}")


def inspect_response(response):
    """Display information about the HTTP response."""
    print("\n========== RESPONSE DETAILS ==========")
    print("Status Code:", response.status_code)
    print("Final URL:", response.url)
    print("HTTP Version:", response.raw.version)

    print("\nResponse Headers:")
    for name, value in response.headers.items():
        print(f"{name}: {value}")

    print("\nResponse Body:")
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print(response.text[:1000])

def main():
    session = requests.Session()

    try:
        print("[*] Sending a test GET request...")

        response = session.get(
            "https://httpbin.org/anything",
            params={"api-security": "http-security"},
            timeout=10
        )

        inspect_request(response)
        inspect_response(response)

        print("\n[*] Testing cookie persistence...")

        cookie_response = session.get(
            "https://httpbin.org/cookies/set",
            params={"lab_session": "day2-demo"},
            timeout=10
        )

        print("Cookie-setting response:", cookie_response.status_code)
        print("Session cookies:", session.cookies.get_dict())

        check_response = session.get(
            "https://httpbin.org/cookies",
            timeout=10
        )

        print("Server-received cookies:")
        print(check_response.json())

    except requests.exceptions.RequestException as error:
        print("[ERROR] HTTP request failed:", error)

    finally:
        session.close()


if __name__ == "__main__":
    main()
