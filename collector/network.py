import psutil


def collect_network_info():
    """Collect network interface and connection statistics."""
    interfaces = psutil.net_if_addrs()
    stats = psutil.net_io_counters(pernic=True)

    return {
        'interfaces': {
            name: [addr.address for addr in addrs]
            for name, addrs in interfaces.items()
        },
        'traffic': {
            name: {
                'bytes_sent': stat.bytes_sent,
                'bytes_recv': stat.bytes_recv,
            }
            for name, stat in stats.items()
        },
    }
