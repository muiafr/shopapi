from fastapi import APIRouter

router = APIRouter(tags=["api"], prefix="/health")


@router.get('/')
def health() -> dict[str, str]:
    return {"status": "ok"}
