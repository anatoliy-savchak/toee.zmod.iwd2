# About
This project is IWD2 to ToEE Temple+ port. Currently in development.

# Installation For Users
## Requirements
1. **ToEE** installed.
2. **Temple+** installed latest version.
3. **The Circle of Eight Modpack: Standard Edition** (or New Content Edition) installed and activated. [Co8 Download Central](https://co8.org/community/forums/download-central.90/)

## Steps to install
1. Download or clone this repo into some folder.
2. Copy `src\zmod_iwd2` into ToEE\modules folder.
3. Copy `src\zmod_iwd2_core`_core into ToEE\modules folder.
4. Activate zmod_iwd2 module in **Temple+ Configuration** app:
    1. Open %USERPROFILE%\Saved Games\TemplePlus\TemplePlus.ini in a Text Editor
    2. Change defaultModule setting to zmod_iwd2
    3. Should be: `defaultModule=zmod_iwd2`
    4. *Note: Temple+ Configuration app will reset the setting if launched and Okayed. After which redo sub-steps again.*
5. Run **Temple+** to try out.

## Recommendations
1. Do not spend time to create uber heroes PC until the project is completed or ins some playable state. Use pregenerated to try out.

# Installation For Developers
1. Same as for Users, but move zmod_iwd2 and zmod_iwd2_core folders into ToEE/modules and make hard links back to src. See commands in settings\map_module.cmd
2. *Recommended* Temple+ built in Visual Studio 2019 (tested in Community 16.9.4).
    1. Place breakpoints everywhere on line `PyErr_Print();` to debug Python error occurences.
    2. Place breakpoint on `PyArg_ParseTuple(args, "s:info", &s);` in python_debug.cpp to debug semi-breakpoints in Python.
3. Open `src\toee.zmod.iwd2.sln` in Visual Studio 2019 just for editing.