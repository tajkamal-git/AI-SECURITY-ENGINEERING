# HTTP Notes (`HTTP-NOTES.md`)

A plain-English guide to how the web talks: HTTP basics, requests, responses, methods, headers, status codes, cookies, and sessions.

---

## 1. HTTP Fundamentals

### What is HTTP and how does it work?
**HTTP (HyperText Transfer Protocol)** is simply the language that your web browser and a website's server use to talk to each other.

Think of it like ordering food at a restaurant:
- **Client / Browser** = You (the customer)
- **Web Server** = The kitchen
- **HTTP Request** = Your order
- **HTTP Response** = The food brought back to your table

Every time you open a website, this 4-step loop happens:
1. **Request:** Your browser sends an HTTP request asking for a page or data.
2. **Process:** The server receives the request and figures out what to do (like fetching data from a database).
3. **Response:** The server sends back an HTTP response with the result.
4. **Display:** Your browser reads the response and shows the webpage on your screen.

```text
+-------------------+      HTTP Request (Method, Headers, Cookies, Body)      +-------------------+
| Client / Browser  | ------------------------------------------------------> |    Web Server     |
|   (Sends request) | <------------------------------------------------------ | (Processes & sends|
+-------------------+      HTTP Response (Status, Headers, Cookies, Body)     |     response)     |
                                                                              +-------------------+
```

---

## 2. Anatomy of an HTTP Request

An **HTTP request** is a structured message your browser sends to a server saying: *"Here is what I want, where to find it, and a few details about who I am."*

### Example Request
```http
GET /products HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html
Connection: keep-alive
```

### Breaking It Down
| Part | Example | Plain-English Meaning |
| :--- | :--- | :--- |
| **HTTP Method** | `GET` | What action you want to take (here, just *read/fetch* data). |
| **Path** | `/products` | The specific page or resource you want on the website. |
| **HTTP Version** | `HTTP/1.1` | The version of the HTTP rules being used. |
| **Host** | `example.com` | The website's domain name (which server you are talking to). |
| **User-Agent** | `Mozilla/5.0` | Tells the server what browser/device is making the request. |
| **Accept** | `text/html` | Tells the server what format you prefer back (like an HTML webpage). |
| **Connection** | `keep-alive` | Asks to keep the network connection open briefly so future requests are faster. |

---

## 3. Anatomy of an HTTP Response

An **HTTP response** is the server's reply. It tells your browser: *"Here is whether your request worked, some info about what I'm sending, and the actual content."*

### Example Response
```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 27

{"message": "Hello World"}
```

### Breaking It Down
- **HTTP Version (`HTTP/1.1`):** The version of HTTP the server is replying with.
- **Status Code (`200`):** A 3-digit number summarizing the result (`200` means everything went fine).
- **Status Message (`OK`):** A short human-readable label for the status code.
- **Response Headers (`Content-Type`, `Content-Length`):** Extra info about the data being returned—here, it says the data is in JSON format and is 27 bytes long.
- **Response Body (`{"message": "Hello World"}`):** The actual content you asked for (separated from the headers by a blank line).

---

## 4. HTTP Methods

HTTP methods tell the server **what kind of action** the client wants to perform on a resource.

| Method | Plain-English Purpose | Real-World Example |
| :--- | :--- | :--- |
| **GET** | Read or fetch data (does not change anything). | Viewing a user's profile. |
| **POST** | Send new data to create something or trigger an action. | Logging in or creating a new account. |
| **PUT** | Replace an entire existing item with a new version. | Overwriting an entire user profile. |
| **PATCH** | Update only a small part of an existing item. | Changing just a username. |
| **DELETE** | Remove an item. | Deleting a user account. |
| **HEAD** | Same as `GET`, but returns **only the headers** (no body). | Checking if a file exists or how big it is without downloading it. |
| **OPTIONS** | Ask the server what methods or actions are allowed. | Browser checking permissions before sending a request. |

> **Important Note:** HTTP methods only describe the *intended* action. The actual behavior depends on how the developer coded the server.

---

## 5. Important HTTP Headers

Headers are like **sticky notes attached to an envelope**. They carry extra details about the request or response without being part of the main content.

| Header | Who Sends It? | Plain-English Purpose |
| :--- | :--- | :--- |
| **Host** | Client | Specifies the website domain being requested. |
| **User-Agent** | Client | Identifies the browser, app, or device making the request. |
| **Accept** | Client | Lists the data formats the client can understand (e.g., HTML, JSON). |
| **Content-Type** | Client or Server | States the exact format of the data inside the body (e.g., `application/json`). |
| **Authorization** | Client | Carries login proof, such as a token or API key. |
| **Cookie** | Client | Sends saved cookies back to the server so it remembers you. |
| **Set-Cookie** | Server | Tells the browser to save a new cookie. |
| **Origin** | Client | Shows which website/domain started the request (used for security checks). |
| **Referer** | Client | Shows the exact previous page URL that linked to this request. |

---

## 6. HTTP Status Codes

Status codes are 3-digit shortcuts that tell you what happened with your request.

