from fastapi import FastAPI, Response
from prometheus_client import Counter, Gauge, generate_latest
import os
import time

app = FastAPI(
    title="SRE Reliable API",
    description="Self-healing SRE demonstration service",
    version="1.0.0"
)

REQUEST_COUNT = Counter(
    "api_requests_total",
    "Total number of API requests"
)

ACTIVE_REQUESTS = Gauge(
    "api_active_requests",
    "Number of active API requests"
)

START_TIME = time.time()


@app.get("/")
def root():
    REQUEST_COUNT.inc()

    return {
        "service": "reliable-api",
        "status": "running",
        "version": "1.0.0"
    }


@app.get("/health")
def health():

    if os.getenv("FAILURE_MODE", "false").lower() == "true":
        return Response(
            content="Service unhealthy",
            status_code=500
        )

    return {
        "status": "healthy"
    }


@app.get("/ready")
def readiness():

    return {
        "status": "ready"
    }


@app.get("/api/v1/status")
def status():

    uptime = round(time.time() - START_TIME, 2)

    return {
        "service": "reliable-api",
        "status": "operational",
        "uptime_seconds": uptime
    }


@app.get("/metrics")
def metrics():

    return Response(
        content=generate_latest(),
        media_type="text/plain"
    )