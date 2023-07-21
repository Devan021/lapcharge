# Charger Automation Project

This project automates the process of running the `limitd.sh` shell script to set a charge limit on your laptop when you plug in your charger. The Python script provided here detects charger connection events and executes the `limitd.sh` script with the specified charge limit.

## Requirements

- Python 3
- `pyudev` library (for Linux) or `pywin32` (for Windows) to monitor charger connection events.
- `dbus-python` library (for Linux) or `PyGObject` for D-Bus interaction (if using the `gi.repository` version).

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone <repository_url>
Install the required Python libraries:

For Linux:

  ```bash
   Copy code
   pip install pyudev


For D-Bus version:

   ```bash

    Copy code
    pip install dbus-python
For D-Bus using gi.repository version:

    ```bash
    Copy code
    pip install PyGObject
 Usage
Navigate to the project directory:

```bash
Copy code
cd charger_automation
Make sure the limitd.sh script has the correct permissions to execute:

```bash
Copy code
chmod +x lapcharge/lapchar/limitd.sh
Run the Python script to start monitoring charger connection events:

```bash
Copy code
python charger_automation.py
The script will now listen for charger connection events and automatically run the limitd.sh script with the specified charge limit when the charger is plugged in.

To stop the script, press Ctrl + C in the terminal.

Customization
You can customize the limitd.sh script to set the desired charge limit based on your preferences. The script accepts a charge limit value as a command-line argument.

For Windows users, make sure to modify the script to use the appropriate method for detecting charger connection events. Additionally, install the required pywin32 library using pip install pywin32.

Troubleshooting
If you encounter any issues or errors, check the following:

Ensure the correct path to the limitd.sh script is provided in the run_limitd function.

For Linux users, verify that the pyudev library is installed, and the monitor.filter_by(subsystem='power_supply') correctly filters power supply events.

For D-Bus users, check the correct service name and signal name in the charger_changed_callback function.

For Windows users, ensure the pywin32 library is installed and the method for detecting charger connection events is appropriate.

Verify that the Python script has executable permissions.

If you need further assistance, feel free to reach out.

License
This project is licensed under the MIT License.


