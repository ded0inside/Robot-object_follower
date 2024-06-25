from flask import Flask, request, jsonify, render_template
import base64
# import cv2
import numpy as np


app = Flask(__name__)

commands = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_frame', methods=['POST'])
def process_frame():
    data = request.json
    if "frame" in data:
        frame_data = data["frame"]
        # jpg_original = base64.b64decode(jpg_as_text)
        # frame = np.frombuffer(jpg_original, dtype=np.uint8)
        # frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        #
        # # Dummy processing - replace with your actual processing logic
        # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Generate commands based on processing
        global commands
        commands = {"move": "forward"}  # Replace with actual commands based on processing

        print(type(frame_data))

        # return jsonify({"status": "frame processed"}), 200
        return render_template('index.html', frame_data=frame_data)
    else:
        return jsonify({"error": "No frame received"}), 400


@app.route('/send_commands', methods=['GET'])
def send_commands():
    global commands
    return jsonify(commands)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
