# **Spotify Get Recent Playing**

Spotify Get Recent Playing is a Python program that allows you to fetch information about the most recent song you played on Spotify using Spotify's Web API. This program can be used to display the currently playing song on a website, show the song you just played on Discord, or even keep a log of the songs you've listened to.

## **Prerequisites**

Before you can use this program, you must have the following:

- Python 3.x
- A Spotify account
- A Spotify Web API Client ID and Client Secret

## **Installation**

1. Clone the repository: **`git clone https://github.com/yutaron2/spotify_get_recent_playing.git`**
2. Install the required packages: **`pip install -r requirements.txt`**
3. Set your Spotify Web API Client ID and Client Secret as environment variables:Alternatively, you can set these variables in your code by modifying the **`SPOTIPY_CLIENT_ID`** and **`SPOTIPY_CLIENT_SECRET`** variables in **`main.py`**.
    
    ```
    export SPOTIPY_CLIENT_ID='your_client_id_here'
    export SPOTIPY_CLIENT_SECRET='your_client_secret_here'
    
    ```
    

## **Usage**

1. Run the program: **`python main.py`**
2. The program will fetch information about your most recently played song and display it in the terminal.

## **Customization**

You can customize the behavior of this program by modifying the following variables in **`main.py`**:

- **`MARKDOWN_FORMAT`**: If set to **`True`**, the program will output the song information in Markdown format.
- **`LOG_FILE_PATH`**: If set to a valid file path, the program will write the song information to a log file.
