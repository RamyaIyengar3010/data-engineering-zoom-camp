FROM python:3.13.10-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

COPY pyproject.toml uv.lock .python-version ./

COPY pipeline/pipeline.py pipeline.py

# --no-install-project keep uv from trying to install the app before its code is present.
RUN uv sync --locked --no-install-project  

# --no-sync at runtime avoids a sync that could try to install it then
ENTRYPOINT ["uv", "run", "--no-sync", "python", "pipeline.py"]