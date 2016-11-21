RAPP robots API
===============

**Note:** All classes are under ```rapp::robots``` namespace


communication class Reference
==========================================

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

#### communication::communication (int argc, char \*argv\[\])

Create communication module. Implementation object (pimpl) should be created here.

#### communication::~communication ()

Destroy communication module. Implementation object should be destroyed here.

#### bool communication::play\_audio (const std::string &file\_path, double position=0, double volume=1, double balance=0, bool play\_in\_loop=false)

Produce Audio from robot's speakers



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

#### bool communication::text\_to\_speech (const std::string &str, Language language=Language::ENGLISH)

Say given sentence in selected language



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

#### std::string communication::word\_spotting (const std::vector&lt; std::string &gt; &dictionary)

Recognize the word included in the database



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

#### std::string communication::capture\_audio (int time)

Record the audio message from the microphones by the desired time



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

#### std::string communication::capture\_audio (std::string &file\_path, float waiting\_time, int microphone\_energy)

Record the audio message with silence detection



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

#### int communication::microphone\_energy (std::string &name)

Return signal energy of the selected microphone



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

#### void communication::voice\_record (bool start, std::vector&lt; std::vector&lt; unsigned char &gt; &gt; &buffer)

Record the audio message to the buffer



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


info class Reference
=================================

#### Member Data Documentation

#### info::info (int argc, char \*argv\[\])

Constructor takes command-line arguments and parses them to retrieve information passed by core-agent during application deployment. Those arguments may be: –base\_path

#### info::info (const info &rhs)=default

Copy constructor

#### const std::string& info::base\_path () const

Get path to root folder, from which application is run.

**Returns:.**

absolute path to application directory

#### std::string info::get\_path (const std::string &relative\_path) const

Get absolute path to the file given its name and relative path.

**Returns:.**

absolute path to specified file

**Note:.**

file have to be installed with application (use CMake macro)

#### info::info ()=delete

Default contructor removed
localization class Reference
=========================================

#### localization::localization (int argc=0, char \*\*argv=NULL)

Create localization module. Handles transformation matrices, convertion to rapp::object::pose objects and other localication related methods.

#### localization::~localization ()

Destroy localization module. Implementation object should be destroyed here.

#### rapp::object::quaternion localization::quaternion\_from\_euler (float roll, float pitch, float yaw)

quaternion\_from\_euler - convert euler (ZYX) angles to rapp::object::quaternion object.



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">roll</td>
<td align="left"><p>- angle around X direction.</p></td>
</tr>
<tr class="even">
<td align="left">pitch</td>
<td align="left"><p>- angle around Y direction.</p></td>
</tr>
<tr class="odd">
<td align="left">yaw</td>
<td align="left"><p>- angle around Z direction.</p></td>
</tr>
</tbody>
</table>

**Returns:.**

rapp::object::quaternion

#### std::vector&lt;std::vector&lt;float&gt; &gt; localization::invert\_transform (std::vector&lt; std::vector&lt; float &gt;&gt; matrix\_input)

invert\_transform - invert transformation matrix.



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">matrix_input</td>
<td align="left"><p>- input matrix.</p></td>
</tr>
</tbody>
</table>

**Returns:.**

std::vector&lt;std::vector&lt;float&gt;&gt; inverted matrix

#### std::vector&lt;float&gt; localization::euler\_from\_quaternion (rapp::object::quaternion &rapp\_quaternion)

euler\_from\_quaternion - convert rapp::object::quaternion object to euler (ZYX) angles.



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">rapp_quaternion</td>
<td align="left"><p>- input quaternion object.</p></td>
</tr>
</tbody>
</table>

**Returns:.**

std::vector&lt;float&gt; - euler angles: \[0\] - angle around X direction, \[1\] - angle around Y direction, \[2\] - angle around Z direction.

#### void localization::pose\_from\_matrix (std::vector&lt; std::vector&lt; float &gt;&gt; &matrix, rapp::object::pose &pose)

pose\_from\_matrix - convert transformation matrix to the rapp::object::pose object.



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">matrix</td>
<td align="left"><p>- input transformation matrix.</p></td>
</tr>
<tr class="even">
<td align="left">pose</td>
<td align="left"><p>- output rapp::object::pose object.</p></td>
</tr>
</tbody>
</table>

#### void localization::multiply\_poses (rapp::object::pose &pose1, rapp::object::pose &pose2, rapp::object::pose &end\_pose)

