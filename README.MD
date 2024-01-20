# Google Chat History Viewer

A simple Flask app to read the Google Chat history from Google Takeout. This project reads the JSON files from various directories within the Takeout folder and presents it in an organized manner.

## Configuration

In `app.py`, `BASE_PATH` and `USER_EMAIL` should be updated before you run the app. `BASE_PATH` should be till the Groups folder inside the Takeout, and `USER_EMAIL` should be the email of the Takeout owner.

```python
BASE_PATH = "C:\\Users\\John\\Documents\\Takeout\\Google Chat\\Groups"
USER_EMAIL = "johnd@gmail.com"
```
## Run

1. Download the zip of the master branch and extract it to a folder. 
2. Open the app.py and make the required changes.
3. Install latest version of Python for your OS.
4. Execute the below commands.

```commandline
python -m venv venv
venv\Scripts\activate
pip install flask
flask run
```
You can view the chat history by navigating to http://localhost:5000/ on your web browser.


## Limitations:

Since modern browsers does not allow to host files from the file system, to view attachments you have to right click -> Copy link address and open the link in a new tab.
