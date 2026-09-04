FROM python:3.12-slim

WORKDIR /benchmark
COPY pyproject.toml README.md ./
COPY src ./src
COPY tasks ./tasks
RUN pip install --no-cache-dir .

ENTRYPOINT ["azure-infra-bench"]
CMD ["list", "--tasks", "tasks"]
