import os
import subprocess
import pyudev

def run_limitd(charge_limit):
    # Replace 'home/devan/lapcharge/lapchar' with the actual path to the 'limitd.sh' script
    script_path = '/home/devan/lapcharge/lapchar/limitd.sh'
    subprocess.run([script_path, str(charge_limit)])

def main():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='power_supply')

    for device in iter(monitor.poll, None):
        if device.action == 'add' and 'AC' in device.tags:
            # Replace 60 with the desired charge limit you want to set
            charge_limit = 60
            run_limitd(charge_limit)
            print(f"Charger connected. Charge limit set to {charge_limit}%.")

if __name__ == "__main__":
    main()
