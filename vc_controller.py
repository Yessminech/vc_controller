import Jetson.GPIO as GPIO
import time

def configure_pin(remote_on_off_pin=9):
    """
    Configures the GPIO pin for remote on/off control.

    Args:
        remote_on_off_pin (int): Pin number for remote on/off control (default is 9).
    """
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(remote_on_off_pin, GPIO.OUT)

def enable_converter(remote_on_off_pin=9):
    """
    Enables the converter using the specified GPIO pin.

    Args:
        remote_on_off_pin (int): Pin number for remote on/off control (default is 9).
    """
    GPIO.output(remote_on_off_pin, GPIO.HIGH)

def disable_converter(remote_on_off_pin=9):
    """
    Disables the converter and performs GPIO cleanup.

    Args:
        remote_on_off_pin (int): Pin number for remote on/off control (default is 9).
    """
    GPIO.output(remote_on_off_pin, GPIO.LOW)
    GPIO.cleanup()

def reboot_converter(sleep_time_seconds: int = 20, sleep_time_minutes: float = 20/60) -> None:
    """
    Reboots the converter by enabling and disabling it after a specified sleep time.

    Args:
        sleep_time_seconds (int): Sleep time in seconds (default is 20).
        sleep_time_minutes (float): Sleep time in minutes (default is 1/3).
    """
    cycle_time_s = round(sleep_time_minutes * 60)
    configure_pin()
    enable_converter()
    time.sleep(cycle_time_s)
    disable_converter()
