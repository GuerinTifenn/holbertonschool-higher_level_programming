# RESTful API Project

### Introduction
In the evolving world of software development, understanding how to communicate and transfer data efficiently between systems is essential. This project delves into the domain of RESTful APIs, a cornerstone in the realm of web services. The Representational State Transfer (REST) architecture is a set of constraints that ensure a scalable, stateless, and cacheable communication system. This approach allows for the easy integration of web services, making them accessible to a wide range of applications.

### Learning Objectives
- **HTTP/HTTPS Basics**: Grasp the foundational principles of the web’s primary protocol, understanding how data transfer occurs, methods involved, and the difference between the secure and non-secure versions.
- **API Consumption with Command Line**: Hands-on experience in interacting with APIs using basic command-line tools, laying the groundwork for more advanced interactions.
- **API Consumption with Python**: Elevate your data fetching skills by leveraging Python’s capabilities, allowing for more advanced processing and data manipulation.
- **API Development with http.server**: Understand the basics of crafting an API from scratch using Python’s built-in modules, setting a solid foundation.
- **API Development with Flask**: Dive deeper into API development using the lightweight Flask framework, focusing on routing, data management, and scalability.
- **API Security & Authentication**: Address the crucial aspect of security, understanding how to protect data transfer and ensure only authorized access to resources.
- **API Standards & Documentation with OpenAPI**: Conclude with the importance of maintaining standardized documentation, ensuring that APIs are usable, understandable, and maintainable.

### Importance
In our interconnected digital age, RESTful APIs play a pivotal role in the integration of different systems. They serve as the middlemen, translating requests into understandable actions, fetching data, or triggering procedures. From social media platforms sharing data with advertisement agencies to complex industrial systems communicating with each other for automation, APIs are ubiquitous.

Developing a solid understanding of how to consume, develop, secure, and document these APIs equips you with a critical skill set. It’s a blend of understanding both the technical intricacies and the larger design picture, ensuring seamless and efficient communication in the digital world.

### REST API Conceptual Diagram
```
+-------+           +-------+           +---------+           +---------+
|       |  Request  |       |  Process  |         |  Fetch/   |         |
|       |   ----->  |       |  -------> |         |  Modify   |         |
|       |           |       |           |         |  -------> |         |
|       | <-----    |       | <-------  |         |           |         |
|       |  Response |       |  Return   |         |           |         |
+-------+           +-------+           +---------+           +---------+
  Client            Web Server           API Server           Database
```

### Components
- **Client**: The requester of the service, often a web browser or application.
- **Web Server**: Handles the incoming request, acts as a middleman before passing it to the API server.
- **API Server**: The actual logic layer that processes the request, determining what data or action is required.
- **Database**: Stores the data which the API might fetch or modify.

### Flow
1. The client sends an HTTP/HTTPS request to the Web Server.
2. The Web Server, after potential routing and load balancing, forwards the request to the API Server.
3. The API Server processes the request, interacts with the database if needed.
4. The API Server returns the processed response to the Web Server.
5. The Web Server sends back the final HTTP/HTTPS response to the client.

This diagram provides a high-level view of how RESTful API communication typically works. In simpler setups, the Web Server and API Server might be combined into one. The separation here illustrates potential layers in a more complex or scaled environment.

## Tasks

- [2-task_02_requests.py](./task_02_requests.py)
- [3-task_03_http_server.py](./task_03_http_server.py)
- [4-task_04_flask.py](./task_04_flask.py)
- [5-task_05_basic_security.py](./task_05_basic_security.py)

### 0. Basics of HTTP/HTTPS
**Objective**:
- Differentiate between HTTP and HTTPS.
- Understand the basic working and structure of HTTP requests and responses.
- Recognize and explain the common HTTP methods and status codes.

**Instructions**:
1. **Differentiating HTTP and HTTPS**:
   - Read the provided resources to understand the basic differences between HTTP and HTTPS.
   - Jot down the main differences, focusing on security aspects.
   - Optional: Use a packet sniffer tool like Wireshark to observe the traffic of an HTTP and an HTTPS request.

2. **Understanding HTTP Structure**:
   - Visit a simple website, right-click, and choose “Inspect” or “Inspect Element”. Navigate to the “Network” tab. This shows all network requests made by the page.
   - Reload the page and observe the first request. Click on it. Explore the “Headers” section to understand the structure of HTTP requests and responses.

