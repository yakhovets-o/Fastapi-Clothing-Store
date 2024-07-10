from fastapi import (
    HTTPException,
    status,
)


class CustomHTTPException(HTTPException):
    """Raised when entity was not found in database."""

    def __init__(self, status_code: int, detail: dict) -> None:
        super().__init__(status_code=status_code, detail=detail)


class EntityDoesNotExistApi(CustomHTTPException):
    def __init__(self, _id: int) -> None:
        detail = {"message": f"{_id} not found"}
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
