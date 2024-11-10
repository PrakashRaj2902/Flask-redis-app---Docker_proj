**Flask App with Redis Caching**

Project Overview:
This simple web application fetches data from a simulated external source and caches it in Redis for fast retrieval. The data is cached for a specified time (30 seconds in this case) to avoid repeatedly fetching the same data. This approach is commonly used to reduce load times for frequently accessed data.

Technologies Used:
1. Flask: A lightweight Python web framework.
2. Redis: A fast, in-memory data structure store used for caching.
3. Docker: To containerize the Flask app and Redis.
4. Docker Compose: For managing multi-container Docker applications.