multiply\_poses - multiply transformation matrices given by rapp::object::pose objects: pose1\_matrix \* pose2\_matrix = end\_pose\_matrix.



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">pose1</td>
<td align="left"><p>- input rapp::object::pose object -&gt; pose1.</p></td>
</tr>
<tr class="even">
<td align="left">pose2</td>
<td align="left"><p>- input rapp::object::pose object -&gt; pose2.</p></td>
</tr>
<tr class="odd">
<td align="left">end_pose</td>
<td align="left"><p>- output rapp::object::pose object.</p></td>
</tr>
</tbody>
</table>

#### rapp::object::pose localization::qr\_code\_localization (rapp::object::qr\_code\_3d QRcodes, std::vector&lt; std::vector&lt; float &gt;&gt; camera\_to\_robot\_matrix, std::string \*MapPath)

qr\_code\_localization - multiply transformation matrices given by rapp::object::pose objects: pose1\_matrix \* pose2\_matrix = end\_pose\_matrix.



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">QRcodes</td>
<td align="left"><p>- found QR Codes (using <a href="#classrapp_1_1robot_1_1vision_1a69686bb466264298e39f08bf1362a39a">vision::qr_code_detection</a> method),</p></td>
</tr>
<tr class="even">
<td align="left">camera_to_robot_matrix</td>
<td align="left"><p>- transformation matrix from camera coordination frame to robot coordination frame,</p></td>
</tr>
<tr class="odd">
<td align="left">MapPath</td>
<td align="left"><p>- path to the QRcode map (given by .xml file as desribed here: <a href="https://github.com/rapp-project/rapp-robots-api/wiki/localization#create-qr-code-map">QR code map creation tutorial</a> ).</p></td>
</tr>
</tbody>
</table>

**Returns:.**

pose - robot pose in the global coordination frame.

#### rapp::object::pose localization::qr\_code\_localization (rapp::object::qr\_code\_3d QRcodes, std::vector&lt; std::vector&lt; float &gt;&gt; camera\_to\_robot\_matrix, rapp::object::qr\_code\_map QRmap)

qr\_code\_localization - multiply transformation matrices given by rapp::object::pose objects: pose1\_matrix \* pose2\_matrix = end\_pose\_matrix.



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">QRcodes</td>
<td align="left"><p>- found QR Codes (using <a href="#classrapp_1_1robot_1_1vision_1a69686bb466264298e39f08bf1362a39a">vision::qr_code_detection</a> method),</p></td>
</tr>
<tr class="even">
<td align="left">camera_to_robot_matrix</td>
<td align="left"><p>- transformation matrix from camera coordination frame to robot coordination frame,</p></td>
</tr>
<tr class="odd">
<td align="left">QRmap</td>
<td align="left"><p>- QR code map object, can be loaded using <a href="#classrapp_1_1robot_1_1localization_1a3241d5c934ca278e90e93ee27b1ae70e">localization::load_qr_code_map</a> method.</p></td>
</tr>
</tbody>
</table>

**Returns:.**

pose - robot pose in the global coordination frame.

#### rapp::object::qr\_code\_map localization::load\_qr\_code\_map (std::string \*is)

load\_qr\_code\_map - multiply transformation matrices given by rapp::object::pose objects: pose1\_matrix \* pose2\_matrix = end\_pose\_matrix.



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">is</td>
<td align="left"><p>- path to the QR code map file (.xml file). Map file shoud be created as desribed here: <a href="https://github.com/rapp-project/rapp-robots-api/wiki/localization#create-qr-code-map">QR code map creation tutorial</a>),</p></td>
</tr>
</tbody>
</table>

**Returns:.**

QRcodeMap - contains poses of all lendmarks in the environment.
navigation class Reference
=======================================

#### Member Data Documentation

#### navigation::navigation (int argc=0, char \*\*argv=NULL)

Create navigation module. Implementation object (pimpl) should be created here.

#### navigation::~navigation ()

Destroy navigation module. Implementation object should be destroyed here.

#### bool navigation::point\_arm (float x, float y, float z)

point\_arm - move NAO arm to point its fingers to the reqested point given in the global coordinate frame.



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">x</td>
<td align="left"><p>- X coordination of the requested point.</p></td>
</tr>
<tr class="even">
<td align="left">y</td>
<td align="left"><p>- Y coordination of the requested point.</p></td>
</tr>
<tr class="odd">
<td align="left">z</td>
<td align="left"><p>- z coordination of the requested point.</p></td>
</tr>
</tbody>
</table>

**Returns:.**

