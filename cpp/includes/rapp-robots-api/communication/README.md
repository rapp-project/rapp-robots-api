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

#### bool rapp::robot::communication::play\_audio (const std::string &file\_path, double position, double volume, double balance, bool play\_in\_loop)

Produce Audio from robot's speakers

| Argument | Description |
|---|---|
|file\_path|path to the audio file|
|position||
|volume||
|balance||
|play\_in\_loop||

#### bool rapp::robot::communication::text\_to\_speech (const std::string &str, Language language=Language::ENGLISH)

Say given sentence in selected language

| Argument | Description |
|---|---|
|str||
|lanugage||

#### std::string rapp::robot::communication::word\_spotting (std::string dictionary[], int size)

Recognize the word included in the database

| Argument | Description |
|---|---|
|dictionary||
|size||

[Todo](#todo_1_todo000001)

use vector\<string\> instead of string[]

#### std::string rapp::robot::communication::capture\_audio (int time)

Record the audio message from the microphones by the desired time

| Argument | Description |
|---|---|
|time||

#### std::string rapp::robot::communication::capture\_audio (std::string &file\_path, float waiting\_time, int microphone\_energy)

Record the audio message with silence detection

| Argument | Description |
|---|---|
|file\_path||
|waiting\_time||
|microphone\_energy||

#### int rapp::robot::communication::microphone\_energy (std::string &name)

Return signal energy of the selected microphone

| Argument | Description |
|---|---|
|name||

#### void rapp::robot::communication::voice\_record (bool start, std::vector\< std::vector\< unsigned char \> \> &buffer)

Record the audio message to the buffer

| Argument | Description |
|---|---|
|start||
|buffer||


