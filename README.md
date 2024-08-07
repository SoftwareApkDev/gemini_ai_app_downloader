# gemini_ai_app_downloader

An app which can be used to easily download any apps with Google Gemini AI integrated into them.

# Downloadable Apps

| Name                                                                                 | Author                                                          | Latest Version |
|--------------------------------------------------------------------------------------|-----------------------------------------------------------------|----------------|
| [Gemini Simple Game](https://pypi.org/project/gemini-simple-game/)                   | [SoftwareApkDev](https://github.com/SoftwareApkDev)             | 1              |
| [Gemini TXT Analyser](https://pypi.org/project/gemini-txt-analyser/)                 | [SoftwareApkDev](https://github.com/SoftwareApkDev)             | 1              |
| [Gemini PDF Analyser](https://pypi.org/project/gemini-pdf-analyser/)                 | [SoftwareApkDev](https://github.com/SoftwareApkDev)             | 1              |
| [Gemini Code Generator](https://pypi.org/project/gemini-code-generator/)             | [SoftwareApkDev](https://github.com/SoftwareApkDev)             | 1              |
| [Gemini Match Word Puzzle](https://pypi.org/project/gemini-match-word-puzzle/)       | [SoftwareApkDev](https://github.com/SoftwareApkDev)             | 1              | 
| [Gemini Random Generator](https://pypi.org/project/gemini-random-generator/)         | [SoftwareApkDev](https://github.com/SoftwareApkDev)             | 1              | 
| [Gemini CLI Planet Adventure](https://pypi.org/project/gemini-cli-planet-adventure/) | [GlobalCreativeApkDev](https://github.com/GlobalCreativeApkDev) | 1              |
| [Gemini CLI Creature Hunter](https://pypi.org/project/gemini-cli-creature-hunter/)   | [GlobalCreativeApkDev](https://github.com/GlobalCreativeApkDev) | 1              |

# How to Add Your Downloadable App?

1. Enter the name of your app on a new line in the file apps.txt.
2. Ensure that the name of the app you entered is already available as a PyPi project, with the format containing 
at least like below, where [your_app_name] is the name of your app and [entry_point_name] is the name
of the entry point of your app.

[your_app_name]

----└── [your_app_name]

--------├── [entry_point_name].py

----├── setup.py

3. Create a fork or a new branch and then merge it to **master** branch of this repository.
4. Add the app to **Downloadable Apps** section of this document.

# Source Code

The source code of the application **Gemini AI App Downloader** is found 
in [main.py](https://github.com/SoftwareApkDev/gemini_ai_app_downloader/blob/master/main.py).

# Installation

```
pip install gemini-ai-app-downloader
```

# How to Use the Application?

Pre-requisites:

1. [Python](https://www.python.org/downloads/) installed in your device.
2. .env file in the same directory as <GEMINI_AI_APP_DOWNLOADER_DIRECTORY> and has the value of GEMINI_API_KEY.

First, open a Terminal or Command Prompt window and run the following commands.

```
cd <GEMINI_AI_APP_DOWNLOADER_DIRECTORY>
python3 main.py
```

**Note:** Replace <GEMINI_AI_APP_DOWNLOADER_DIRECTORY> with the path to the directory of the 
application **Gemini AI App Downloader**.

Then, the application will start with something looking like in the screenshot below.

![Main Menu](images/Main%20Menu.png)

You can now do one of the following by following the instructions shown in the command prompt.

1. Install an app.
2. Run an app you have installed.
3. Uninstall an app.

# Install an App

Once you chose to install an app, you can enter the name of the app of your choice.

![Install App](images/Install%20App.png)

# Running an Installed App

Once you chose to play an app you have installed, you can enter the name of the app of your choice.

![Run Installed App](images/Run%20Installed%20App.png)

Then, the app of your choice is started.

# Uninstall an App

Once you chose to uninstall an app, you can enter the index of the app of your choice.

![Uninstall App](images/Uninstall%20App.png)
