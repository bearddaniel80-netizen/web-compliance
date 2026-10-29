from .security.api_key_check import verify_internal_key
from .routers.run_process import ProcessRequest
from .routers.main_router import api_router
from .routers.minio import router as minio_router

from pathlib import Path
from fastapi import FastAPI, Header
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --------------------------------------------------
# Routers
# --------------------------------------------------

app.include_router(minio_router)
app.include_router(api_router("manifest"))
app.include_router(api_router("suite"))
app.include_router(api_router("tag"))

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/api/data")
async def get_data(
    x_internal_key: str | None = Header(default=None),
):
    verify_internal_key(x_internal_key)

    return {
        "message": "Hello from FastAPI"
    }

@app.get("/api/index")
async def get_compliance_test_readme(
    x_internal_key: str | None = Header(default=None),
):
    verify_internal_key(x_internal_key)
    filename = "README"
    process = ProcessRequest()
    input_file = str(Path.cwd() /  f"{filename}.md")
    output_file = str(Path.cwd() /  f"{filename}.html")
    await process._run_markdown_conversion(input_file, output_file)
    with open(output_file, "r") as f:
        html = f.read()
    return HTMLResponse(content=html)



