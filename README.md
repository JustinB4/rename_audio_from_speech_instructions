# rename_audio_from_speech_instructions
How to rename wav files based on their speech contents on Windows 10.

![](example.gif)

1.	Have a Python environment set up with version 3.3+.  I have Python 3.7 in Anaconda on Windows 10.
2.	Download the [SpeechToTextFileRename_Sphinx.py](https://raw.githubusercontent.com/JustinB4/rename_audio_from_speech_instructions/main/SpeechToTextFileRename_Sphinx.py) and save it to the folder where your .wav files exist.
3.	Download [Swig for Windows](https://netix.dl.sourceforge.net/project/swig/swigwin/swigwin-3.0.12/swigwin-3.0.12.zip) – needed for pocketsphinx installation.
4.	To find your python path, at the command prompt type: `Where python`
5.	Extract the contents of the swig download to a temp folder.  Copy swig.exe to the python installation folder (ex. C:\Users\Justin\Anaconda3\envs\py37\)
6.	Open swigwin-3.0.12/Lib folder and copy all *.swg files and the typemaps folder to the py37\lib or equivalent python path.
7.	Open swigwin-3.0.12/lib/python and copy all the files to py37\lib or equivalent python path.
8.	At the command prompt type: `pip install SpeechRecognition`
9.	At the command prompt type: `pip install pocketsphinx`
10.	Cd to the directory where you r .wav files exist.
11.	At the command prompt type: `python "Speech To Text File Rename.py"`

References:
https://realpython.com/python-speech-recognition/#picking-a-python-speech-recognition-package
https://stackoverflow.com/questions/44504899/installing-pocketsphinx-python-module-command-swig-exe-failed
