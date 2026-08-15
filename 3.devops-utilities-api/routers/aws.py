from botocore.exceptions import BotoCoreError, ClientError
from fastapi import APIRouter, HTTPException

from services.aws_service import get_bucket_info

router = APIRouter(tags=["aws"])


@router.get("/s3", status_code=200)
def get_buckets():
    try:
        return get_bucket_info()
    except (BotoCoreError, ClientError) as exc:
        raise HTTPException(status_code=502, detail=f"AWS error: {exc}")


@router.get("/ec2", status_code=200)
def get_instances():
    return {"message": "EC2 utilities in progress"}
