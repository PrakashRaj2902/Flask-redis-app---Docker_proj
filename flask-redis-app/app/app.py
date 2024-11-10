from flask import Flask, jsonify
import redis
import time

app = Flask(__name__)

# Set up the Redis client to connect to Redis
redis_client = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)

@app.route('/data')
def get_data():
    # Check if data is cached
    cached_data = redis_client.get('mydata')
    if cached_data:
        return jsonify({"message": "Data from cache", "data": cached_data})

    # Simulate a slow database call (for example)
    time.sleep(2)
    data = "This is some real-time data fetched from a database or external source."

    # Store data in Redis cache for next time
    redis_client.set('mydata', data, ex=30)  # Cache expires in 30 seconds

    return jsonify({"message": "Data fetched from source", "data": data})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 
