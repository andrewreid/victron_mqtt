from .constants import VictronEnum


class GenericOnOff(VictronEnum):
    """On/Off  Enum"""
    Off = (0, "Off")
    On = (1, "On")

class InverterMode(VictronEnum):
    """Inverter Mode Enum"""
    ChargerOnly = (1, "Charger Only")
    InverterOnly = (2, "Inverter Only")
    On = (3, "On")
    Off = (4, "Off")

class EvChargerMode(VictronEnum):
    """EVCharger Mode Enum"""
    Manual = (0, "Manual")
    Auto = (1, "Auto")
    ScheduledCharge = (2, "Scheduled Charge")


class EssMode(VictronEnum):
    """Energy Storage System operating mode."""

    OptimizedWithBatteryLife = (1, "Optimized (with BatteryLife)")
    OptimizedWithoutBatteryLife = (2, "Optimized (without BatteryLife)")
    KeepBatteriesCharged = (3, "Keep batteries charged")
    ExternalControl = (4, "External control")
