from fastapi import APIRouter, HTTPException

from services.metrics_service import get_system_metrics

router = APIRouter(tags=["metrics"])


@router.get("/metrics", status_code=200)
def get_metrics():
    try:
        return get_system_metrics()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Could not read metrics: {exc}")
