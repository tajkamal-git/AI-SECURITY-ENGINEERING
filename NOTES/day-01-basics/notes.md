A **function** in Python is a reusable block of code that performs one specific job.
---

## 1. Core Concepts Explained

### Function Definition (`def`)

To create a function, you use the keyword `def` 

```python
def check_port():
    print("Scanning port...")

```

Writing `def` only **creates** the tool—it does not run it yet. To run it, you have to **call** it by name: `check_port()`.

### Parameters vs. Arguments

People often mix these two up, so use this quick memory trick:

* **P**arameter = **P**laceholder (the variable name inside the `def` line).
* **A**rgument = **A**ctual value (the real data you pass in when you call the function).

```python
def scan_ip(ip_address):  # ip_address is the PARAMETER (placeholder)
    print("Scanning:", ip_address)

scan_ip("192.168.1.1")    # "192.168.1.1" is the ARGUMENT (actual value)

```

### Return Values (`return` vs. `print`)

* **`print()`** only displays text on your screen for humans to read. The rest of your program cannot use that result.
* **`return`** hands the result **back** to your program so you can store it in a variable, make decisions with it (`if/else`), or pass it to another function.

```python
def is_admin(role):
    return role == "admin"  # Sends True or False back to the program

access = is_admin("guest")  # access now holds the value False

```

Once Python hits a `return` statement, the function immediately stops running.

### Default Arguments

You can give a parameter a fallback value. If the caller doesn't provide an argument, Python automatically uses the default.

```python
def connect(host, port=443):  # port defaults to 443 (HTTPS)
    print(f"Connecting to {host} on port {port}")

connect("example.com")        # Uses default -> port 443
connect("example.com", 8080)  # Overrides default -> port 8080

```

*Rule:* Parameters with default values must always come **after** parameters without default values.

### Keyword Arguments

Normally, Python matches arguments by their **position** 
def display_request(method, url):
    print("Method:", method)
    print("URL:", url)

# Keyword arguments (order doesn't matter, and it's easier to read)
display_request(url="/login", method="POST")

```

### Reusable Functions

A reusable function does **one small, clear job** and doesn't hardcode specific data inside it. Instead of writing separate functions for `validate_get()`, `validate_post()`, and `validate_delete()`, you write one `validate_method(method)` function that handles any input you throw at it.

---

## 2. Line-by-Line Breakdown of Your Practice Code

First, here is your practice code properly formatted with indentation (Python relies on indentation to know what is inside a function):

```python
def validate_method(method):
    allowed_methods = ["GET", "POST", "PUT", "DELETE"]
    return method.upper() in allowed_methods

def calculate_length(data):
    return len(data)

def display_request(method, url):
    print("Method:", method)
    print("URL:", url)

print(validate_method("GET"))
print(calculate_length("security"))
display_request("POST", "/login")

```


## 3. The Security Engineering Connection

In security engineering, functions are how you build **centralized, consistent defenses**:

* **Single Source of Truth:** Suppose your web app checks HTTP methods in 50 different places. If you decide to block `DELETE` requests later, you only edit `allowed_methods` inside `validate_method()` once—and all 50 places are instantly updated.
* **Fewer Mistakes:** Copy-pasting security checks leads to human error (like forgetting `.upper()` in one spot, which an attacker could exploit). Wrapping the logic in a tested function eliminates that risk.
* **Chaining Defenses:** Because `validate_method()` and `calculate_length()` **return** values instead of just printing them, you can combine them into real security rules:

```python
if validate_method("POST") and calculate_length("my_payload") < 1000:
    print("Request accepted")
else:
    print("Request blocked")

```

A **dictionary** in Python is a collection of data stored as **labeled pairs**. Think of it like a **contact list** on your phone: you don't look up someone's number by saying "give me the 4th contact"—you look it up by their **name** (the key) to get their **phone number** (the value).

---

## 1. Core Concepts Explained

### Key-Value Pairs

Dictionaries use curly braces `{}`. Inside, every item has a **key** (the label) and a **value** (the data), separated by a colon `:`.

```python
user = {
    "username": "admin",
    "role": "superuser",
    "failed_logins": 0
}

```

* **Keys must be unique.** You can't have two `"username"` keys in the same dictionary.
* **Values can be anything:** strings, numbers, lists, booleans, or even other dictionaries.

### Accessing Values (`[]`)

To grab a value, put its key inside square brackets `[]`.

```python
print(user["username"])  # Output: admin

```

**The catch:** If you ask for a key that doesn't exist—like `user["email"]`—Python will immediately crash with a `KeyError`.

### Adding and Updating Values

Python uses the exact same syntax for both adding and updating:

* If the key **doesn't exist yet**, Python **adds** it.
* If the key **already exists**, Python **overwrites** its value.

```python
user["ip_address"] = "10.0.0.5"  # Adds a brand-new key-value pair
user["failed_logins"] = 3        # Updates the existing value from 0 to 3

```

### `get()` and `get()` with Default Values

Because `[]` crashes your program when a key is missing, security engineers prefer `.get()`.

* **Without a default:** If the key is missing, `.get()` safely returns `None` instead of crashing.
* **With a default:** You can pass a second argument as a fallback value if the key isn't found.

```python
# Safe lookup (no crash)
print(user.get("email"))                    # Output: None

# Safe lookup with a fallback default
print(user.get("role", "guest"))            # Output: superuser (key exists)
print(user.get("mfa_enabled", False))       # Output: False (key missing, uses default)

```

### `keys()`, `values()`, and `items()`

These three built-in methods let you inspect or loop through a dictionary:

* **`.keys()`** — gives you all the labels (`"username"`, `"role"`, `"failed_logins"`).
* **`.values()`** — gives you all the data (`"admin"`, `"superuser"`, `0`).
* **`.items()`** — gives you **both** together as `(key, value)` pairs. This is the most common way to loop through a dictionary.

```python
for key, value in user.items():
    print(f"{key} -> {value}")

```

### Nested Dictionaries

A **nested dictionary** is simply a dictionary stored *inside* another dictionary—just like having a folder inside another folder. To reach the inner data, you chain your lookups from the outside in:

```python
# Outer key ["headers"], then inner key ["User-Agent"]
request["headers"]["User-Agent"]

```

---

## 2. Line-by-Line Breakdown of Your Practice Code

Here is your practice code formatted properly so you can see the nested structure clearly:

```python
request = {
    "method": "POST",
    "url": "/login",
    "headers": {
        "Content-Type": "application/json",
        "User-Agent": "Python Client"
    },
    "body": {
        "username": "admin",
        "password": "test123"
    }
}

print(request["method"])
print(request.get("url"))
print(request["headers"].get("Content-Type"))

for key, value in request.items():
    print(key, value)

```

## 3. The Security Engineering Connection

Almost every piece of structured data you will touch in security engineering is either a Python dictionary or **JSON** (which converts directly into a Python dictionary):

* **HTTP Requests & API Responses:** Headers, query parameters, and JSON payloads are all key-value pairs.
* **Security Logs (SIEM / Sysmon / CloudTrail):** A single security alert is a nested dictionary containing timestamps, source IPs, user accounts, and process details.
* **Defensive Coding with `.get()`:** Attackers constantly send malformed or incomplete requests (for example, stripping out the `User-Agent` or `Authorization` header). If your security script uses `request["headers"]["Authorization"]`, an attacker can crash your tool with a `KeyError`. Using `.get()` keeps your defense running smoothly:

```python
# Safely check for an Authorization header without crashing
auth_header = request.get("headers", {}).get("Authorization", "Missing")

if auth_header == "Missing":
    print("Alert: Unauthenticated request blocked!")

```

Notice that chaining `.get("headers", {})` with an empty dictionary `{}` as the default ensures that even if the entire `"headers"` section is missing, the second `.get()` still won't crash.

**JSON** (JavaScript Object Notation) is a universal, text-based format for storing and sending data. A Python dictionary only exists inside Python's memory—if you want to send that data over the internet to an API or save it to a log file, you convert it into JSON text first.

---

## 1. Python vs. JSON Data Types

When Python converts data to JSON (and back), it automatically translates the data types:

| Python | JSON | What Changes? |
| --- | --- | --- |
| **Dictionary** (`{"a": 1}`) | **Object** (`{"a": 1}`) | JSON strictly requires **double quotes** `""` for keys and strings (single quotes `''` are invalid). |
| **List** (`[1, 2]`) | **Array** (`[1, 2]`) | Looks identical. |
| **String** (`'hi'` or `"hi"`) | **String** (`"hi"`) | Always converted to double quotes. |
| **Integer / Float** (`200`) | **Number** (`200`) | Looks identical. |
| **Boolean** (`True` / `False`) | **Boolean** (`true` / `false`) | Capitalized in Python, **lowercase** in JSON. |
| **`None`** | **`null`** | Python's empty value becomes `null` in JSON. |

---

## 2. The Four Core JSON Functions

Almost everyone confuses these four at first. Use this simple memory trick:

* **`dump`** = Python $\rightarrow$ JSON (packing data up to send or save).
* **`load`** = JSON $\rightarrow$ Python (unpacking data so Python can use it).
* The letter **`s`** at the end = **String** (working in memory). No `s` = **File** (working on your hard drive).

| Function | Direction | Works With | When to Use It |
| --- | --- | --- | --- |
| **`json.dumps()`** | Python $\rightarrow$ JSON | **S**tring | Preparing a dictionary to send in an HTTP/API request or print as text. |
| **`json.loads()`** | JSON $\rightarrow$ Python | **S**tring | Turning a raw JSON response from an API into a Python dictionary you can inspect. |
| **`json.dump()`** | Python $\rightarrow$ JSON | **File** | Saving a dictionary directly into a `.json` file (like saving a scan report). |
| **`json.load()`** | JSON $\rightarrow$ Python | **File** | Reading a `.json` file from disk (like loading a config file or saved logs). |

### Quick Example of File Functions (`dump` and `load`)

Since your practice snippet only shows `dumps` and `loads`, here is how the file versions look:

```python
import json

alert = {"event": "failed_login", "ip": "192.168.1.50", "blocked": True}

# Save Python dict directly to a file (dump)
with open("alert.json", "w") as file:
    json.dump(alert, file, indent=4)

# Read JSON file directly into a Python dict (load)
with open("alert.json", "r") as file:
    loaded_alert = json.load(file)

print(loaded_alert["ip"])  # Output: 192.168.1.50

```

---

## 3. Line-by-Line Breakdown of Your Practice Code

Here is your practice code properly formatted:

```python
import json

request = {
    "method": "GET",
    "url": "/users",
    "status": 200
}

# Python dictionary to JSON
json_data = json.dumps(request, indent=4)
print(json_data)

# JSON to Python dictionary
parsed_data = json.loads(json_data)
print(parsed_data["method"])

```

### What Each Part Does

1. **`import json`**: Loads Python's built-in JSON library (no extra installation needed).
2. **`request = { ... }`**: Creates a normal Python dictionary.
3. **`json_data = json.dumps(request, indent=4)`**:
* Converts the `request` dictionary into a **JSON string**.
* `indent=4` adds 4 spaces of indentation and line breaks so it's readable for humans ("pretty-printing"). Without `indent=4`, it prints everything mashed onto one single line.
* **Important:** `json_data` is now just plain text (`str`). You **cannot** do `json_data["method"]` on it anymore.


4. **`parsed_data = json.loads(json_data)`**:
* Takes that JSON text string and converts it **back** into a usable Python dictionary.


5. **`print(parsed_data["method"])`**:
* Because `parsed_data` is a Python dictionary again, you can access `"method"` by its key.



### Output on Screen

```text
{
    "method": "GET",
    "url": "/users",
    "status": 200
}
GET

```

---

## 4. The Security Engineering Connection

JSON is the backbone of modern security tooling:

* **API Testing & Automation:** When you interact with REST APIs (like VirusTotal, Shodan, or Splunk's REST API), you send payloads with `json.dumps()` and parse the returned threat intelligence with `json.loads()`.
* **Log Analysis:** Cloud logs (AWS CloudTrail, Azure) and security tools (Suricata, Sysmon exports) store alerts as JSON files. You use `json.load()` to ingest them and hunt for suspicious activity.
* **Defensive Tip — Never Trust Incoming JSON:** Attackers often send broken or malformed JSON to crash your server or security script. Always wrap `json.loads()` in a `try/except` block when handling untrusted data:

```python
import json

bad_payload = '{"username": "admin", '  # Broken JSON from an attacker


**HTTP** (Hypertext Transfer Protocol) is the language clients (browsers, mobile apps, Python scripts) and servers use to talk to each other. Everything you just learned in Hour 1—Python dictionaries and JSON—maps directly to HTTP: an HTTP request is essentially a structured message with labeled metadata (headers) and a data payload (body).

---

## 1. Anatomy of an HTTP Request
<img width="540" height="322" alt="image" src="https://github.com/user-attachments/assets/61c6e419-d2bd-4f5f-b097-8714ded92838" />

Here is your example request, broken down piece by piece:

```http
POST /login HTTP/1.1
Host: example.com
Content-Type: application/json
User-Agent: Python Client

{
  "username": "admin",
  "password": "example"
}

```

### The Request Line (Line 1)

* **`POST` (HTTP Method):** Tells the server *what action* you want to perform. Here, you are submitting login data.
* **`/login` (Request Path / Endpoint):** The specific door or resource on the server you are knocking on.
* **`HTTP/1.1` (Protocol Version):** The version of HTTP rules being used (1.1 is text-based and the easiest to read when debugging or intercepting traffic in tools like Burp Suite).

### The Headers (Lines 2–4)

Headers are key-value pairs—just like a Python dictionary—that describe the request:

* **`Host: example.com`:** Specifies which domain/server should handle the request. One physical server often hosts multiple websites, so this tells it which one you want.
* **`Content-Type: application/json`:** Tells the server how to read the body. Here, it warns the server: *"Expect JSON data."*
* **`User-Agent: Python Client`:** Identifies the software making the request (e.g., Chrome, curl, or your Python script).
* *Security note:* Never trust `User-Agent` for security decisions—anyone can fake it in one line of code.



### The Blank Line & Request Body

* **Blank Line (CRLF):** A mandatory empty line that separates the headers from the body.
* **Request Body:** The actual data being sent to the application—in this case, a JSON object containing the `username` and `password`.

---

## 2. HTTP Methods (The Verbs)

HTTP methods tell the server what you want to do with a resource. Think of them like actions on a database:

| Method | Meaning | Real-World Example | Security Engineering Angle |
| --- | --- | --- | --- |
| **`GET`** | Retrieve information | Loading a user profile (`/users/42`) | Data goes in the URL, which gets saved in browser history and server logs. **Never send passwords or tokens in a `GET` request.** |
| **`POST`** | Submit new information | Logging in (`/login`) or creating an account | Sends data in the request body. Always validate and sanitize the body to prevent injection attacks. |
| **`PUT`** | Replace an entire resource | Overwriting a user's entire profile object | If access controls are weak, attackers can use `PUT` to overwrite files or elevate privileges. |
| **`PATCH`** | Update *part* of a resource | Changing only a user's email address | Check which fields are allowed to be updated—otherwise attackers can sneak in `"role": "admin"` (Mass Assignment). |
| **`DELETE`** | Delete a resource | Removing a post (`/posts/99`) | High-risk action. Always verify the requester actually owns the resource before deleting it (prevents IDOR). |

---

## 3. Headers & Cookies

* **Headers:** Extra metadata attached to both requests and responses. In security, headers carry critical items like `Authorization` tokens, API keys, and security policies (such as `Content-Security-Policy`).
* **Cookies:** Small pieces of data stored by the browser and automatically sent back to the server with every future request.
* **Why they exist:** HTTP is **stateless**—the server forgets who you are the second a request finishes. When you log in, the server hands you a **session cookie** (like a wristband at a concert) so you don't have to re-enter your password on every page.
* **Security angle:** If an attacker steals your session cookie, they become you. Security engineers protect cookies with flags like `HttpOnly` (blocks JavaScript from reading them) and `Secure` (only sends them over HTTPS).



---

## 4. HTTP Status Codes (The Server's Reply)

Every time a client sends a request, the server replies with a 3-digit **status code**. The first digit tells you the general category:

* **2xx** = Success
* **3xx** = Redirection
* **4xx** = Client Error (you/the requester did something wrong)
* **5xx** = Server Error (the server broke)

| Code | Name | What It Means | Security Engineering Context |
| --- | --- | --- | --- |
| **`200`** | **OK** | Request succeeded and returned data. | Normal response. Watch out if a restricted endpoint returns `200` without authentication. |
| **`201`** | **Created** | A new resource was successfully created (usually after `POST`). | Confirms account creation, new record insertion, or file upload. |
| **`301`** | **Moved Permanently** | Resource moved to a new URL; browser redirects automatically. | Commonly used to redirect insecure `http://` traffic to `https://`. |
| **`400`** | **Bad Request** | The server couldn't understand your request (e.g., broken JSON). | Good sign when testing input validation—means the server rejected malformed payloads. |
| **`401`** | **Unauthorized** | **Who are you?** Missing or invalid login credentials/token. | Authentication failed. The user needs to log in first. |
| **`403`** | **Forbidden** | **I know who you are, but no.** Authenticated, but lacking permission. | Authorization failed (e.g., a regular user trying to access `/admin`). |
| **`404`** | **Not Found** | The requested path or resource doesn't exist. | Attackers scan for `200` vs `404` to discover hidden endpoints (directory enumeration). |
| **`500`** | **Internal Server Error** | Something crashed inside the server's code. | **Red flag in security:** Often means an attacker's weird input triggered an unhandled exception or potential vulnerability. |

> **Classic Interview Distinction — `401` vs. `403`:**
> * **`401 Unauthorized`** = You don't have a valid ID badge.
> * **`403 Forbidden`** = Your ID badge is valid, but it doesn't open the server room door.
> 
> 

---

## Interactive Lab: Test How Requests Trigger Status Codes

Use the interactive simulator below to change the **HTTP method**, **authentication/cookie state**, and **request body**, and watch how the server's validation logic produces different status codes in real time:



try:
    data = json.loads(bad_payload)
except json.JSONDecodeError:
    print("Alert: Malformed JSON payload blocked!")

```[Uploading interactive_visual_im_7f```html
<!DOCTYPE html>
<html lang="en">
<head>
<script id="artifact-state-bridge">
(function() {
'use strict';
if (window.pageVault) {
  return;
}
// Single-reporter guard: the generic form-snapshot script checks this flag and
// stays inert.
window.__GEMINI_STATE_PRESERVER_INSTALLED__ = true;

const MAX_BYTES = 64 * 1024;
const POST_INTERVAL_MS = 100;
const ECHO_MEMORY = 8;

let map = {};
let hostSeed = {};
let isReady = false;
let resolveReady = null;
const readyPromise = new Promise(function(r) {
  resolveReady = r;
});
let queued = [];
const pending = {};
const restoreCallbacks = [];
const recentReports = [];
let postTimer = null;
let postDue = false;
// Write gate. Becomes true on the first trusted user input in this frame.
// Until then nothing is posted to the host.
let userActivated = false;

function hasOwn(o, k) {
  return Object.prototype.hasOwnProperty.call(o, k);
}
function isPlainObject(v) {
  return v !== null && typeof v === 'object' && !Array.isArray(v);
}
function clone(v) {
  return v === undefined ? undefined : JSON.parse(JSON.stringify(v));
}
function makeError(code, msg) {
  const e = new Error('pageVault: ' + msg);
  e.code = code;
  return e;
}
function byteLength(s) {
  if (typeof TextEncoder === 'function') {
    return new TextEncoder().encode(s).length;
  }
  return s.length;
}
function deepEqual(a, b) {
  if (a === b) {
    return true;
  }
  if (a === null || b === null || typeof a !== 'object' ||
      typeof b !== 'object') {
    return false;
  }
  const aArr = Array.isArray(a), bArr = Array.isArray(b);
  if (aArr !== bArr) {
    return false;
  }
  if (aArr) {
    if (a.length !== b.length) {
      return false;
    }
    for (let i = 0; i < a.length; i++) {
      if (!deepEqual(a[i], b[i])) {
        return false;
      }
    }
    return true;
  }
  const ka = Object.keys(a), kb = Object.keys(b);
  if (ka.length !== kb.length) {
    return false;
  }
  for (let j = 0; j < ka.length; j++) {
    if (!hasOwn(b, ka[j]) || !deepEqual(a[ka[j]], b[ka[j]])) {
      return false;
    }
  }
  return true;
}

function toSeedMap(raw) {
  if (raw === undefined || raw === null) {
    return null;
  }
  if (typeof raw === 'string') {
    if (raw.trim() === '') {
      return {};
    }
    try {
      raw = JSON.parse(raw);
    } catch (e) {
      return {};
    }
  }
  if (!isPlainObject(raw)) {
    return {};
  }
  try {
    return JSON.parse(JSON.stringify(raw));
  } catch (e) {
    return {};
  }
}
function unwrapSnapshotEnvelope(seed) {
  if (seed && seed.version === 1 && isPlainObject(seed.forms) &&
      isPlainObject(seed.scroll) && hasOwn(seed, 'custom')) {
    return isPlainObject(seed.custom) ? seed.custom : {};
  }
  return seed;
}
function takeSeed(raw) {
  const seed = toSeedMap(raw);
  if (seed === null) {
    return;
  }
  applySeed(
      unwrapSnapshotEnvelope(seed), typeof raw === 'string' ? raw : undefined);
}
function clearConfirmedPending(seed) {
  const keys = Object.keys(pending);
  for (let i = 0; i < keys.length; i++) {
    const k = keys[i];
    if (pending[k].removed) {
      if (!hasOwn(seed, k)) {
        delete pending[k];
      }
    } else if (hasOwn(seed, k) && deepEqual(pending[k].value, seed[k])) {
      delete pending[k];
    }
  }
}
function applySeed(seed, rawString) {
  if (!isReady) {
    map = seed;
    hostSeed = clone(seed);
    isReady = true;
    drainQueue(Object.keys(seed));
    resolveReady();
    return;
  }
  if (rawString !== undefined && recentReports.indexOf(rawString) !== -1) {
    hostSeed = clone(seed);
    clearConfirmedPending(seed);
    return;
  }
  if (deepEqual(seed, hostSeed)) {
    clearConfirmedPending(seed);
    if (userActivated && Object.keys(pending).length > 0) {
      schedulePost();
    }
    return;
  }
  const next = {}, changed = [];
  let k, i;
  const seedKeys = Object.keys(seed);
  for (i = 0; i < seedKeys.length; i++) {
    k = seedKeys[i];
    if (hasOwn(pending, k)) {
      if (pending[k].removed) {
        continue;
      }
      next[k] = map[k];
      if (deepEqual(pending[k].value, seed[k])) {
        delete pending[k];
      }
    } else if (hasOwn(hostSeed, k) && deepEqual(hostSeed[k], seed[k])) {
      next[k] = hasOwn(map, k) ? map[k] : seed[k];
    } else {
      next[k] = seed[k];
      if (!hasOwn(map, k) || !deepEqual(map[k], seed[k])) {
        changed.push(k);
      }
    }
  }
  const mapKeys = Object.keys(map);
  for (i = 0; i < mapKeys.length; i++) {
    k = mapKeys[i];
    if (hasOwn(next, k) || hasOwn(seed, k)) {
      continue;
    }
    if ((hasOwn(pending, k) && !pending[k].removed) || !hasOwn(hostSeed, k)) {
      next[k] = map[k];
    } else {
      changed.push(k);
    }
  }
  const pk = Object.keys(pending);
  for (i = 0; i < pk.length; i++) {
    if (pending[pk[i]].removed && !hasOwn(seed, pk[i])) {
      delete pending[pk[i]];
    }
  }
  hostSeed = clone(seed);
  if (userActivated && Object.keys(pending).length > 0) {
    schedulePost();
  }
  if (changed.length === 0) {
    return;
  }
  map = next;
  changed.sort();
  const cbs = restoreCallbacks.slice();
  for (i = 0; i < cbs.length; i++) {
    try {
      cbs[i](changed.slice());
    } catch (e) {
      console.warn('pageVault: onRestore callback failed', e);
    }
  }
}

function normalizeValue(value) {
  let text;
  try {
    text = JSON.stringify(value);
  } catch (e) {
    text = undefined;
  }
  if (typeof text !== 'string') {
    return {
      ok: false,
      error: makeError('NOT_SERIALIZABLE', 'value is not JSON-serializable')
    };
  }
  return {ok: true, value: JSON.parse(text)};
}
function applySave(key, value) {
  if (hasOwn(map, key) && deepEqual(map[key], value)) {
    if (userActivated &&
        (!hasOwn(hostSeed, key) || !deepEqual(hostSeed[key], value)) &&
        !(hasOwn(pending, key) && !pending[key].removed &&
          deepEqual(pending[key].value, value))) {
      trackEdit(key, {value: clone(value)});
    }
    return clone(value);
  }
  const next = Object.assign({}, map);
  next[key] = value;
  if (byteLength(JSON.stringify(next)) > MAX_BYTES) {
    throw makeError('TOO_LARGE', 'saved data would exceed 64 KB');
  }
  map = next;
  trackEdit(key, {value: clone(value)});
  return clone(value);
}
function applyRemove(key) {
  if (!hasOwn(map, key)) {
    if (userActivated && hasOwn(hostSeed, key) &&
        !(hasOwn(pending, key) && pending[key].removed)) {
      trackEdit(key, {removed: true});
    }
    return false;
  }
  const next = Object.assign({}, map);
  delete next[key];
  map = next;
  trackEdit(key, {removed: true});
  return true;
}
// Marks a local edit as pending and schedules a post. Before the first
// trusted user input an edit only changes `map`: it is not pending, so a seed
// that arrives later replaces it and onRestore reports the key.
function trackEdit(key, entry) {
  if (!userActivated) {
    return;
  }
  pending[key] = entry;
  schedulePost();
}
function drainQueue(seededKeys) {
  const ops = queued;
  queued = [];
  for (let i = 0; i < ops.length; i++) {
    const op = ops[i];
    try {
      if (op.op === 'save') {
        if (seededKeys.indexOf(op.key) !== -1) {
          op.resolve(clone(map[op.key]));
        } else {
          op.resolve(applySave(op.key, op.value));
        }
      } else {
        if (seededKeys.indexOf(op.key) !== -1) {
          op.resolve(false);
        } else {
          op.resolve(applyRemove(op.key));
        }
      }
    } catch (e) {
      op.reject(e);
    }
  }
}

function schedulePost() {
  if (!isReady) {
    return;
  }
  postDue = true;
  if (postTimer !== null) {
    return;
  }
  postTimer = setTimeout(flush, POST_INTERVAL_MS);
}
function flush() {
  if (postTimer !== null) {
    clearTimeout(postTimer);
    postTimer = null;
  }
  if (!postDue || !isReady || !userActivated) {
    return;
  }
  postDue = false;
  let payload;
  try {
    payload = JSON.stringify(map);
  } catch (e) {
    return;
  }
  recentReports.push(payload);
  if (recentReports.length > ECHO_MEMORY) {
    recentReports.shift();
  }
  try {
    window.parent.postMessage(
        {
          'type': 'WIDGET_STATE_UPDATE',
          'widgetType': 'artifact',
          'payload': payload
        },
        '*');
  } catch (e) { /* host unreachable: keep the in-memory session */
  }
}
window.addEventListener('pagehide', flush);
window.addEventListener('blur', flush);
if (typeof document !== 'undefined' && document.addEventListener) {
  document.addEventListener('visibilitychange', function() {
    if (document.visibilityState === 'hidden') {
      flush();
    }
  });
}

// The write gate opens on the first trusted pointer, touch, key, wheel,
// clipboard, form input or drop event in this frame, so startup code,
// onRestore callbacks and in-memory migrations cannot post on their own.
// Capture-phase listeners on `window` run before the page's handlers, so a
// save made while handling that same input is posted. Opening the gate posts
// nothing by itself: the next save posts the whole map, including earlier
// in-memory edits.
const USER_INPUT_EVENTS = [
  'pointerdown', 'mousedown', 'touchstart', 'keydown', 'input', 'change',
  'click', 'paste', 'cut', 'drop', 'wheel'
];
function onUserInput(event) {
  if (!event.isTrusted) {
    return;
  }
  userActivated = true;
  for (let i = 0; i < USER_INPUT_EVENTS.length; i++) {
    window.removeEventListener(USER_INPUT_EVENTS[i], onUserInput, true);
  }
}
for (let i = 0; i < USER_INPUT_EVENTS.length; i++) {
  window.addEventListener(
      USER_INPUT_EVENTS[i], onUserInput, {capture: true, passive: true});
}

window.addEventListener('message', function(event) {
  if (event.source !== window.parent) {
    return;
  }
  const d = event.data;
  if (!d || typeof d !== 'object') {
    return;
  }
  if (d.type === 'SUPPLEMENTAL_DATA_UPDATE') {
    takeSeed(d.data);
  } else if (d.type === 'RESTORE_STATE') {
    takeSeed(d.state);
  }
});
window.__onRestoreState = function(state) {
  takeSeed(state);
};
window.__getWidgetState = function() {
  return clone(map);
};

const api = {
  ready: readyPromise,
  load: function(key) {
    return readyPromise.then(function() {
      return (typeof key === 'string' && hasOwn(map, key)) ? clone(map[key]) :
                                                             undefined;
    });
  },
  save: function(key, value) {
    if (typeof key !== 'string' || key === '') {
      return Promise.reject(
          makeError('INVALID_KEY', 'key must be a non-empty string'));
    }
    const n = normalizeValue(value);
    if (!n.ok) {
      return Promise.reject(n.error);
    }
    if (!isReady) {
      return new Promise(function(resolve, reject) {
        queued.push({
          op: 'save',
          key: key,
          value: n.value,
          resolve: resolve,
          reject: reject
        });
      });
    }
    try {
      return Promise.resolve(applySave(key, n.value));
    } catch (e) {
      return Promise.reject(e);
    }
  },
  remove: function(key) {
    if (typeof key !== 'string') {
      return Promise.resolve(false);
    }
    if (!isReady) {
      return new Promise(function(resolve, reject) {
        queued.push({op: 'remove', key: key, resolve: resolve, reject: reject});
      });
    }
    return Promise.resolve(applyRemove(key));
  },
  keys: function() {
    return readyPromise.then(function() {
      return Object.keys(map);
    });
  },
  onRestore: function(cb) {
    if (typeof cb !== 'function') {
      return function() {};
    }
    restoreCallbacks.push(cb);
    return function() {
      const i = restoreCallbacks.indexOf(cb);
      if (i !== -1) {
        restoreCallbacks.splice(i, 1);
      }
    };
  }
};
Object.freeze(api);
window.pageVault = api;

// `ready` resolves right away, so the page never waits on the host. A host
// that embeds the saved data before this script runs hands it over through
// `window.__artifact_seed`. Without an embedded seed the page starts from an
// empty session. Saved data that the host delivers later (through
// SUPPLEMENTAL_DATA_UPDATE or RESTORE_STATE) still arrives: applySeed merges
// it, keeps the keys the page has written since the first user input, and
// reports the changed keys through onRestore.
const embeddedSeed = window.__artifact_seed;
if (embeddedSeed !== undefined && embeddedSeed !== null) {
  takeSeed(embeddedSeed);
} else {
  takeSeed({});
}
})();

