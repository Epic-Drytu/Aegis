import psutil


def collect_disk_details():
    """Collect disk usage details for mounted partitions."""
    partitions = psutil.disk_partitions(all=False)
    return {
        'partitions': [
            {
                'device': p.device,
                'mountpoint': p.mountpoint,
                'fstype': p.fstype,
                'usage': psutil.disk_usage(p.mountpoint)._asdict(),
            }
            for p in partitions
        ]
    }
