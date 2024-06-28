import Jetson.GPIO as GPIO
import time

PIN_NUM = 7
# Update the pin number according to your hardware setup
def configure_pin(remote_on_off_pin=PIN_NUM): 
    """
    Configures the GPIO pin for remote on/off control.

    Args:
        remote_on_off_pin (int): Pin number for remote on/off control.
    """
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(remote_on_off_pin, GPIO.OUT)

def enable_converter(remote_on_off_pin=PIN_NUM):
    """
    Enables the converter using the specified GPIO pin.

    Args:
        remote_on_off_pin (int): Pin number for remote on/off control.
    """
    GPIO.output(remote_on_off_pin, GPIO.HIGH)

def disable_converter(remote_on_off_pin=PIN_NUM):
    """
    Disables the converter and performs GPIO cleanup.

    Args:
        remote_on_off_pin (int): Pin number for remote on/off control.
    """
    GPIO.output(remote_on_off_pin, GPIO.LOW)
    GPIO.cleanup()

def reboot_converter(sleep_time_seconds: int = 5, sleep_time_minutes: float = 5/60) -> None:
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

if __name__ == "__main__":
    configure_pin()
    reboot_converter()

#jnx45@jnx45-desktop:/sys/class/gpio$ sudo chmod 777 unexport
#jnx45@jnx45-desktop:/sys/class/gpio$ sudo chmod 777 export
#328 GPIO04 [https://developer.download.nvidia.com/assets/embedded/secure/jetson/orin_nx/docs/Jetson_Orin_NX_DS-10712-001_v0.5.pdf?6zfO8L1bTgeh6Kw_6S3fWXdLZDBSWonJZFpHgSUIIOuUfXTDRLsCpoLmebc3bqCBK2Pp4R9pGo4VVyw9-pwsySBqm4hnE0ZiyXORj9LYUDPeMI5xTXmO28pE50RJOaSXM9lg8AoOS7hIyKqP2jHajumEFOWR8TRQtbhdOzmFShvcO8N0jdIRRO-yCXrdNg==&t=eyJscyI6ImdzZW8iLCJsc2QiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyJ9]
#GPIOnumber = GPIOletter*8 + GPIOnumber + GPIOoffset
# Jetson Nano -> GPIOoffset = 0 [https://auvidea.eu/download/manual/JNX42/JNX42_Manual.pdf]
# 340 -> EE01