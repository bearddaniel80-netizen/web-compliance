from .run_process import ProcessRequest
from ..security.api_key_check import verify_internal_key

from fastapi import Header, APIRouter
from fastapi.responses import HTMLResponse

def api_router(FOLDER):
    router = APIRouter(prefix=f"/api/{FOLDER}")
    process = ProcessRequest()

    @router.get("/list")
    async def router_list(
        x_internal_key: str | None = Header(default=None),
    ):
        import re
        verify_internal_key(x_internal_key)
        command = ["compliance", FOLDER, "list"]
        results = await process.run_query(command)
        clean_result = list(filter(None, re.split(r"\n+", results)))
        return {"result": clean_result }

# --------------
# Format
# --------------

    @router.get("/github/{filename}")
    async def run_github_test(
        filename:str,
        x_internal_key: str | None = Header(default=None),
    ):
        verify_internal_key(x_internal_key)
        command = ["compliance", FOLDER, "run", filename, "--format", "github"]
        html = await process.render_github(command)
        return HTMLResponse(content=html)

    @router.get("/html/{filename}")
    async def run_html_test(
        filename:str,
        x_internal_key: str | None = Header(default=None),
    ):
        verify_internal_key(x_internal_key)
        command = ["compliance", FOLDER, "run", filename, "--format", "html"]
        html = await process.render_html(command)
        return HTMLResponse(content=html)

    @router.get("/markdown/{filename}")
    async def run_markdown_test(
        filename:str,
        x_internal_key: str | None = Header(default=None),
    ):
        verify_internal_key(x_internal_key)
        command = ["compliance", FOLDER, "run", filename, "--format", "md"]
        html = await process.render_markdown(command)
        return HTMLResponse(content=html)

    @router.get("/pdf/{filename}")
    async def run_pdf_test(
        filename:str,
        x_internal_key: str | None = Header(default=None),
    ):
        verify_internal_key(x_internal_key)
        command = ["compliance", FOLDER, "run", filename, "--format", "pdf"]
        await process.render_pdf(command)
        return HTMLResponse(content=html)

# --------------
# Features
# --------------

    @router.get("/cache/{filename}")
    async def run_cache_test(
        filename:str,
        x_internal_key: str | None = Header(default=None),
    ):
        verify_internal_key(x_internal_key)
        command = ["compliance", FOLDER, "run", filename]
        await process.run_query(command)
        command = ["compliance", FOLDER, "run", filename, "--cache", "--format", "json"]
        return await process.render_json(command)


    @router.get("/failfast/{filename}")
    async def run_failfast_test(
        filename:str,
        x_internal_key: str | None = Header(default=None),
    ):
        verify_internal_key(x_internal_key)
        command = ["compliance", FOLDER, "run", filename, "--fail-fast", "--format", "json"]
        return await process.render_json(command)
    
    @router.get("/failfast/query/{filename}")
    async def run_failfast_query_test(
        filename:str,
        x_internal_key: str | None = Header(default=None),
    ):
        verify_internal_key(x_internal_key)
        command = ["compliance", FOLDER, "run", filename, "--fail-fast-query", "--format", "json"]
        return await process.render_json(command)

    @router.get("/profile/{filename}")
    async def run_profile_test(
        filename:str,
        x_internal_key: str | None = Header(default=None),
    ):
        verify_internal_key(x_internal_key)
        command = ["compliance", FOLDER, "run", filename, "--profile", "--format", "json"]
        return await process.render_json(command)

    @router.get("/retry/{times}/{filename}")
    async def run_retry_test(
        times:str,
        filename:str,
        x_internal_key: str | None = Header(default=None),
    ):
        verify_internal_key(x_internal_key)
        command = ["compliance", FOLDER, "run", filename, "--retry", times, "--format", "json"]
        return await process.render_json(command)

    @router.get("/{filename}")
    async def run_test(
        filename:str,
        x_internal_key: str | None = Header(default=None),
    ):
        verify_internal_key(x_internal_key)
        command = ["compliance", FOLDER, "run", filename, "--format", "json"]
        return await process.render_json(command)
    
    return router