call status (false - Failed, true - Success)

#### bool navigation::move\_to (float x, float y, float theta)

moveTo - initiate move to specified point given by (x,y,theta) coordinates, with respect to current NAO coordination frame.



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">x</td>
<td align="left"><p>- X coordination of the goal point.</p></td>
</tr>
<tr class="even">
<td align="left">y</td>
<td align="left"><p>- Y coordination of the goal point.</p></td>
</tr>
<tr class="odd">
<td align="left">theta</td>
<td align="left"><p>- Orientation of NAO in the goal point.</p></td>
</tr>
</tbody>
</table>

**Returns:.**

call status (false - Failed, true - Success)

#### bool navigation::move\_vel (float x, float y, float theta)

moveVel - initiate move with the specified linear velocities in x, y axis direction and angular velocity theta. This version works with holonomic robots (like NAO)



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">x</td>
<td align="left"><p>- velocity along robots X axis.</p></td>
</tr>
<tr class="even">
<td align="left">y</td>
<td align="left"><p>- velocity along robots Y axis.</p></td>
</tr>
<tr class="odd">
<td align="left">theta</td>
<td align="left"><p>- velocity around robots Z axis.</p></td>
</tr>
</tbody>
</table>

**Returns:.**

call status (false - Failed, true - Success)

#### bool navigation::move\_vel (float x, float theta)

moveVel - initiate move with the specified linear velocities in x, y axis direction and angular velocity theta. This version works for non-holonimic robots (e.g. differential drive)



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">x</td>
<td align="left"><p>- velocity along robots X axis.</p></td>
</tr>
<tr class="even">
<td align="left">theta</td>
<td align="left"><p>- velocity around robots Z axis.</p></td>
</tr>
</tbody>
</table>

**Returns:.**

call status (false - Failed, true - Success)

#### bool navigation::move\_stop ()

moveStop - Stop robot movement - movement initiated by moveTo, moveVel and moveAlongPath methods.

**Returns:.**

call status (false - Failed, true - Success)

#### bool navigation::move\_joint (std::vector&lt; std::string &gt; joint, std::vector&lt; float &gt; angle, float speed)

moveJoint - move given joints/given chain to specified angle with specified maximum joints speed fraction.



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">joint</td>
<td align="left"><p>- joints/chain names that are being requested to move.</p></td>
</tr>
<tr class="even">
<td align="left">angle</td>
<td align="left"><p>- Destination angle of joints.</p></td>
</tr>
<tr class="odd">
<td align="left">speed</td>
<td align="left"><p>- maximum joints speed fraction (Value of 1 - max speed, value of 0 - no move).</p></td>
</tr>
</tbody>
</table>

Avaliable joints and chains are as follows:

|                      |                    |                |                 |                 |                |
|----------------------|--------------------|----------------|-----------------|-----------------|----------------|
| The chain ...        | Head               | LArm           | LLeg            | RLeg            | RArm           |
| joints ...           | HeadYaw            | LShoulderPitch | LHipYawPitch !! | RHipYawPitch !! | RShoulderPitch |
| \_\_\_\_\_\_\_\_\_\_ | HeadPitch          | LShoulderRoll  | LHipRoll        | RHipRoll        | RShoulderRoll  |
| \_\_\_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_\_ | LElbowYaw      | LHipPitch       | RHipPitch       | RElbowYaw      |
| \_\_\_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_\_ | LElbowRoll     | LKneePitch      | RKneePitch      | RElbowRoll     |
| \_\_\_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_\_ | LWristYaw !    | LAnklePitch     | RAnklePitch     | RWristYaw !    |
| \_\_\_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_\_ | LHand !        | RAnkleRoll      | LAnkleRoll      | RHand !        |

-&gt; ! - these joints do not exist in the NAO Body type “H21”. -&gt; !! - LHipYawPitch and RHipYawPitch share the same motor so they move simultaneously and symmetrically. In case of conflicting orders, LHipYawPitch always takes the priority.

**Returns:.**

call status (false - Failed, true - Success)

#### bool navigation::move\_joint (std::vector&lt; std::string &gt; joint, std::vector&lt; float &gt; angle)

#### bool navigation::take\_predefined\_posture (std::string posture, float speed)

takePredefinedPosture - Take predefined robot posture.



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">posture</td>
<td align="left"><p>- name of the predefined posture: StandInit, Stand, StandZero, LyingBack, LyingBelly, Crouch, Sit, SitRelax.</p></td>
</tr>
<tr class="even">
<td align="left">speed</td>
<td align="left"><p>- maximum speed fraction (Value of 1 - max speed, value of 0 - no move).</p></td>
</tr>
</tbody>
</table>

