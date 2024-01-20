import json
import os
import sys
from flask import Flask, render_template

BASE_PATH = "C:\\Users\\PeerMohamedSharfaraz\\OneDrive - Cloud Destinations Infotech Pvt Ltd\\Takeout\\Google Chat\\Groups"
USER_EMAIL = "sharfarazb@clouddestinations.com"


def read_google_takeout(filePath):
    with open(f'{filePath}\\messages.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_folders_data(base_path):
    folders_data = []
    for folder_name in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder_name)
        if os.path.isdir(folder_path):
            group_info_path = os.path.join(folder_path, 'group_info.json')
            if folder_name.startswith('DM'):
                users_name_from_json = read_users_name_from_json(group_info_path)
                folders_data.append({"name": "Direct Message with " + users_name_from_json, "path": folder_path})
            elif folder_name.startswith('Space'):
                users_name_from_json = read_space_name_from_json(group_info_path)
                folders_data.append({"name": "Space: " + users_name_from_json, "path": folder_path})
            else:
                users_name_from_json = read_users_name_from_json(group_info_path)
                folders_data.append({"name": users_name_from_json, "path": folder_path})
    return sorted(folders_data, key=lambda x: x['name'])


def read_users_name_from_json(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        members_name = ', '.join(member["name"] for member in data["members"] if member.get("email") != USER_EMAIL)
        if not members_name:
            return "Deleted User"
        return members_name
    except (IOError, json.JSONDecodeError, KeyError) as e:
        print(f"Error reading {json_path}: {e}")
        return "Unknown"


def read_space_name_from_json(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        space_name = data["name"]
        if space_name == "Group Chat":
            return read_users_name_from_json(json_path)
        return space_name
    except (IOError, json.JSONDecodeError, KeyError) as e:
        print(f"Error reading {json_path}: {e}")
        return "Unknown"


# Check if a command line argument is provided
# if len(sys.argv) == 3:
#     BASE_PATH = sys.argv[2]
#     USER_EMAIL = sys.argv[1]
# else:
#     print("Error: Please provide the user email and the base path to the takeout folder.")
#     print("Example: python app.py user@gmail.com C:\\Users\\user\\Takeout\\Google Chat\\Groups")
#     sys.exit(1)
app = Flask(__name__)


@app.route('/')
def index():
    folders_data = get_folders_data(BASE_PATH)
    return render_template('index.html', folders=folders_data)


@app.route('/messages/<path:file_path>')
def messages(file_path):
    data = read_google_takeout(file_path)
    return render_template('messages.html', data=data, user_email=USER_EMAIL, path=file_path)
