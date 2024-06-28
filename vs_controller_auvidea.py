import os
import time

def export_gpio(pin):
    with open("/sys/class/gpio/export", 'w') as f:
        f.write(str(pin))

def unexport_gpio(pin):
    with open("/sys/class/gpio/unexport", 'w') as f:
        f.write(str(pin))
        
def set_gpio_direction(pin, direction):
    with open(f"/sys/class/gpio/"+ gpiodir + "/direction", 'w') as f:
        f.write(direction)

def set_gpio_value(pin, value):
    with open(f"/sys/class/gpio/"+ gpiodir + "/value", 'w') as f:
        f.write(str(value))

def read_gpio_value(pin):
    with open(f"/sys/class/gpio/"+ gpiodir + "/value", 'r') as f:
        return f.read().strip()

def perform_reboot(pin, delay_s):
    # Check if the pin is already exported
    if os.path.exists(f"/sys/class/gpio/"+ gpiodir ):
        # print("Pin is already exported. Unexporting...")
        unexport_gpio(pin)
    export_gpio(pin)
    set_gpio_direction(pin, "out")
    print("Controller is now rebooting. Please wait for the system to finish rest")
    set_gpio_value(pin, 0) 
    time.sleep(delay)
    set_gpio_value(pin, 1)
    unexport_gpio(pin) 
    print("Reboot performed successfully!")
    
# Example usage for pin PCC.01 [https://docs.nvidia.com/jetson/archives/r35.3.1/DeveloperGuide/text/HR/JetsonModuleAdaptationAndBringUp/JetsonOrinNxNanoSeries.html?highlight=cvb]
# PCC.01 should be specified under Customer usage here [https://developer.nvidia.com/downloads/jetson-orin-nx-and-orin-nano-series-pinmux-config-template]. Or by the carrierboard manufacturer.
gpiodir= "PCC.01"
# pin = base + CC + 01
pin = 316 + 12 + 1
delay = 1
perform_reboot(pin, delay)
