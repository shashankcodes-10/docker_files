from pathlib import Path

LEVELS = ("INFO", "WARNING", "ERROR")
DEFAULT_LOG = Path(__file__).parent.parent / "app.log"


def analyze_logs(log_path=None):
    """Read a log file and return counts of INFO / WARNING / ERROR lines."""
    path = Path(log_path) if log_path else DEFAULT_LOG
    text = path.read_text(encoding="utf-8")

    counts = {level: 0 for level in LEVELS}
    for line in text.splitlines():
        tokens = set(line.split())
        for level in LEVELS:
            if level in tokens:
                counts[level] += 1

    return {"log_file": str(path), "counts": counts}
