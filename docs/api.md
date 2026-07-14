# API Documentation

## Endpoint

`POST /telemetry`

### Request

Headers:
- `Content-Type: application/json`
- `Authorization: Bearer <API_KEY>`

Body:

```json
{
  "device_id": "local-device",
  "metrics": {...},
  "network": {...},
  "battery": {...},
  "disk": {...}
}
```

### Response

- `200 OK`: Payload accepted.
- `4xx/5xx`: Error details in response body.
