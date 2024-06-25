import json
import time
# from jetbot import Robot
# robot = Robot()

# Define a function to process robot commands
def process_commands(commands):
    for command in commands:
        action = command.get('command')
        if action == 'set_motors':
            print(f'command: {action}, inputs: {command.get("parameter")[0]}, {command.get("parameter")[1]}')
#             robot.set_motors(command.get('left_motor'), command.get('right_motor'))
        elif action == 'stop':
            print(f'command: {action}')
#             robot.stop()
        elif action == 'sleep':
            print(f'command: {action}, inputs: {command.get("parameter")[0]}')
#             time.sleep(command.get('duration'))
        else:
            print(f"Unknown action: {action}")


# Read JSON data from file
with open('data.json', 'r') as f:
    data = json.load(f)

# Extract commands from JSON data
commands_list = data.get('commands', [])

# Process commands
process_commands(commands_list)