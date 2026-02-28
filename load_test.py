import requests
import time
import statistics

url = "http://127.0.0.1:8000/health"

times = []

print("Starting load test...")

for i in range(50):
    start = time.time()
    response = requests.get(url)
    end = time.time()

    times.append(end - start)
    print(f"Request {i+1}: {response.status_code}")

print("\nLatency Results:")
print("P50:", statistics.median(times))
print("P95:", sorted(times)[int(len(times)*0.95)])
print("Max:", max(times))