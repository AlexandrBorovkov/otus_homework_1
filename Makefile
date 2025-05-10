install:
	uv sync

start:
	uv run parser

lint:
	uv run ruff check