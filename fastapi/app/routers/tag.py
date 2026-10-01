from .run_process import run_query, run_test
from ..security.api_key_check import verify_internal_key

from fastapi import Header
from fastapi import APIRouter

router = APIRouter(prefix="/api/tag")

@router.get("/list")
async def list_tag(
    x_internal_key: str | None = Header(default=None),
):
    verify_internal_key(x_internal_key)
    command = ["compliance", "tag", "list"]
    results = await run_query(command)
    clean_result = list(filter(None, results.split("\n")))
    return {"result": clean_result }
        
@router.get("/{tag}")
async def run_test_tag(
    tag:str,
    x_internal_key: str | None = Header(default=None),
):
    verify_internal_key(x_internal_key)
    command = ["compliance", "tag", "run", tag, "--format", "json"]
    return await run_test(command)