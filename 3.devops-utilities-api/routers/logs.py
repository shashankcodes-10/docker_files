from fastapi import APIRouter, HTTPException

from services.logs_service import analyze_logs

router = APIRouter(tags=["logs"])


@router.get("/logs", status_code=200)
def get_log_summary(file: str | None = None):
    """Analyze a log file and return level counts. Defaults to the bundled app.log."""
    try:
        return analyze_logs(file)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Log file not found: {file}")