> **Quick Memory Trick:**
> - **2xx** = **Success** ("Here you go!")
> - **3xx** = **Redirect** ("Go look over there.")
> - **4xx** = **Client Error** ("You messed up.")
> - **5xx** = **Server Error** ("I messed up.")

### 2xx – Success
- **`200 OK`** – Everything worked and here is your response.
- **`201 Created`** – Your request succeeded and a brand-new resource was created (common after a `POST`).
- **`204 No Content`** – It worked, and there is no data to send back (common after a `DELETE`).

### 3xx – Redirection
- **`301 Moved Permanently`** – This page has moved to a new URL forever; update your bookmarks.
- **`302 Found`** – This page is temporarily at a different URL.
- **`304 Not Modified`** – Nothing changed since you last loaded this; just use your saved local copy (cache).

### 4xx – Client Errors
- **`400 Bad Request`** – The server couldn't understand your request (usually bad syntax or missing fields).
- **`401 Unauthorized`** – You are not logged in (authentication is missing or invalid).
- **`403 Forbidden`** – The server knows who you are, but you don't have permission to access this.
- **`404 Not Found`** – The requested page or resource does not exist.
- **`405 Method Not Allowed`** – You used the wrong HTTP method (e.g., sending `DELETE` to a URL that only accepts `GET`).
- **`429 Too Many Requests`** – Slow down! You hit the rate limit.

### 5xx – Server Errors
- **`500 Internal Server Error`** – Something crashed or broke inside the server's code.
- **`502 Bad Gateway`** – A server acting as a middleman received a broken response from an upstream server.
- **`503 Service Unavailable`** – The server is overloaded or down for maintenance right now.
- **`504 Gateway Timeout`** – A middleman server waited too long for another server to reply and gave up.

---

## 7. Cookies

HTTP is **stateless**, meaning the server has a short memory—it treats every request as if it came from a total stranger.

A **cookie** is a small piece of text that a server asks your browser to save. Every time your browser visits that website again, it automatically attaches the cookie to the request so the server recognizes you (like a wristband at an amusement park).

### Example
```http
Set-Cookie: sessionid=abc123; HttpOnly; Secure; SameSite=Lax
```

### Important Cookie Attributes
- **`HttpOnly`** – Blocks JavaScript (`document.cookie`) from reading the cookie. Even if a hacker injects malicious JavaScript into a page, they can't grab this cookie.
- **`Secure`** – Forces the browser to send the cookie **only over encrypted HTTPS connections**, never over plain HTTP.
- **`SameSite`** – Controls whether the cookie is sent when a request comes from a different website (helps stop cross-site attacks like CSRF).
- **`Expires` / `Max-Age`** – Sets how long the browser should keep the cookie before deleting it automatically.

---

## 8. Sessions

A **session** is how a server keeps track of your visit (like who is logged in or what is in your shopping cart). Instead of storing all your private data in the browser, the server stores it safely on its own side and only hands your browser a **Session ID** (like a coat-check ticket).

### Typical Login & Session Flow
1. **Login:** You enter your username and password.
2. **Create Session:** The server verifies your credentials and creates a session record for you.
3. **Send ID:** The server sends the unique Session ID back to your browser inside a `Set-Cookie` header.
4. **Auto-Send:** On every page you click next, your browser automatically sends that cookie back to the server.
5. **Recognize User:** The server reads the Session ID, looks up your session record, and knows it's still you.

### Key Session Security Risks
- **Session Hijacking:** An attacker steals your active Session ID and uses it to impersonate you without needing your password.
- **Session Fixation:** An attacker forces or tricks you into using a Session ID *they already know* before you log in. Once you log in, that ID becomes authenticated, and the attacker gets right into your account.
- **Session Expiration:** If sessions never expire, a stolen or forgotten session stays valid forever. Sessions should automatically time out after inactivity and be destroyed on logout.
- **Cookie Theft:** Attackers stealing session cookies—most commonly through malicious scripts on a page (XSS) or by snooping on unencrypted public Wi-Fi.
- **Missing Security Flags:** Forgetting `HttpOnly`, `Secure`, or `SameSite` leaves session cookies exposed to JavaScript theft, unencrypted network interception, and cross-site attacks.

import requests

s = requests.Session()
s.headers.update({"User-Agent": "HTTP-Inspector/1.0"})

r = s.get("https://httpbin.org/get", params={"test": "1"})

print("=== REQUEST SENT ===")
print(r.request.method, r.request.url)
for k, v in r.request.headers.items():
    print(f"{k}: {v}")

print("\n=== RESPONSE RECEIVED ===")
print("Status:", r.status_code, r.reason)
print("Content-Type:", r.headers.get("Content-Type"))
print("Raw Text (first 120 chars):", r.text[:120])
print("Parsed JSON keys:", list(r.json().keys()))

print("\n=== COOKIES & SESSION ===")
s.get("https://httpbin.org/cookies/set/sessionid/xyz789")
r2 = s.get("https://httpbin.org/cookies")
print("Session cookies:", r2.json()["cookies"])
