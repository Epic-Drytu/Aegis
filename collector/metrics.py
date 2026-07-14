import psutil


def collect_metrics():
    """Collect CPU and memory usage metrics."""
    return {
        'cpu_percent': psutil.cpu_percent(interval=1),
        'memory': {
            'total': psutil.virtual_memory().total,
            'available': psutil.virtual_memory().available,
            'percent': psutil.virtual_memory().percent,
        },
    }