</script>
<script id="lumi-getcssvar">
window.getCssVar = window.getCssVar || function(name, fallback) {
  try {
    var v = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
    return v || fallback || '';
  } catch (e) { return fallback || ''; }
};
</script>

<style id="lumi-runtime">
/* luminous.css */
/*
 * Luminous runtime stylesheet — injected once into every generated widget's
 * <head> by the C++ widget agent (id="lumi-runtime"). Single Source of Truth
 * for ALL design tokens and pre-baked .lumi-* component classes. The SI prompts
 * (design.md / html_generation.jinja2 / chart.jinja2) must NOT re-declare these
 * tokens or component CSS; they only reference them.
 *
 * Sections:
 *   1. Web fonts (Google Sans Flex + Google Sans Code)
 *   2. Light token :root (from previewer tokens.css, verbatim)
 *   3. Dark token overrides — REMAPPED to :root so canvas/D3 readers of
 *      getComputedStyle(document.documentElement) resolve dark values (D3).
 *   4. Short diagram/chart aliases (bridge legacy --surface / --chart-N names).
 *   5. In-scope pre-baked .lumi-* component classes.
 */

/* ============================================================
 * 1. WEB FONTS & ICONOGRAPHY
 *    Loads Google Sans Flex, Google Sans Code, and Material Symbols Outlined.
 *    Enforces the dual-class iconography rendering protocol.
 * ============================================================ */
@import url('https://fonts.googleapis.com/css2?family=Google+Sans+Flex:ital,wght@0,300..700;1,300..700&family=Google+Sans+Code:ital,wght,MONO@0,300..700,0..1;1,300..700,0..1&family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&display=swap');

/* Dual-Class Iconography */
.lumi-icon {
  font-family: 'Luminous Symbols', 'Material Symbols Outlined';
  font-weight: normal;
  font-style: normal;
  font-size: 20px;
  line-height: 1;
  letter-spacing: normal;
  text-transform: none;
  display: inline-block;
  white-space: nowrap;
  word-wrap: normal;
  direction: ltr;
  font-feature-settings: 'liga';
  -webkit-font-smoothing: antialiased;
  vertical-align: middle;
}

.material-icon {
  font-family: 'Material Symbols Outlined';
  font-weight: normal;
  font-style: normal;
  font-size: 20px;
  line-height: 1;
  letter-spacing: normal;
  text-transform: none;
  display: inline-block;
  white-space: nowrap;
  word-wrap: normal;
  direction: ltr;
  -webkit-font-smoothing: antialiased;
  vertical-align: middle;
}

/* ============================================================
 * 2. LIGHT TOKENS (:root)
 * ============================================================ */
:root {
  color-scheme: light;
  --body-bg: transparent;
  --ff-sans: 'Google Sans Flex', 'Google Sans Text', 'Google Sans', sans-serif;
  --ff-mono: 'Google Sans Code', 'Google Sans Mono', monospace;

  --lumi-sys-spacing--xxs: 2px;
  --lumi-sys-spacing--xs: 4px;
  --lumi-sys-spacing--s: 8px;
  --lumi-sys-spacing--m: 12px;
  --lumi-sys-spacing--l: 16px;
  --lumi-sys-spacing--xl: 20px;
  --lumi-sys-spacing--xxl: 24px;
  --lumi-sys-spacing--3xl: 28px;
  --lumi-sys-spacing--4xl: 36px;

  --lumi-sys-shape--none: 0px;
  --lumi-sys-shape--extra-small: 4px;
  --lumi-sys-shape--small: 8px;
  --lumi-sys-shape--medium: 12px;
  --lumi-sys-shape--large: 16px;
  --lumi-sys-shape--large-increased: 20px;
  --lumi-sys-shape--large-max: 24px;
  --lumi-sys-shape--xl: 28px;
  --lumi-sys-shape--xl-increased: 32px;
  --lumi-sys-shape--xl-max: 40px;
  --lumi-sys-shape--xxl: 48px;
  --lumi-sys-shape--xxl-increased: 56px;
  --lumi-sys-shape--full: 999px;

  --lumi-sys-elevation--level1: 0 0 20px 0 rgba(0, 0, 0, 0.04);
  --lumi-sys-elevation--level2: 0 0 20px 0 rgba(0, 0, 0, 0.11);

  --lumi-sys-color--surface: #fdfcfc;
  --lumi-sys-color--surface-dim: #f2f0f0;
  --lumi-sys-color--surface-bright: #ffffff;
  --lumi-sys-color--surface-background: #fdfcfc;
  --lumi-sys-color--surface-accent: #9dd2ff;
  --lumi-sys-color--surface-container: #f2f0f0;
  --lumi-sys-color--surface-container-high: #e6e6e6;
  --lumi-sys-color--surface-translucent: rgba(255, 255, 255, 0.88);
  --lumi-sys-color--on-surface: #000000;
  --lumi-sys-color--on-surface-default: #000000;
  --lumi-sys-color--on-surface-variant: rgba(0, 0, 0, 0.62);
  --lumi-sys-color--on-surface-de-emphasis: rgba(0, 0, 0, 0.62);
  --lumi-sys-color--on-surface-low: rgba(0, 0, 0, 0.08);
  --lumi-sys-color--positive: #008052;
  --lumi-sys-color--positive-container: #daf9d4;
  --lumi-sys-color--on-positive-container: #009954;
  --lumi-sys-color--error: #de2d29;
  --lumi-sys-color--error-container: #ffdeec;
  --lumi-sys-color--on-error-container: #de2d29;
  --lumi-sys-color--accent: #9dd2ff;
  --lumi-sys-color--accent-container: #dcf1ff;
  --lumi-sys-color--accent-fixed: #3186ff;
  --lumi-sys-color--primary: #3186ff;
  --lumi-sys-color--on-primary: #ffffff;
  --lumi-sys-color--black: #000000;
  --lumi-sys-color--white: #ffffff;
  --lumi-sys-color--outline: #727676;
  --lumi-sys-color--stroke-default: #e3e3e3;

  /* --- Luminous Typography Tokens: Display (Carbon SSoT) --- */
  --lumi-sys-typography-type-scale--display-l-font-name: 'Google Sans Flex';
  --lumi-sys-typography-type-scale--display-l-font-size: 2.625rem;
  --lumi-sys-typography-type-scale--display-l-line-height: 3rem;
  --lumi-sys-typography-type-scale--display-l-font-tracking: 0rem;
  --lumi-sys-typography-type-scale--display-l-font-weight: 280;
  --lumi-sys-typography-type-scale--display-l-font-wght: 280;
  --lumi-sys-typography-type-scale--display-l-font-width: 100;
  --lumi-sys-typography-type-scale--display-l-font-rond: 100;
  --lumi-sys-typography-type-scale--display-l-opsz: 42;

  --lumi-sys-typography-type-scale--display-m-font-name: 'Google Sans Flex';
  --lumi-sys-typography-type-scale--display-m-font-size: 2.25rem;
  --lumi-sys-typography-type-scale--display-m-line-height: 2.75rem;
  --lumi-sys-typography-type-scale--display-m-font-tracking: 0rem;
  --lumi-sys-typography-type-scale--display-m-font-weight: 320;
  --lumi-sys-typography-type-scale--display-m-font-wght: 320;
  --lumi-sys-typography-type-scale--display-m-font-width: 100;
  --lumi-sys-typography-type-scale--display-m-font-rond: 100;
  --lumi-sys-typography-type-scale--display-m-opsz: 36;

  --lumi-sys-typography-type-scale--display-s-font-name: 'Google Sans Flex';
  --lumi-sys-typography-type-scale--display-s-font-size: 2rem;
  --lumi-sys-typography-type-scale--display-s-line-height: 2.375rem;
  --lumi-sys-typography-type-scale--display-s-font-tracking: 0rem;
  --lumi-sys-typography-type-scale--display-s-font-weight: 360;
  --lumi-sys-typography-type-scale--display-s-font-wght: 360;
  --lumi-sys-typography-type-scale--display-s-font-width: 100;
  --lumi-sys-typography-type-scale--display-s-font-rond: 100;
  --lumi-sys-typography-type-scale--display-s-opsz: 32;

  /* --- Luminous Typography Tokens: Headline (Carbon SSoT) --- */
  --lumi-sys-typography-type-scale--headline-l-font-name: 'Google Sans Flex';
  --lumi-sys-typography-type-scale--headline-l-font-size: 1.75rem;
  --lumi-sys-typography-type-scale--headline-l-line-height: 2.25rem;
  --lumi-sys-typography-type-scale--headline-l-font-tracking: 0rem;
  --lumi-sys-typography-type-scale--headline-l-font-weight: 350;
  --lumi-sys-typography-type-scale--headline-l-font-wght: 350;
  --lumi-sys-typography-type-scale--headline-l-font-width: 100;
  --lumi-sys-typography-type-scale--headline-l-font-rond: 20;
  --lumi-sys-typography-type-scale--headline-l-opsz: 28;

  --lumi-sys-typography-type-scale--headline-m-font-name: 'Google Sans Flex';
  --lumi-sys-typography-type-scale--headline-m-font-size: 1.5rem;
  --lumi-sys-typography-type-scale--headline-m-line-height: 1.75rem;
  --lumi-sys-typography-type-scale--headline-m-font-tracking: 0rem;
  --lumi-sys-typography-type-scale--headline-m-font-weight: 380;
  --lumi-sys-typography-type-scale--headline-m-font-wght: 380;
  --lumi-sys-typography-type-scale--headline-m-font-width: 100;
  --lumi-sys-typography-type-scale--headline-m-font-rond: 20;
  --lumi-sys-typography-type-scale--headline-m-opsz: 24;

  --lumi-sys-typography-type-scale--headline-s-font-name: 'Google Sans Flex';
  --lumi-sys-typography-type-scale--headline-s-font-size: 1.25rem;
  --lumi-sys-typography-type-scale--headline-s-line-height: 1.5rem;
  --lumi-sys-typography-type-scale--headline-s-font-tracking: 0rem;
  --lumi-sys-typography-type-scale--headline-s-font-weight: 470;
  --lumi-sys-typography-type-scale--headline-s-font-wght: 470;
  --lumi-sys-typography-type-scale--headline-s-font-width: 94;
  --lumi-sys-typography-type-scale--headline-s-font-rond: 20;
  --lumi-sys-typography-type-scale--headline-s-opsz: 20;

  /* --- Luminous Typography Tokens: Body (Carbon SSoT) --- */
  --lumi-sys-typography-type-scale--body-l-font-name: 'Google Sans Flex';
  --lumi-sys-typography-type-scale--body-l-font-size: 1.0625rem;
  --lumi-sys-typography-type-scale--body-l-line-height: 1.5rem;
  --lumi-sys-typography-type-scale--body-l-font-tracking: 0rem;
  --lumi-sys-typography-type-scale--body-l-font-weight: 400;
  --lumi-sys-typography-type-scale--body-l-font-wght: 400;
  --lumi-sys-typography-type-scale--body-l-font-width: 92;
  --lumi-sys-typography-type-scale--body-l-font-rond: 0;
  --lumi-sys-typography-type-scale--body-l-opsz: 17;

  --lumi-sys-typography-type-scale--body-m-font-name: 'Google Sans Flex';
  --lumi-sys-typography-type-scale--body-m-font-size: 0.9375rem;
  --lumi-sys-typography-type-scale--body-m-line-height: 1.25rem;
  --lumi-sys-typography-type-scale--body-m-font-tracking: 0rem;
  --lumi-sys-typography-type-scale--body-m-font-weight: 400;
  --lumi-sys-typography-type-scale--body-m-font-wght: 400;
  --lumi-sys-typography-type-scale--body-m-font-width: 92;
  --lumi-sys-typography-type-scale--body-m-font-rond: 0;
  --lumi-sys-typography-type-scale--body-m-opsz: 15;

  --lumi-sys-typography-type-scale--body-s-font-name: 'Google Sans Flex';
  --lumi-sys-typography-type-scale--body-s-font-size: 0.8125rem;
  --lumi-sys-typography-type-scale--body-s-line-height: 1.0625rem;
  --lumi-sys-typography-type-scale--body-s-font-tracking: 0rem;
  --lumi-sys-typography-type-scale--body-s-font-weight: 400;
  --lumi-sys-typography-type-scale--body-s-font-wght: 400;
  --lumi-sys-typography-type-scale--body-s-font-width: 92;
  --lumi-sys-typography-type-scale--body-s-font-rond: 0;
  --lumi-sys-typography-type-scale--body-s-opsz: 13;

  /* --- Luminous Typography Tokens: Label (Carbon SSoT) --- */
  --lumi-sys-typography-type-scale--label-l-font-name: 'Google Sans Flex';
  --lumi-sys-typography-type-scale--label-l-font-size: 1.0625rem;
  --lumi-sys-typography-type-scale--label-l-line-height: 1.5rem;
  --lumi-sys-typography-type-scale--label-l-font-tracking: 0rem;
  --lumi-sys-typography-type-scale--label-l-font-weight: 370;
  --lumi-sys-typography-type-scale--label-l-font-wght: 370;
  --lumi-sys-typography-type-scale--label-l-font-width: 92;
  --lumi-sys-typography-type-scale--label-l-font-rond: 0;
  --lumi-sys-typography-type-scale--label-l-opsz: 17;

  --lumi-sys-typography-type-scale--label-m-font-name: 'Google Sans Flex';
  --lumi-sys-typography-type-scale--label-m-font-size: 0.9375rem;
  --lumi-sys-typography-type-scale--label-m-line-height: 1.25rem;
  --lumi-sys-typography-type-scale--label-m-font-tracking: 0rem;
  --lumi-sys-typography-type-scale--label-m-font-weight: 370;
  --lumi-sys-typography-type-scale--label-m-font-wght: 370;
  --lumi-sys-typography-type-scale--label-m-font-width: 92;
  --lumi-sys-typography-type-scale--label-m-font-rond: 0;
  --lumi-sys-typography-type-scale--label-m-opsz: 15;

  --lumi-sys-typography-type-scale--label-s-font-name: 'Google Sans Flex';
  --lumi-sys-typography-type-scale--label-s-font-size: 0.8125rem;
  --lumi-sys-typography-type-scale--label-s-line-height: 1.25rem;
  --lumi-sys-typography-type-scale--label-s-font-tracking: 0rem;
  --lumi-sys-typography-type-scale--label-s-font-weight: 370;
  --lumi-sys-typography-type-scale--label-s-font-wght: 370;
  --lumi-sys-typography-type-scale--label-s-font-width: 92;
  --lumi-sys-typography-type-scale--label-s-font-rond: 0;
  --lumi-sys-typography-type-scale--label-s-opsz: 13;

  --lumi-sys-opacity-state--hover: 0.08;
  --lumi-sys-opacity-state--focus: 0.08;
  --lumi-sys-opacity-state--pressed: 0.12;
  --lumi-sys-opacity-state--disabled: 0.12;
  --lumi-sys-opacity-state--disabled-label: 0.38;

  --lumi-sys-color--code-background: #000000;
  --lumi-sys-color--code-primary-text: #ffffff;
  --lumi-sys-color--code-blue-text: #4fa0ff;
  --lumi-sys-color--code-green-text: #60d673;
  --lumi-sys-color--code-grey-text: #808080;
  --lumi-sys-color--code-pink-text: #ff96da;
  --lumi-sys-color--code-purple-text: #969dff;
  --lumi-sys-color--code-red-text: #ff5a59;
  --lumi-sys-color--code-yellow-text: #ffdb0f;

  --lumi-sys-color--chart-series-1: #2575fc;
  --lumi-sys-color--chart-series-2: #5b6e9e;
  --lumi-sys-color--chart-series-3: #228a49;
  --lumi-sys-color--chart-series-4: #62991b;
  --lumi-sys-color--chart-series-5: #1e564d;
  --lumi-sys-color--chart-series-6: #526a45;
  --lumi-sys-color--chart-series-7: #2780c4;
  --lumi-sys-color--chart-series-8: #997112;
  --lumi-sys-color--chart-series-9: #705ec2;
  --lumi-sys-color--chart-series-10: #c84288;
}

:root[data-theme="light"] {
  color-scheme: light;
}

/* ============================================================
 * 3. DARK TOKENS  (REMAPPED to :root — Decision D3)
 *    Canvas / Chart.js / D3 read getComputedStyle(document.documentElement);
 *    the theme-sync listener sets data-theme="dark" on <html>, so dark values
 *    MUST live on :root (not scoped to body) to prevent black-chart regressions.
 * ============================================================ */
:root[data-theme="dark"],
:root:not([data-theme="light"]):has(> body.dark-mode),
body.dark-mode,
:root[data-theme="dark"] body {
  color-scheme: dark;
  --body-bg: transparent;
  --lumi-sys-elevation--level1: 0 0 20px 0 rgba(0, 0, 0, 0.28);
  --lumi-sys-elevation--level2: 0 0 20px 0 rgba(0, 0, 0, 0.40);

  --lumi-sys-color--surface: #0f0f0f;
  --lumi-sys-color--surface-dim: #141414;
  --lumi-sys-color--surface-bright: #1c1c1c;
  --lumi-sys-color--surface-background: #0f0f0f;
  --lumi-sys-color--surface-accent: #14204f;
  --lumi-sys-color--surface-container: #141414;
  --lumi-sys-color--surface-container-high: #1c1c1c;
  --lumi-sys-color--surface-translucent: rgba(24, 24, 27, 0.88);
  --lumi-sys-color--on-surface: #e0e0e0;
  --lumi-sys-color--on-surface-default: #e0e0e0;
  --lumi-sys-color--on-surface-variant: rgba(255, 255, 255, 0.55);
  --lumi-sys-color--on-surface-de-emphasis: rgba(255, 255, 255, 0.55);
  --lumi-sys-color--on-surface-low: rgba(255, 255, 255, 0.12);
  --lumi-sys-color--positive: #0ebc5f;
  --lumi-sys-color--positive-container: #002220;
  --lumi-sys-color--on-positive-container: #0ebc5f;
  --lumi-sys-color--error: #ff4c45;
  --lumi-sys-color--error-container: #3c0202;
  --lumi-sys-color--on-error-container: #ff4c45;
  --lumi-sys-color--accent: #1f3b9b;
  --lumi-sys-color--accent-container: #192967;
  --lumi-sys-color--accent-fixed: #3186ff;
  --lumi-sys-color--primary: #9dd2ff;
  --lumi-sys-color--on-primary: #192967;
  --lumi-sys-color--black: #000000;
  --lumi-sys-color--white: #ffffff;
  --lumi-sys-color--outline: #9a9b9c;
  --lumi-sys-color--stroke-default: #2d2f38;

  --lumi-sys-color--code-background: #141414;
  --lumi-sys-color--code-primary-text: #ffffff;
  --lumi-sys-color--code-blue-text: #4fa0ff;
  --lumi-sys-color--code-green-text: #60d673;
  --lumi-sys-color--code-grey-text: #808080;
  --lumi-sys-color--code-pink-text: #ff96da;
  --lumi-sys-color--code-purple-text: #969dff;
  --lumi-sys-color--code-red-text: #ff5a59;
  --lumi-sys-color--code-yellow-text: #ffdb0f;

  --lumi-sys-color--chart-series-1: #9dd2ff;
  --lumi-sys-color--chart-series-2: #96a7d6;
  --lumi-sys-color--chart-series-3: #50e389;
  --lumi-sys-color--chart-series-4: #c8f585;
  --lumi-sys-color--chart-series-5: #f5f2e6;
  --lumi-sys-color--chart-series-6: #dcd8c0;
  --lumi-sys-color--chart-series-7: #82c7ff;
  --lumi-sys-color--chart-series-8: #f5d77f;
  --lumi-sys-color--chart-series-9: #d9ceff;
  --lumi-sys-color--chart-series-10: #ffa6d7;
}

/* ============================================================
 * 3b. OS-LEVEL DARK FALLBACK  (prefers-color-scheme)
 *     A prior refactor introduced this stylesheet and moved the dark tokens onto
 *     :root[data-theme="dark"], but dropped the @media (prefers-color-scheme:
 *     dark) trigger that widgets previously carried in their own <style>.
 *     Inline widgets whose host sends no set-theme / data-theme message therefore
 *     stayed on the light --surface (#fdfcfc), rendering white in dark mode.
 *     Re-apply the dark values on OS dark; an explicit host data-theme="light"
 *     still opts back to light. Keep in sync with the :root[data-theme="dark"]
 *     block above.
 * ============================================================ */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    color-scheme: dark;
    --body-bg: transparent;
    --lumi-sys-elevation--level1: 0 0 20px 0 rgba(0, 0, 0, 0.28);
    --lumi-sys-elevation--level2: 0 0 20px 0 rgba(0, 0, 0, 0.40);

    --lumi-sys-color--surface: #0f0f0f;
    --lumi-sys-color--surface-dim: #141414;
    --lumi-sys-color--surface-bright: #1c1c1c;
    --lumi-sys-color--surface-background: #0f0f0f;
    --lumi-sys-color--surface-accent: #14204f;
    --lumi-sys-color--surface-container: #141414;
    --lumi-sys-color--surface-container-high: #1c1c1c;
    --lumi-sys-color--surface-translucent: rgba(24, 24, 27, 0.88);
    --lumi-sys-color--on-surface: #e0e0e0;
    --lumi-sys-color--on-surface-default: #e0e0e0;
    --lumi-sys-color--on-surface-variant: rgba(255, 255, 255, 0.55);
    --lumi-sys-color--on-surface-de-emphasis: rgba(255, 255, 255, 0.55);
    --lumi-sys-color--on-surface-low: rgba(255, 255, 255, 0.12);
    --lumi-sys-color--positive: #0ebc5f;
    --lumi-sys-color--positive-container: #002220;
    --lumi-sys-color--on-positive-container: #0ebc5f;
    --lumi-sys-color--error: #ff4c45;
    --lumi-sys-color--error-container: #3c0202;
    --lumi-sys-color--on-error-container: #ff4c45;
    --lumi-sys-color--accent: #1f3b9b;
    --lumi-sys-color--accent-container: #192967;
    --lumi-sys-color--accent-fixed: #3186ff;
    --lumi-sys-color--primary: #9dd2ff;
    --lumi-sys-color--on-primary: #192967;
    --lumi-sys-color--black: #000000;
    --lumi-sys-color--white: #ffffff;
    --lumi-sys-color--outline: #9a9b9c;
    --lumi-sys-color--stroke-default: #2d2f38;

    --lumi-sys-color--code-background: #141414;
    --lumi-sys-color--code-primary-text: #ffffff;
    --lumi-sys-color--code-blue-text: #4fa0ff;
    --lumi-sys-color--code-green-text: #60d673;
    --lumi-sys-color--code-grey-text: #808080;
    --lumi-sys-color--code-pink-text: #ff96da;
    --lumi-sys-color--code-purple-text: #969dff;
    --lumi-sys-color--code-red-text: #ff5a59;
    --lumi-sys-color--code-yellow-text: #ffdb0f;

    --lumi-sys-color--chart-series-1: #9dd2ff;
    --lumi-sys-color--chart-series-2: #96a7d6;
    --lumi-sys-color--chart-series-3: #50e389;
    --lumi-sys-color--chart-series-4: #c8f585;
    --lumi-sys-color--chart-series-5: #f5f2e6;
    --lumi-sys-color--chart-series-6: #dcd8c0;
    --lumi-sys-color--chart-series-7: #82c7ff;
    --lumi-sys-color--chart-series-8: #f5d77f;
    --lumi-sys-color--chart-series-9: #d9ceff;
    --lumi-sys-color--chart-series-10: #ffa6d7;
  }
}