3. **Exploring HTTP Methods and Status Codes**:
   - Based on the resources provided, make a list of at least four common HTTP methods and explain when each would be used.
   - Make another list of five common HTTP status codes. For each status code, provide a brief description and a scenario where it might be encountered.

**Expected Output**:
- A brief summary explaining the differences between HTTP and HTTPS.
- A depiction or outline of the structure of an HTTP request and response.
- Lists of common HTTP methods and status codes with their descriptions and possible use cases.

### 1. Consume Data from an API using Command Line Tools (curl)
**Objective**:
- Install and use curl from the command line.
- Construct and execute basic API requests using curl, including setting headers and inspecting the output.
- Interpret the results of common API requests.

**Instructions**:
1. **Installing and Basic Interaction with curl**:
   - Install curl on your system. It’s usually available in standard repositories for Linux/Mac systems. For Windows, consider using Windows Subsystem for Linux (WSL) or downloading a Windows version of curl.
   - Once installed, run `curl --version` to confirm its availability.
   - Use curl to fetch the content of a webpage. For instance: `curl http://example.com`.

2. **Fetching Data from an API**:
   - Use curl to retrieve posts from JSONPlaceholder: `curl https://jsonplaceholder.typicode.com/posts`
   - Observe the output. It should be a JSON array of posts.

3. **Using Headers and Other Options with curl**:
   - Fetch only the headers of the same request using `curl -I https://jsonplaceholder.typicode.com/posts`.
   - Use curl to make a POST request to the same API: `curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts`

**Expected Output**:
- Upon running `curl --version`, you should see details about your installed version of curl, including supported protocols.
- Fetching posts from JSONPlaceholder should provide a JSON output of various posts, each having attributes like userId, id, title, and body.
- Fetching only headers should give a concise output showing status codes and headers without the actual content.
- Making a POST request should yield a response from the server acknowledging the reception of the data.

### 2. Consuming and Processing Data from an API using Python
**Objective**:
- Utilize the requests library to send HTTP requests and process responses.
- Parse and manipulate JSON data using Python.
- Convert structured data into other formats, e.g., CSV.

**Instructions**:
1. **Setup**:
   - If not installed, install the requests library using pip: `pip install requests`.

2. **Fetching Data**:
   - Write a basic Python script to fetch posts from JSONPlaceholder using `requests.get()`.
   - Create a function `fetch_and_print_posts()` that fetches all posts from JSONPlaceholder.
   - Print the status code of the response, e.g., `Status Code: 200`.
   - If the request was successful, parse the fetched data into a JSON object using the `.json()` method of the response object.
   - Iterate through the parsed JSON data and print out the titles of all the posts.

3. **Saving Data to CSV**:
   - Create a function `fetch_and_save_posts()` that fetches all posts from JSONPlaceholder.
   - If the request was successful, instead of printing titles, structure the data into a list of dictionaries, where each dictionary represents a post with keys and values for id, title, and body.
   - Using Python’s csv module, write this data into a CSV file called `posts.csv` with columns corresponding to the dictionary keys.

**Expected Output**:
- After the basic interaction script, you should have an output indicating a 200 status code, suggesting a successful GET request.
- When parsing JSON data, you should see printed titles of the posts, e.g., “sunt aut facere repellat provident occaecati excepturi optio reprehenderit.”
- After the data manipulation and conversion task, you should have a CSV file with columns id, title, and body. Each row in the CSV should correspond to a post from the fetched data.

### 3. Develop a Simple API using Python with the `http.server` Module
**Objective**:
- Set up a basic web server using the http.server module.
- Handle different types of HTTP requests (GET, POST, etc.).
- Serve JSON data in response to specific endpoints.

**Instructions**:
1. **Setting Up a Basic HTTP Server**:
   - Use the `http.server` module to set up a simple HTTP server. Start by creating a subclass of `http.server.BaseHTTPRequestHandler`.
   - Implement the `do_GET` method to handle GET requests. Within this method, send a simple text response back to the client: “Hello, this is a simple API!”

.
   - Start the server and verify its functionality by making GET requests using curl or a web browser.

2. **Serving JSON Data**:
   - Modify the `do_GET` method to return JSON data. Define a dictionary within the method and use the `json` module to serialize this dictionary into a JSON string.
   - Set the appropriate headers (`Content-Type: application/json`) before sending the response.