**Returns:.**

call status (false - Failed, true - Success)

#### bool navigation::look\_at\_point (float x, float y, float z)

lookAtPoint - Move robot to point it's main camera to a given point (x,y,z).



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">x</td>
<td align="left"><p>- X coordination of the point in the global frame.</p></td>
</tr>
<tr class="even">
<td align="left">y</td>
<td align="left"><p>- Y coordination of the point in the global frame.</p></td>
</tr>
<tr class="odd">
<td align="left">z</td>
<td align="left"><p>- Z coordination of the point in the global frame.</p></td>
</tr>
</tbody>
</table>

**Returns:.**

call status (false - Failed, true - Success)

#### bool navigation::rest (std::string posture)

rest - take given safe posture and remove motors stiffness. If the given posture is not safe - returns False.



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">posture</td>
<td align="left"><p>- name of the safe posture: &quot;Crouch&quot;,&quot;Sit&quot;,&quot;SitRelax&quot;,&quot;LyingBelly&quot;,&quot;LyingBack&quot;.</p></td>
</tr>
</tbody>
</table>

**Returns:.**

call status (false - Failed, true - Success)

#### bool navigation::move\_along\_path (std::vector&lt; rapp::object::pose\_stamped &gt; poses)

moveAlongPath - move robot along the given path. It moves with standard velocity, untill the end is reached or any obstacle was met.



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">poses</td>
<td align="left"><p>- vector of poses that specifies the desired path.</p></td>
</tr>
</tbody>
</table>

**Returns:.**

call status (false - Failed, true - Success)

#### rapp::object::pose\_stamped navigation::get\_global\_pose ()

getRobotPose - returns robot pose given in the global frame.

**Returns:.**

current robot pose in the global frame.

#### bool navigation::set\_global\_pose (rapp::object::pose rapp\_pose)

setGlobalPose - sets new robot pose in the global frame. Usually is used to set new robots pose that was estimated by one of global localization methods (e.g. QR-localization).

**Returns:.**

call status (false - Failed, true - Success)

#### std::vector&lt;std::vector&lt;float&gt; &gt; navigation::get\_transform (std::string chainName, int space)

getTransform - return homogeneous transformation matrix of given chain in the given space.


<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">chainName</td>
<td align="left"><p>- name of the desired chain:</p></td>
</tr>
<tr class="even">
<td align="left">space</td>
<td align="left"><p>- desired space.</p></td>
</tr>
</tbody>
</table>

Avaliable joints are as follows:

|                    |                |                 |                 |                |
|--------------------|----------------|-----------------|-----------------|----------------|
| Head               | LArm           | LLeg            | RLeg            | RArm           |
| HeadYaw            | LShoulderPitch | LHipYawPitch !! | RHipYawPitch !! | RShoulderPitch |
| HeadPitch          | LShoulderRoll  | LHipRoll        | RHipRoll        | RShoulderRoll  |
| \_\_\_\_\_\_\_\_\_ | LElbowYaw      | LHipPitch       | RHipPitch       | RElbowYaw      |
| \_\_\_\_\_\_\_\_\_ | LElbowRoll     | LKneePitch      | RKneePitch      | RElbowRoll     |
| \_\_\_\_\_\_\_\_\_ | LWristYaw !    | LAnklePitch     | RAnklePitch     | RWristYaw !    |
| \_\_\_\_\_\_\_\_\_ | LHand !        | RAnkleRoll      | LAnkleRoll      | RHand !        |

-&gt; ! - these joints do not exist in the NAO Body type “H21”. -&gt; !! - LHipYawPitch and RHipYawPitch share the same motor so they move simultaneously and symmetrically. In case of conflicting orders, LHipYawPitch always takes the priority.

**Returns:.**

homogeneous transformation matrix of given chain in the given space
vision class Reference
===================================

#### enum camera\_params

Camera parameters

**Enumerator:.**

brightness  

contrast  

gain  

auto\_exposure  

auto\_white\_balance  

exposure  

Definition at line 36 of file vision.hpp `
{
brightness= 0, 
contrast= 1, 
gain= 6, 
auto_exposure= 11, 
auto_white_balance= 12, 
exposure= 17, 
}camera_params;
                    `

#### enum camera\_resolution

Camera resolution

**Enumerator:.**

qqvga  

qvga  

