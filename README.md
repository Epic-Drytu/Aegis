# Project Aegis

Project Aegis is a lightweight endpoint telemetry collector designed to gather laptop system metrics, network details, battery status, and disk storage information, then package these metrics into a structured payload and forward them to an API Gateway endpoint.

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

