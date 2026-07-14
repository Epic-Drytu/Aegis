from collector import metrics, network, battery, disk


def test_collect_metrics_returns_dict():
    data = metrics.collect_metrics()
    assert isinstance(data, dict)
    assert 'cpu_percent' in data


def test_collect_network_info_returns_dict():
    info = network.collect_network_info()
    assert isinstance(info, dict)
    assert 'interfaces' in info


def test_collect_battery_details_returns_dict():
    battery_data = battery.collect_battery_details()
    assert isinstance(battery_data, dict)
    assert 'available' in battery_data


def test_collect_disk_details_returns_dict():
    disk_data = disk.collect_disk_details()
    assert isinstance(disk_data, dict)
    assert 'partitions' in disk_data