vga  

vga4  

Definition at line 48 of file vision.hpp `
{
qqvga= 0, 
qvga= 1, 
vga= 2, 
vga4= 3, 
}camera_resolution;
                    `

#### Member Data Documentation

Pointer to implementation class.

**See also:.**

Cheshire Cat (pimpl) programming pattern

Definition at line 145 of file vision.hpp

The Documentation for this struct was generated from the following file:

-   vision.hpp

#### vision::vision (int argc=0, char \*argv\[\]=NULL)

Create vision module. Implementation object (pimpl) should be created here.



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">argc</td>
<td align="left"><p>number of arguments passed from host process</p></td>
</tr>
<tr class="even">
<td align="left">argv</td>
<td align="left"><p>list of arguments passed from host process</p></td>
</tr>
</tbody>
</table>

#### vision::~vision ()

Destroy vision module. Implementation object should be destroyed here.

#### rapp::object::picture::Ptr vision::capture\_image (int camera\_id, int camera\_resolution, const std::string &encoding)

Capture an image frame from the robot’s camera.



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">camera_id</td>
<td align="left"><p>ID of the camera to be used</p></td>
</tr>
<tr class="even">
<td align="left">camera_resolution</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left">encoding</td>
<td align="left"><p>output image encoding type (e.g. &quot;png&quot;, &quot;jpg&quot;)</p></td>
</tr>
</tbody>
</table>

**Returns:.**

captured image as raw byte stream

#### bool vision::set\_camera\_param (int camera\_id, int parameter\_id, int new\_value)

Set camera parameter.



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">camera_id</td>
<td align="left"><p>ID of the camera to be used</p></td>
</tr>
<tr class="even">
<td align="left">parameter_id</td>
<td align="left"><p>ID of the parameter to be changed</p></td>
</tr>
<tr class="odd">
<td align="left">new_value</td>
<td align="left"><p>new value for the selected parameter</p></td>
</tr>
</tbody>
</table>

**Returns:.**

true on success, false otherwise

#### std::map&lt;int, bool&gt; vision::set\_camera\_params (int camera\_id, const std::map&lt; int, int &gt; &params)

Set multiple camera parameters at once.



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">camera_id</td>
<td align="left"><p>ID of the camera to be used</p></td>
</tr>
<tr class="even">
<td align="left">params</td>
<td align="left"><p>map of pairs param_id-&gt;new_value</p></td>
</tr>
</tbody>
</table>

**Returns:.**

success flag for each parameter

#### std::vector&lt; std::vector &lt;float&gt; &gt; vision::face\_detect (rapp::object::picture image, int camera\_id, int camera\_resolution)

Detects faces.



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">image</td>
<td align="left"><p>for the face detection</p></td>
</tr>
<tr class="even">
<td align="left">camera_id</td>
<td align="left"><p>ID of the camera to be used</p></td>
</tr>
<tr class="odd">
<td align="left">camera_resolution</td>
<td align="left"><p>map of pairs param_id-&gt;new_value</p></td>
</tr>
</tbody>
</table>

**Returns:.**

vector of informations about the detected face

#### rapp::object::qr\_code\_3d vision::qr\_code\_detection (rapp::object::picture::Ptr image, std::vector&lt; std::vector&lt; float &gt;&gt; robot\_to\_camera\_matrix, double camera\_matrix\[\]\[3\], float landmark\_theoretical\_size=0.16f)

Detects QR-codes.



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">image</td>
<td align="left"><p>image for the QR-code detection</p></td>
</tr>
<tr class="even">
<td align="left">robot_to_camera_matrix</td>
<td align="left"><p>transformation matrix from robot to camera framework</p></td>
</tr>
<tr class="odd">
<td align="left">camera_matrix</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left">landmark_theoretical_size</td>
<td align="left"></td>
</tr>
</tbody>
</table>

**Returns:.**

QR-codes informations

#### camera\_info vision::load\_camera\_info (int camera\_id)

Load camera calibration info for selected camera. If no calibration data is present, default values are returned.



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">camera_id</td>
<td align="left"><p>selected camera id</p></td>
</tr>
</tbody>
</table>

#### void vision::save\_camera\_info (int camera\_id, camera\_info info)

Save camera info for selected camera in persistend storage



<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">camera_id</td>
<td align="left"><p>selected caemra id</p></td>
</tr>
<tr class="even">
<td align="left">info</td>
<td align="left"><p>new camera parameters to be stored</p></td>
</tr>
</tbody>
</table>


