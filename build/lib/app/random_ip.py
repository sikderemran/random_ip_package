import subprocess
import time
import platform

while True:
    try:
        os_name=platform.system()
        subprocess.run(["sudo", "dhclient", "-r"])
        subprocess.run(["sudo", "dhclient"])

        print("DHCP lease renewed successfully.")
    except Exception as e:
        print(f'Error: {str(e)}')
    time.sleep(5)
