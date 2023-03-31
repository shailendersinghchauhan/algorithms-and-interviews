import time
import random
from datetime import datetime, timedelta
from prometheus_client import Gauge, start_http_server

# Define SLA metrics
sla_gauge = Gauge('sla_metric', 'SLA Metric', ['service', 'sla'])

# Define SLA targets
target_sla = {
    'service1': 0.95,
    'service2': 0.98,
    'service3': 0.99
}

# Define function to simulate service performance
def simulate_service(service):
    while True:
        # Simulate service performance
        performance = random.random()
        # Update SLA metrics
        sla_gauge.labels(service=service, sla='target').set(target_sla[service])
        sla_gauge.labels(service=service, sla='actual').set(performance)
        # Sleep for 1 minute
        time.sleep(60)

# Start Prometheus metrics server
start_http_server(8000)

# Start service simulation threads
services = ['service1', 'service2', 'service3']
for service in services:
    t = threading.Thread(target=simulate_service, args=(service,))
    t.start()
