rapp::robot::communication class Reference
==========================================

#### enum Language

Language for text-to-speech module

ENGLISH  

GREEK  

Definition at line 24 of file communication.hpp

    {
    ENGLISH, 
    GREEK, 
    }Language;
                        

#### rapp::robot::communication::communication (int argc, char \*argv[])

Create communication module. Implementation object (pimpl) should be created here.

#### rapp::robot::communication::\~communication ()

Destroy communication module. Implementation object should be destroyed here.

#### bool rapp::robot::communication::play\_audio (const std::string &file\_path, double position=0, double volume=1, double balance=0, bool play\_in\_loop=false)

Produce Audio from robot's speakers


| Argument | Description |
|---|---|
|file\_path|path to the audio file|
|position|starting position|
|volume|volume level|
|balance|balance between the speakers|
|play\_in\_loop|flag for playing audio file in the loop|

#### bool rapp::robot::communication::text\_to\_speech (const std::string &str, Language language=Language::ENGLISH)

Say given sentence in selected language


| Argument | Description |
|---|---|
|str|message which will be spoken|
|lanugage|flag of the language in which the message is given|

#### std::string rapp::robot::communication::word\_spotting (const std::vector\< std::string \> &dictionary)

Recognize the word included in the database


| Argument | Description |
|---|---|
|dictionary|list of short commands|

[Todo](#todo_1_todo000001)

use vector\<string\> instead of string[]

#### std::string rapp::robot::communication::capture\_audio (int time)

Record the audio message from the microphones by the desired time


| Argument | Description |
|---|---|
|time|recording time|

#### std::string rapp::robot::communication::capture\_audio (std::string &file\_path, float waiting\_time, int microphone\_energy)

Record the audio message with silence detection


| Argument | Description |
|---|---|
|file\_path|path to the audio file, which will be recorded|
|waiting\_time|a desired waiting time in which if silence will not be broken than audio recording will be terminated|
|microphone\_energy|minimal energy for which sillence will occur|

#### int rapp::robot::communication::microphone\_energy (std::string &name)

Return signal energy of the selected microphone


| Argument | Description |
|---|---|
|name|microphone's name|

#### void rapp::robot::communication::voice\_record (bool start, std::vector\< std::vector\< unsigned char \> \> &buffer)

Record the audio message to the buffer


| Argument | Description |
|---|---|
|start||
|buffer|list of buffered messages|


