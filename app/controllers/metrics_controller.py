"""
metrics_controller.py
---------------------
Exposes Prometheus metrics endpoint for observability.
"""

from fastapi import APIRouter, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

# Create router instance
metrics_router = APIRouter()


@metrics_router.get('/metrics')
async def metrics():
    """
    Expose Prometheus metrics.

    Returns
    -------
    Response
        Prometheus-formatted metrics for scraping.
    """
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
