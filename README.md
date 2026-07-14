# Project Argus

Project Argus is a lightweight endpoint telemetry collector designed to gather laptop system metrics, network details, battery status, and disk storage information, then package these metrics into a structured payload and forward them to an API Gateway endpoint.

## Architecture

- `config/` contains project configuration and environment loading logic.
- `collector/` collects system and device telemetry data.
- `sender/` sends JSON payloads to a remote API gateway.
- `models/` defines the JSON payload data structure.
- `scheduler/` orchestrates periodic collection and transmission.
- `lambda/` provides AWS Lambda integration for server-side processing.
- `docs/` stores architecture documentation and API references.
- `tests/` includes unit tests for collector and sender functionality.
- `scripts/` contains project setup utilities.
- `assets/screenshots/` is reserved for project screenshots.

## Getting Started

1. Copy `.env.example` to `.env` and configure the environment variables.
2. Install dependencies with `pip install -r requirements.txt`.
3. Run the scheduler or invoke collector modules directly.

## License

This project is provided as a sample architecture and is intended for educational use.
