import json
commands_list = []


def add_command(command, parameters):
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


# Convert the command to JSON
add_command("set_motors", [0.1, 0.1])
add_command("stop", [])
add_command("sleep", [2])
add_command("set_motors", [0.1, 0.1])
add_command("stop", [1])

print(commands_to_json())
