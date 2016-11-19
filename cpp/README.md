RAPP robots API


Communication module


rapp::robot::communication class Reference
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

#### rapp::robot::communication::communication (int argc, char \*argv\[\])

Create communication module. Implementation object (pimpl) should be created here.

#### rapp::robot::communication::~communication ()

Destroy communication module. Implementation object should be destroyed here.

#### bool rapp::robot::communication::play\_audio (const std::string &file\_path, double position=0, double volume=1, double balance=0, bool play\_in\_loop=false)

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

#### bool rapp::robot::communication::text\_to\_speech (const std::string &str, Language language=Language::ENGLISH)

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

#### std::string rapp::robot::communication::word\_spotting (const std::vector&lt; std::string &gt; &dictionary)

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

#### std::string rapp::robot::communication::capture\_audio (int time)

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

#### std::string rapp::robot::communication::capture\_audio (std::string &file\_path, float waiting\_time, int microphone\_energy)

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

#### int rapp::robot::communication::microphone\_energy (std::string &name)

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

#### void rapp::robot::communication::voice\_record (bool start, std::vector&lt; std::vector&lt; unsigned char &gt; &gt; &buffer)

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


Info module


rapp::robot::info class Reference
=================================

#### Member Data Documentation

#### rapp::robot::info::info (int argc, char \*argv\[\])

Constructor takes command-line arguments and parses them to retrieve information passed by core-agent during application deployment. Those arguments may be: –base\_path

#### rapp::robot::info::info (const info &rhs)=default

Copy constructor

#### const std::string& rapp::robot::info::base\_path () const

Get path to root folder, from which application is run.

**Returns:.**

absolute path to application directory

#### std::string rapp::robot::info::get\_path (const std::string &relative\_path) const

Get absolute path to the file given its name and relative path.

**Returns:.**

absolute path to specified file

**Note:.**

file have to be installed with application (use CMake macro)

#### rapp::robot::info::info ()=delete

Default contructor removed
Localization module


rapp::robot::localization class Reference
=========================================

#### rapp::robot::localization::localization (int argc=0, char \*\*argv=NULL)

#### rapp::robot::localization::~localization ()

#### void rapp::robot::localization::pose\_from\_matrix (std::vector&lt; std::vector&lt; float &gt;&gt; matrix, rapp::object::pose &pose)

#### void rapp::robot::localization::multiply\_poses (rapp::object::pose &pose1, rapp::object::pose &pose2, rapp::object::pose &end\_pose)

#### rapp::object::pose rapp::robot::localization::qr\_code\_localization (rapp::object::qr\_code\_3d QRcodes, std::vector&lt; std::vector&lt; float &gt;&gt; camera\_to\_robot\_matrix, std::string \*MapPath)

#### rapp::object::pose rapp::robot::localization::qr\_code\_localization (rapp::object::qr\_code\_3d QRcodes, std::vector&lt; std::vector&lt; float &gt;&gt; camera\_to\_robot\_matrix, rapp::object::qr\_code\_map QRmap)

#### rapp::object::qr\_code\_map rapp::robot::localization::load\_qr\_code\_map (std::string \*is)
Navigation module


rapp::robot::navigation class Reference
=======================================

#### Member Data Documentation

#### rapp::robot::navigation::navigation (int argc=0, char \*\*argv=NULL)

Create navigation module. Implementation object (pimpl) should be created here.

#### rapp::robot::navigation::~navigation ()

Destroy navigation module. Implementation object should be destroyed here.

#### bool rapp::robot::navigation::point\_arm (float x, float y, float z)

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

#### bool rapp::robot::navigation::move\_to (float x, float y, float theta)

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

#### bool rapp::robot::navigation::move\_vel (float x, float y, float theta)

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

#### bool rapp::robot::navigation::move\_vel (float x, float theta)

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

#### bool rapp::robot::navigation::move\_stop ()

moveStop - Stop robot movement - movement initiated by moveTo, moveVel and moveAlongPath methods.

**Returns:.**

call status (false - Failed, true - Success)

#### bool rapp::robot::navigation::move\_joint (std::vector&lt; std::string &gt; joint, std::vector&lt; float &gt; angle, float speed)

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

#### bool rapp::robot::navigation::move\_joint (std::vector&lt; std::string &gt; joint, std::vector&lt; float &gt; angle)

#### bool rapp::robot::navigation::take\_predefined\_posture (std::string posture, float speed)

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

#### bool rapp::robot::navigation::look\_at\_point (float x, float y, float z)

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

#### bool rapp::robot::navigation::rest (std::string posture)

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

#### bool rapp::robot::navigation::move\_along\_path (std::vector&lt; rapp::object::pose\_stamped &gt; poses)

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

#### rapp::object::pose\_stamped rapp::robot::navigation::get\_global\_pose ()

getRobotPose - returns robot pose given in the global frame.

**Returns:.**

current robot pose in the global frame.

#### bool rapp::robot::navigation::set\_global\_pose (rapp::object::pose rapp\_pose)

setGlobalPose - sets new robot pose in the global frame. Usually is used to set new robots pose that was estimated by one of global localization methods (e.g. QR-localization).

**Returns:.**

call status (false - Failed, true - Success)

#### std::vector&lt;std::vector&lt;float&gt; &gt; rapp::robot::navigation::get\_transform (std::string chainName, int space)

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
Vision module


rapp::robot::vision class Reference
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

#### rapp::robot::vision::vision (int argc=0, char \*argv\[\]=NULL)

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

#### rapp::robot::vision::~vision ()

Destroy vision module. Implementation object should be destroyed here.

#### rapp::object::picture::Ptr rapp::robot::vision::capture\_image (int camera\_id, int camera\_resolution, const std::string &encoding)

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

#### bool rapp::robot::vision::set\_camera\_param (int camera\_id, int parameter\_id, int new\_value)

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

#### std::map&lt;int, bool&gt; rapp::robot::vision::set\_camera\_params (int camera\_id, const std::map&lt; int, int &gt; &params)

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

#### std::vector&lt; std::vector &lt;float&gt; &gt; rapp::robot::vision::face\_detect (rapp::object::picture image, int camera\_id, int camera\_resolution)

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

#### rapp::object::qr\_code\_3d rapp::robot::vision::qr\_code\_detection (rapp::object::picture::Ptr image, std::vector&lt; std::vector&lt; float &gt;&gt; robot\_to\_camera\_matrix, double camera\_matrix\[\]\[3\], float landmark\_theoretical\_size=0.16f)

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

#### camera\_info rapp::robot::vision::load\_camera\_info (int camera\_id)

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

#### void rapp::robot::vision::save\_camera\_info (int camera\_id, camera\_info info)

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


