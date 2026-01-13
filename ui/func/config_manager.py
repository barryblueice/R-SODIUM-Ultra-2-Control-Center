import sys
import os
from PySide6.QtCore import QSettings

class ConfigManager:
    _instance = None
    settings: QSettings

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            config_path = os.path.join(os.getcwd(), "config.ini")
            cls._instance.settings = QSettings(config_path, QSettings.Format.IniFormat)
        return cls._instance

    def set(self, key, value):
        self.settings.setValue(key, value)

    def get(self, key, default=None):
        return self.settings.value(key, default)

    def import_dict(self, data, group=""):
        for key, value in data.items():
            path = f"{group}/{key}" if group else key
            
            if isinstance(value, dict):
                self.import_dict(value, path)
            else:
                self.set(path, value)
        self.settings.sync()

config = ConfigManager()


    
settings_value = {
    "debug_ui": 0,
    "enclosure_setting": {
        "disk_on_power_cfg": {
            "self_pwr" : {
                "nvme": 0,
                "sata1": 0,
                "sata2": 0
            },
            "ext_pwr" : {
                "nvme": 0,
                "sata1": 0,
                "sata2": 0
            }
        },
        "_1352r_cfg": {
            "pm": 1,
            "jbod": 0,
            "r1": 0,
            "r0": 0
        },
        "other_cfg": {
            "hddpc_suspend": 0,
            "pd_mode": 0
        }
    },
    "controller_setting": {
        "fan_mode": 0,
        "fan_curve": {
            "temp_min": 0,
            "temp_max": 0,
            "speed_min": 0,
            "speed_max": 0
        },
        "fan_fixed": {
            "temp": 0,
            "speed": 0
        },
        "rgb": {
            "temp_warn_threshold": 40
        }
    },
    "center_setting": {
        "auto_update_firmware": 0,
        "auto_update_center": 0,
        "auto_launch_startup": 0,
        "minimized_center_after_startup": 0,
        "exit_the_ceter_after_close_the_window": 0
    }
}

config.import_dict(settings_value)