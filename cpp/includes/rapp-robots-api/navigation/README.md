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
