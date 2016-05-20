rapp::robot::navigation class Reference
=======================================

#### rapp::robot::navigation::navigation (int argc=0, char \*\*argv=NULL)

Create navigation module. Implementation object (pimpl) should be created here.

#### rapp::robot::navigation::\~navigation ()

Destroy navigation module. Implementation object should be destroyed here.

#### bool rapp::robot::navigation::moveTo (float x, float y, float theta)

moveTo - initiate move to specified point given by (x,y,theta) coordinates, with respect to current NAO coordination frame.


| Argument | Description |
|---|---|
|x|- X coordination of the goal point.|
|y|- Y coordination of the goal point.|
|theta|- Orientation of NAO in the goal point.|

*Returns:*.
call status (false - Failed, true - Success)

#### bool rapp::robot::navigation::moveVel (float x, float y, float theta)

moveVel - initiate move with the specified linear velocities in x, y axis direction and angular velocity theta.


| Argument | Description |
|---|---|
|x|- velocity along NAO X axis.|
|y|- velocity along NAO Y axis.|
|theta|- velocity around NAO Z axis.|

*Returns:*.
call status (false - Failed, true - Success)

#### bool rapp::robot::navigation::moveVel (float x, float theta)

#### bool rapp::robot::navigation::moveStop ()

moveStop - Stop robot movement - movement initiated by moveTo, moveVel and moveAlongPath methods.

*Returns:*.
call status (false - Failed, true - Success)

#### bool rapp::robot::navigation::moveJoint (std::vector\< std::string \> joint, std::vector\< float \> angle, float speed)

moveJoint - move given joints/given chain to specified angle with specified maximum joints speed fraction.


| Argument | Description |
|---|---|
|joint|- joints/chain names that are being requested to move.|
|angle|- Destination angle of joints.|
|speed|- maximum joints speed fraction (Value of 1 - max speed, value of 0 - no move).|

Avaliable joints and chains are as follows:


|   |   |   |   |   |   |
|---|---|---|---|---|---|
|The chain ...|Head|LArm|LLeg|RLeg|RArm|
|joints ...|HeadYaw|LShoulderPitch|LHipYawPitch !!|RHipYawPitch !!|RShoulderPitch|
|\_\_\_\_\_\_\_\_\_\_|HeadPitch|LShoulderRoll|LHipRoll|RHipRoll|RShoulderRoll|
|\_\_\_\_\_\_\_\_\_\_|\_\_\_\_\_\_\_\_\_|LElbowYaw|LHipPitch|RHipPitch|RElbowYaw|
|\_\_\_\_\_\_\_\_\_\_|\_\_\_\_\_\_\_\_\_|LElbowRoll|LKneePitch|RKneePitch|RElbowRoll|
|\_\_\_\_\_\_\_\_\_\_|\_\_\_\_\_\_\_\_\_|LWristYaw !|LAnklePitch|RAnklePitch|RWristYaw !|
|\_\_\_\_\_\_\_\_\_\_|\_\_\_\_\_\_\_\_\_|LHand !|RAnkleRoll|LAnkleRoll|RHand !|


*  ! - these joints do not exist in the NAO Body type “H21”. 
*  !! - LHipYawPitch and RHipYawPitch share the same motor so they move simultaneously and symmetrically. In case of conflicting orders, LHipYawPitch always takes the priority.

*Returns:*.
call status (false - Failed, true - Success)

#### bool rapp::robot::navigation::moveJoint (std::vector\< std::string \> joint, std::vector\< float \> angle)

#### bool rapp::robot::navigation::takePredefinedPosture (std::string posture, float speed)

takePredefinedPosture - Take predefined robot posture.


| Argument | Description |
|---|---|
|posture|- name of the predefined posture: StandInit, Stand, StandZero, LyingBack, LyingBelly, Crouch, Sit, SitRelax.|
|speed|- maximum speed fraction (Value of 1 - max speed, value of 0 - no move).|

*Returns:*.
call status (false - Failed, true - Success)

#### bool rapp::robot::navigation::lookAtPoint (float x, float y, float z)

lookAtPoint - Move robot to point it's main camera to a given point (x,y,z).


| Argument | Description |
|---|---|
|x|- X coordination of the point in the global frame.|
|y|- Y coordination of the point in the global frame.|
|z|- Z coordination of the point in the global frame.|

*Returns:*.
call status (false - Failed, true - Success)

#### bool rapp::robot::navigation::rest (std::string posture)

rest - take given safe posture and remove motors stiffness. If the given posture is not safe - returns False.


| Argument | Description |
|---|---|
|posture|- name of the safe posture: "Crouch","Sit","SitRelax","LyingBelly","LyingBack".|

*Returns:*.
call status (false - Failed, true - Success)

#### bool rapp::robot::navigation::moveAlongPath (std::vector\< rapp::object::pose\_stamped \> poses)

moveAlongPath - move robot along the given path. It moves with standard velocity, untill the end is reached or any obstacle was met.


| Argument | Description |
|---|---|
|poses|- vector of poses that specifies the desired path.|

*Returns:*.
call status (false - Failed, true - Success)

#### rapp::object::pose\_stamped rapp::robot::navigation::getRobotPose ()

getRobotPose - returns robot pose given in the global frame.

*Returns:*.
current robot pose in the global frame.

#### bool rapp::robot::navigation::setGlobalPose (rapp::object::pose rapp\_pose)

setGlobalPose - sets new robot pose in the global frame. Usually is used to set new robots pose that was estimated by one of global localization methods (e.g. QR-localization).

*Returns:*.
call status (false - Failed, true - Success)

#### std::vector\<std::vector\<float\> \> rapp::robot::navigation::getTransform (std::string chainName, int space)

getTransform - return homogeneous transformation matrix of given chain in the given space.

| Argument | Description |
|---|---|
|chainName|- name of the desired chain:|
|space|- desired space.|

Avaliable joints are as follows:


|   |   |   |   |   |
|---|---|---|---|---|
|Head|LArm|LLeg|RLeg|RArm|
|HeadYaw|LShoulderPitch|LHipYawPitch !!|RHipYawPitch !!|RShoulderPitch|
|HeadPitch|LShoulderRoll|LHipRoll|RHipRoll|RShoulderRoll|
|\_\_\_\_\_\_\_\_\_|LElbowYaw|LHipPitch|RHipPitch|RElbowYaw|
|\_\_\_\_\_\_\_\_\_|LElbowRoll|LKneePitch|RKneePitch|RElbowRoll|
|\_\_\_\_\_\_\_\_\_|LWristYaw !|LAnklePitch|RAnklePitch|RWristYaw !|
|\_\_\_\_\_\_\_\_\_|LHand !|RAnkleRoll|LAnkleRoll|RHand !|


*  ! - these joints do not exist in the NAO Body type “H21”. 
*  !! - LHipYawPitch and RHipYawPitch share the same motor so they move simultaneously and symmetrically. In case of conflicting orders, LHipYawPitch always takes the priority.

*Returns:*.
homogeneous transformation matrix of given chain in the given space
