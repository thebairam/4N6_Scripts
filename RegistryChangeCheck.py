import winreg

def get_registry_value(key, subkey, value_name):
    try:
        registry_key = winreg.OpenKey(key, subkey, 0, winreg.KEY_READ)
        value, _ = winreg.QueryValueEx(registry_key, value_name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None

# Registry paths to monitor with their expected values
registry_to_monitor = {
    ("HKEY_LOCAL_MACHINE", "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", "ExampleValue"): "ExpectedValue",
    # Add more registry paths and their expected values as needed
}

for (hive_name, subkey, value_name), expected_value in registry_to_monitor.items():
    hive = getattr(winreg, hive_name)
    current_value = get_registry_value(hive, subkey, value_name)
    if current_value != expected_value:
        print(f"WARNING: Registry change detected in {subkey}\\{value_name}.")
    else:
        print(f"Registry {subkey}\\{value_name} is unchanged.")

