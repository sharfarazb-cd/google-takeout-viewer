# Google Chat History Viewer

A simple Flask app to read the Google Chat history from Google Takeout. This project reads the JSON files from various directories within the Takeout folder and presents it in an organized manner.

## Configuration

In `app.py`, `BASE_PATH` and `USER_EMAIL` should be updated before you run the app. `BASE_PATH` should be till the Groups folder inside the Takeout, and `USER_EMAIL` should be the email of the Takeout owner.

```python
BASE_PATH = "C:\\Users\\John\\Documents\\Takeout\\Google Chat\\Groups"
USER_EMAIL = "johnd@gmail.com"
```

## Limitations:

Since modern browsers does not allow to host files from the file system, to view attachments you have to right click -> Copy link address and open the link in a new tab.
