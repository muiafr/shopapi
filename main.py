"""Entry point: uvicorn main:app --reload."""

from src.api.main import app

__all__ = ["app"]
