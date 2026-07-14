from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class TelemetryPayload:
    device_id: str
    metrics: Dict[str, Any]
    network: Dict[str, Any]
    battery: Dict[str, Any]
    disk: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return {
            'device_id': self.device_id,
            'metrics': self.metrics,
            'network': self.network,
            'battery': self.battery,
            'disk': self.disk,
        }