/* Dark mode slider thumb override */
:root[data-theme="dark"] .lumi-slider::-webkit-slider-thumb,
body.dark-mode .lumi-slider::-webkit-slider-thumb {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'%3E%3Crect x='14' y='6' width='4' height='20' rx='2' fill='%23ffffff'/%3E%3C/svg%3E");
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) .lumi-slider::-webkit-slider-thumb {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'%3E%3Crect x='14' y='6' width='4' height='20' rx='2' fill='%23ffffff'/%3E%3C/svg%3E");
  }
}

/* ============================================================
 * 4. SHORT DIAGRAM / CHART ALIASES
 *    Legacy diagram.md and chart.jinja2 reference short names such as
 *    --surface, --on-surface, --chart-1..10, --primary, --r-full. These MUST
 *    resolve to the canonical --lumi-sys-color--* tokens (which flip in dark
 *    mode) — otherwise every diagram var() falls back to black (historical
 *    mass-regression bug #4). Light-hex fallbacks are a last resort only.
 * ============================================================ */
:root {
  /* surfaces */
  --surface: var(--lumi-sys-color--surface, #fdfcfc);
  --surface-dim: var(--lumi-sys-color--surface-dim, #f2f0f0);
  --surface-bright: var(--lumi-sys-color--surface-bright, #ffffff);
  --surface-container: var(--lumi-sys-color--surface-container, #f2f0f0);
  --surface-container-high: var(--lumi-sys-color--surface-container-high, #e6e6e6);
  --surface-container-lowest: var(--lumi-sys-color--surface, #ffffff);
  --surface-accent: var(--lumi-sys-color--surface-accent, #9dd2ff);
  --surface-translucent: var(--lumi-sys-color--surface-translucent, rgba(255, 255, 255, 0.88));
  --surface-glass: var(--lumi-sys-color--surface-translucent, rgba(255, 255, 255, 0.88));
  /* foreground */
  --on-surface: var(--lumi-sys-color--on-surface, #000000);
  --on-surface-variant: var(--lumi-sys-color--on-surface-variant, rgba(0, 0, 0, 0.62));
  --on-surface-low: var(--lumi-sys-color--on-surface-low, rgba(0, 0, 0, 0.08));
  /* accents / brand */
  --primary: var(--lumi-sys-color--primary, #3186ff);
  --primary-container: var(--lumi-sys-color--accent-container, #dcf1ff);
  --accent: var(--lumi-sys-color--accent, #9dd2ff);
  --accent-container: var(--lumi-sys-color--accent-container, #dcf1ff);
  --accent-fixed: var(--lumi-sys-color--accent-fixed, #3186ff);
  /* status */
  --positive: var(--lumi-sys-color--positive, #008052);
  --positive-container: var(--lumi-sys-color--positive-container, #daf9d4);
  --error: var(--lumi-sys-color--error, #de2d29);
  --error-container: var(--lumi-sys-color--error-container, #ffdeec);
  /* structure */
  --outline: var(--lumi-sys-color--outline, #727676);
  --stroke-default: var(--lumi-sys-color--stroke-default, #e3e3e3);
  /* chart series 1..10 */
  --chart-1: var(--lumi-sys-color--chart-series-1, #2575fc);
  --chart-2: var(--lumi-sys-color--chart-series-2, #5b6e9e);
  --chart-3: var(--lumi-sys-color--chart-series-3, #228a49);
  --chart-4: var(--lumi-sys-color--chart-series-4, #62991b);
  --chart-5: var(--lumi-sys-color--chart-series-5, #1e564d);
  --chart-6: var(--lumi-sys-color--chart-series-6, #526a45);
  --chart-7: var(--lumi-sys-color--chart-series-7, #2780c4);
  --chart-8: var(--lumi-sys-color--chart-series-8, #997112);
  --chart-9: var(--lumi-sys-color--chart-series-9, #705ec2);
  --chart-10: var(--lumi-sys-color--chart-series-10, #c84288);
  /* code palette */
  --code-background: var(--lumi-sys-color--code-background, #000000);
  --code-primary-text: var(--lumi-sys-color--code-primary-text, #ffffff);
  /* spacing shorthands */
  --spacing-xs: var(--lumi-sys-spacing--xs, 4px);
  --spacing-s: var(--lumi-sys-spacing--s, 8px);
  --spacing-m: var(--lumi-sys-spacing--m, 12px);
  --spacing-l: var(--lumi-sys-spacing--l, 16px);
  --spacing-xl: var(--lumi-sys-spacing--xl, 20px);
  /* radius shorthands */
  --r-container: var(--lumi-sys-shape--xl-max, 40px);
  --r-xl: var(--lumi-sys-shape--xl, 28px);
  --r-l: var(--lumi-sys-shape--large-max, 24px);
  --r-m: var(--lumi-sys-shape--large, 16px);
  --r-s: var(--lumi-sys-shape--small, 8px);
  --r-full: var(--lumi-sys-shape--full, 999px);
}

/* ============================================================
 * 5. IN-SCOPE PRE-BAKED COMPONENT CLASSES
 *    Interactive controls + simple display components only (Decision D5).
 *    Complex components (timeline, sequence, stepper, pros-cons, hero, HUD,
 *    hotspot, media grid) are intentionally excluded.
 * ============================================================ */

/* Global font rendering quality + transparent root backdrop.
 * Keep --body-bg transparent in both light and dark modes so inline widgets
 * blend into both desktop (#0f0f0f) and mobile / <960px (#000000) host
 * surfaces. Matching :root color-scheme rules prevent Chromium from painting an
 * opaque white canvas behind transparent dark-mode iframes (b/566242402). */
*, *::before, *::after {
  box-sizing: border-box;
}

html, body {
  background: var(--body-bg, transparent) !important;
  color: var(--on-surface) !important;
  /* Auto-resizing iframe: content grows the frame, never scrolls the document.
   * Model widgets already emit this; declared here as the SSoT default. */
  overflow-y: hidden;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-optical-sizing: auto;
  text-rendering: optimizeLegibility;
}

.widget-container {
  width: 100% !important;
  max-width: 100% !important;
  padding-inline: 0 !important;
  box-sizing: border-box;
}

/* ============================================================
 * SCROLLBAR DISCIPLINE (single source of truth)
 *   Long lists/cards flow and let the iframe auto-resize (see the C++
 *   NeutralizeInnerScroll pass, which removes accidental tiny scroll boxes).
 *   For LEGITIMATE overflow that remains (wide tables, code, pan-containers,
 *   large >=240px viewports) render a slim, theme-aware scrollbar.
 *   One token carries the correct light/dark contrast (the auto-flipped
 *   stroke token is too dark on #0f0f0f), referenced once = SSoT.
 * ============================================================ */
:root { --lumi-scrollbar-thumb: rgba(0, 0, 0, 0.20); }
:root[data-theme="dark"], body.dark-mode { --lumi-scrollbar-thumb: rgba(255, 255, 255, 0.20); }
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) { --lumi-scrollbar-thumb: rgba(255, 255, 255, 0.20); }
}
* {
  scrollbar-width: thin;
  scrollbar-color: var(--lumi-scrollbar-thumb) transparent;
}
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
  background-color: var(--lumi-scrollbar-thumb);
  border-radius: var(--lumi-sys-shape--full, 999px);
}

/* --- Buttons --- */
/* Universal button fallback (element specificity 0,0,1) — beats `* { padding: 0 }`
   author resets (0,0,0) while still yielding to any author class selector (0,1,0). */
button {
  appearance: none;
  -webkit-appearance: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--lumi-sys-spacing--xs, 6px);
  min-height: 36px;
  padding: 6px 16px;
  font-family: var(--ff-sans, 'Google Sans Flex', 'Google Sans', sans-serif);
  font-size: 13px;
  font-weight: 500;
  line-height: 18px;
  color: var(--on-surface, #000000);
  background-color: var(--surface-bright, #ffffff);
  border: 1px solid var(--stroke-default, #e3e3e3);
  border-radius: var(--lumi-sys-shape--full, 999px);
  cursor: pointer;
  user-select: none;
  box-sizing: border-box;
  transition: background-color 0.15s, color 0.15s, border-color 0.15s;
}
button:hover {
  background-color: var(--surface-container-high, #e6e6e6);
}
button.active, button.is-active, button.selected, button.is-selected, button[aria-pressed="true"], button[aria-selected="true"], button[aria-checked="true"] {
  background-color: var(--accent-container, #dcf1ff);
  color: var(--lumi-sys-color--on-surface-default, #000000);
  border-color: var(--lumi-sys-color--primary, #3186ff);
}

.lumi-btn, [class^="lumi-btn-"], [class*=" lumi-btn-"] { display: inline-flex; align-items: center; justify-content: center; gap: var(--lumi-sys-spacing--s, 8px); min-height: 40px; padding: 0px 20px; font-family: var(--ff-sans, 'Google Sans Flex', 'Google Sans', sans-serif); font-size: 14px; font-weight: 500; line-height: 20px; border-radius: var(--lumi-sys-shape--full, 999px); border: 1px solid var(--lumi-sys-color--stroke-default, #e3e3e3); cursor: pointer; user-select: none; transition: background-color 0.15s, color 0.15s, border-color 0.15s, box-shadow 0.15s, transform 0.1s; text-decoration: none; box-sizing: border-box; white-space: nowrap; }
.lumi-btn:active, .lumi-btn.is-pressed, [class^="lumi-btn-"]:active, [class*=" lumi-btn-"]:active { transform: scale(0.98); }
.lumi-btn--tonal, .lumi-btn-tonal, .lumi-btn--secondary, .lumi-btn-secondary, [class^="lumi-btn-"], [class*=" lumi-btn-"] { background-color: var(--lumi-sys-color--surface-bright, #ffffff); color: var(--lumi-sys-color--on-surface-default, #000000); }
.lumi-btn--tonal:hover, .lumi-btn-tonal:hover, .lumi-btn--secondary:hover, .lumi-btn-secondary:hover, [class^="lumi-btn-"]:hover, [class*=" lumi-btn-"]:hover { background-color: var(--lumi-sys-color--surface-container-high, #e6e6e6); }
.lumi-btn--accent, .lumi-btn-accent, .lumi-btn--primary, .lumi-btn-primary { background-color: var(--lumi-sys-color--accent, #9dd2ff); color: var(--lumi-sys-color--on-surface-default, #000000); border-color: transparent; }
.lumi-btn--accent:hover, .lumi-btn-accent:hover, .lumi-btn--primary:hover, .lumi-btn-primary:hover { background-color: var(--lumi-sys-color--accent-container, #dcf1ff); }
.lumi-btn--bright, .lumi-btn-bright { background-color: var(--lumi-sys-color--surface-bright, #ffffff); color: var(--lumi-sys-color--on-surface-default, #000000); border-color: var(--lumi-sys-color--stroke-default, #e3e3e3); box-shadow: none; }
.lumi-btn--bright:hover, .lumi-btn-bright:hover { background-color: var(--lumi-sys-color--surface-container-high, #e6e6e6); }
.lumi-btn--ghost, .lumi-btn-ghost, .lumi-btn--on-surface { background-color: var(--lumi-sys-color--on-surface-low, rgba(0, 0, 0, 0.04)); color: var(--lumi-sys-color--on-surface-default, #000000); border-color: transparent; }
.lumi-btn--ghost:hover, .lumi-btn-ghost:hover, .lumi-btn--on-surface:hover { background-color: var(--lumi-sys-color--on-surface-low, rgba(0, 0, 0, 0.08)); }
.lumi-btn--translucent { background-color: rgba(255, 255, 255, 0.25); backdrop-filter: blur(12px); color: var(--lumi-sys-color--on-surface-default, #000000); border-color: rgba(255, 255, 255, 0.3); }
.lumi-btn--translucent:hover { background-color: rgba(255, 255, 255, 0.35); }
.lumi-btn--small, .lumi-btn-small { min-height: 36px; padding: 0px 16px; font-size: 13px; line-height: 18px; gap: var(--lumi-sys-spacing--xs, 4px); }
.lumi-btn--xsmall, .lumi-btn-xsmall { min-height: 24px; padding: 0px 10px; font-size: 11px; line-height: 16px; gap: 4px; }
/* Toggleable Buttons */
.lumi-btn.is-selected,
.lumi-btn.selected,
.lumi-btn.is-active,
.lumi-btn.active,
.lumi-btn[aria-pressed="true"],
.lumi-btn[aria-selected="true"],
.lumi-btn[aria-checked="true"] {
  background-color: var(--lumi-sys-color--accent-container, #dcf1ff);
  color: var(--lumi-sys-color--on-surface-default, #000000);
  border: 1px solid var(--lumi-sys-color--primary, #3186ff);
  box-shadow: none;
}
.lumi-btn.is-selected:hover,
.lumi-btn.selected:hover,
.lumi-btn.is-active:hover,
.lumi-btn.active:hover,
.lumi-btn[aria-pressed="true"]:hover,
.lumi-btn[aria-selected="true"]:hover,
.lumi-btn[aria-checked="true"]:hover {
  background-color: var(--lumi-sys-color--accent, #9dd2ff);
  color: var(--lumi-sys-color--on-surface-default, #000000);
}
.lumi-btn.is-selected:active,
.lumi-btn.selected:active,
.lumi-btn.is-active:active,
.lumi-btn.active:active,
.lumi-btn[aria-pressed="true"]:active,
.lumi-btn[aria-selected="true"]:active,
.lumi-btn[aria-checked="true"]:active {
  transform: scale(0.98);
}

:root[data-theme="dark"] .lumi-btn.is-selected,
:root[data-theme="dark"] .lumi-btn.selected,
:root[data-theme="dark"] .lumi-btn.is-active,
:root[data-theme="dark"] .lumi-btn.active,
:root[data-theme="dark"] .lumi-btn[aria-pressed="true"],
:root[data-theme="dark"] .lumi-btn[aria-selected="true"],
:root[data-theme="dark"] .lumi-btn[aria-checked="true"],
body.dark-mode .lumi-btn.is-selected,
body.dark-mode .lumi-btn.selected,
body.dark-mode .lumi-btn.is-active,
body.dark-mode .lumi-btn.active,
body.dark-mode .lumi-btn[aria-pressed="true"],
body.dark-mode .lumi-btn[aria-selected="true"],
body.dark-mode .lumi-btn[aria-checked="true"],
.lumi-theme-dark .lumi-btn.is-selected,
.lumi-theme-dark .lumi-btn.selected,
.lumi-theme-dark .lumi-btn.is-active,
.lumi-theme-dark .lumi-btn.active,
.lumi-theme-dark .lumi-btn[aria-pressed="true"],
.lumi-theme-dark .lumi-btn[aria-selected="true"],
.lumi-theme-dark .lumi-btn[aria-checked="true"] {
  background-color: var(--lumi-sys-color--accent-container, #192967);
  color: var(--lumi-sys-color--on-surface-default, #e0e0e0);
  border: 1px solid var(--lumi-sys-color--primary, #9dd2ff);
  box-shadow: none;
}
:root[data-theme="dark"] .lumi-btn.is-selected:hover,
:root[data-theme="dark"] .lumi-btn.selected:hover,
:root[data-theme="dark"] .lumi-btn.is-active:hover,
:root[data-theme="dark"] .lumi-btn.active:hover,
:root[data-theme="dark"] .lumi-btn[aria-pressed="true"]:hover,
:root[data-theme="dark"] .lumi-btn[aria-selected="true"]:hover,
:root[data-theme="dark"] .lumi-btn[aria-checked="true"]:hover,
body.dark-mode .lumi-btn.is-selected:hover,
body.dark-mode .lumi-btn.selected:hover,
body.dark-mode .lumi-btn.is-active:hover,
body.dark-mode .lumi-btn.active:hover,
body.dark-mode .lumi-btn[aria-pressed="true"]:hover,
body.dark-mode .lumi-btn[aria-selected="true"]:hover,
body.dark-mode .lumi-btn[aria-checked="true"]:hover,
.lumi-theme-dark .lumi-btn.is-selected:hover,
.lumi-theme-dark .lumi-btn.selected:hover,
.lumi-theme-dark .lumi-btn.is-active:hover,
.lumi-theme-dark .lumi-btn.active:hover,
.lumi-theme-dark .lumi-btn[aria-pressed="true"]:hover,
.lumi-theme-dark .lumi-btn[aria-selected="true"]:hover,
.lumi-theme-dark .lumi-btn[aria-checked="true"]:hover {
  background-color: var(--lumi-sys-color--accent, #1f3b9b);
  color: var(--lumi-sys-color--on-surface-default, #e0e0e0);
}

/* --- Switch --- */
.lumi-switch { display: inline-flex; align-items: center; gap: var(--lumi-sys-spacing--s, 8px); cursor: pointer; font-family: var(--ff-sans, 'Google Sans Flex', 'Google Sans', sans-serif); font-size: 15px; color: var(--lumi-sys-color--on-surface-default, #000000); user-select: none; }
.lumi-switch input[type="checkbox"] { position: absolute; opacity: 0; width: 0px; height: 0px; pointer-events: none; }
.lumi-switch__track { position: relative; display: inline-flex; align-items: center; width: 52px; height: 32px; background-color: var(--lumi-sys-color--surface-dim, #f2f0f0); border: 2px solid var(--lumi-sys-color--stroke-default, rgba(0, 0, 0, 0.12)); border-radius: var(--lumi-sys-shape--full, 999px); transition: background-color 0.2s, border-color 0.2s; flex-shrink: 0; box-sizing: border-box; }
.lumi-switch__thumb, .lumi-switch__track::after { content: ""; position: absolute; top: 50%; left: 6px; transform: translateY(-50%); width: 16px; height: 16px; border-radius: 50%; background-color: var(--lumi-sys-color--on-surface-variant, #757575); transition: 0.2s cubic-bezier(0.4, 0, 0.2, 1); display: flex; align-items: center; justify-content: center; box-sizing: border-box; }
.lumi-switch input[type="checkbox"]:checked + .lumi-switch__track { background-color: var(--lumi-sys-color--accent-fixed, #3186ff); border-color: transparent; }
.lumi-switch input[type="checkbox"]:checked + .lumi-switch__track .lumi-switch__thumb, .lumi-switch input[type="checkbox"]:checked + .lumi-switch__track::after { left: 22px; width: 24px; height: 24px; background-color: rgb(255, 255, 255); }
.lumi-switch input[type="checkbox"]:disabled + .lumi-switch__track { opacity: var(--lumi-sys-opacity-state--disabled, 0.38); cursor: not-allowed; }
.lumi-switch--small .lumi-switch__track, .lumi-switch--mini .lumi-switch__track { width: 32px; height: 20px; }
.lumi-switch--small .lumi-switch__thumb, .lumi-switch--small .lumi-switch__track::after, .lumi-switch--mini .lumi-switch__thumb, .lumi-switch--mini .lumi-switch__track::after { width: 12px; height: 12px; left: 2px; }
.lumi-switch--small input[type="checkbox"]:checked + .lumi-switch__track .lumi-switch__thumb, .lumi-switch--small input[type="checkbox"]:checked + .lumi-switch__track::after, .lumi-switch--mini input[type="checkbox"]:checked + .lumi-switch__track .lumi-switch__thumb, .lumi-switch--mini input[type="checkbox"]:checked + .lumi-switch__track::after { left: 12px; width: 16px; height: 16px; }

/* --- Checkbox --- */
.lumi-checkbox-label { display: inline-flex; align-items: center; gap: var(--lumi-sys-spacing--s, 8px); cursor: pointer; font-family: var(--ff-sans, 'Google Sans Flex', 'Google Sans', sans-serif); font-size: 15px; color: var(--lumi-sys-color--on-surface-default, #000000); user-select: none; }
.lumi-checkbox-label input[type="checkbox"] { position: absolute; opacity: 0; width: 0px; height: 0px; pointer-events: none; }
.lumi-checkbox { position: relative; width: 24px; height: 24px; border-radius: var(--lumi-sys-shape--small, 8px); border: 2px solid var(--lumi-sys-color--on-surface-variant, rgba(0, 0, 0, 0.62)); background-color: transparent; transition: background-color 0.15s, border-color 0.15s, box-shadow 0.15s; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-sizing: border-box; }
.lumi-checkbox-label:hover .lumi-checkbox { background-color: var(--lumi-sys-color--on-surface-low, rgba(0, 0, 0, 0.04)); border-color: var(--lumi-sys-color--on-surface-default, #000000); }
.lumi-checkbox-label input[type="checkbox"]:checked ~ .lumi-checkbox, .lumi-checkbox-label input[type="checkbox"]:indeterminate ~ .lumi-checkbox, .lumi-checkbox.is-indeterminate { background-color: var(--lumi-sys-color--on-surface-default, #000000); border-color: transparent; }
.lumi-checkbox .lumi-checkmark { font-size: 18px; line-height: 1; color: var(--lumi-sys-color--surface, #ffffff); fill: var(--lumi-sys-color--surface, #ffffff); display: none; user-select: none; }
.lumi-checkbox-label input[type="checkbox"]:checked ~ .lumi-checkbox .lumi-checkmark, .lumi-checkbox-label input[type="checkbox"]:checked ~ .lumi-checkbox .lumi-checkbox__check { display: block; }
.lumi-checkbox-label input[type="checkbox"]:indeterminate ~ .lumi-checkbox .lumi-checkbox__indeterminate, .lumi-checkbox.is-indeterminate .lumi-checkbox__indeterminate { display: block; }
.lumi-checkbox-label input[type="checkbox"]:disabled ~ .lumi-checkbox, .lumi-checkbox-label input[type="checkbox"]:disabled ~ span { opacity: var(--lumi-sys-opacity-state--disabled, 0.38); cursor: not-allowed; }

/* --- Slider --- */
.lumi-slider-container { display: flex; align-items: center; gap: var(--lumi-sys-spacing--m, 16px); width: 100%; }
.lumi-slider-row { display: flex; flex-direction: column; gap: var(--lumi-sys-spacing--xs, 4px); width: 100%; }
.lumi-slider-label { font-family: var(--ff-sans, 'Google Sans Flex', 'Google Sans', sans-serif); font-size: 15px; font-weight: 400; color: var(--lumi-sys-color--on-surface-default, #000000); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.lumi-slider { appearance: none; width: calc(100% + 28px); margin-left: -14px; margin-right: -14px; height: 40px; background: transparent; cursor: pointer; box-sizing: border-box; }
.lumi-slider:focus { outline: none; }
.lumi-slider::-webkit-slider-runnable-track { height: 4px; --thumb-center: clamp(14px, var(--progress, 50%), calc(100% - 14px)); --active-end: max(14px, calc(var(--thumb-center) - 8px)); background-image: radial-gradient(circle at calc(100% - 18px) center, var(--lumi-sys-color--on-surface-variant, #757575) 2px, transparent 2.5px), linear-gradient( to right, transparent 0, transparent 14px, var(--lumi-sys-color--on-surface-default, #000000) 14px, var(--lumi-sys-color--on-surface-default, #000000) var(--active-end), transparent var(--active-end), transparent calc(var(--thumb-center) + 8px), var(--lumi-sys-color--stroke-default, rgba(0, 0, 0, 0.12)) calc(var(--thumb-center) + 8px), var(--lumi-sys-color--stroke-default, rgba(0, 0, 0, 0.12)) calc(100% - 16px), transparent calc(100% - 16px), transparent 100% ); border-radius: var(--lumi-sys-shape--full, 999px); border-width: medium; border-style: none; border-color: currentcolor; border-image: none; }
.lumi-slider[style*="--progress-ratio"]::-webkit-slider-runnable-track { --thumb-center: calc(14px + (100% - 28px) * var(--progress-ratio, 0.5)); --active-end: calc(var(--thumb-center) - 8px + var(--progress-ratio, 0.5) * 6px); }
@supports (left: calc(1px * (50% / 100%))) { .lumi-slider::-webkit-slider-runnable-track, .lumi-slider[style*="--progress-ratio"]::-webkit-slider-runnable-track { --thumb-center: calc(14px + (100% - 28px) * (var(--progress, 50%) / 100%)); --active-end: calc(var(--thumb-center) - 8px + (var(--progress, 50%) / 100%) * 6px); } }
.lumi-slider::-webkit-slider-thumb { appearance: none; width: 32px; height: 32px; border-radius: 50%; background-color: transparent; background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'%3E%3Crect x='14' y='6' width='4' height='20' rx='2' fill='%23000000'/%3E%3C/svg%3E"); background-size: 32px 32px; background-repeat: no-repeat; background-position: center center; border-width: medium; border-style: none; border-color: currentcolor; border-image: none; box-sizing: border-box; margin-top: -14px; cursor: pointer; transition: background-color 0.15s; }
.lumi-slider:hover::-webkit-slider-thumb { background-color: var(--lumi-sys-color--on-surface-low, rgba(0, 0, 0, 0.08)); }
.lumi-slider:active::-webkit-slider-thumb { background-color: var(--lumi-sys-color--on-surface-low, rgba(0, 0, 0, 0.12)); }
.lumi-slider:disabled { opacity: var(--lumi-sys-opacity-state--disabled, 0.38); cursor: not-allowed; }
.lumi-slider:disabled::-webkit-slider-thumb { cursor: not-allowed; box-shadow: none; }
.lumi-slider-value { display: flex; align-items: center; justify-content: center; min-width: 64px; height: 40px; padding: 0px 12px; background-color: var(--lumi-sys-color--surface-dim, #f2f0f0); border-radius: var(--lumi-sys-shape--medium, 16px); font-family: var(--ff-sans, 'Google Sans Flex', sans-serif); font-size: 15px; line-height: 20px; font-weight: 540; font-variation-settings: "wght" 540, "wdth" 92, "opsz" 15; font-variant-numeric: tabular-nums; color: var(--lumi-sys-color--on-surface-default, #000000); flex-shrink: 0; box-sizing: border-box; }

/* --- Text input --- */
.lumi-input-group { display: flex; flex-direction: column; gap: var(--lumi-sys-spacing--xs, 4px); width: 100%; }
.lumi-input-label { font-family: var(--ff-sans, 'Google Sans Flex', 'Google Sans', sans-serif); font-size: 14px; font-weight: 500; line-height: 20px; color: var(--lumi-sys-color--on-surface-default, #000000); }
.lumi-input { appearance: none; width: 100%; min-height: 48px; padding: 0px 16px; font-family: var(--ff-sans, 'Google Sans Flex', 'Google Sans', sans-serif); font-size: 15px; font-weight: 400; line-height: 22px; color: var(--lumi-sys-color--on-surface-default, #000000); background-color: var(--lumi-sys-color--surface-bright, #ffffff); border: 1px solid var(--lumi-sys-color--stroke-default, rgba(0, 0, 0, 0.12)); border-radius: var(--lumi-sys-shape--large, 16px); background-clip: padding-box; outline: none; box-sizing: border-box; transition: border-color 0.15s, box-shadow 0.15s, background-color 0.15s; }
.lumi-input::placeholder { color: var(--lumi-sys-color--on-surface-variant, rgba(0, 0, 0, 0.62)); }
.lumi-input:hover { border-color: var(--lumi-sys-color--on-surface-default, #000000); }
.lumi-input:focus, .lumi-input:focus-visible { border-color: var(--lumi-sys-color--accent-fixed, #3186ff); box-shadow: 0 0 0 2px var(--lumi-sys-color--accent-container, rgba(49, 134, 255, 0.25)); }
textarea.lumi-input, .lumi-input--area { min-height: 100px; padding: 12px 16px; resize: vertical; line-height: 22px; }
.lumi-input.is-error, .lumi-input-group.is-error .lumi-input { border-color: var(--lumi-sys-color--error, #ff4c45); }
.lumi-input-helper { font-family: var(--ff-sans, 'Google Sans Flex', 'Google Sans', sans-serif); font-size: 12px; line-height: 16px; color: var(--lumi-sys-color--on-surface-variant, rgba(0, 0, 0, 0.62)); }
.lumi-input-group.is-error .lumi-input-helper, .lumi-input-helper--error { color: var(--lumi-sys-color--error, #ff4c45); }
.lumi-input:disabled, .lumi-input.is-disabled { opacity: var(--lumi-sys-opacity-state--disabled, 0.38); background-color: var(--lumi-sys-color--surface-dim, #f2f0f0); cursor: not-allowed; }

/* --- Focus ring --- */
:focus-visible { outline: 2px solid var(--lumi-sys-color--on-surface-default, #000000) !important; outline-offset: 2px !important; box-shadow: none !important; }
.lumi-btn:focus-visible, .lumi-switch input[type="checkbox"]:focus-visible + .lumi-switch__track, .lumi-checkbox-label input[type="checkbox"]:focus-visible ~ .lumi-checkbox, .lumi-slider:focus-visible::-webkit-slider-thumb, .lumi-input:focus-visible { outline: 2px solid var(--lumi-sys-color--on-surface-default, #000000); outline-offset: 2px; box-shadow: none; }
[role="application"]:focus-visible, [aria-roledescription*="chart"]:focus-visible { outline: 2px solid var(--lumi-sys-color--primary, #3186ff) !important; outline-offset: 4px !important; }

/* --- Typography: Display / Headline / Body / Label --- */
.lumi-display-l { font-family: var(--lumi-sys-typography-type-scale--display-l-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--display-l-font-size, 2.625rem); line-height: var(--lumi-sys-typography-type-scale--display-l-line-height, 3rem); letter-spacing: var(--lumi-sys-typography-type-scale--display-l-font-tracking, 0rem); font-weight: var(--lumi-sys-typography-type-scale--display-l-font-weight, 280); font-variation-settings: "wght" 280, "wdth" 100, "opsz" 42, "ROND" 100; }
.lumi-display-l-emphasized { font-family: var(--lumi-sys-typography-type-scale--display-l-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--display-l-font-size, 2.625rem); line-height: var(--lumi-sys-typography-type-scale--display-l-line-height, 3rem); letter-spacing: var(--lumi-sys-typography-type-scale--display-l-font-tracking, 0rem); font-weight: var(--lumi-sys-typography-type-scale--display-l-font-weight, 280); font-variation-settings: "wght" 280, "wdth" 100, "opsz" 42, "ROND" 100; }
.lumi-display-m { font-family: var(--lumi-sys-typography-type-scale--display-m-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--display-m-font-size, 2.25rem); line-height: var(--lumi-sys-typography-type-scale--display-m-line-height, 2.75rem); letter-spacing: var(--lumi-sys-typography-type-scale--display-m-font-tracking, 0rem); font-weight: var(--lumi-sys-typography-type-scale--display-m-font-weight, 320); font-variation-settings: "wght" 320, "wdth" 100, "opsz" 36, "ROND" 100; }
.lumi-display-m-emphasized { font-family: var(--lumi-sys-typography-type-scale--display-m-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--display-m-font-size, 2.25rem); line-height: var(--lumi-sys-typography-type-scale--display-m-line-height, 2.75rem); letter-spacing: var(--lumi-sys-typography-type-scale--display-m-font-tracking, 0rem); font-weight: var(--lumi-sys-typography-type-scale--display-m-font-weight, 320); font-variation-settings: "wght" 320, "wdth" 100, "opsz" 36, "ROND" 100; }
.lumi-display-s { font-family: var(--lumi-sys-typography-type-scale--display-s-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--display-s-font-size, 2rem); line-height: var(--lumi-sys-typography-type-scale--display-s-line-height, 2.375rem); letter-spacing: var(--lumi-sys-typography-type-scale--display-s-font-tracking, 0rem); font-weight: var(--lumi-sys-typography-type-scale--display-s-font-weight, 360); font-variation-settings: "wght" 360, "wdth" 100, "opsz" 32, "ROND" 100; }
.lumi-display-s-emphasized { font-family: var(--lumi-sys-typography-type-scale--display-s-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--display-s-font-size, 2rem); line-height: var(--lumi-sys-typography-type-scale--display-s-line-height, 2.375rem); letter-spacing: var(--lumi-sys-typography-type-scale--display-s-font-tracking, 0rem); font-weight: var(--lumi-sys-typography-type-scale--display-s-font-weight, 360); font-variation-settings: "wght" 360, "wdth" 100, "opsz" 32, "ROND" 100; }
.lumi-headline-l { font-family: var(--lumi-sys-typography-type-scale--headline-l-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--headline-l-font-size, 1.75rem); line-height: var(--lumi-sys-typography-type-scale--headline-l-line-height, 2.25rem); letter-spacing: var(--lumi-sys-typography-type-scale--headline-l-font-tracking, 0rem); font-weight: var(--lumi-sys-typography-type-scale--headline-l-font-weight, 350); font-variation-settings: "wght" 350, "wdth" 100, "opsz" 28, "ROND" 20; }
.lumi-headline-l-emphasized { font-family: var(--lumi-sys-typography-type-scale--headline-l-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--headline-l-font-size, 1.75rem); line-height: var(--lumi-sys-typography-type-scale--headline-l-line-height, 2.25rem); letter-spacing: var(--lumi-sys-typography-type-scale--headline-l-font-tracking, 0rem); font-weight: var(--lumi-sys-typography-type-scale--headline-l-font-weight, 350); font-variation-settings: "wght" 350, "wdth" 100, "opsz" 28, "ROND" 20; }
.lumi-headline-m { font-family: var(--lumi-sys-typography-type-scale--headline-m-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--headline-m-font-size, 1.5rem); line-height: var(--lumi-sys-typography-type-scale--headline-m-line-height, 1.75rem); letter-spacing: var(--lumi-sys-typography-type-scale--headline-m-font-tracking, 0rem); font-weight: var(--lumi-sys-typography-type-scale--headline-m-font-weight, 380); font-variation-settings: "wght" 380, "wdth" 100, "opsz" 24, "ROND" 20; }
.lumi-headline-m-emphasized { font-family: var(--lumi-sys-typography-type-scale--headline-m-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--headline-m-font-size, 1.5rem); line-height: var(--lumi-sys-typography-type-scale--headline-m-line-height, 1.75rem); letter-spacing: var(--lumi-sys-typography-type-scale--headline-m-font-tracking, 0rem); font-weight: var(--lumi-sys-typography-type-scale--headline-m-font-weight, 380); font-variation-settings: "wght" 380, "wdth" 100, "opsz" 24, "ROND" 20; }
.lumi-headline-s { font-family: var(--lumi-sys-typography-type-scale--headline-s-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--headline-s-font-size, 1.25rem); line-height: var(--lumi-sys-typography-type-scale--headline-s-line-height, 1.5rem); letter-spacing: var(--lumi-sys-typography-type-scale--headline-s-font-tracking, 0rem); font-weight: var(--lumi-sys-typography-type-scale--headline-s-font-weight, 470); font-variation-settings: "wght" 470, "wdth" 94, "opsz" 20, "ROND" 20; }
.lumi-headline-s-emphasized { font-family: var(--lumi-sys-typography-type-scale--headline-s-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--headline-s-font-size, 1.25rem); line-height: var(--lumi-sys-typography-type-scale--headline-s-line-height, 1.5rem); letter-spacing: var(--lumi-sys-typography-type-scale--headline-s-font-tracking, 0rem); font-weight: var(--lumi-sys-typography-type-scale--headline-s-font-weight, 470); font-variation-settings: "wght" 470, "wdth" 94, "opsz" 20, "ROND" 20; }
.lumi-body-l { font-family: var(--lumi-sys-typography-type-scale--body-l-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--body-l-font-size, 1.0625rem); line-height: var(--lumi-sys-typography-type-scale--body-l-line-height, 1.5rem); letter-spacing: var(--lumi-sys-typography-type-scale--body-l-font-tracking, 0rem); font-weight: var(--lumi-sys-typography-type-scale--body-l-font-weight, 400); font-variation-settings: "wght" 400, "wdth" 92, "opsz" 17; }
.lumi-body-l-emphasized { font-family: var(--lumi-sys-typography-type-scale--body-l-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--body-l-font-size, 1.0625rem); line-height: var(--lumi-sys-typography-type-scale--body-l-line-height, 1.5rem); letter-spacing: var(--lumi-sys-typography-type-scale--body-l-font-tracking, 0rem); font-weight: 540; font-variation-settings: "wght" 540, "wdth" 92, "opsz" 17; font-variant-numeric: tabular-nums; }
.lumi-body-m { font-family: var(--lumi-sys-typography-type-scale--body-m-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--body-m-font-size, 0.9375rem); line-height: var(--lumi-sys-typography-type-scale--body-m-line-height, 1.25rem); letter-spacing: var(--lumi-sys-typography-type-scale--body-m-font-tracking, 0rem); font-weight: var(--lumi-sys-typography-type-scale--body-m-font-weight, 400); font-variation-settings: "wght" 400, "wdth" 92, "opsz" 15; }
.lumi-body-m-emphasized { font-family: var(--lumi-sys-typography-type-scale--body-m-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--body-m-font-size, 0.9375rem); line-height: var(--lumi-sys-typography-type-scale--body-m-line-height, 1.25rem); letter-spacing: var(--lumi-sys-typography-type-scale--body-m-font-tracking, 0rem); font-weight: 540; font-variation-settings: "wght" 540, "wdth" 92, "opsz" 15; font-variant-numeric: tabular-nums; }
.lumi-body-s { font-family: var(--lumi-sys-typography-type-scale--body-s-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--body-s-font-size, 0.8125rem); line-height: var(--lumi-sys-typography-type-scale--body-s-line-height, 1.0625rem); letter-spacing: var(--lumi-sys-typography-type-scale--body-s-font-tracking, 0rem); font-weight: var(--lumi-sys-typography-type-scale--body-s-font-weight, 400); font-variation-settings: "wght" 400, "wdth" 92, "opsz" 13; }
.lumi-body-s-emphasized { font-family: var(--lumi-sys-typography-type-scale--body-s-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--body-s-font-size, 0.8125rem); line-height: var(--lumi-sys-typography-type-scale--body-s-line-height, 1.0625rem); letter-spacing: var(--lumi-sys-typography-type-scale--body-s-font-tracking, 0rem); font-weight: 540; font-variation-settings: "wght" 540, "wdth" 92, "opsz" 13; font-variant-numeric: tabular-nums; }
.lumi-label-l { font-family: var(--lumi-sys-typography-type-scale--label-l-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--label-l-font-size, 1.0625rem); line-height: var(--lumi-sys-typography-type-scale--label-l-line-height, 1.5rem); letter-spacing: var(--lumi-sys-typography-type-scale--label-l-font-tracking, 0rem); font-weight: var(--lumi-sys-typography-type-scale--label-l-font-weight, 370); font-variation-settings: "wght" 370, "wdth" 92, "opsz" 17; }
.lumi-label-l-emphasized { font-family: var(--lumi-sys-typography-type-scale--label-l-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--label-l-font-size, 1.0625rem); line-height: var(--lumi-sys-typography-type-scale--label-l-line-height, 1.5rem); letter-spacing: var(--lumi-sys-typography-type-scale--label-l-font-tracking, 0rem); font-weight: var(--lumi-sys-typography-type-scale--label-l-font-weight, 370); font-variation-settings: "wght" 370, "wdth" 92, "opsz" 17; }
.lumi-label-m { font-family: var(--lumi-sys-typography-type-scale--label-m-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--label-m-font-size, 0.9375rem); line-height: var(--lumi-sys-typography-type-scale--label-m-line-height, 1.25rem); letter-spacing: var(--lumi-sys-typography-type-scale--label-m-font-tracking, 0rem); font-weight: var(--lumi-sys-typography-type-scale--label-m-font-weight, 370); font-variation-settings: "wght" 370, "wdth" 92, "opsz" 15; }
.lumi-label-m-emphasized { font-family: var(--lumi-sys-typography-type-scale--label-m-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--label-m-font-size, 0.9375rem); line-height: var(--lumi-sys-typography-type-scale--label-m-line-height, 1.25rem); letter-spacing: var(--lumi-sys-typography-type-scale--label-m-font-tracking, 0rem); font-weight: var(--lumi-sys-typography-type-scale--label-m-font-weight, 370); font-variation-settings: "wght" 370, "wdth" 92, "opsz" 15; }
.lumi-label-s { font-family: var(--lumi-sys-typography-type-scale--label-s-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--label-s-font-size, 0.8125rem); line-height: var(--lumi-sys-typography-type-scale--label-s-line-height, 1.25rem); letter-spacing: var(--lumi-sys-typography-type-scale--label-s-font-tracking, 0rem); font-weight: var(--lumi-sys-typography-type-scale--label-s-font-weight, 370); font-variation-settings: "wght" 370, "wdth" 92, "opsz" 13; }
.lumi-label-s-emphasized { font-family: var(--lumi-sys-typography-type-scale--label-s-font-name, 'Google Sans Flex', sans-serif); font-size: var(--lumi-sys-typography-type-scale--label-s-font-size, 0.8125rem); line-height: var(--lumi-sys-typography-type-scale--label-s-line-height, 1.25rem); letter-spacing: var(--lumi-sys-typography-type-scale--label-s-font-tracking, 0rem); font-weight: var(--lumi-sys-typography-type-scale--label-s-font-weight, 370); font-variation-settings: "wght" 370, "wdth" 92, "opsz" 13; }

/* --- Typography: Monospace / Extended (Google Sans Code) --- */
.lumi-blockquote { font-family: var(--ff-mono, 'Google Sans Code', monospace); font-style: italic; font-size: 22px; line-height: 30px; font-weight: 300; font-variation-settings: "wght" 300, "opsz" 22, "MONO" 0; }
.lumi-takeaway { font-family: var(--ff-mono, 'Google Sans Code', monospace); font-style: italic; font-size: 17px; line-height: 24px; font-weight: 400; font-variation-settings: "wght" 400, "opsz" 17, "MONO" 0; }
.lumi-caption { font-family: var(--ff-mono, 'Google Sans Code', monospace); font-style: italic; font-size: 13px; line-height: 20px; font-weight: 400; font-variation-settings: "wght" 400, "opsz" 13, "MONO" 0; }
.lumi-code { font-family: var(--ff-mono, 'Google Sans Code', monospace); font-size: 15px; line-height: 20px; font-weight: 400; font-variation-settings: "wght" 400, "MONO" 1; }
.lumi-bullet { font-family: var(--ff-mono, 'Google Sans Code', monospace); font-size: 15px; line-height: 24px; font-weight: 650; font-variation-settings: "wght" 650, "MONO" 1; }

/* --- Cards & attribution --- */
.lumi-summary-card { padding: var(--lumi-sys-spacing--l, 16px); background-color: var(--lumi-sys-color--surface-bright, #ffffff); border-radius: var(--lumi-sys-shape--medium, 12px); color: var(--lumi-sys-color--on-surface-default, #000000); font-family: var(--ff-sans, 'Google Sans Flex', sans-serif); font-size: 15px; line-height: 20px; box-sizing: border-box; }
.lumi-link-card { display: flex; align-items: center; justify-content: space-between; padding: var(--lumi-sys-spacing--l, 16px); background-color: var(--lumi-sys-color--surface-bright, #ffffff); border-radius: var(--lumi-sys-shape--medium, 12px); text-decoration: none; color: var(--lumi-sys-color--on-surface-default, #000000); transition: background-color 0.15s; box-sizing: border-box; }
.lumi-link-card:hover { background-color: var(--lumi-sys-color--surface-container-high, #e6e6e6); }
.lumi-attribution-buffer { margin-top: var(--lumi-sys-spacing--xxl, 24px); font-family: var(--ff-sans, 'Google Sans Flex', sans-serif); font-size: 13px; color: var(--lumi-sys-color--on-surface-de-emphasis, rgba(0, 0, 0, 0.62)); }
.lumi-card { background-color: var(--lumi-sys-color--surface-bright, #ffffff); border-radius: var(--lumi-sys-shape--xl-max, 40px); padding: var(--lumi-sys-spacing--3xl, 28px); display: flex; flex-direction: column; gap: var(--lumi-sys-spacing--s, 8px); width: 100%; box-sizing: border-box; }
.lumi-card.is-prominent, .lumi-card--prominent, .lumi-card.surface-dim { background-color: var(--lumi-sys-color--surface-dim, #f2f0f0); }
.lumi-card-title { font-family: var(--ff-sans, 'Google Sans Flex', sans-serif); font-size: 20px; font-weight: 500; font-variation-settings: "wght" 470, "wdth" 94, "opsz" 20; color: var(--lumi-sys-color--on-surface, #000000); margin: 0px; }
.lumi-card-subtitle { font-family: var(--ff-sans, 'Google Sans Flex', sans-serif); font-size: 13px; font-weight: 400; font-variation-settings: "wght" 400, "wdth" 92, "opsz" 13; color: var(--lumi-sys-color--on-surface-variant, rgba(0, 0, 0, 0.62)); margin: 0; }
.lumi-card-body { font-family: var(--ff-sans, 'Google Sans Flex', sans-serif); font-size: 15px; font-weight: 400; font-variation-settings: "wght" 400, "wdth" 92, "opsz" 15; color: var(--lumi-sys-color--on-surface, #000000); margin: var(--lumi-sys-spacing--xs, 4px) 0 0 0; }
.lumi-overlay-card { background-color: var(--surface-translucent, rgba(255, 255, 255, 0.88)); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border: 1px solid var(--stroke-default); border-radius: var(--lumi-sys-shape--medium, 12px); padding: var(--lumi-sys-spacing--m, 12px) var(--lumi-sys-spacing--l, 16px); color: var(--on-surface); box-shadow: var(--lumi-sys-elevation--level1); box-sizing: border-box; }

/* --- Progress bar --- */
.lumi-progress-tracker { display: flex; flex-direction: column; gap: var(--lumi-sys-spacing--xs, 4px); width: 100%; }
.lumi-progress-bar { width: 100%; height: 8px; background-color: var(--lumi-sys-color--stroke-default, #e3e3e3); border: 1px solid transparent; box-sizing: border-box; border-radius: var(--lumi-sys-shape--full, 999px); overflow: hidden; }
.lumi-progress-fill { height: 100%; background-color: var(--lumi-sys-color--accent-fixed, #3186ff); border-radius: var(--lumi-sys-shape--full, 999px); transition: width 0.3s; }

/* --- Accordion (card group variant) --- */
.lumi-accordion-group { display: flex; flex-direction: column; gap: var(--lumi-sys-spacing--s, 8px); }
.lumi-accordion-group .lumi-accordion-item { background-color: var(--lumi-sys-color--surface-container, #f2f0f0); border-radius: var(--lumi-sys-shape--medium, 12px); overflow: hidden; transition: background-color 0.15s; }
.lumi-accordion-group .lumi-accordion-header { padding: var(--lumi-sys-spacing--l, 16px); font-family: var(--ff-sans, sans-serif); font-size: 15px; font-weight: 540; cursor: pointer; user-select: none; display: flex; justify-content: space-between; align-items: center; color: var(--lumi-sys-color--on-surface-default, #000000); }
.lumi-accordion-group .lumi-accordion-chevron { transition: transform 0.2s; font-size: 12px; }
.lumi-accordion-group .lumi-accordion-item.active .lumi-accordion-chevron { transform: rotate(180deg); }
.lumi-accordion-group .lumi-accordion-body { display: none; padding: 0 var(--lumi-sys-spacing--l, 16px) var(--lumi-sys-spacing--l, 16px) var(--lumi-sys-spacing--l, 16px); font-family: var(--ff-sans, sans-serif); font-size: 15px; color: var(--lumi-sys-color--on-surface-de-emphasis, rgba(0, 0, 0, 0.62)); line-height: 20px; }
.lumi-accordion-group .lumi-accordion-item.active .lumi-accordion-body { display: block; }

/* --- Accordion (borderless list variant) --- */
.lumi-accordion { display: flex; flex-direction: column; width: 100%; border-top: 1px solid var(--lumi-sys-color--on-surface-low, rgba(0, 0, 0, 0.08)); }
.lumi-accordion-item { display: flex; flex-direction: column; width: 100%; background: transparent; border-radius: 0px; border-bottom: 1px solid var(--lumi-sys-color--on-surface-low, rgba(0, 0, 0, 0.08)); }
.lumi-accordion-header { display: flex; justify-content: space-between; align-items: center; padding: var(--lumi-sys-spacing--xl, 20px) 0; cursor: pointer; user-select: none; }
.lumi-accordion-title { margin: 0px; color: var(--lumi-sys-color--on-surface-default, #000000); }
.lumi-accordion-item.active .lumi-accordion-content { display: flex; flex-direction: column; gap: var(--lumi-sys-spacing--l, 16px); }
.lumi-accordion-content { display: none; padding-bottom: var(--lumi-sys-spacing--xxl, 24px); }
.lumi-accordion-field { display: flex; flex-direction: column; gap: var(--lumi-sys-spacing--xxs, 2px); }
.lumi-accordion-field-label { margin: 0px; color: var(--lumi-sys-color--on-surface-default, #000000); }
.lumi-accordion-field-val { margin: 0px; color: var(--lumi-sys-color--on-surface-default, #000000); }

/* --- Segmented control --- */
.lumi-segmented-group { display: flex; background-color: var(--lumi-sys-color--surface-container, #f2f0f0); padding: 4px; border-radius: var(--lumi-sys-shape--full, 999px); gap: 4px; }
.lumi-segmented-btn { flex: 1 1 0%; padding: 8px 16px; border: 1px solid transparent; border-radius: var(--lumi-sys-shape--full, 999px); background-color: transparent; font-family: var(--ff-sans, sans-serif); font-size: 14px; font-weight: 510; cursor: pointer; color: var(--lumi-sys-color--on-surface-de-emphasis, rgba(0, 0, 0, 0.62)); transition: 0.2s; }
.lumi-segmented-btn.is-active, .lumi-segmented-btn.active, .lumi-segmented-btn.is-selected, .lumi-segmented-btn.selected, .lumi-segmented-btn[aria-pressed="true"], .lumi-segmented-btn[aria-selected="true"], .lumi-segmented-btn[aria-checked="true"] { background-color: var(--lumi-sys-color--surface-bright, #ffffff); color: var(--lumi-sys-color--on-surface-default, #000000); box-shadow: var(--lumi-sys-elevation--level1); }

/* --- Tabs --- */
.lumi-tab-group { display: flex; flex-direction: column; gap: var(--lumi-sys-spacing--4xl, 36px); width: 100%; }
.lumi-tab-bar { display: flex; gap: var(--lumi-sys-spacing--l, 16px); padding-bottom: 0px; overflow-x: auto; scrollbar-width: none; }
.lumi-tab-bar::-webkit-scrollbar { display: none; }
.lumi-tab { height: 40px; padding: 0 var(--lumi-sys-spacing--xl, 20px); display: flex; align-items: center; justify-content: center; font-family: var(--ff-sans, 'Google Sans Flex', sans-serif); font-size: 17px; line-height: 24px; font-weight: 370; font-variation-settings: "wght" 370, "wdth" 92, "opsz" 17; color: var(--lumi-sys-color--on-surface-de-emphasis, rgba(0, 0, 0, 0.62)); background: transparent; border: 1px solid transparent; border-radius: var(--lumi-sys-shape--full, 999px); cursor: pointer; white-space: nowrap; transition: background-color 0.15s, color 0.15s; }
.lumi-tab:hover { color: var(--lumi-sys-color--on-surface-default, #000000); }
.lumi-tab.active, .lumi-tab.is-active, .lumi-tab.is-selected, .lumi-tab.selected, .lumi-tab[aria-pressed="true"], .lumi-tab[aria-selected="true"], .lumi-tab[aria-checked="true"] { background-color: var(--lumi-sys-color--surface-container-high, #f2f0f0); color: var(--lumi-sys-color--on-surface-default, #000000); font-weight: 510; font-variation-settings: "wght" 510, "wdth" 92, "opsz" 17; }
.lumi-tab-content { display: flex; flex-direction: column; gap: var(--lumi-sys-spacing--m, 12px); padding-top: 0px; padding-bottom: 0px; }
.lumi-tab-content .lumi-body-l-emphasized, .lumi-tab-content .lumi-headline-s { margin: 0px; }
.lumi-tab-content .lumi-body-l { margin: 0px; color: var(--lumi-sys-color--on-surface-default, #000000); }

/* --- Callout / pullquote --- */
.lumi-callout { display: flex; flex-direction: column; gap: var(--lumi-sys-spacing--xs, 4px); width: 100%; }
.lumi-callout .lumi-body-l-emphasized { margin: 0px; }
.lumi-pullquote { display: flex; gap: var(--lumi-sys-spacing--xl, 20px); width: 100%; margin: 0px; }
.lumi-pullquote-mark { width: 30px; height: 22px; flex-shrink: 0; margin-top: 4px; color: var(--lumi-sys-color--on-surface-default, #000000); }
.lumi-pullquote-body { display: flex; flex-direction: column; gap: var(--lumi-sys-spacing--l, 16px); flex: 1 1 0%; min-width: 0px; }
p.lumi-pullquote-text, .lumi-pullquote-text { font-family: var(--ff-mono, 'Google Sans Code', monospace); font-style: italic; font-weight: 300; font-variation-settings: "wght" 300, "opsz" 22, "MONO" 0; color: var(--lumi-sys-color--on-surface-default, #000000); margin: 0px; font-size: 22px !important; line-height: 30px !important; }
.lumi-pullquote-cite { display: flex; flex-direction: column; font-style: normal; }
.lumi-pullquote-cite .lumi-de-emphasis { color: var(--lumi-sys-color--on-surface-de-emphasis, rgba(0, 0, 0, 0.62)); }

/* --- Data table (simple) --- */
.lumi-data-table-container { width: 100%; overflow-x: auto; border-radius: var(--lumi-sys-shape--medium, 12px); border: 1px solid var(--lumi-sys-color--stroke-default, rgba(0, 0, 0, 0.12)); }
.lumi-data-table { width: 100%; border-collapse: collapse; font-family: var(--ff-sans, sans-serif); font-size: 14px; text-align: left; }
.lumi-data-table th { padding: 12px 16px; font-weight: 600; background-color: var(--lumi-sys-color--surface-container, #f2f0f0); border-bottom: 1px solid var(--lumi-sys-color--stroke-default, rgba(0, 0, 0, 0.12)); color: var(--lumi-sys-color--on-surface-default, #000000); }
.lumi-data-table td { padding: 12px 16px; border-bottom: 1px solid var(--lumi-sys-color--stroke-default, rgba(0, 0, 0, 0.12)); color: var(--lumi-sys-color--on-surface-default, #000000); }
.lumi-data-table tr:last-child td { border-bottom-width: medium; border-bottom-style: none; border-bottom-color: currentcolor; }

/* --- Table widget (prose-style) --- */
.lumi-table-widget { display: flex; flex-direction: column; gap: var(--lumi-sys-spacing--xxl, 24px); width: 100%; }
.lumi-table-title { margin: 0px; color: var(--lumi-sys-color--on-surface-default, #000000); }
.lumi-table { width: 100%; border-collapse: collapse; font-family: var(--ff-sans, 'Google Sans Flex', sans-serif); text-align: left; }
.lumi-table th { padding: 12px 16px 12px 0px; font-size: 17px; line-height: 24px; font-weight: 540; font-variation-settings: "wght" 540, "wdth" 92, "opsz" 17; color: var(--lumi-sys-color--on-surface-default, #000000); border-bottom: 1px solid var(--lumi-sys-color--on-surface-low, rgba(0, 0, 0, 0.08)); }
.lumi-table td { padding: 16px 16px 16px 0px; font-size: 17px; line-height: 24px; font-weight: 400; font-variation-settings: "wght" 400, "wdth" 92, "opsz" 17; color: var(--lumi-sys-color--on-surface-default, #000000); border-bottom: 1px solid var(--lumi-sys-color--on-surface-low, rgba(0, 0, 0, 0.08)); }
.lumi-table td:last-child, .lumi-table th:last-child { padding-right: 0px; }
.lumi-table tr.lumi-table-ellipsis-row td { padding: 16px 0 0; border-bottom-width: medium; border-bottom-style: none; border-bottom-color: currentcolor; color: var(--lumi-sys-color--on-surface-variant, rgba(0, 0, 0, 0.62)); }

/* --- Luminous Spec Table (Figma 8543-1878) --- */
.lumi-spec-table-container { width: 100%; overflow-x: auto; background: transparent; }
.lumi-spec-table { width: 100%; border-collapse: collapse; font-family: var(--ff-sans, 'Google Sans Flex', sans-serif); text-align: left; background: transparent; }
.lumi-spec-table th { padding: 12px 28px 16px 0px; font-size: 17px; line-height: 24px; font-weight: 540; font-variation-settings: "wght" 540, "wdth" 100, "opsz" 17; color: var(--lumi-sys-color--on-surface-default, #000000); border-bottom: 1px solid var(--lumi-sys-color--on-surface-low, rgba(0, 0, 0, 0.08)); background: transparent; }
.lumi-spec-table td { padding: 16px 28px 16px 0px; border-bottom: 1px solid var(--lumi-sys-color--on-surface-low, rgba(0, 0, 0, 0.08)); vertical-align: top; background: transparent; }
.lumi-spec-table th:last-child, .lumi-spec-table td:last-child { padding-right: 0px; }
.lumi-spec-label { display: block; font-family: var(--ff-sans, 'Google Sans Flex', sans-serif); font-size: 13px; line-height: 17px; font-weight: 400; font-variation-settings: "wght" 400, "wdth" 92, "opsz" 13; color: var(--lumi-sys-color--on-surface-variant, rgba(0, 0, 0, 0.62)); margin-bottom: 2px; }
.lumi-spec-value { display: block; font-family: var(--ff-sans, 'Google Sans Flex', sans-serif); font-size: 15px; line-height: 20px; font-weight: 400; font-variation-settings: "wght" 400, "wdth" 92, "opsz" 15; color: var(--lumi-sys-color--on-surface-default, #000000); }
.lumi-spec-table-more { display: flex; align-items: center; justify-content: center; padding: 12px; color: var(--lumi-sys-color--on-surface-variant, rgba(0, 0, 0, 0.62)); font-size: 15px; line-height: 20px; cursor: pointer; }

/* --- Sortable Table Headers --- */
th[aria-sort] { color: var(--lumi-sys-color--on-surface-default, #000000); }
button.lumi-sort-btn, .lumi-sort-btn { all: unset; box-sizing: border-box; cursor: pointer; display: inline-flex; align-items: center; gap: 4px; font: inherit; color: inherit; letter-spacing: inherit; text-transform: inherit; text-align: inherit; width: 100%; justify-content: inherit; border-radius: var(--lumi-sys-shape--small, 4px); }
button.lumi-sort-btn:hover, .lumi-sort-btn:hover { background-color: var(--lumi-sys-color--on-surface-low, rgba(0, 0, 0, 0.06)) !important; }
button.lumi-sort-btn:focus-visible, .lumi-sort-btn:focus-visible { outline: 2px solid var(--lumi-sys-color--on-surface-default, #000000) !important; outline-offset: 2px !important; }

/* --- Code block --- */
.lumi-code-block { background-color: var(--lumi-sys-color--code-background, #000000); border-radius: var(--lumi-sys-shape--xl-max, 40px); padding: 32px; display: flex; flex-direction: column; gap: var(--lumi-sys-spacing--l, 16px); width: 100%; box-sizing: border-box; }
.lumi-code-header { display: flex; justify-content: space-between; align-items: center; width: 100%; }
.lumi-code-lang { font-family: var(--ff-sans, 'Google Sans Flex', sans-serif); font-size: 15px; font-weight: 500; font-variation-settings: "wght" 540, "wdth" 92, "opsz" 15; color: var(--lumi-sys-color--code-primary-text, #ffffff); }
.lumi-code-copy { background: transparent; border-width: medium; border-style: none; border-color: currentcolor; border-image: none; color: var(--lumi-sys-color--code-primary-text, #ffffff); cursor: pointer; display: flex; align-items: center; justify-content: center; padding: 4px; border-radius: var(--lumi-sys-shape--full, 999px); transition: background-color 0.2s; }
.lumi-code-copy:hover { background-color: rgba(255, 255, 255, 0.1); }
.lumi-code-snippet { margin: 0px; overflow-x: auto; width: 100%; }
.lumi-code-snippet code { font-family: var(--ff-mono, 'Google Sans Code', monospace); font-size: 15px; line-height: 20px; color: var(--lumi-sys-color--code-primary-text, #ffffff); display: block; white-space: pre; }

/* --- Section / prose --- */
.lumi-section { display: flex; flex-direction: column; align-items: stretch; width: 100%; }
.lumi-section h1 { font-family: var(--ff-sans, 'Google Sans Flex', sans-serif); font-size: 28px; line-height: 36px; font-weight: 350; font-variation-settings: "wght" 350, "wdth" 100, "opsz" 28; color: var(--lumi-sys-color--on-surface, #000000); margin-top: var(--lumi-sys-spacing--m, 12px); margin-bottom: var(--lumi-sys-spacing--xxl, 24px); }
.lumi-section h1:first-child { margin-top: 0px; }
.lumi-section h2 { font-family: var(--ff-sans, 'Google Sans Flex', sans-serif); font-size: 24px; line-height: 28px; font-weight: 380; font-variation-settings: "wght" 380, "wdth" 100, "opsz" 24; color: var(--lumi-sys-color--on-surface, #000000); margin-top: var(--lumi-sys-spacing--m, 12px); margin-bottom: var(--lumi-sys-spacing--m, 12px); }
.lumi-section h2:first-child { margin-top: 0px; }
.lumi-section h3 { font-family: var(--ff-sans, 'Google Sans Flex', sans-serif); font-size: 20px; line-height: 24px; font-weight: 470; font-variation-settings: "wght" 470, "wdth" 94, "opsz" 20; color: var(--lumi-sys-color--on-surface, #000000); margin-top: var(--lumi-sys-spacing--m, 12px); margin-bottom: var(--lumi-sys-spacing--xs, 4px); }
.lumi-section h3:first-child { margin-top: 0px; }
.lumi-section p { font-family: var(--ff-sans, 'Google Sans Flex', sans-serif); font-size: 17px; line-height: 24px; font-weight: 400; font-variation-settings: "wght" 400, "wdth" 92, "opsz" 17; color: var(--lumi-sys-color--on-surface, #000000); margin-top: 0px; margin-bottom: var(--lumi-sys-spacing--m, 12px); }
.lumi-section p:last-child { margin-bottom: 0px; }
.lumi-section ul { list-style: none; padding: 0px; margin: 0 0 var(--lumi-sys-spacing--m, 12px) 0; width: 100%; }
.lumi-section ul:last-child { margin-bottom: 0px; }
.lumi-section li { position: relative; padding-left: 40px; padding-bottom: 12px; font-family: var(--ff-sans, 'Google Sans Flex', sans-serif); font-size: 17px; line-height: 24px; font-weight: 400; font-variation-settings: "wght" 400, "wdth" 92, "opsz" 17; color: var(--lumi-sys-color--on-surface, #000000); box-sizing: border-box; }
.lumi-section li:last-child { padding-bottom: 0px; }
.lumi-section li::before { content: "○"; position: absolute; left: 3.5px; top: 0px; width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; font-family: var(--ff-mono, 'Google Sans Code', monospace); font-size: 15px; font-weight: 650; font-variation-settings: "MONO" 1, "wght" 650; color: var(--lumi-sys-color--on-surface, #000000); }
.lumi-section li ul { margin-top: 12px; margin-bottom: 0px; padding-left: 40px; }

/* --- Chart legend (1:1 series color match) --- */
.lumi-chart-header, .lumi-chart-title { margin-bottom: 32px; }
.lumi-chart-legend { display: flex; justify-content: center; align-items: center; gap: 24px; margin-top: 32px; padding-top: 0px; width: 100%; flex-wrap: wrap; }
.lumi-legend-item { display: inline-flex; align-items: center; gap: 8px; }
.lumi-legend-dot { width: 20px; height: 20px; display: inline-flex; align-items: center; justify-content: center; flex-shrink: 0; }
.lumi-legend-dot-swatch { width: 20px; height: 20px; border-radius: 50%; display: block; }
span.lumi-legend-dot[style*="background"] { width: 20px; height: 20px; border-radius: 50%; flex-shrink: 0; display: inline-block; }
.lumi-legend-label { font-family: var(--ff-mono, 'Google Sans Code', monospace); font-style: italic; font-size: 13px; font-weight: 400; line-height: 20px; color: var(--lumi-sys-color--on-surface, #000000); font-variation-settings: "wght" 400, "opsz" 13, "MONO" 0; font-feature-settings: "kern" 1, "liga" 1; white-space: nowrap; }

/* Canonical themed <select>. Uses element+class specificity (select.lumi-select)
   so it intentionally wins over any model hand-rolled `.lumi-select` rule: the
   runtime stylesheet is injected before widget <style> blocks, so a bare
   `.lumi-select` (same specificity, later) would otherwise override it. This
   provides appearance:none + a theme-neutral chevron so no native OS arrow leaks. */
select.lumi-select {
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  width: 100%;
  padding: var(--lumi-sys-spacing--s, 8px) 40px var(--lumi-sys-spacing--s, 8px)
    var(--lumi-sys-spacing--m, 12px);
  border: 1px solid var(--stroke-default);
  border-radius: var(--r-full, 999px);
  background-color: var(--surface);
  color: var(--on-surface);
  font-family: var(--ff-sans, 'Google Sans Flex', sans-serif);
  font-size: 15px;
  line-height: 20px;
  cursor: pointer;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%2380868b' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 14px center;
  background-size: 14px;
}
select.lumi-select:focus-visible {
  outline: 2px solid var(--lumi-sys-color--accent-fixed, #3186ff);
  outline-offset: 2px;
}

/* Toggle / filter chip. Models frequently emit `<button class="lumi-chip">`
   (or `.lumi-chip-btn`, `.lumi-filter-btn`, `[class^="lumi-chip-"]`, with
   `.is-active`/`.active`/`.is-selected`) for toggle pills; without a
   canonical rule these fall back to native (retro) browser button chrome.
   Theme-aware via runtime tokens so it is correct in light and dark. */
.lumi-chip,
[class^="lumi-chip"],
[class*=" lumi-chip"],
[class^="lumi-pill"],
[class*=" lumi-pill"] {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--lumi-sys-spacing--s, 8px);
  min-height: 32px;
  padding: 0 16px;
  font-family: var(--ff-sans, 'Google Sans Flex', 'Google Sans', sans-serif);
  font-size: 14px;
  font-weight: 500;
  line-height: 20px;
  color: var(--lumi-sys-color--on-surface-default, #1f1f1f);
  background: var(--lumi-sys-color--surface-dim, #f2f0f0);
  border: 1px solid transparent;
  border-radius: var(--lumi-sys-shape--full, 999px);
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
  box-sizing: border-box;
  transition: background-color 0.15s, color 0.15s, border-color 0.15s;
  -webkit-appearance: none;
  appearance: none;
}
.lumi-chip:hover,
[class^="lumi-chip"]:hover,
[class*=" lumi-chip"]:hover,
[class^="lumi-pill"]:hover,
[class*=" lumi-pill"]:hover {
  background: var(--lumi-sys-color--surface-container-high, #e6e6e6);
}
.lumi-chip.is-active,
.lumi-chip.active,
.lumi-chip.is-selected,
.lumi-chip.selected,
.lumi-chip[aria-pressed="true"],
.lumi-chip[aria-selected="true"],
.lumi-chip[aria-checked="true"],
[class^="lumi-chip"].is-active,
[class^="lumi-chip"].active,
[class^="lumi-chip"].is-selected,
[class^="lumi-chip"].selected,
[class^="lumi-chip"][aria-pressed="true"],
[class^="lumi-chip"][aria-selected="true"],
[class^="lumi-chip"][aria-checked="true"],
[class*=" lumi-chip"].is-active,
[class*=" lumi-chip"].active,
[class*=" lumi-chip"].is-selected,
[class*=" lumi-chip"].selected,
[class*=" lumi-chip"][aria-pressed="true"],
[class*=" lumi-chip"][aria-selected="true"],
[class*=" lumi-chip"][aria-checked="true"],
[class^="lumi-pill"].is-active,
[class^="lumi-pill"].active,
[class^="lumi-pill"].is-selected,
[class^="lumi-pill"].selected,
[class^="lumi-pill"][aria-pressed="true"],
[class^="lumi-pill"][aria-selected="true"],
[class^="lumi-pill"][aria-checked="true"],
[class*=" lumi-pill"].is-active,
[class*=" lumi-pill"].active,
[class*=" lumi-pill"].is-selected,
[class*=" lumi-pill"].selected,
[class*=" lumi-pill"][aria-pressed="true"],
[class*=" lumi-pill"][aria-selected="true"],
[class*=" lumi-pill"][aria-checked="true"] {
  color: var(--lumi-sys-color--on-surface-default, #000000);
  background: var(--lumi-sys-color--accent-container, #dcf1ff);
  border-color: var(--lumi-sys-color--primary, #3186ff);
  font-weight: 600;
}
.lumi-chip:focus-visible,
[class^="lumi-chip"]:focus-visible,
[class*=" lumi-chip"]:focus-visible,
[class^="lumi-pill"]:focus-visible,
[class*=" lumi-pill"]:focus-visible {
  outline: 2px solid var(--lumi-sys-color--accent-fixed, #3186ff);
  outline-offset: 2px;
}

/* ============================================================
 * DIAGRAM GUARD — SVG <text> is fill-only.
 *   An inherited group stroke (e.g. `.node:hover { stroke }` on a <g>)
 *   otherwise cascades into child <text>, thickening glyph outlines
 *   (fake-bold) and recoloring the label. Highlight strokes belong on
 *   shapes (rect/path); text never paints a stroke.
 * ============================================================ */
svg text { stroke: none; paint-order: fill; }

/* ============================================================
 * 6. HIGH CONTRAST MODE (Windows Forced Colors)
 *    Ensures buttons, selectable pills/tabs/segments, sliders, and switches
 *    remain clearly identifiable and convey active/selected state in
 *    @media (forced-colors: active).
 * ============================================================ */
@media (forced-colors: active) {
  button,
  .lumi-btn,
  [class^="lumi-btn-"],
  [class*=" lumi-btn-"],
  .lumi-chip,
  [class^="lumi-chip"],
  [class*=" lumi-chip"],
  [class^="lumi-pill"],
  [class*=" lumi-pill"],
  .lumi-segmented-btn,
  .lumi-tab {
    border: 1px solid ButtonBorder !important;
  }

  button.active,
  button.is-active,
  button.selected,
  button.is-selected,
  button[aria-pressed="true"],
  button[aria-selected="true"],
  button[aria-checked="true"],
  .lumi-btn.active,
  .lumi-btn.is-active,
  .lumi-btn.selected,
  .lumi-btn.is-selected,
  .lumi-btn[aria-pressed="true"],
  .lumi-btn[aria-selected="true"],
  .lumi-btn[aria-checked="true"],
  .lumi-chip.active,
  .lumi-chip.is-active,
  .lumi-chip.selected,
  .lumi-chip.is-selected,
  .lumi-chip[aria-pressed="true"],
  .lumi-chip[aria-selected="true"],
  .lumi-chip[aria-checked="true"],
  [class^="lumi-chip"].active,
  [class^="lumi-chip"].is-active,
  [class^="lumi-chip"].selected,
  [class^="lumi-chip"].is-selected,
  [class^="lumi-chip"][aria-pressed="true"],
  [class^="lumi-chip"][aria-checked="true"],
  [class*=" lumi-chip"].active,
  [class*=" lumi-chip"].is-active,
  [class*=" lumi-chip"].selected,
  [class*=" lumi-chip"].is-selected,
  [class*=" lumi-chip"][aria-pressed="true"],
  [class*=" lumi-chip"][aria-checked="true"],
  [class^="lumi-pill"].active,
  [class^="lumi-pill"].is-active,
  [class^="lumi-pill"][aria-pressed="true"],
  [class^="lumi-pill"][aria-checked="true"],
  [class*=" lumi-pill"].active,
  [class*=" lumi-pill"].is-active,
  [class*=" lumi-pill"][aria-pressed="true"],
  [class*=" lumi-pill"][aria-checked="true"],
  .lumi-segmented-btn.active,
  .lumi-segmented-btn.is-active,
  .lumi-segmented-btn.selected,
  .lumi-segmented-btn.is-selected,
  .lumi-segmented-btn[aria-pressed="true"],
  .lumi-segmented-btn[aria-selected="true"],
  .lumi-segmented-btn[aria-checked="true"],
  .lumi-tab.active,
  .lumi-tab.is-active,
  .lumi-tab.selected,
  .lumi-tab.is-selected,
  .lumi-tab[aria-pressed="true"],
  .lumi-tab[aria-selected="true"],
  .lumi-tab[aria-checked="true"] {
    forced-color-adjust: none;
    background-color: Highlight !important;
    color: HighlightText !important;
    border-color: Highlight !important;
    outline: 2px solid Highlight;
    outline-offset: -2px;
  }

  input[type="range"],
  .lumi-slider {
    forced-color-adjust: none;
    width: 100% !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
  }
  input[type="range"]::-webkit-slider-runnable-track,
  .lumi-slider::-webkit-slider-runnable-track {
    background-image: none !important;
    background-color: Canvas !important;
    border: 1px solid ButtonBorder !important;
    height: 6px !important;
  }
  input[type="range"]::-webkit-slider-thumb,
  .lumi-slider::-webkit-slider-thumb {
    background-image: none !important;
    background-color: ButtonText !important;
    border: 2px solid Canvas !important;
    outline: 2px solid ButtonBorder !important;
    width: 20px !important;
    height: 20px !important;
    margin-top: -8px !important;
  }
  input[type="range"]:hover::-webkit-slider-thumb,
  input[type="range"]:focus-visible::-webkit-slider-thumb,
  .lumi-slider:hover::-webkit-slider-thumb,
  .lumi-slider:focus-visible::-webkit-slider-thumb {
    background-color: Highlight !important;
    outline-color: Highlight !important;
  }

  .lumi-progress-bar {
    forced-color-adjust: none;
    background-color: Canvas !important;
    border: 1px solid ButtonBorder !important;
  }
  .lumi-progress-fill {
    forced-color-adjust: none;
    background-color: Highlight !important;
  }

  .lumi-switch__track {
    forced-color-adjust: none;
    background-color: Canvas !important;
    border: 2px solid ButtonBorder !important;
  }
  .lumi-switch__thumb,
  .lumi-switch__track::after {
    background-color: ButtonText !important;
  }
  .lumi-switch input[type="checkbox"]:checked + .lumi-switch__track {
    background-color: Highlight !important;
    border-color: Highlight !important;
  }
  .lumi-switch input[type="checkbox"]:checked + .lumi-switch__track .lumi-switch__thumb,
  .lumi-switch input[type="checkbox"]:checked + .lumi-switch__track::after {
    background-color: HighlightText !important;
  }

  .lumi-checkbox {
    forced-color-adjust: none;
    border: 2px solid ButtonBorder !important;
    background-color: Canvas !important;
  }
  .lumi-checkbox-label input[type="checkbox"]:checked ~ .lumi-checkbox,
  .lumi-checkbox-label input[type="checkbox"]:indeterminate ~ .lumi-checkbox {
    background-color: Highlight !important;
    border-color: Highlight !important;
  }
  .lumi-checkbox .lumi-checkmark {
    color: HighlightText !important;
    fill: HighlightText !important;
  }
}

</style>
<style id="lumi-surface-button-fallbacks">
.widget-container {
  width: 100% !important;
  max-width: 100% !important;
  padding-inline: 0 !important;
  box-sizing: border-box;
}
:root {
  --lumi-sys-color--surface-translucent: rgba(255, 255, 255, 0.88);
  --surface-translucent: var(--lumi-sys-color--surface-translucent, rgba(255, 255, 255, 0.88));
  --surface-glass: var(--lumi-sys-color--surface-translucent, rgba(255, 255, 255, 0.88));
}
:root[data-theme="dark"], body.dark-mode {
  --lumi-sys-color--surface-translucent: rgba(24, 24, 27, 0.88);
  --surface-translucent: rgba(24, 24, 27, 0.88);
  --surface-glass: rgba(24, 24, 27, 0.88);
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --lumi-sys-color--surface-translucent: rgba(24, 24, 27, 0.88);
    --surface-translucent: rgba(24, 24, 27, 0.88);
    --surface-glass: rgba(24, 24, 27, 0.88);
  }
}
button {
  appearance: none;
  -webkit-appearance: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  min-height: 36px;
  padding: 8px 18px;
  font-family: var(--ff-sans, 'Google Sans Flex', sans-serif);
  font-size: 13px;
  font-weight: 500;
  line-height: 18px;
  color: var(--on-surface, #000000);
  background-color: var(--lumi-sys-color--surface-bright, #ffffff);
  border: 1px solid var(--stroke-default, #e3e3e3);
  border-radius: 999px;
  cursor: pointer;
  box-sizing: border-box;
}
button:hover {
  background-color: var(--surface-container-high, #e6e6e6);
}
button.active, button.is-active, button.selected, button.is-selected, button[aria-pressed="true"], button[aria-selected="true"], button[aria-checked="true"] {
  background-color: var(--accent-container, #dcf1ff);
  color: var(--on-surface, #000000);
  border-color: var(--primary, #3186ff);
}
[role="application"]:focus-visible, [aria-roledescription*="chart"]:focus-visible {
  outline: 2px solid var(--primary, #3186ff) !important;
  outline-offset: 4px !important;
}
button.lumi-sort-btn, .lumi-sort-btn {
  all: unset;
  box-sizing: border-box;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font: inherit;
  color: inherit;
  letter-spacing: inherit;
  text-transform: inherit;
  text-align: inherit;
  width: 100%;
  justify-content: inherit;
  border-radius: 4px;
}
button.lumi-sort-btn:focus-visible, .lumi-sort-btn:focus-visible {
  outline: 2px solid var(--on-surface, #000000) !important;
  outline-offset: 2px !important;
}
.lumi-segmented-btn, .lumi-tab {
  border: 1px solid transparent;
}
.lumi-btn, [class^="lumi-btn-"], [class*=" lumi-btn-"] {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  min-height: 38px;
  padding: 8px 18px;
  background-color: var(--lumi-sys-color--surface-bright, #ffffff);
  color: var(--on-surface, #000000);
  border: 1px solid var(--stroke-default, #e3e3e3);
  border-radius: 999px;
  box-sizing: border-box;
}
.lumi-btn--primary, .lumi-btn-primary {
  background-color: var(--lumi-sys-color--accent, #9dd2ff);
  color: var(--lumi-sys-color--on-surface-default, #000000);
  border-color: transparent;
}
.lumi-btn--primary:hover, .lumi-btn-primary:hover {
  background-color: var(--lumi-sys-color--accent-container, #dcf1ff);
}
:where(.lumi-chip, [class^="lumi-chip"], [class*=" lumi-chip"], [class^="lumi-pill"], [class*=" lumi-pill"]) {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 32px;
  padding: 0 16px;
  font-family: var(--ff-sans, 'Google Sans Flex', sans-serif);
  font-size: 14px;
  font-weight: 500;
  color: var(--on-surface, #1f1f1f);
  background: var(--surface-dim, #f2f0f0);
  border: 1px solid transparent;
  border-radius: 999px;
  cursor: pointer;
}
.lumi-chip.is-active, .lumi-chip.active, .lumi-chip.is-selected, .lumi-chip.selected, .lumi-chip[aria-pressed="true"], .lumi-chip[aria-selected="true"], .lumi-chip[aria-checked="true"],
[class^="lumi-chip"].is-active, [class^="lumi-chip"].active, [class^="lumi-chip"].is-selected, [class^="lumi-chip"].selected, [class^="lumi-chip"][aria-pressed="true"], [class^="lumi-chip"][aria-selected="true"], [class^="lumi-chip"][aria-checked="true"],
[class*=" lumi-chip"].is-active, [class*=" lumi-chip"].active, [class*=" lumi-chip"].is-selected, [class*=" lumi-chip"].selected, [class*=" lumi-chip"][aria-pressed="true"], [class*=" lumi-chip"][aria-selected="true"], [class*=" lumi-chip"][aria-checked="true"],
[class^="lumi-pill"].is-active, [class^="lumi-pill"].active, [class^="lumi-pill"].is-selected, [class^="lumi-pill"].selected, [class^="lumi-pill"][aria-pressed="true"], [class^="lumi-pill"][aria-selected="true"], [class^="lumi-pill"][aria-checked="true"],
[class*=" lumi-pill"].is-active, [class*=" lumi-pill"].active, [class*=" lumi-pill"].is-selected, [class*=" lumi-pill"].selected, [class*=" lumi-pill"][aria-pressed="true"], [class*=" lumi-pill"][aria-selected="true"], [class*=" lumi-pill"][aria-checked="true"] {
  color: var(--on-surface, #000000);
  background: var(--accent-container, #dcf1ff);
  border-color: var(--primary, #3186ff);
  font-weight: 600;
}
@media (forced-colors: active) {
  button, .lumi-btn, .lumi-chip, [class^="lumi-chip"], [class*=" lumi-chip"], [class^="lumi-pill"], [class*=" lumi-pill"], .lumi-segmented-btn, .lumi-tab {
    border: 1px solid ButtonText !important;
  }
  button.active, button.is-active, button.selected, button.is-selected, button[aria-pressed="true"], button[aria-selected="true"], button[aria-checked="true"], .lumi-btn.active, .lumi-btn.is-active, .lumi-btn.selected, .lumi-btn.is-selected, .lumi-btn[aria-pressed="true"], .lumi-btn[aria-selected="true"], .lumi-btn[aria-checked="true"], .lumi-chip.is-active, .lumi-chip.active, .lumi-chip.is-selected, .lumi-chip.selected, .lumi-chip[aria-pressed="true"], .lumi-chip[aria-selected="true"], .lumi-chip[aria-checked="true"], .lumi-segmented-btn.is-active, .lumi-segmented-btn.active, .lumi-segmented-btn.is-selected, .lumi-segmented-btn.selected, .lumi-segmented-btn[aria-pressed="true"], .lumi-segmented-btn[aria-selected="true"], .lumi-segmented-btn[aria-checked="true"], .lumi-tab.active, .lumi-tab.is-active, .lumi-tab.selected, .lumi-tab.is-selected, .lumi-tab[aria-pressed="true"], .lumi-tab[aria-selected="true"], .lumi-tab[aria-checked="true"] {
    border: 2px solid Highlight !important;
  }
  .lumi-slider::-webkit-slider-runnable-track {
    border: 1px solid ButtonText !important;
  }
  .lumi-slider::-webkit-slider-thumb {
    border: 2px solid Highlight !important;
    background-color: ButtonText !important;
  }
}
</style>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HTTP Request-Response Security Flow</title>
<style>
  html, body {
    margin: 0;
    padding: 0;
    overflow-y: hidden;
  }

  .widget-container {
    width: 100%;
    max-width: 708px;
    margin-inline: auto;
    padding-inline: 0;
    overflow-x: hidden;
    display: flex;
    flex-direction: column;
    gap: var(--spacing-l, 16px);
    box-sizing: border-box;
  }

  .diagram-stage {
    background-color: var(--surface-bright);
    border-radius: var(--r-container, 40px);
    padding: var(--spacing-l, 16px);
    overflow: hidden;
  }

  .diagram-svg-wrap {
    position: relative;
    width: 100%;
    overflow: hidden;
  }

  .diagram-svg {
    width: 100%;
    max-width: 660px;
    height: auto;
    display: block;
    margin: 0 auto;
  }

  .diagram-svg text {
    stroke: none;
    paint-order: fill;
    user-select: none;
  }

  .gate-node rect,
  .endpoint-node rect {
    transition: fill 220ms ease, stroke 220ms ease, stroke-width 220ms ease;
  }

  .gate-node.is-passed rect {
    fill: var(--surface-dim);
    stroke: var(--positive);
    stroke-width: 1.5;
  }

  .gate-node.is-blocked-4xx rect {
    fill: var(--surface-dim);
    stroke: var(--chart-8);
    stroke-width: 2;
  }

  .gate-node.is-blocked-5xx rect {
    fill: var(--error-container);
    stroke: var(--error);
    stroke-width: 2;
  }

  .gate-node.is-idle rect {
    fill: var(--surface-dim);
    stroke: var(--stroke-default);
    stroke-width: 1;
  }

  .gate-node.is-dimmed {
    opacity: 0.42;
  }

  .response-node.is-2xx rect {
    fill: var(--positive-container);
    stroke: var(--positive);
    stroke-width: 1.8;
  }

  .response-node.is-4xx rect {
    fill: var(--surface-dim);
    stroke: var(--chart-8);
    stroke-width: 1.8;
  }

  .response-node.is-5xx rect {
    fill: var(--error-container);
    stroke: var(--error);
    stroke-width: 1.8;
  }

  .packet-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: var(--spacing-m, 12px);
  }

  @media (max-width: 540px) {
    .packet-grid {
      grid-template-columns: minmax(0, 1fr);
    }
  }

  .packet-panel {
    background-color: var(--surface-bright);
    border-radius: var(--r-l, 24px);
    padding: var(--spacing-l, 16px);
    display: flex;
    flex-direction: column;
    gap: var(--spacing-s, 8px);
    min-width: 0;
  }

  .packet-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: var(--spacing-s, 8px);
    flex-wrap: wrap;
  }

  .status-pill {
    display: inline-flex;
    align-items: center;
    padding: 4px 12px;
    border-radius: var(--r-full, 999px);
    font-family: var(--ff-mono);
    font-size: 13px;
    line-height: 17px;
    font-weight: 400;
  }

  .status-pill.is-2xx {
    background-color: var(--positive-container);
    color: var(--positive);
  }

  .status-pill.is-4xx {
    background-color: var(--surface-dim);
    color: var(--chart-8);
  }

  .status-pill.is-5xx {
    background-color: var(--error-container);
    color: var(--error);
  }

  .http-pre {
    margin: 0;
    padding: var(--spacing-m, 12px);
    background-color: var(--surface-dim);
    border-radius: var(--r-m, 16px);
    font-family: var(--ff-mono);
    font-size: 13px;
    line-height: 19px;
    color: var(--on-surface);
    white-space: pre-wrap;
    word-break: break-word;
    overflow-wrap: anywhere;
  }

  .security-note {
    margin: 0;
    color: var(--on-surface-variant);
  }

  .control-deck {
    background-color: var(--surface-bright);
    border-radius: var(--r-container, 40px);
    padding: var(--spacing-l, 16px) var(--spacing-xl, 20px);
    display: flex;
    flex-direction: column;
    gap: var(--spacing-m, 12px);
  }

  .control-group {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-s, 8px);
  }

  .control-group-label {
    color: var(--on-surface-variant);
    margin: 0;
  }

  .btn-row {
    display: flex;
    flex-wrap: wrap;
    gap: var(--spacing-s, 8px);
  }

  </style>
<script id="lumi-os-theme-init">
(function() {
  function syncBody() {
    var dt = document.documentElement.getAttribute('data-theme');
    if (document.body && (dt === 'dark' || dt === 'light')) {
      document.body.classList.toggle('dark-mode', dt === 'dark');
    }
  }
  function syncTheme(theme) {
    if (theme !== 'dark' && theme !== 'light') return;
    document.documentElement.setAttribute('data-theme', theme);
    syncBody();
  }
  if (typeof MutationObserver === 'function') {
    new MutationObserver(syncBody).observe(document.documentElement, {
      attributes: true, attributeFilter: ['data-theme']
    });
  }
  if (typeof document.addEventListener === 'function') {
    document.addEventListener('DOMContentLoaded', syncBody);
  }
  try {
    var mq = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)');
    if (mq) {
      var cur = document.documentElement.getAttribute('data-theme');
      if (!cur) {
        syncTheme(mq.matches ? 'dark' : 'light');
      } else {
        syncTheme(cur);
      }
      if (mq.addEventListener) {
        mq.addEventListener('change', function(e) {
          syncTheme(e.matches ? 'dark' : 'light');
        });
      }
    }
  } catch (e) {}
  window.addEventListener('message', function(e) {
    if (e.data && (e.data.type === 'set-theme' || e.data.type === 'APPLY_THEME') && e.data.theme) {
      syncTheme(e.data.theme);
    }
  });
})();
</script>
</head>
<body>
<div class="widget-container">

  <!-- Interactive SVG Sequence & Validation Pipeline -->
  <div class="diagram-stage" id="diagram-zone">
    <div class="diagram-svg-wrap">
      <svg id="flow-svg" class="diagram-svg" viewBox="0 0 660 396" role="img" aria-label="HTTP request and server security validation pipeline diagram">
        <defs>
          <marker id="lumi-caret" viewBox="0 0 10 10" refX="7.5" refY="5"
                  markerUnits="userSpaceOnUse" markerWidth="10" markerHeight="10" orient="auto">
            <path d="M 3 1.2 L 7.5 5 L 3 8.8" fill="none" stroke="var(--on-surface)"
                  stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
          </marker>
          <marker id="lumi-caret-muted" viewBox="0 0 10 10" refX="7.5" refY="5"
                  markerUnits="userSpaceOnUse" markerWidth="10" markerHeight="10" orient="auto">
            <path d="M 3 1.2 L 7.5 5 L 3 8.8" fill="none" stroke="var(--outline)"
                  stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
          </marker>
        </defs>

        <!-- Layer 1: Static & Dynamic Connectors (z-order: edges first) -->
        <g id="connectors-layer" pointer-events="none">
          <!-- Client -> Gate 1 (Route Check) -->
          <path id="edge-client-g1"
                d="M 176 184 L 188 184 Q 204 184 204 168 L 204 68 Q 204 52 220 52 L 228 52"
                fill="none" stroke="var(--on-surface)" stroke-width="1.3"
                stroke-linecap="round" stroke-dasharray="0 4" marker-end="url(#lumi-caret)"/>

          <!-- Gate 1 -> Gate 2 -->
          <line id="edge-g1-g2" x1="336" y1="84" x2="336" y2="104"
                stroke="var(--on-surface)" stroke-width="1.3"
                stroke-linecap="round" stroke-dasharray="0 4" marker-end="url(#lumi-caret)"/>

          <!-- Gate 2 -> Gate 3 -->
          <line id="edge-g2-g3" x1="336" y1="172" x2="336" y2="192"
                stroke="var(--on-surface)" stroke-width="1.3"
                stroke-linecap="round" stroke-dasharray="0 4" marker-end="url(#lumi-caret)"/>

          <!-- Gate 3 -> Gate 4 -->
          <line id="edge-g3-g4" x1="336" y1="260" x2="336" y2="280"
                stroke="var(--on-surface)" stroke-width="1.3"
                stroke-linecap="round" stroke-dasharray="0 4" marker-end="url(#lumi-caret)"/>

          <!-- Active Exit Path from halting/final gate -> Response -->
          <path id="edge-gate-resp"
                d="M 436 316 L 448 316 Q 464 316 464 300 L 464 200 Q 464 184 480 184 L 484 184"
                fill="none" stroke="var(--on-surface)" stroke-width="1.3"
                stroke-linecap="round" stroke-dasharray="0 4" marker-end="url(#lumi-caret)"/>

          <!-- Return Response Path along bottom -> Client -->
          <path id="edge-resp-client"
                d="M 564 244 L 564 360 Q 564 376 548 376 L 112 376 Q 96 376 96 360 L 96 240"
                fill="none" stroke="var(--on-surface)" stroke-width="1.3"
                stroke-linecap="round" stroke-dasharray="0 4" marker-end="url(#lumi-caret)"/>
        </g>

        <!-- Layer 2: Label Pills on Connectors -->
        <g id="pills-layer" pointer-events="none">
          <rect id="return-pill-bg" x="284" y="366" width="104" height="20" rx="10" fill="var(--surface-dim)"/>
          <text id="return-pill-text" x="336" y="380" text-anchor="middle"
                font-family="var(--ff-mono)" font-size="13" font-style="italic" fill="var(--on-surface)">200 OK</text>
        </g>

        <!-- Layer 3: Nodes -->
        <g id="nodes-layer">
          <!-- Client Node (Left) -->
          <g class="endpoint-node" id="node-client">
            <rect x="16" y="136" width="152" height="96" rx="40"
                  fill="var(--accent-container)" stroke="var(--primary)" stroke-width="1.5"/>
            <text x="92" y="176" text-anchor="middle" font-family="var(--ff-sans)" font-size="15" font-weight="400" fill="var(--on-surface)">Client</text>
            <text id="svg-client-sub" x="92" y="198" text-anchor="middle" font-family="var(--ff-mono)" font-size="13" font-style="italic" fill="var(--on-surface)">POST /login</text>
          </g>

          <!-- Gate 1: Route Check -->
          <g class="gate-node is-passed" id="gate-route">
            <rect x="236" y="20" width="200" height="64" rx="32" fill="var(--surface-dim)"/>
            <text x="336" y="48" text-anchor="middle" font-family="var(--ff-sans)" font-size="15" font-weight="400" fill="var(--on-surface)">1. Route Check</text>
            <text id="gate-route-sub" x="336" y="67" text-anchor="middle" font-family="var(--ff-mono)" font-size="13" font-style="italic" fill="var(--on-surface-variant)">matched /login</text>
          </g>

          <!-- Gate 2: JSON Parser -->
          <g class="gate-node is-passed" id="gate-parser">
            <rect x="236" y="108" width="200" height="64" rx="32" fill="var(--surface-dim)"/>
            <text x="336" y="136" text-anchor="middle" font-family="var(--ff-sans)" font-size="15" font-weight="400" fill="var(--on-surface)">2. JSON Parser</text>
            <text id="gate-parser-sub" x="336" y="155" text-anchor="middle" font-family="var(--ff-mono)" font-size="13" font-style="italic" fill="var(--on-surface-variant)">valid payload</text>
          </g>

          <!-- Gate 3: Auth/Session Check -->
          <g class="gate-node is-passed" id="gate-auth">
            <rect x="236" y="196" width="200" height="64" rx="32" fill="var(--surface-dim)"/>
            <text x="336" y="224" text-anchor="middle" font-family="var(--ff-sans)" font-size="15" font-weight="400" fill="var(--on-surface)">3. Auth Check</text>
            <text id="gate-auth-sub" x="336" y="243" text-anchor="middle" font-family="var(--ff-mono)" font-size="13" font-style="italic" fill="var(--on-surface-variant)">public route</text>
          </g>

          <!-- Gate 4: Role Permission Check -->
          <g class="gate-node is-passed" id="gate-role">
            <rect x="236" y="284" width="200" height="64" rx="32" fill="var(--surface-dim)"/>
            <text x="336" y="312" text-anchor="middle" font-family="var(--ff-sans)" font-size="15" font-weight="400" fill="var(--on-surface)">4. Role Check</text>
            <text id="gate-role-sub" x="336" y="331" text-anchor="middle" font-family="var(--ff-mono)" font-size="13" font-style="italic" fill="var(--on-surface-variant)">session issued</text>
          </g>

          <!-- Server Response Node (Right) -->
          <g class="endpoint-node response-node is-2xx" id="node-response">
            <rect x="492" y="136" width="152" height="96" rx="40"
                  fill="var(--positive-container)" stroke="var(--positive)" stroke-width="1.8"/>
            <text id="svg-resp-code" x="568" y="176" text-anchor="middle" font-family="var(--ff-sans)" font-size="15" font-weight="400" fill="var(--on-surface)">200 OK</text>
            <text id="svg-resp-sub" x="568" y="198" text-anchor="middle" font-family="var(--ff-mono)" font-size="13" font-style="italic" fill="var(--on-surface)">Allowed</text>
          </g>
        </g>

        <!-- Layer 4: Animated Packet Dot -->
        <g id="packet-layer" pointer-events="none">
          <circle id="anim-packet" cx="92" cy="184" r="6" fill="var(--primary)"/>
        </g>
      </svg>
    </div>
  </div>

  <!-- Live HTTP Request & Response Inspector -->
  <div class="packet-grid">
    <section class="packet-panel" aria-label="HTTP Request Preview">
      <div class="packet-header">
        <span class="lumi-body-m">HTTP Request</span>
        <span class="lumi-caption" id="req-meta">Client &rarr; Server</span>
      </div>
      <pre class="http-pre" id="http-request-text">POST /login HTTP/1.1
Host: api.example.com
Content-Type: application/json

{"user": "alice", "pass": "***"}</pre>
    </section>

    <section class="packet-panel" aria-label="HTTP Response Preview">
      <div class="packet-header">
        <span class="lumi-body-m">HTTP Response</span>
        <span class="status-pill is-2xx" id="resp-status-badge">200 OK</span>
      </div>
      <pre class="http-pre" id="http-response-text">HTTP/1.1 200 OK
Set-Cookie: session=abc123; HttpOnly; Secure
Content-Type: application/json

{"status": "authenticated"}</pre>
      <p class="lumi-body-s security-note" id="security-explanation">Credentials verified. Server issues an HttpOnly, Secure session cookie to prevent client-side script theft.</p>
    </section>
  </div>

  <!-- Control Deck -->
  <div class="control-deck">
    <div class="control-group">
      <p class="lumi-body-s control-group-label" id="lbl-endpoint">Endpoint &amp; Method</p>
      <div class="btn-row" role="radiogroup" aria-labelledby="lbl-endpoint" data-group="endpoint">
        <button type="button" class="lumi-btn lumi-btn--tonal lumi-btn--small is-selected" role="radio" aria-checked="true" tabindex="0" data-method="POST" data-endpoint="/login">/login (POST)</button>
        <button type="button" class="lumi-btn lumi-btn--tonal lumi-btn--small" role="radio" aria-checked="false" tabindex="-1" data-method="GET" data-endpoint="/admin">/admin (GET)</button>
        <button type="button" class="lumi-btn lumi-btn--tonal lumi-btn--small" role="radio" aria-checked="false" tabindex="-1" data-method="DELETE" data-endpoint="/admin">/admin (DELETE)</button>
        <button type="button" class="lumi-btn lumi-btn--tonal lumi-btn--small" role="radio" aria-checked="false" tabindex="-1" data-method="GET" data-endpoint="/unknown">/unknown (GET)</button>
      </div>
    </div>

    <div class="control-group">
      <p class="lumi-body-s control-group-label" id="lbl-auth">Cookie / Auth</p>
      <div class="btn-row" role="radiogroup" aria-labelledby="lbl-auth" data-group="auth">
        <button type="button" class="lumi-btn lumi-btn--tonal lumi-btn--small is-selected" role="radio" aria-checked="true" tabindex="0" data-auth="None">No Cookie</button>
        <button type="button" class="lumi-btn lumi-btn--tonal lumi-btn--small" role="radio" aria-checked="false" tabindex="-1" data-auth="Valid User Cookie">User Cookie</button>
        <button type="button" class="lumi-btn lumi-btn--tonal lumi-btn--small" role="radio" aria-checked="false" tabindex="-1" data-auth="Admin Cookie">Admin Cookie</button>
      </div>
    </div>

    <div class="control-group">
      <p class="lumi-body-s control-group-label" id="lbl-payload">Payload</p>
      <div class="btn-row" role="radiogroup" aria-labelledby="lbl-payload" data-group="payload">
        <button type="button" class="lumi-btn lumi-btn--tonal lumi-btn--small is-selected" role="radio" aria-checked="true" tabindex="0" data-payload="Valid JSON">Valid JSON</button>
        <button type="button" class="lumi-btn lumi-btn--tonal lumi-btn--small" role="radio" aria-checked="false" tabindex="-1" data-payload="Malformed JSON">Malformed JSON</button>
        <button type="button" class="lumi-btn lumi-btn--tonal lumi-btn--small" role="radio" aria-checked="false" tabindex="-1" data-payload="Server Crash Input">Trigger Crash</button>
      </div>
    </div>
  </div>

</div>

<script>
function getCssVar(name) {
  if (!name) return '';
  const clean = name.replace(/^var\(/, '').replace(/\)$/, '').trim();
  return getComputedStyle(document.documentElement).getPropertyValue(clean.startsWith('--') ? clean : '--' + clean).trim();
}

const VALID_ENDPOINTS = ['/login', '/admin', '/unknown'];
const VALID_METHODS = ['GET', 'POST', 'DELETE'];
const VALID_AUTH = ['None', 'Valid User Cookie', 'Admin Cookie'];
const VALID_PAYLOAD = ['Valid JSON', 'Malformed JSON', 'Server Crash Input'];

const state = {
  method: 'POST',
  endpoint: '/login',
  authState: 'None',
  payloadState: 'Valid JSON'
};

function evaluatePipeline(s) {
  let code = 200;
  let text = 'OK';
  let category = '2xx';
  let stopGate = 4; // 1=Route, 2=Parser, 3=Auth, 4=Role
  let blocked = false;
  let respHeaders = 'Content-Type: application/json';
  let respBody = '{"status": "ok"}';
  let explanation = '';
  const gateSubs = {
    route: 'matched ' + s.endpoint,
    parser: 'valid payload',
    auth: s.authState === 'None' ? 'no cookie' : (s.authState === 'Admin Cookie' ? 'admin session' : 'user session'),
    role: 'permitted'
  };

  if (s.endpoint === '/unknown') {
    code = 404;
    text = 'Not Found';
    category = '4xx';
    stopGate = 1;
    blocked = true;
    gateSubs.route = 'no matching route';
    gateSubs.parser = 'skipped';
    gateSubs.auth = 'skipped';
    gateSubs.role = 'skipped';
    respBody = '{"error": "route_not_found"}';
    explanation = 'Rejected at Route Check. Unknown endpoints fail fast before parsing or touching auth logic.';
  } else if (s.payloadState === 'Malformed JSON') {
    code = 400;
    text = 'Bad Request';
    category = '4xx';
    stopGate = 2;
    blocked = true;
    gateSubs.parser = 'syntax error';
    gateSubs.auth = 'skipped';
    gateSubs.role = 'skipped';
    respBody = '{"error": "invalid_json"}';
    explanation = 'Rejected at JSON Parser. Strict schema and syntax validation stops malformed input early.';
  } else if (s.payloadState === 'Server Crash Input') {
    code = 500;
    text = 'Internal Server Error';
    category = '5xx';
    stopGate = 2;
    blocked = true;
    gateSubs.parser = 'unhandled exception';
    gateSubs.auth = 'skipped';
    gateSubs.role = 'skipped';
    respBody = '{"error": "internal_error"}';
    explanation = 'Unhandled server exception. Return a generic 500 without leaking stack traces to the client.';
  } else if (s.endpoint === '/admin' && s.authState === 'None') {
    code = 401;
    text = 'Unauthorized';
    category = '4xx';
    stopGate = 3;
    blocked = true;
    gateSubs.auth = 'missing session';
    gateSubs.role = 'skipped';
    respHeaders = 'WWW-Authenticate: Cookie\nContent-Type: application/json';
    respBody = '{"error": "auth_required"}';
    explanation = 'Blocked at Auth Check. Protected routes require a valid session cookie proving identity (401).';
  } else if (s.endpoint === '/admin' && s.authState === 'Valid User Cookie') {
    code = 403;
    text = 'Forbidden';
    category = '4xx';
    stopGate = 4;
    blocked = true;
    gateSubs.role = 'requires admin';
    respBody = '{"error": "insufficient_role"}';
    explanation = 'Blocked at Role Check. The user is authenticated, but lacks admin privileges for this action (403).';
  } else if (s.method === 'POST' && s.endpoint === '/login') {
    code = 200;
    text = 'OK';
    category = '2xx';
    stopGate = 4;
    blocked = false;
    gateSubs.auth = 'public route';
    gateSubs.role = 'session issued';
    respHeaders = 'Set-Cookie: session=abc123; HttpOnly; Secure\nContent-Type: application/json';
    respBody = '{"status": "authenticated"}';
    explanation = 'Credentials verified. Server issues an HttpOnly, Secure session cookie to prevent script theft.';
  } else if (s.method === 'POST') {
    code = 201;
    text = 'Created';
    category = '2xx';
    stopGate = 4;
    blocked = false;
    gateSubs.role = 'admin granted';
    respBody = '{"status": "created"}';
    explanation = 'All security checks passed. Resource created successfully with verified admin scope.';
  } else {
    code = 200;
    text = 'OK';
    category = '2xx';
    stopGate = 4;
    blocked = false;
    gateSubs.role = 'admin granted';
    respBody = s.method === 'DELETE' ? '{"status": "deleted"}' : '{"data": "admin_panel"}';
    explanation = 'All security checks passed. Valid admin cookie authorized the ' + s.method + ' operation.';
  }

  return { code, text, category, stopGate, blocked, respHeaders, respBody, explanation, gateSubs };
}

function buildRequestText(s) {
  const lines = [s.method + ' ' + s.endpoint + ' HTTP/1.1', 'Host: api.example.com'];
  if (s.authState === 'Valid User Cookie') {
    lines.push('Cookie: session=usr_8f2a; role=user');
  } else if (s.authState === 'Admin Cookie') {
    lines.push('Cookie: session=adm_9c4e; role=admin');
  }
  if (s.method !== 'GET' || s.payloadState !== 'Valid JSON') {
    lines.push('Content-Type: application/json');
  }
  lines.push('');
  if (s.payloadState === 'Malformed JSON') {
    lines.push('{"user": "alice", broken');
  } else if (s.payloadState === 'Server Crash Input') {
    lines.push('{"__proto__": {"crash": true}}');
  } else if (s.endpoint === '/login') {
    lines.push('{"user": "alice", "pass": "***"}');
  } else if (s.method === 'DELETE') {
    lines.push('{"targetId": 42}');
  } else {
    lines.push('(no body)');
  }
  return lines.join('\n');
}

// Packet animation state
let animFrameId = null;
let animStartTime = 0;
let activeSegments = [];
let activeRespCategory = '2xx';

function buildAnimationSegments(stopGate) {
  const gateY = { 1: 52, 2: 140, 3: 228, 4: 316 };
  const exitY = gateY[stopGate];

  // Update exit path geometry dynamically
  const exitPath = document.getElementById('edge-gate-resp');
  if (exitY < 184) {
    exitPath.setAttribute('d', `M 436 ${exitY} L 448 ${exitY} Q 464 ${exitY} 464 ${exitY + 16} L 464 168 Q 464 184 480 184 L 484 184`);
  } else {
    exitPath.setAttribute('d', `M 436 ${exitY} L 448 ${exitY} Q 464 ${exitY} 464 ${exitY - 16} L 464 200 Q 464 184 480 184 L 484 184`);
  }

  const segs = [];
  const eC1 = document.getElementById('edge-client-g1');
  if (eC1) segs.push({ el: eC1, phase: 'req' });
  if (stopGate >= 2) segs.push({ el: document.getElementById('edge-g1-g2'), phase: 'req' });
  if (stopGate >= 3) segs.push({ el: document.getElementById('edge-g2-g3'), phase: 'req' });
  if (stopGate >= 4) segs.push({ el: document.getElementById('edge-g3-g4'), phase: 'req' });
  segs.push({ el: exitPath, phase: 'resp' });
  segs.push({ el: document.getElementById('edge-resp-client'), phase: 'resp' });
  return segs;
}

function getCategoryColor(cat) {
  if (cat === '2xx') return getCssVar('--positive') || '#008052';
  if (cat === '4xx') return getCssVar('--chart-8') || '#997112';
  return getCssVar('--error') || '#de2d29';
}

function startPacketAnimation(stopGate, category) {
  if (animFrameId) cancelAnimationFrame(animFrameId);
  activeSegments = buildAnimationSegments(stopGate);
  activeRespCategory = category;
  animStartTime = performance.now();

  const dot = document.getElementById('anim-packet');
  const totalDur = 2400;

  function step(now) {
    const elapsed = (now - animStartTime) % totalDur;
    const progress = elapsed / totalDur;
    const segCount = activeSegments.length;
    const scaled = progress * segCount;
    const idx = Math.min(segCount - 1, Math.floor(scaled));
    const localT = scaled - idx;
    const seg = activeSegments[idx];

    if (seg && seg.el && typeof seg.el.getTotalLength === 'function') {
      const len = seg.el.getTotalLength();
      const pt = seg.el.getPointAtLength(localT * len);
      dot.setAttribute('cx', pt.x.toFixed(1));
      dot.setAttribute('cy', pt.y.toFixed(1));
      const color = seg.phase === 'req'
        ? (getCssVar('--primary') || '#3186ff')
        : getCategoryColor(activeRespCategory);
      dot.setAttribute('fill', color);
    }
    animFrameId = requestAnimationFrame(step);
  }
  animFrameId = requestAnimationFrame(step);
}

function updateViz() {
  try {
    const res = evaluatePipeline(state);

    // 1. Update SVG Client & Response nodes
    document.getElementById('svg-client-sub').textContent = state.method + ' ' + state.endpoint;
    document.getElementById('svg-resp-code').textContent = res.code + ' ' + res.text;
    document.getElementById('svg-resp-sub').textContent = res.blocked ? 'Blocked' : 'Allowed';
    document.getElementById('return-pill-text').textContent = res.code + ' ' + res.text;

    const pillW = Math.max(84, (res.code + ' ' + res.text).length * 7.8 + 20);
    const pillBg = document.getElementById('return-pill-bg');
    pillBg.setAttribute('width', pillW);
    pillBg.setAttribute('x', (336 - pillW / 2).toFixed(1));

    const respNode = document.getElementById('node-response');
    respNode.classList.remove('is-2xx', 'is-4xx', 'is-5xx');
    respNode.classList.add('is-' + res.category);

    // 2. Update 4 Gate Nodes
    const gates = [
      { id: 'gate-route', subId: 'gate-route-sub', idx: 1, sub: res.gateSubs.route },
      { id: 'gate-parser', subId: 'gate-parser-sub', idx: 2, sub: res.gateSubs.parser },
      { id: 'gate-auth', subId: 'gate-auth-sub', idx: 3, sub: res.gateSubs.auth },
      { id: 'gate-role', subId: 'gate-role-sub', idx: 4, sub: res.gateSubs.role }
    ];

    gates.forEach(g => {
      const el = document.getElementById(g.id);
      document.getElementById(g.subId).textContent = g.sub;
      el.classList.remove('is-passed', 'is-blocked-4xx', 'is-blocked-5xx', 'is-idle', 'is-dimmed');

      if (g.idx < res.stopGate) {
        el.classList.add('is-passed');
      } else if (g.idx === res.stopGate) {
        if (res.blocked) {
          el.classList.add(res.category === '5xx' ? 'is-blocked-5xx' : 'is-blocked-4xx');
        } else {
          el.classList.add('is-passed');
        }
      } else {
        el.classList.add('is-idle', 'is-dimmed');
      }
    });

    // Dim unused inter-gate edges
    const edges = [
      { id: 'edge-g1-g2', minGate: 2 },
      { id: 'edge-g2-g3', minGate: 3 },
      { id: 'edge-g3-g4', minGate: 4 }
    ];
    edges.forEach(e => {
      const line = document.getElementById(e.id);
      const active = res.stopGate >= e.minGate;
      line.setAttribute('opacity', active ? '1' : '0.25');
      line.setAttribute('marker-end', active ? 'url(#lumi-caret)' : 'url(#lumi-caret-muted)');
    });

    // 3. Update Live HTTP Request & Response Inspector
    document.getElementById('http-request-text').textContent = buildRequestText(state);
    document.getElementById('http-response-text').textContent =
      'HTTP/1.1 ' + res.code + ' ' + res.text + '\n' + res.respHeaders + '\n\n' + res.respBody;

    const badge = document.getElementById('resp-status-badge');
    if (badge) badge.textContent = res.code + ' ' + res.text;
    badge.classList.remove('is-2xx', 'is-4xx', 'is-5xx');
    badge.classList.add('is-' + res.category);

    document.getElementById('security-explanation').textContent = res.explanation;

    // 4. Restart packet animation along active route
    startPacketAnimation(res.stopGate, res.category);
  } catch (err) {
    console.error('Render error:', err);
  }
}

function syncControlsFromState() {
  document.querySelectorAll('[data-group="endpoint"] button').forEach(btn => {
    const match = btn.dataset.method === state.method && btn.dataset.endpoint === state.endpoint;
    btn.classList.toggle('is-selected', match);
    btn.setAttribute('aria-checked', match ? 'true' : 'false');
    btn.setAttribute('tabindex', match ? '0' : '-1');
  });

  document.querySelectorAll('[data-group="auth"] button').forEach(btn => {
    const match = btn.dataset.auth === state.authState;
    btn.classList.toggle('is-selected', match);
    btn.setAttribute('aria-checked', match ? 'true' : 'false');
    btn.setAttribute('tabindex', match ? '0' : '-1');
  });

  document.querySelectorAll('[data-group="payload"] button').forEach(btn => {
    const match = btn.dataset.payload === state.payloadState;
    btn.classList.toggle('is-selected', match);
    btn.setAttribute('aria-checked', match ? 'true' : 'false');
    btn.setAttribute('tabindex', match ? '0' : '-1');
  });
}

function saveUserState() {
  if (window.pageVault && typeof window.pageVault.save === 'function') {
    window.pageVault.save('viz.state', { ...state }).catch(() => {});
  }
}

function applySavedState(raw) {
  if (typeof raw === 'string') { try { raw = JSON.parse(raw); } catch (_) { return false; } }
  if (!raw || typeof raw !== 'object' || Array.isArray(raw)) return false;
  if (VALID_METHODS.includes(raw.method)) state.method = raw.method;
  if (VALID_ENDPOINTS.includes(raw.endpoint)) state.endpoint = raw.endpoint;
  if (VALID_AUTH.includes(raw.authState)) state.authState = raw.authState;
  if (VALID_PAYLOAD.includes(raw.payloadState)) state.payloadState = raw.payloadState;
  syncControlsFromState();
  updateViz();
  return true;
}

// Wire radiogroup clicks + Arrow-key navigation
document.querySelectorAll('.btn-row[role="radiogroup"]').forEach(group => {
  const buttons = Array.from(group.querySelectorAll('button[role="radio"]'));
  buttons.forEach((btn, idx) => {
    btn.addEventListener('click', () => {
      const grp = group.dataset.group;
      if (grp === 'endpoint') {
        state.method = btn.dataset.method;
        state.endpoint = btn.dataset.endpoint;
      } else if (grp === 'auth') {
        state.authState = btn.dataset.auth;
      } else if (grp === 'payload') {
        state.payloadState = btn.dataset.payload;
      }
      syncControlsFromState();
      updateViz();
      saveUserState();
    });

    btn.addEventListener('keydown', (e) => {
      if (!['ArrowRight', 'ArrowDown', 'ArrowLeft', 'ArrowUp'].includes(e.key)) return;
      e.preventDefault();
      const dir = (e.key === 'ArrowRight' || e.key === 'ArrowDown') ? 1 : -1;
      const next = buttons[(idx + dir + buttons.length) % buttons.length];
      next.focus();
      next.click();
    });
  });
});

// Hydrate persisted state before first render
(async function hydrateState() {
  if (!window.pageVault) { syncControlsFromState(); updateViz(); return; }
  if (typeof window.pageVault.onRestore === 'function') {
    window.pageVault.onRestore(async () => {
      const next = await window.pageVault.load('viz.state');
      if (next !== undefined) applySavedState(next);
    });
  }
  try {
    await window.pageVault.ready;
    const saved = await window.pageVault.load('viz.state');
    if (saved !== undefined && applySavedState(saved)) return;
  } catch (_) {}
  syncControlsFromState();
  updateViz();
})();

// Dynamic Theme Sync & Iframe Auto-Resize
const applyTheme = t => { document.documentElement.setAttribute('data-theme', t); if (typeof updateViz === 'function') updateViz(); };
if (!document.documentElement.hasAttribute('data-theme') && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) applyTheme('dark');
window.addEventListener('message', e => { if (e.data && (e.data.type === 'set-theme' || e.data.type === 'APPLY_THEME')) applyTheme(e.data.theme); });
(function autoResize() {
  function notifyHeight() {
    const root = document.querySelector('.widget-container') || document.body;
    const h = Math.ceil(Math.max(root.getBoundingClientRect().bottom, root.scrollHeight));
    window.parent.postMessage({ type: 'widget-resize', height: h }, '*');
  }
  window.addEventListener('load', () => setTimeout(notifyHeight, 120));
  new ResizeObserver(notifyHeight).observe(document.documentElement);
})();
</script>

<script>/*luminous-slider-normalizer*/(function(){function f(r){if(!r||r.type!=='range')return;var mn=parseFloat(r.min||'0'),mx=parseFloat(r.max||'100'),v=parseFloat(r.value);if(isNaN(v))v=(mn+mx)/2;var p=mx>mn?((v-mn)/(mx-mn))*100:50;r.style.setProperty('--progress',p+'%');r.style.removeProperty('--slider-fill');}function all(){document.querySelectorAll('input[type="range"], .lumi-slider').forEach(f);}document.addEventListener('input',function(e){f(e.target);});document.addEventListener('change',function(e){f(e.target);});window.addEventListener('message',function(e){var d=e&&e.data;if(d&&(d.type==='SUPPLEMENTAL_DATA_UPDATE'||d.type==='RESTORE_STATE')){all();setTimeout(all,0);setTimeout(all,50);}});if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',function(){all();setTimeout(all,0);});else{all();setTimeout(all,0);}})();</script>

<script id="lumi-a11y-normalizer">(function(){
var lastLiveMsg='';
var liveToggle=false;
function getOrCreateChartLive(){
  var live=document.getElementById('lumi-chart-live');
  if(!live&&document.body){
    live=document.createElement('div');
    live.id='lumi-chart-live';
    live.setAttribute('role','status');
    live.setAttribute('aria-live','polite');
    live.setAttribute('aria-atomic','true');
    live.style.cssText='position:absolute;width:1px;height:1px;padding:0;margin:-1px;clip:rect(0,0,0,0);clip-path:inset(50%);white-space:nowrap;border:0;';
    document.body.appendChild(live);
  }
  return live;
}
function announceChartMsg(msg){
  var live=getOrCreateChartLive();
  if(!live||!msg)return;
  if(msg===lastLiveMsg)liveToggle=!liveToggle;
  else{lastLiveMsg=msg;liveToggle=false;}
  while(live.childNodes.length)live.removeChild(live.childNodes[0]);
  live.appendChild(document.createTextNode(liveToggle?(msg+'\u00a0'):msg));
}
function showChartKbdBadge(anchorEl,msg){
  try{
    var wrap=(anchorEl&&anchorEl.parentElement)||document.body;
    if(!wrap)return;
    var cs=window.getComputedStyle?window.getComputedStyle(wrap):null;
    if(cs&&cs.position==='static')wrap.style.position='relative';
    var badge=wrap.querySelector('.lumi-chart-kbd-tip');
    if(!msg){
      if(badge)badge.style.display='none';
      return;
    }
    if(!badge){
      badge=document.createElement('div');
      badge.className='lumi-chart-kbd-tip';
      badge.setAttribute('aria-hidden','true');
      badge.style.cssText='position:absolute;top:8px;right:8px;z-index:20;max-width:88%;padding:6px 12px;border-radius:8px;font-family:var(--ff-sans,sans-serif);font-size:13px;font-weight:500;line-height:18px;background:var(--surface-bright,#ffffff);color:var(--on-surface,#000000);border:1px solid var(--primary,#3186ff);box-shadow:0 2px 8px rgba(0,0,0,0.14);pointer-events:none;';
      wrap.appendChild(badge);
    }
    badge.style.display='block';
    while(badge.childNodes.length)badge.removeChild(badge.childNodes[0]);
    badge.appendChild(document.createTextNode(msg));
  }catch(e){}
}
function syncSliders(){
  try{
    document.querySelectorAll('input[type="range"], .lumi-slider').forEach(function(r){
      if(!r||r.type!=='range')return;
      var mn=parseFloat(r.min||'0'),mx=parseFloat(r.max||'100'),v=parseFloat(r.value);
      if(isNaN(v))v=(mn+mx)/2;
      var p=mx>mn?((v-mn)/(mx-mn))*100:50;
      r.style.setProperty('--progress',p+'%');
      r.style.removeProperty('--slider-fill');
    });
  }catch(e){}
}
var isSyncingA11y=false;
var kSelectableClsRe=new RegExp('\\b(lumi-segmented-\\w+|lumi-'+'chip\\S*|lumi-pill\\S*|togglable|toggle-btn|filter-btn|mode-btn|strategy-btn|tab-btn|option-btn|pill|chip)\\b','i');
var kActiveTokenRe=/^(?:is-|btn-|chip-|tab-|pill-|mode-|seg-|filter-|opt-|strategy-)?(?:active|selected|current)(?:-\w+)?$/i;
var kActionBtnTxtRe=/^(?:reset|clear|cancel|submit|apply|calculate|run|play|pause|stop|step|next|prev|previous|back|close|delete|remove|add|export|copy|share|download|save|undo|redo|randomize)\b/i;
function hasActiveClass(b){
  if(!b||b.nodeType!==1)return false;
  if(b.getAttribute('data-active')==='true'||b.getAttribute('data-selected')==='true')return true;
  var cls=typeof b.className==='string'?b.className:'';
  if(!cls)return false;
  var toks=cls.trim().split(/\s+/);
  for(var i=0;i<toks.length;i++){
    if(kActiveTokenRe.test(toks[i]))return true;
  }
  return false;
}
function hasSelectableDataAttr(b){
  return b&&(b.hasAttribute('data-filter')||b.hasAttribute('data-mode')||b.hasAttribute('data-strategy')||b.hasAttribute('data-view')||b.hasAttribute('data-category')||b.hasAttribute('data-period')||b.hasAttribute('data-option')||b.hasAttribute('data-tab')||b.hasAttribute('data-term'));
}
function getBtnGroup(b){
  if(!b)return null;
  return b.closest('[role="radiogroup"], [role="tablist"], [role="toolbar"], [class*="segmented"], [class*="tab-bar"], [class*="toggle-group"], [class*="btn-group"], [class*="filter-group"], [class*="pill-group"], [class*="chip-group"]')||b.parentElement;
}
function getGroupButtons(b){
  var grp=getBtnGroup(b);
  if(!grp)return b?[b]:[];
  if(grp===b.parentElement){
    return Array.from(grp.children).filter(function(c){return c.tagName==='BUTTON';});
  }
  return Array.from(grp.querySelectorAll('button'));
}
function detectVisualActiveInGroup(sibs){
  if(sibs.some(hasActiveClass)){
    return{hasSignal:true,isActive:function(b){return hasActiveClass(b);}};
  }
  if(sibs.length>=2){
    var kTonalCls='lumi-'+'btn--tonal';
    var kPrimCls='lumi-'+'btn--primary';
    var tonal=sibs.filter(function(s){return s.classList&&s.classList.contains(kTonalCls);});
    if(tonal.length>=1&&tonal.length<sibs.length){
      return{hasSignal:true,isActive:function(b){return b.classList&&b.classList.contains(kTonalCls);}};
    }
    var hasActionTxt=sibs.some(function(s){return kActionBtnTxtRe.test((s.textContent||'').trim());});
    if(!hasActionTxt){
      var prim=sibs.filter(function(s){return s.classList&&s.classList.contains(kPrimCls);});
      if(prim.length>=1&&prim.length<sibs.length){
        return{hasSignal:true,isActive:function(b){return b.classList&&b.classList.contains(kPrimCls);}};
      }
      var withBg=sibs.filter(function(s){
        var bg=(s.style&&(s.style.backgroundColor||s.style.background)||'').trim();
        return bg&&bg!=='transparent'&&bg!=='none'&&!/surface|fff|0000/i.test(bg);
      });
      if(withBg.length===1){
        return{hasSignal:true,isActive:function(b){return withBg.indexOf(b)>=0;}};
      }
    }
  }
  return{hasSignal:false,isActive:function(){return false;}};
}
function isSelectableBtn(b){
  if(!b||b.tagName!=='BUTTON')return false;
  var role=b.getAttribute('role');
  if(role==='tab'||role==='radio'||role==='switch'||role==='menuitem'||b.hasAttribute('aria-expanded')||b.hasAttribute('aria-selected')||b.hasAttribute('aria-checked')||b.classList.contains('lumi-sort-btn'))return false;
  var cls=typeof b.className==='string'?b.className:'';
  if(kSelectableClsRe.test(cls)||hasActiveClass(b)||b.hasAttribute('aria-pressed')||hasSelectableDataAttr(b))return true;
  var sibs=getGroupButtons(b);
  if(sibs.length>=2){
    if(sibs.some(function(s){return kSelectableClsRe.test(typeof s.className==='string'?s.className:'')||hasActiveClass(s)||s.hasAttribute('aria-pressed')||hasSelectableDataAttr(s);})){
      return true;
    }
    if(detectVisualActiveInGroup(sibs).hasSignal)return true;
  }
  return false;
}
function fixDeleteButtons(){
  try{
    document.querySelectorAll('button:not([aria-label]):not([aria-labelledby])').forEach(function(b){
      var t=(b.textContent||'').trim();
      if(t==='\u00d7'||t==='✕'||t==='✖'||t==='&times;'||((t==='x'||t==='X')&&!isSelectableBtn(b))){
        b.setAttribute('aria-label','Delete');
      }
    });
  }catch(e){}
}
function fixFormGroups(){
  try{
    document.querySelectorAll('input:not([type="hidden"]):not([aria-label]):not([aria-labelledby]), select:not([aria-label]):not([aria-labelledby]), textarea:not([aria-label]):not([aria-labelledby])').forEach(function(inp){
      if(inp.id&&document.querySelector('label[for="'+CSS.escape(inp.id)+'"]'))return;
      if(inp.closest('label'))return;
      var ph=inp.getAttribute('placeholder');
      if(ph)inp.setAttribute('aria-label',ph);
    });
    var rawCandidates=new Set();
    document.querySelectorAll('input:not([type="hidden"]), select, textarea').forEach(function(inp){
      var row=inp.parentElement;
      while(row&&row!==document.body){
        var p=row.parentElement;
        if(p&&p!==document.body&&p.children.length>=2){
          rawCandidates.add(p);
        }
        row=p;
      }
    });
    var validContainers=[];
    rawCandidates.forEach(function(container){
      var rows=Array.from(container.children).filter(function(ch){
        return ch.querySelectorAll&&ch.querySelectorAll('input:not([type="hidden"]), select, textarea').length>=2;
      });
      if(rows.length>=2)validContainers.push({container:container,rows:rows});
    });
    validContainers.forEach(function(entry){
      var container=entry.container;
      var hasInnerCandidate=validContainers.some(function(other){
        return other.container!==container&&container.contains(other.container);
      });
      if(hasInnerCandidate)return;
      var baseLabel='Item';
      var prev=container.previousElementSibling;
      if(prev){
        var hdr=(/^H[1-6]$/.test(prev.tagName)||prev.matches('[role="heading"], [class*="card-title"]'))?prev:prev.querySelector('h1, h2, h3, h4, h5, h6, [role="heading"], [class*="card-title"]');
        if(hdr){
          baseLabel=(hdr.textContent||'').trim().replace(/s$/i,'')||'Item';
        }
      }
      entry.rows.forEach(function(r,idx){
        if(!r.hasAttribute('role')&&r.tagName!=='FIELDSET'){
          r.setAttribute('role','group');
        }
        if(r.getAttribute('role')==='group'&&(!r.hasAttribute('aria-label')||r.dataset.lumiAutoGroup==='1')&&!r.hasAttribute('aria-labelledby')){
          r.setAttribute('aria-label',baseLabel+' '+(idx+1));
          r.dataset.lumiAutoGroup='1';
        }
      });
    });
  }catch(e){}
}
function isBtnActiveState(b){
  return hasActiveClass(b)||b.getAttribute('aria-checked')==='true'||b.getAttribute('aria-selected')==='true'||b.getAttribute('aria-pressed')==='true';
}
function syncSelectableButtons(){
  if(isSyncingA11y)return;
  isSyncingA11y=true;
  try{
    document.querySelectorAll('[role="radiogroup"]').forEach(function(rg){
      rg.querySelectorAll('button').forEach(function(b){
        if(!b.hasAttribute('role'))b.setAttribute('role','radio');
      });
    });
    document.querySelectorAll('[role="tablist"], [class*="tab-bar"]').forEach(function(tl){
      if(!tl.hasAttribute('role'))tl.setAttribute('role','tablist');
      tl.querySelectorAll('button').forEach(function(b){
        if(!b.hasAttribute('role'))b.setAttribute('role','tab');
      });
    });
    document.querySelectorAll('button[role="radio"]').forEach(function(b){
      var p=getBtnGroup(b);
      if(p&&!p.hasAttribute('role'))p.setAttribute('role','radiogroup');
      var sibs=p?Array.from(p.querySelectorAll('button[role="radio"]')):[b];
      var sig=detectVisualActiveInGroup(sibs);
      if(sig.hasSignal){
        var wanted=sig.isActive(b)?'true':'false';
        if(b.getAttribute('aria-checked')!==wanted)b.setAttribute('aria-checked',wanted);
      }else if(sibs.some(function(s){return s.dataset&&s.dataset.lumiClickedActive==='1';})){
        var cWanted=(b.dataset&&b.dataset.lumiClickedActive==='1')?'true':'false';
        if(b.getAttribute('aria-checked')!==cWanted)b.setAttribute('aria-checked',cWanted);
      }else if(!b.hasAttribute('aria-checked')){
        var pressed=b.getAttribute('aria-pressed');
        b.setAttribute('aria-checked',pressed==='true'?'true':'false');
      }
      if(b.hasAttribute('aria-pressed'))b.removeAttribute('aria-pressed');
    });
    document.querySelectorAll('button[role="tab"]').forEach(function(b){
      var p=getBtnGroup(b);
      if(p&&!p.hasAttribute('role'))p.setAttribute('role','tablist');
      var sibs=p?Array.from(p.querySelectorAll('button[role="tab"]')):[b];
      var sig=detectVisualActiveInGroup(sibs);
      if(sig.hasSignal){
        var wanted=sig.isActive(b)?'true':'false';
        if(b.getAttribute('aria-selected')!==wanted)b.setAttribute('aria-selected',wanted);
      }else if(sibs.some(function(s){return s.dataset&&s.dataset.lumiClickedActive==='1';})){
        var cWanted=(b.dataset&&b.dataset.lumiClickedActive==='1')?'true':'false';
        if(b.getAttribute('aria-selected')!==cWanted)b.setAttribute('aria-selected',cWanted);
      }else if(!b.hasAttribute('aria-selected')){
        var pressed=b.getAttribute('aria-pressed');
        b.setAttribute('aria-selected',pressed==='true'?'true':'false');
      }
      if(b.hasAttribute('aria-pressed'))b.removeAttribute('aria-pressed');
    });
    document.querySelectorAll('button').forEach(function(b){
      if(!isSelectableBtn(b))return;
      var sibs=getGroupButtons(b);
      if(sibs.length>=2){
        var p=getBtnGroup(b);
        if(p&&p!==document.body&&!p.hasAttribute('role'))p.setAttribute('role','group');
      }
      var sig=detectVisualActiveInGroup(sibs);
      if(sig.hasSignal){
        var wanted=sig.isActive(b)?'true':'false';
        if(b.getAttribute('aria-pressed')!==wanted){
          b.setAttribute('aria-pressed',wanted);
          b.setAttribute('data-lumi-auto-pressed','1');
        }
        return;
      }
      if(sibs.some(function(s){return s.dataset&&s.dataset.lumiClickedActive!==undefined;})){
        var cWanted=(b.dataset&&b.dataset.lumiClickedActive==='1')?'true':'false';
        if(b.getAttribute('aria-pressed')!==cWanted){
          b.setAttribute('aria-pressed',cWanted);
          b.setAttribute('data-lumi-auto-pressed','1');
        }
        return;
      }
      if(b.hasAttribute('aria-pressed')&&b.getAttribute('data-lumi-auto-pressed')!=='1')return;
      var anyAuthorPressed=sibs.some(function(s){return s.getAttribute('aria-pressed')==='true'&&s.getAttribute('data-lumi-auto-pressed')!=='1';});
      var defActive=!anyAuthorPressed&&sibs.length>=2&&sibs[0]===b&&hasSelectableDataAttr(b);
      var defWanted=defActive?'true':'false';
      if(b.getAttribute('aria-pressed')!==defWanted){
        b.setAttribute('aria-pressed',defWanted);
        b.setAttribute('data-lumi-auto-pressed','1');
      }
    });
    document.querySelectorAll('[role="radiogroup"], [role="tablist"], [role="toolbar"], [role="group"], [class*="segmented-group"], [class*="tab-bar"], [class*="chip-group"]').forEach(function(grp){
      var gRole=grp.getAttribute('role');
      var btns=Array.from(grp.querySelectorAll('button:not([disabled])')).filter(function(b){
        return gRole==='radiogroup'||gRole==='tablist'||gRole==='toolbar'||b.hasAttribute('aria-pressed')||b.hasAttribute('aria-checked')||b.hasAttribute('aria-selected')||isSelectableBtn(b);
      });
      if(btns.length<2)return;
      var focusedIdx=btns.indexOf(document.activeElement);
      var activeIdx=-1;
      if(gRole==='toolbar'&&focusedIdx>=0){
        activeIdx=focusedIdx;
      }else{
        for(var i=0;i<btns.length;i++){
          if(isBtnActiveState(btns[i])){activeIdx=i;break;}
        }
        if(activeIdx<0)activeIdx=focusedIdx>=0?focusedIdx:0;
      }
      btns.forEach(function(b,idx){
        b.setAttribute('tabindex',idx===activeIdx?'0':'-1');
      });
    });
  }catch(e){}
  isSyncingA11y=false;
}
document.addEventListener('keydown',function(ev){
  if(ev.key!=='ArrowRight'&&ev.key!=='ArrowLeft'&&ev.key!=='ArrowDown'&&ev.key!=='ArrowUp'&&ev.key!=='Home'&&ev.key!=='End')return;
  var btn=ev.target&&ev.target.closest?ev.target.closest('button'):null;
  if(!btn||btn.classList.contains('lumi-sort-btn'))return;
  var grp=btn.closest('[role="radiogroup"], [role="tablist"], [role="toolbar"], [role="group"], [class*="segmented-group"], [class*="tab-bar"], [class*="chip-group"]');
  var btns=[];
  if(grp){
    var grpRole=grp.getAttribute('role');
    btns=Array.from(grp.querySelectorAll('button:not([disabled])')).filter(function(b){
      return grpRole==='radiogroup'||grpRole==='tablist'||grpRole==='toolbar'||b.hasAttribute('aria-pressed')||b.hasAttribute('aria-checked')||b.hasAttribute('aria-selected')||isSelectableBtn(b);
    });
  }else{
    var sibs=getGroupButtons(btn).filter(function(c){return !c.disabled;});
    if(sibs.length>=2&&sibs.some(function(s){return isSelectableBtn(s)||s.getAttribute('role')==='radio'||s.getAttribute('role')==='tab';})){
      grp=getBtnGroup(btn);
      btns=sibs;
    }
  }
  if(btns.length<2)return;
  var cur=btns.indexOf(btn);
  if(cur<0)return;
  ev.preventDefault();
  var next=cur;
  if(ev.key==='ArrowRight'||ev.key==='ArrowDown')next=(cur+1)%btns.length;
  else if(ev.key==='ArrowLeft'||ev.key==='ArrowUp')next=(cur-1+btns.length)%btns.length;
  else if(ev.key==='Home')next=0;
  else if(ev.key==='End')next=btns.length-1;
  var target=btns[next];
  if(!target)return;
  var gRole=grp?grp.getAttribute('role'):null;
  if(gRole==='radiogroup'||gRole==='tablist'||gRole==='toolbar'||gRole==='group'||(grp&&grp.matches&&grp.matches('[class*="segmented-group"], [class*="tab-bar"], [class*="chip-group"]'))){
    btns.forEach(function(b,i){b.setAttribute('tabindex',i===next?'0':'-1');});
  }
  target.focus();
  var tRole=target.getAttribute('role');
  var activeSibs=btns.filter(isBtnActiveState);
  var isMultiSelect=gRole==='toolbar'||btns.some(function(b){return b.classList&&b.classList.contains('togglable');});
  if(tRole==='radio'||tRole==='tab'||gRole==='radiogroup'||gRole==='tablist'||(grp&&grp.matches&&grp.matches('[class*="segmented-group"], [class*="tab-bar"]'))||(!isMultiSelect&&activeSibs.length===1)){
    target.click();
  }
  setTimeout(syncSelectableButtons,0);
});
var lastSortedColIndex=-1;
var lastSortedTable=null;
function isThExplicitlySortable(th){
  return th.hasAttribute('onclick')||th.hasAttribute('data-sort')||th.hasAttribute('data-col')||th.hasAttribute('data-key')||th.matches('.sortable, .is-sortable, [aria-sort]')||(window.getComputedStyle&&window.getComputedStyle(th).cursor==='pointer');
}
function syncSortableTables(){
  try{
    document.querySelectorAll('table').forEach(function(tbl){
      var hdrRow=tbl.querySelector('thead tr')||tbl.querySelector('tr');
      var ths=hdrRow?Array.from(hdrRow.querySelectorAll('th')):[];
      if(!ths.length)return;
      var explicitCount=ths.filter(isThExplicitlySortable).length;
      if(!explicitCount)return;
      var hasPerColHints=ths.some(function(th){
        return th.hasAttribute('onclick')||th.hasAttribute('data-sort')||th.hasAttribute('data-col')||th.hasAttribute('data-key')||th.matches('.sortable, .is-sortable');
      });
      ths.forEach(function(th,idx){
        var txt=(th.textContent||'').trim();
        if(!txt||th.matches('.no-sort, [data-sortable="false"]')||th.querySelector('input, select, textarea'))return;
        if(hasPerColHints&&!isThExplicitlySortable(th))return;
        var isAsc=/[▲▴↑]/.test(txt)||th.matches('.asc, .sort-asc, .is-asc, [data-order="asc"], [data-dir="asc"]');
        var isDesc=/[▼▾↓]/.test(txt)||th.matches('.desc, .sort-desc, .is-desc, [data-order="desc"], [data-dir="desc"]');
        var sortVal=isAsc?'ascending':(isDesc?'descending':'none');
        th.setAttribute('aria-sort',sortVal);
        var walker=document.createTreeWalker(th,NodeFilter.SHOW_TEXT,null,false);
        var tnodes=[];
        while(walker.nextNode())tnodes.push(walker.currentNode);
        tnodes.forEach(function(tn){
          if(tn.parentElement&&tn.parentElement.getAttribute('aria-hidden')==='true')return;
          if(/[▲▼▴▾↑↓↕]/.test(tn.nodeValue)){
            var frag=document.createDocumentFragment();
            tn.nodeValue.split(/([▲▼▴▾↑↓↕]+)/).forEach(function(part){
              if(!part)return;
              if(/[▲▼▴▾↑↓↕]/.test(part)){
                var sp=document.createElement('span');
                sp.setAttribute('aria-hidden','true');
                sp.appendChild(document.createTextNode(part));
                frag.appendChild(sp);
              }else{
                frag.appendChild(document.createTextNode(part));
              }
            });
            if(tn.parentNode)tn.parentNode.replaceChild(frag,tn);
          }
        });
        var btn=th.querySelector('button');
        if(!btn){
          btn=document.createElement('button');
          btn.type='button';
          btn.className='lumi-sort-btn';
          btn.style.cssText='all:unset;box-sizing:border-box;cursor:pointer;display:inline-flex;align-items:center;gap:4px;font:inherit;color:inherit;letter-spacing:inherit;text-transform:inherit;text-align:inherit;width:100%;justify-content:inherit;border-radius:4px;';
          for(var a=0;a<th.attributes.length;a++){
            var an=th.attributes[a].name;
            if(an.indexOf('data-')===0)btn.setAttribute(an,th.attributes[a].value);
          }
          while(th.childNodes.length)btn.appendChild(th.childNodes[0]);
          th.appendChild(btn);
        }
        if(!th.dataset.lumiSortBound){
          th.dataset.lumiSortBound='1';
          th.addEventListener('click',function(){
            lastSortedTable=tbl;
            lastSortedColIndex=idx;
            setTimeout(function(){
              syncSortableTables();
              if(lastSortedTable===tbl&&lastSortedColIndex===idx){
                var curRow=tbl.querySelector('thead tr')||tbl.querySelector('tr');
                var curThs=curRow?curRow.querySelectorAll('th'):[];
                var targetBtn=curThs[idx]&&curThs[idx].querySelector('button');
                if(targetBtn&&document.activeElement!==targetBtn)targetBtn.focus();
              }
            },0);
          });
        }
      });
    });
  }catch(e){}
}
function formatChartVal(v){
  if(v===null||v===undefined)return '';
  if(typeof v==='object'){
    if(v.label||v.name){
      var nm=v.label||v.name;
      if(v.x!==undefined&&v.y!==undefined)return [nm,'('+v.x+', '+v.y+')'].join(' ');
    }
    if(v.y!==undefined&&v.x!==undefined&&typeof v.x==='number')return '('+v.x+', '+v.y+')';
    if(v.y!==undefined)return String(v.y);
    return JSON.stringify(v);
  }
  return String(v);
}
function buildChartSteps(chart){
  var cfg=chart.config||{};
  var data=chart.data||cfg.data||{};
  var labels=Array.isArray(data.labels)?data.labels:[];
  var dsList=Array.isArray(data.datasets)?data.datasets:[];
  var type=(cfg.type||'').toString();
  var visDs=[];
  for(var d=0;d<dsList.length;d++){
    var meta=chart.getDatasetMeta?chart.getDatasetMeta(d):null;
    var hidden=(meta&&meta.hidden===true)||(dsList[d]&&dsList[d].hidden===true);
    if(!hidden&&dsList[d]&&Array.isArray(dsList[d].data)&&dsList[d].data.length){
      visDs.push(d);
    }
  }
  if(!visDs.length)return[];
  var steps=[];
  if(type==='scatter'||type==='bubble'||!labels.length){
    var maxLen=0;
    visDs.forEach(function(d){if(dsList[d].data.length>maxLen)maxLen=dsList[d].data.length;});
    if(type==='scatter'||type==='bubble'){
      visDs.forEach(function(d){
        var arr=dsList[d].data;
        for(var i=0;i<arr.length;i++){
          if(arr[i]!==null&&arr[i]!==undefined)steps.push([{datasetIndex:d,index:i}]);
        }
      });
    }else{
      for(var idx=0;idx<maxLen;idx++){
        var els=[];
        visDs.forEach(function(d){
          if(idx<dsList[d].data.length&&dsList[d].data[idx]!==null&&dsList[d].data[idx]!==undefined){
            els.push({datasetIndex:d,index:idx});
          }
        });
        if(els.length)steps.push(els);
      }
    }
  }else{
    for(var c=0;c<labels.length;c++){
      var cEls=[];
      visDs.forEach(function(d){
        if(c<dsList[d].data.length&&dsList[d].data[c]!==null&&dsList[d].data[c]!==undefined){
          cEls.push({datasetIndex:d,index:c});
        }
      });
      if(cEls.length)steps.push(cEls);
    }
  }
  return steps;
}
function activateChartStep(chart,stepEls,stepIdx,totalSteps){
  var cv=chart&&chart['can'+'vas'];
  if(!stepEls||!stepEls.length)return;
  var pos={x:0,y:0};
  try{
    var fEl=stepEls[0];
    var meta=chart.getDatasetMeta?chart.getDatasetMeta(fEl.datasetIndex):null;
    var el=meta&&meta.data&&meta.data[fEl.index];
    if(el&&typeof el.tooltipPosition==='function')pos=el.tooltipPosition();
    else if(el&&el.x!==undefined&&el.y!==undefined)pos={x:el.x,y:el.y};
  }catch(e){}
  if(chart.setActiveElements)chart.setActiveElements(stepEls);
  if(chart.tooltip&&chart.tooltip.setActiveElements)chart.tooltip.setActiveElements(stepEls,pos);
  if(chart.update)chart.update('none');
  var msg='';
  try{
    var tt=chart.tooltip;
    if(tt&&Array.isArray(tt.body)&&tt.body.length){
      var tTitle=Array.isArray(tt.title)?tt.title.join(' '):'';
      var tLines=[];
      tt.body.forEach(function(b){
        if(b&&Array.isArray(b.lines))b.lines.forEach(function(l){if(l)tLines.push(l);});
      });
      if(tLines.length)msg=(tTitle?(tTitle+': '):'')+tLines.join('; ');
    }
  }catch(e){}
  if(!msg){
    var data=chart.data||{};
    var labels=Array.isArray(data.labels)?data.labels:[];
    var dsList=Array.isArray(data.datasets)?data.datasets:[];
    var f=stepEls[0];
    var lbl=labels[f.index]!==undefined?String(labels[f.index]):('Point '+(stepIdx+1));
    var parts=stepEls.map(function(item){
      var ds=dsList[item.datasetIndex]||{};
      var dsLbl=ds.label||('Series '+(item.datasetIndex+1));
      var raw=ds.data&&ds.data[item.index];
      return [dsLbl,formatChartVal(raw)].join(': ');
    });
    msg=lbl+' — '+parts.join(', ');
  }
  var fullMsg=msg+' ('+(stepIdx+1)+' of '+totalSteps+')';
  announceChartMsg(fullMsg);
  var ttOpts=chart.options&&chart.options.plugins&&chart.options.plugins.tooltip;
  if(ttOpts&&ttOpts.enabled===false)showChartKbdBadge(cv,msg);
}
var kChartKbdHint=' Use Left and Right arrow keys to navigate data points.';
function summarizeChart(chart){
  try{
    var cv=chart&&chart['can'+'vas'];
    if(!cv)return;
    cv.setAttribute('role','application');
    cv.setAttribute('aria-roledescription','interactive chart');
    if(!cv.hasAttribute('tabindex'))cv.setAttribute('tabindex','0');
    if(cv.style&&cv.style.outline==='none')cv.style.outline='';
    var cfg=chart.config||{};
    var data=chart.data||cfg.data||{};
    var labels=Array.isArray(data.labels)?data.labels:[];
    var datasets=Array.isArray(data.datasets)?data.datasets:[];
    var type=(cfg.type||'chart').toString();
    var titleEl=cv.closest('[class*="lumi-card"], section, .widget-container, body');
    var heading=titleEl?titleEl.querySelector('.lumi-chart-title, h1, h2, h3, h4'):null;
    var titleTxt=heading?(heading.textContent||'').trim():'';
    var parts=[];
    if(titleTxt)parts.push(titleTxt+' ('+type+' chart).');
    else parts.push(type.charAt(0).toUpperCase()+type.slice(1)+' chart.');
    datasets.slice(0,4).forEach(function(ds,di){
      var dsName=ds.label||('Series '+(di+1));
      var vals=Array.isArray(ds.data)?ds.data:[];
      var pairs=[];
      for(var i=0;i<Math.min(vals.length,8);i++){
        var valStr=formatChartVal(vals[i]);
        var lbl=labels[i]!==undefined?String(labels[i]):('Point '+(i+1));
        pairs.push(lbl+': '+valStr);
      }
      if(vals.length>8)pairs.push('and '+(vals.length-8)+' more');
      if(pairs.length)parts.push(dsName+' — '+pairs.join(', ')+'.');
    });
    var summary=parts.join(' ').split(/\s+/).slice(0,130).join(' ')+kChartKbdHint;
    if(!cv.hasAttribute('aria-label')||cv.dataset.lumiAutoLabel==='1'){
      cv.setAttribute('aria-label',summary);
      cv.dataset.lumiAutoLabel='1';
    }else{
      var curLbl=cv.getAttribute('aria-label')||'';
      if(!/arrow keys/i.test(curLbl)){
        cv.setAttribute('aria-label',curLbl.replace(/\.\s*$/,'')+'.'+kChartKbdHint);
      }
    }
    if(!cv.dataset.lumiChartKeyBound&&!cv.dataset.lumiKbdBound&&!cv.dataset.lumiKeyA11y){
      cv.dataset.lumiChartKeyBound='1';
      cv.dataset.lumiKbdBound='1';
      var stepCursor=-1;
      cv.addEventListener('keydown',function(ev){
        if(ev.defaultPrevented)return;
        if(ev.key==='Escape'){
          stepCursor=-1;
          if(chart.setActiveElements)chart.setActiveElements([]);
          if(chart.tooltip&&chart.tooltip.setActiveElements)chart.tooltip.setActiveElements([],{x:0,y:0});
          if(chart.update)chart.update('none');
          showChartKbdBadge(cv,'');
          return;
        }
        if(ev.key!=='ArrowRight'&&ev.key!=='ArrowLeft'&&ev.key!=='ArrowDown'&&ev.key!=='ArrowUp'&&ev.key!=='Home'&&ev.key!=='End')return;
        var steps=buildChartSteps(chart);
        if(!steps.length)return;
        ev.preventDefault();
        if(ev.key==='ArrowRight'||ev.key==='ArrowDown')stepCursor=(stepCursor+1)%steps.length;
        else if(ev.key==='ArrowLeft'||ev.key==='ArrowUp')stepCursor=stepCursor<=0?(steps.length-1):(stepCursor-1);
        else if(ev.key==='Home')stepCursor=0;
        else if(ev.key==='End')stepCursor=steps.length-1;
        activateChartStep(chart,steps[stepCursor],stepCursor,steps.length);
      });
      cv.addEventListener('blur',function(){
        stepCursor=-1;
        try{
          if(chart.setActiveElements)chart.setActiveElements([]);
          if(chart.tooltip&&chart.tooltip.setActiveElements)chart.tooltip.setActiveElements([],{x:0,y:0});
          if(chart.update)chart.update('none');
          showChartKbdBadge(cv,'');
        }catch(e){}
      });
    }
  }catch(e){}
}
function describeSvgMark(m,idx){
  var al=m.getAttribute('aria-label')||m.getAttribute('data-label')||m.getAttribute('data-name')||m.getAttribute('data-title');
  var val=m.getAttribute('data-value')||m.getAttribute('data-val')||m.getAttribute('data-y');
  if(al&&val)return [al,val].join(': ');
  if(al)return al;
  var tEl=m.querySelector('title');
  if(tEl&&tEl.textContent)return tEl.textContent.trim();
  if(m.__data__&&typeof m.__data__==='object'){
    var d=(m.__data__.data&&typeof m.__data__.data==='object')?m.__data__.data:m.__data__;
    var nm=d.name||d.label||d.title||d.id||d.category||d.item||d.food||d.country||d.state||d.group||'';
    var v=d.value!==undefined?d.value:(d.y!==undefined&&typeof d.y!=='object'?d.y:'');
    var kvs=[];
    var skipKey=/^(?:name|label|title|id|category|item|food|country|state|group|x0|x1|y0|y1|vx|vy|fx|fy|index|depth|height|r|color|fill|stroke)$/;
    Object.keys(d).forEach(function(k){
      if(skipKey.test(k)||kvs.length>=4)return;
      var kv=d[k];
      if(typeof kv==='number'||(typeof kv==='string'&&kv.length<=32)){
        kvs.push([k,kv].join(': '));
      }
    });
    if(nm&&kvs.length)return [nm,kvs.join(', ')].join(' — ');
    if(nm&&v!=='')return [nm,v].join(': ');
    if(kvs.length)return kvs.join(', ');
    if(nm)return String(nm);
    if(v!=='')return ['Point '+(idx+1),v].join(': ');
  }
  var pG=m.closest('g');
  if(pG){
    var txt=(pG.textContent||'').trim().replace(/\s+/g,' ');
    if(txt&&txt.length<=80)return txt;
  }
  return ['Data point',idx+1].join(' ');
}
function collectSvgMarks(svg){
  return Array.from(svg.querySelectorAll('circle, rect, path, polygon, g[data-label], g[data-value]')).filter(function(el){
    if(el.tagName==='RECT'&&(el.getAttribute('width')==='100%'||parseFloat(el.getAttribute('width')||'0')>450))return false;
    if(el.hasAttribute('data-label')||el.hasAttribute('data-value')||el.hasAttribute('aria-label')||el.querySelector('title'))return true;
    if(el.__data__!==undefined||el.__on!==undefined)return true;
    var cs=window.getComputedStyle?window.getComputedStyle(el):null;
    return cs&&cs.cursor==='pointer';
  });
}
function hookSvgCharts(){
  try{
    document.querySelectorAll('svg').forEach(function(svg){
      if(svg.closest('button, a, .lumi-icon, .lumi-pullquote-mark'))return;
      var vb=svg.getAttribute('viewBox');
      var w=svg.clientWidth||parseFloat(svg.getAttribute('width')||'0');
      if(w>0&&w<64&&!vb)return;
      var marks=collectSvgMarks(svg);
      if(marks.length<2)return;
      svg.setAttribute('role','application');
      svg.setAttribute('aria-roledescription','interactive chart');
      if(!svg.hasAttribute('tabindex'))svg.setAttribute('tabindex','0');
      var curLbl=svg.getAttribute('aria-label')||'';
      if(!curLbl){
        var card=svg.closest('[class*="lumi-card"], section, .widget-container, body');
        var hdr=card?card.querySelector('.lumi-chart-title, h1, h2, h3, h4'):null;
        var hTxt=hdr?(hdr.textContent||'').trim():'Interactive chart';
        var sample=marks.slice(0,6).map(function(m,i){return describeSvgMark(m,i);}).join(', ');
        svg.setAttribute('aria-label',hTxt+'. '+(sample?(sample+'.'):'')+kChartKbdHint);
      }else if(!/arrow keys/i.test(curLbl)){
        svg.setAttribute('aria-label',curLbl.replace(/\.\s*$/,'')+'.'+kChartKbdHint);
      }
      if(!svg.dataset.lumiSvgKeyBound){
        svg.dataset.lumiSvgKeyBound='1';
        var activeMarkIdx=-1;
        var prevMark=null;
        var clearMark=function(){
          if(prevMark){
            prevMark.style.outline='';
            try{prevMark.dispatchEvent(new MouseEvent('mouseout',{bubbles:true}));prevMark.dispatchEvent(new MouseEvent('mouseleave',{bubbles:true}));}catch(e){}
            prevMark=null;
          }
          showChartKbdBadge(svg,'');
        };
        svg.addEventListener('keydown',function(ev){
          if(ev.defaultPrevented)return;
          if(ev.key==='Escape'){activeMarkIdx=-1;clearMark();return;}
          if(ev.key!=='ArrowRight'&&ev.key!=='ArrowLeft'&&ev.key!=='ArrowDown'&&ev.key!=='ArrowUp'&&ev.key!=='Home'&&ev.key!=='End')return;
          var curMarks=collectSvgMarks(svg);
          if(!curMarks.length)return;
          ev.preventDefault();
          clearMark();
          if(ev.key==='ArrowRight'||ev.key==='ArrowDown')activeMarkIdx=(activeMarkIdx+1)%curMarks.length;
          else if(ev.key==='ArrowLeft'||ev.key==='ArrowUp')activeMarkIdx=activeMarkIdx<=0?(curMarks.length-1):(activeMarkIdx-1);
          else if(ev.key==='Home')activeMarkIdx=0;
          else if(ev.key==='End')activeMarkIdx=curMarks.length-1;
          var target=curMarks[activeMarkIdx];
          if(!target)return;
          prevMark=target;
          target.style.outline='2px solid var(--primary, #3186ff)';
          try{
            var r=target.getBoundingClientRect();
            var mOpts={bubbles:true,clientX:r.left+r.width/2,clientY:r.top+r.height/2};
            target.dispatchEvent(new MouseEvent('mouseenter',mOpts));
            target.dispatchEvent(new MouseEvent('mouseover',mOpts));
            target.dispatchEvent(new MouseEvent('mousemove',mOpts));
          }catch(e){}
          var desc=describeSvgMark(target,activeMarkIdx);
          try{
            var domTts=document.querySelectorAll('.tooltip, [class*="tooltip"], #tooltip');
            for(var ti=0;ti<domTts.length;ti++){
              var ttEl=domTts[ti];
              var ttCs=window.getComputedStyle?window.getComputedStyle(ttEl):null;
              if(ttCs&&ttCs.display!=='none'&&ttCs.visibility!=='hidden'&&parseFloat(ttCs.opacity||'1')>0){
                var ttTxt=(ttEl.textContent||'').trim().replace(/\s+/g,' ');
                if(ttTxt&&ttTxt.length<=160){desc=ttTxt;break;}
              }
            }
          }catch(e){}
          announceChartMsg(desc+' ('+(activeMarkIdx+1)+' of '+curMarks.length+')');
          showChartKbdBadge(svg,desc);
        });
        svg.addEventListener('blur',function(){activeMarkIdx=-1;clearMark();});
      }
    });
  }catch(e){}
}
function wrapChartClass(C){
  if(!C)return C;
  if(!C.__lumiA11yHooked&&C.prototype&&C.prototype.update){
    var origUpdate=C.prototype.update;
    C.prototype.update=function(){
      var res=origUpdate.apply(this,arguments);
      summarizeChart(this);
      return res;
    };
    C.__lumiA11yHooked=true;
  }
  return C;
}
try{
  var curChart=wrapChartClass(window.Chart);
  if(!window.__lumiChartPropHooked){
    window.__lumiChartPropHooked=true;
    Object.defineProperty(window,'Chart',{
      configurable:true,
      enumerable:true,
      get:function(){return curChart;},
      set:function(v){curChart=wrapChartClass(v);}
    });
  }
}catch(e){}
function hookChartJs(){
  try{
    getOrCreateChartLive();
    document.querySelectorAll('.lumi-chart-legend, [class*="chart-legend"]').forEach(function(el){
      el.setAttribute('aria-hidden','true');
    });
    document.querySelectorAll('.lumi-chart-title').forEach(function(el){
      if(!/^H[1-6]$/.test(el.tagName)&&!el.hasAttribute('role')){
        el.setAttribute('role','heading');
        el.setAttribute('aria-level','3');
      }
    });
    if(window.Chart){
      wrapChartClass(window.Chart);
      if(window.Chart.instances){
        Object.values(window.Chart.instances).forEach(summarizeChart);
      }
      document.querySelectorAll('can'+'vas').forEach(function(cv){
        var inst=(window.Chart.getChart&&window.Chart.getChart(cv))||cv.__chartjs__||cv.$chartjs;
        if(inst)summarizeChart(inst);
      });
    }
    hookSvgCharts();
  }catch(e){}
}
function all(){
  syncSliders();
  fixDeleteButtons();
  fixFormGroups();
  syncSelectableButtons();
  syncSortableTables();
  hookChartJs();
}
if(typeof MutationObserver==='function'&&document.documentElement){
  new MutationObserver(function(){
    if(isSyncingA11y)return;
    syncSelectableButtons();
    syncSliders();
  }).observe(document.documentElement,{subtree:true,attributes:true,attributeFilter:['class','style','value']});
}
window.addEventListener('message',function(e){
  var d=e&&e.data;
  if(d&&(d.type==='SUPPLEMENTAL_DATA_UPDATE'||d.type==='RESTORE_STATE')){
    all();
    setTimeout(all,0);
    setTimeout(all,50);
  }
});
document.addEventListener('focusin',function(e){
  var t=e&&e.target;
  if(t&&(t.tagName===('CAN'+'VAS')||t.tagName==='SVG'||t.tagName==='BUTTON')){
    hookChartJs();
    syncSelectableButtons();
  }
});
document.addEventListener('click',function(e){
  var btn=e.target&&e.target.closest?e.target.closest('button'):null;
  if(!btn)return;
  var txt=(btn.textContent||'').trim();
  var isAdd=/^\+|^\+?\s*add\b/i.test(txt)||/\badd\b/i.test(btn.getAttribute('aria-label')||'');
  var preInputs=isAdd?new Set(document.querySelectorAll('input:not([type="hidden"]), select, textarea')):null;
  var wasSelectable=isSelectableBtn(btn)||btn.getAttribute('role')==='radio'||btn.getAttribute('role')==='tab';
  var prevPressed=btn.getAttribute('aria-pressed');
  var prevAria=[prevPressed,btn.getAttribute('aria-checked'),btn.getAttribute('aria-selected')].join('|');
  setTimeout(function(){
    if(wasSelectable&&btn.isConnected){
      var sibs=getGroupButtons(btn);
      var sig=detectVisualActiveInGroup(sibs);
      var curAria=[btn.getAttribute('aria-pressed'),btn.getAttribute('aria-checked'),btn.getAttribute('aria-selected')].join('|');
      var authorUpdatedAria=(curAria!==prevAria);
      if(sig.hasSignal||authorUpdatedAria){
        sibs.forEach(function(s){if(s.dataset)delete s.dataset.lumiClickedActive;});
      }else if(sibs.length>=2){
        sibs.forEach(function(s){
          if(!s.dataset)return;
          s.dataset.lumiClickedActive=(s===btn)?'1':'0';
        });
      }else{
        btn.dataset.lumiClickedActive=(prevPressed==='true')?'0':'1';
      }
    }
    fixDeleteButtons();
    fixFormGroups();
    syncSelectableButtons();
    syncSortableTables();
    hookChartJs();
    if(preInputs){
      var detached=0;
      preInputs.forEach(function(el){if(!el.isConnected)detached++;});
      var allNow=document.querySelectorAll('input:not([type="hidden"]):not([disabled]), select:not([disabled]), textarea:not([disabled])');
      var fresh=[];
      for(var i=0;i<allNow.length;i++){
        if(!preInputs.has(allNow[i]))fresh.push(allNow[i]);
      }
      if(fresh.length>detached&&fresh[detached])fresh[detached].focus();
    }
  },0);
},true);
if(document.readyState==='loading'){
  document.addEventListener('DOMContentLoaded',function(){all();setTimeout(all,0);setTimeout(all,250);setTimeout(all,800);});
}else{
  all();
  setTimeout(all,0);
  setTimeout(all,250);
  setTimeout(all,800);
}
window.addEventListener('load',function(){all();setTimeout(all,250);setTimeout(all,800);});
})();</script>
</body>
</html>
```83723b6d7245aa.html…]()

[interactive_visual_im_7f83723b6d7245aa.html](https://github.com/user-attachments/files/35287128/interactive_visual_im_7f83723b6d7245aa.html)
