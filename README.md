# Prometheus-Monitoring-App


This project demonstrates application monitoring using Prometheus.

## Features
- Flask-based web application
- Custom metric: request_count_total
- Prometheus monitoring using /metrics endpoint
- Real-time visualization

## How to Run
1. Install dependencies:
   pip install flask prometheus_client

2. Run application:
   python app.py

3. Start Prometheus:
   prometheus.exe --config.file=prometheus.yml

4. Open:
   http://localhost:9090
