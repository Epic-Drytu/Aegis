import psutil


def collect_battery_details():
    """Collect battery state and charging status."""
    battery = psutil.sensors_battery()
    if battery is None:
        return {'available': False}

    return {
        'available': True,
        'percent': battery.percent,
        'secsleft': battery.secsleft,
        'power_plugged': battery.power_plugged,
    }
