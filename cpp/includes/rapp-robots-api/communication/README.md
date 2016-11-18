rapp::robot::communication class Reference
==========================================

#### Private Attributes

-   CommunicationImpl \* pimpl

-   [communication](#classrapp_1_1robot_1_1communication_1a7d7dfff1c4e937c5d7533c9fc2a6b10f) ( int argc, char \* argv)

<!-- -->

-   [~communication](#classrapp_1_1robot_1_1communication_1a058277d8b280b5b8e6354a0f1c4d274d) ( )

<!-- -->

-   bool [play\_audio](#classrapp_1_1robot_1_1communication_1a3ac78a92ba140819ccf4d68e4a63e82d) ( const std::string & file\_path, double position, double volume, double balance, bool play\_in\_loop)

<!-- -->

-   bool [text\_to\_speech](#classrapp_1_1robot_1_1communication_1a437818af851c59b0b91e1f60d57a4ab4) ( const std::string & str, [Language](#classrapp_1_1robot_1_1communication_1aa68950f71c5f18df6816725b50c3c62e) language)

<!-- -->

-   std::string [word\_spotting](#classrapp_1_1robot_1_1communication_1a31eded62fe44c2ca36a15fd4f116215e) ( const std::vector&lt; std::string &gt; & dictionary)

<!-- -->

-   std::string [capture\_audio](#classrapp_1_1robot_1_1communication_1a357f732e88ebb692a43b0e11577e8e99) ( int time)

<!-- -->

-   std::string [capture\_audio](#classrapp_1_1robot_1_1communication_1a00360013bf4487ab92eb6543c1325615) ( std::string & file\_path, float waiting\_time, int microphone\_energy)

<!-- -->

-   int [microphone\_energy](#classrapp_1_1robot_1_1communication_1a201a99034d36e19b325a34b764cdb651) ( std::string & name)

<!-- -->

-   void [voice\_record](#classrapp_1_1robot_1_1communication_1a3e7ed35ec0bd788f28b824ecb71490f0) ( bool start, std::vector&lt; std::vector&lt; unsigned char &gt; &gt; & buffer)

Interface class for robot communication module.

**Version:.**

1

**Date:.**

20-September-2015

**Author:.**

Maksym Figat <m.figat@ia.pw.edu.pl>

Definition at line 18 of file communication.hpp

The Documentation for this struct was generated from the following file:

-   communication.hpp

#### enum Language

Language for text-to-speech module

**Enumerator:.**

ENGLISH  

GREEK  

Definition at line 24 of file communication.hpp `
{
ENGLISH, 
GREEK, 
}Language;
                    `

#### Member Data Documentation

#### rapp::robot::communication::communication (int argc, char \*argv\[\])

Create communication module. Implementation object (pimpl) should be created here.

#### rapp::robot::communication::~communication ()

Destroy communication module. Implementation object should be destroyed here.

#### bool rapp::robot::communication::play\_audio (const std::string &file\_path, double position=0, double volume=1, double balance=0, bool play\_in\_loop=false)

Produce Audio from robot's speakers

**.**

<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">file_path</td>
<td align="left"><p>path to the audio file</p></td>
</tr>
<tr class="even">
<td align="left">position</td>
<td align="left"><p>starting position</p></td>
</tr>
<tr class="odd">
<td align="left">volume</td>
<td align="left"><p>volume level</p></td>
</tr>
<tr class="even">
<td align="left">balance</td>
<td align="left"><p>balance between the speakers</p></td>
</tr>
<tr class="odd">
<td align="left">play_in_loop</td>
<td align="left"><p>flag for playing audio file in the loop</p></td>
</tr>
</tbody>
</table>

**Returns:.**

#### bool rapp::robot::communication::text\_to\_speech (const std::string &str, Language language=Language::ENGLISH)

Say given sentence in selected language

**.**

<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">str</td>
<td align="left"><p>message which will be spoken</p></td>
</tr>
<tr class="even">
<td align="left">language</td>
<td align="left"><p>flag of the language in which the message is given</p></td>
</tr>
</tbody>
</table>

**Returns:.**

#### std::string rapp::robot::communication::word\_spotting (const std::vector&lt; std::string &gt; &dictionary)

Recognize the word included in the database

**.**

<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">dictionary</td>
<td align="left"><p>list of short commands</p></td>
</tr>
</tbody>
</table>

**Returns:.**

[Todo](#todo_1_todo000001)

use vector&lt;string&gt; instead of string\[\]

#### std::string rapp::robot::communication::capture\_audio (int time)

Record the audio message from the microphones by the desired time

**.**

<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">time</td>
<td align="left"><p>recording time</p></td>
</tr>
</tbody>
</table>

**Returns:.**

#### std::string rapp::robot::communication::capture\_audio (std::string &file\_path, float waiting\_time, int microphone\_energy)

Record the audio message with silence detection

**.**

<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">file_path</td>
<td align="left"><p>path to the audio file, which will be recorded</p></td>
</tr>
<tr class="even">
<td align="left">waiting_time</td>
<td align="left"><p>a desired waiting time in which if silence will not be broken than audio recording will be terminated</p></td>
</tr>
<tr class="odd">
<td align="left">microphone_energy</td>
<td align="left"><p>minimal energy for which sillence will occur</p></td>
</tr>
</tbody>
</table>

#### int rapp::robot::communication::microphone\_energy (std::string &name)

Return signal energy of the selected microphone

**.**

<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">name</td>
<td align="left"><p>microphone's name</p></td>
</tr>
</tbody>
</table>

**Returns:.**

#### void rapp::robot::communication::voice\_record (bool start, std::vector&lt; std::vector&lt; unsigned char &gt; &gt; &buffer)

Record the audio message to the buffer

**.**

<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">start</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left">buffer</td>
<td align="left"><p>list of buffered messages</p></td>
</tr>
</tbody>
</table>


