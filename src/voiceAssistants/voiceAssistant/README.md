# How to Use
**AS OF RIGHT NOW, ONLY MAC IS SUPPORTED**

1. Navigate to the releases panel
2. Select the version you want to install
3. Download the "Assistant.zip" file
4. Unzip the file
5. Run ``python /path/to/voiceAssistant/folder/main.py`` or ``python3 /path/to/voiceAssistant/folder/main.py`` depending on your computer and the version of python you have installed
6. The voice assistant is now running
   1. In version 0.5.0 the voice assistant doesn't yet have voice recognition, but the primary features have been implemented with a text based input system

# Functions

All caps are parameters that need to be replaced for running. What the paremeters are is specified in the section for that function.

## The Commands Module
The commands module executes the commands based on the operating system. It will choose automatically if it should run the windows, mac or linux versions.

### Open App
**The Function:** ``command.open_app('APP')``

**Parameters:**
1. APP: The name of the app you want to open. (Case Sensitive)

**What it does:** Opens an app from the app provided in the parameter. It returns ```False``` when the app doesn't exist, ```True``` when it opens an app.

### Open Directory
**The Function:** ``command.open_directory_in_files('DIRECTORY')``

**Parameters:**
1. DIRECTORY: The path to the directory you wish to open

**What it does:** Opens a directory in the file explorer for the operating system. Returns ```True``` if the directory exists, ```False``` if it doesn't.

### Open File

**The Function:** ``command.open_file('FILE')``

**Parameters:**
1. FILE: The file you want to open

**What it does:** Opens the file specified in the system default app (The app that opens it when double-clicked in the files app). Returns ```False``` if the files doesn't exist, ```True``` if it does.

### Open Webpage

**The Function:** ``command.open_webpage('PAGE')``

**Parameters:**
1. PAGE: The url for the webpage you want to open

**What it does:** Opens the specified webpage in your browser. ```https://``` is added to the front of the provided webpage, and doesn't need to be done manually

### Google Search

**The Function:** ``command.google_search('QUERY')``

**Parameters:**
1. QUERY: The thing you want to search for

**What it does:** Opens Google in your browser at the specified query and returns the url it sent you to

### Hide App

**The Function:** ```command.hide_app(APP_NAME):```

**Parameters:**
1. APP_NAME: The name of the app you want to hide

**What it does:** On Mac, it hides the app given, the same as pressing ⌘h on the keyboard

### Play Music

**The Function:** ```command.play()```

**Parameters:** This Function has no parameters

**What it does:** Opens spotify and starts playing music

### Pause Music

**The Function:** ```command.pause()```

**Parameters:** This Function has no parameters

**What it does:** Pauses the music playing within spotify

## The Audio Module
The Audio module houses the commands for speaking and voice recognition

### Speak

**The Function:** ``audio.speak('TEXT', printout=True)``

**Parameters:**
1. TEXT: What to say
2. printout: Printout is an optional variable (set to ```True``` by default) that allows you to toggle the printout

**What it does:** Says whatever is specified inside of TEXT

## The Helpers Module
The helpers module has random junk, that isn't used big enough to warrant its own module

### Get Details

**The Function:** ``helpers.get_details()``

**Parameters:** This Function has no parameters

**What it does:** returns the values saved inside ```details.txt```, currently the username and the assistant's name.

### Remove Keyword

**The Function:** ``helpers.remove_keyword(TEXT, KEYWORD)``

**Parameters:**
1. TEXT: The input text
2. KEYWORD: The keyword to be removed

**What it does:** Removes the keyword from the text provided