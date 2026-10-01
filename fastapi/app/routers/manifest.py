from .run_process import run_query, run_test
from ..security.api_key_check import verify_internal_key

from fastapi import Header
from fastapi import APIRouter

router = APIRouter(prefix="/api/manifest")

@router.get("/list")
async def list_manifest(
    x_internal_key: str | None = Header(default=None),
):
    verify_internal_key(x_internal_key)
    command = ["compliance", "manifest", "list"]
    results = await run_query(command)
    clean_result = list(filter(None, results.split("\n\n")))
    return {"result": clean_result }
        
@router.get("/{filename}")
async def run_test_manifest(
    filename:str,
    x_internal_key: str | None = Header(default=None),
):
    verify_internal_key(x_internal_key)
    command = ["compliance", "manifest", "run", filename, "--format", "json"]
    return await run_test(command)