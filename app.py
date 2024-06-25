import json
from flask import Flask, request, jsonify, render_template
import base64
# import cv2
import numpy as np


app = Flask(__name__)

commands_list = []


def add_command( command, parameters):
    global commands_list
    
    if type(command) == str:
        # Create a dictionary for each command
        command_dict = {"command": command}
        if type(parameters) == list:
            command_dict["parameter"] = parameters
        else:
            raise "Parametrs should be a list. Even empty one"

        # Add the command dictionary to the list
        commands_list.append(command_dict)
    else:
        raise "Command name should be a string"


def commands_to_json():
    global commands_list

    # Create the final dictionary to hold all commands
    commands_json = {"commands": commands_list}

    # Convert the dictionary to a JSON string
    json_data = json.dumps(commands_json, indent=2)

    return json_data

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_frame', methods=['POST'])
def process_frame():
    data = request.json
    if "frame" in data:
        frame_data = data["frame"]
        jpg_original = base64.b64decode(frame_data)
        # frame = np.frombuffer(jpg_original, dtype=np.uint8)
        # frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

        # Get and make next package of commands
        global commands_list
        commands_list = []  # Clear up after previous package

        # Generate commands based on processing
        add_command("set_motors", [0.1, 0.1])  # dumb values
        add_command("stop", [])     # Dumb values


        print(type(jpg_original))

        # return jsonify({"status": "frame processed"}), 200
        return render_template('index.html', frame_data=jpg_original)
    else:
        return jsonify({"error": "No frame received"}), 400


@app.route('/send_commands', methods=['GET'])
def send_commands():
    print(commands_to_json())
    return commands_to_json()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