3. **Handling Different Endpoints**:
   - Extend the server to handle different endpoints. For instance, `/posts` could return a list of posts (similar to JSONPlaceholder).
   - For now, the data can be hardcoded within the server.

4. **Handling POST Requests**:
   - Implement the `do_POST` method to handle POST requests.
   - For simplicity, parse the incoming data as a JSON object and store it in a list (this list acts as a temporary storage or database).
   - Return a confirmation message with the stored data as a response.

**Expected Output**:
- A simple server responding to GET requests with a text message initially, and then with JSON data.
- Different endpoints returning different data structures, e.g., `/posts` returning a JSON array of posts.
- The server handling POST requests, storing incoming data, and returning it in the response.

### 4. Develop a RESTful API using Flask
**Objective**:
- Create a RESTful API using Flask.
- Implement routes that handle CRUD operations.
- Integrate with a simple data store (in-memory or file-based).

**Instructions**:
1. **Setting Up Flask**:
   - Install Flask using pip: `pip install flask`.
   - Create a basic Flask application that returns “Welcome to my API!” when accessing the root endpoint (`/`).

2. **Defining the API Structure**:
   - Create endpoints for managing a resource, such as `/items`.
   - Implement the following routes:
     - `GET /items`: Return a list of items.
     - `GET /items/<id>`: Return a specific item by ID.
     - `POST /items`: Create a new item.
     - `PUT /items/<id>`: Update an existing item.
     - `DELETE /items/<id>`: Delete an item by ID.

3. **Implementing the Endpoints**:
   - For simplicity, use an in-memory list to store items. Each item can be a dictionary with keys `id` and `name`.
   - In the `POST /items` route, generate a new ID for the item, add it to the list, and return the created item.
   - In the `PUT /items/<id>` route, find the item by ID, update its name, and return the updated item.
   - Ensure the `DELETE /items/<id>` route removes the item from the list and returns a confirmation message.

4. **Running and Testing the API**:
   - Run the Flask application and use curl or a tool like Postman to test each endpoint, ensuring that the API correctly handles all CRUD operations.

**Expected Output**:
- A Flask application with a root endpoint returning a welcome message.
- Endpoints for managing items, with each route performing its respective CRUD operation correctly.
- Ability to create, retrieve, update, and delete items using the implemented API.

### 5. Securing the API: Authentication and Authorization
**Objective**:
- Implement basic security mechanisms to protect the API.
- Add authentication and authorization layers to ensure only authorized users can access specific endpoints.

**Instructions**:
1. **Implementing Basic Authentication**:
   - Use Flask’s request handling capabilities to check for basic authentication headers in requests.
   - Implement a simple authentication check in your routes, returning a 401 Unauthorized response if credentials are missing or incorrect.

2. **Role-Based Access Control**:
   - Extend the authentication mechanism to include roles (e.g., user, admin).
   - Implement role-based access control by checking the user’s role before allowing access to certain endpoints (e.g., only admins can delete items).

3. **Testing Authentication**:
   - Use curl or Postman to test accessing endpoints with and without correct credentials.
   - Ensure that unauthorized access attempts are correctly handled, and appropriate responses are returned.

**Expected Output**:
- Basic authentication implemented, protecting the API endpoints.
- Role-based access control in place, ensuring only users with the appropriate roles can access certain operations.
- Verification through testing that the API enforces these security measures correctly.

### 6. API Standards and Documentation using OpenAPI
**Objective**:
- Document the API using the OpenAPI specification.
- Generate interactive documentation that can be used to explore and test the API.

**Instructions**:
1. **Defining the OpenAPI Specification**:
   - Create an OpenAPI specification file (YAML or JSON format) that describes the API, its endpoints, request/response formats, and authentication methods.
   - Use tools like Swagger Editor to help design and validate the specification.

2. **Integrating Swagger UI**:
   - Integrate Swagger UI into the Flask application to serve the generated documentation.
   - Ensure that the documentation is accessible via a specific route (e.g., `/docs`).

3. **Testing the Documentation**:
   - Access the Swagger UI and use it to explore and test the API endpoints.
   - Ensure that the documentation is accurate and up-to-date with the implemented API.

**Expected Output**:
- A complete OpenAPI specification file describing the API.
- Integrated Swagger UI providing interactive documentation accessible via the specified route.
- Verified accuracy and usability of the documentation for exploring and testing the API.
