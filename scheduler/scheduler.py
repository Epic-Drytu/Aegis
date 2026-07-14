import time
from config.config import SCHEDULE_INTERVAL_MINUTES
from collector.metrics import collect_metrics
from collector.network import collect_network_info
from collector.battery import collect_battery_details
from collector.disk import collect_disk_details
from models.payload import TelemetryPayload
from sender.api_client import APIClient


def run_scheduler():
    client = APIClient()
    while True:
        payload = TelemetryPayload(
            device_id='local-device',
            metrics=collect_metrics(),
            network=collect_network_info(),
            battery=collect_battery_details(),
            disk=collect_disk_details(),
        )
        client.send_payload(payload.to_dict())
        time.sleep(SCHEDULE_INTERVAL_MINUTES * 60)


if __name__ == '__main__':
    run_scheduler()
