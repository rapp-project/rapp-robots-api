#ifndef RAPP_ROBOT_NAVIGATION
#define RAPP_ROBOT_NAVIGATION
#include "includes.ihh"
/**
 * @class Navigation
 * @brief Class which defines the interface for Robot navigation capabilities (movement, localization)
 * @date 10-August-2015
 * @author Wojciech Dudek <wojciechsbox@gmail.com>
 * @note This class uses pimpl pattern to make ABI as stable as possible when deploying new library versions
 */

namespace rapp {
namespace robot {

class NavigationImpl;

class navigation
{
  public:
  
    
    /**
     * Create navigation module. Implementation object (pimpl) should be created here.
     */
    navigation(int argc=0, char ** argv = NULL);
    /**
     * Destroy navigation module. Implementation object should be destroyed here.
     */
    ~navigation();
        /**
     * moveTo - initiate move to specified point given by (x,y,theta) coordinates, with respect to current NAO coordination frame.
     *
     * @param x - X coordination of the goal point.
     * @param y - Y coordination of the goal point.
     * @param theta - Orientation of NAO in the goal point.
     *
     * @return call status (false - Failed, true - Success)
     */
    // This is a BLOCKING CALL.
    bool moveTo(float x, float y, float theta);
    /**
     * moveVel - initiate move with the specified linear velocities in x, y axis direction and angular velocity theta.
     *
     * @param x - velocity along NAO X axis.
     * @param y - velocity along NAO Y axis.
     * @param theta - velocity around NAO Z axis.
     *
     * @return call status (false - Failed, true - Success)
     */
    // this is NOT a BLOCKING CALL.
    bool moveVel(float x, float y, float theta);
    // version for non-holonomic
    bool moveVel(float x, float theta);

    /**
     * moveStop - Stop robot movement - movement initiated by moveTo, moveVel and moveAlongPath methods.

     * @return call status (false - Failed, true - Success)
     */

    // this is NOT a BLOCKING CALL.
    bool moveStop();
    /**
     * moveJoint - move given joints/given chain to specified angle with specified maximum joints speed fraction.
     *
     * @param joint - joints/chain names that are being requested to move.
     * @param angle - Destination angle of joints.
     * @param speed - maximum joints speed fraction (Value of 1 - max speed, value of 0 - no move).
  
     * @details  Avaliable joints and chains are as follows:
     *       
     * The chain ...  | Head      | LArm            | LLeg             | RLeg              | RArm              |
     * -------------- | --------- | --------------- | ---------------- | ----------------- | ----------------- |
     * joints ...     | HeadYaw   |  LShoulderPitch | LHipYawPitch  !! |  RHipYawPitch  !! |  RShoulderPitch   |
     * __________     | HeadPitch |  LShoulderRoll  | LHipRoll         |  RHipRoll         |  RShoulderRoll    |
     * __________     | _________ |  LElbowYaw      | LHipPitch        |  RHipPitch        |  RElbowYaw        |
     * __________     | _________ |  LElbowRoll     | LKneePitch       |  RKneePitch       |  RElbowRoll       |
     * __________     | _________ |  LWristYaw  !   | LAnklePitch      |  RAnklePitch      |  RWristYaw  !     |
     * __________     | _________ |  LHand      !   | RAnkleRoll       |  LAnkleRoll       |  RHand  !         |
     * 
     * -> ! - these joints do not exist in the NAO Body type “H21”.
     * -> !! - LHipYawPitch and RHipYawPitch share the same motor so they move simultaneously and symmetrically. In case of conflicting orders, LHipYawPitch always takes the priority.
     *

     *
     * @return call status (false - Failed, true - Success)
     */
    // this is a BLOCKING CALL.
    bool moveJoint(std::vector<std::string> joint, std::vector<float> angle, float speed);
    bool moveJoint(std::vector<std::string> joint, std::vector<float> angle);
     /**
     * takePredefinedPosture - Take predefined robot posture. 
     *
     * @param posture - name of the predefined posture: StandInit, Stand, StandZero, LyingBack, LyingBelly, Crouch, Sit, SitRelax.
     * @param speed - maximum speed fraction (Value of 1 - max speed, value of 0 - no move).
     *
     * @return call status (false - Failed, true - Success)
     */
    // this is a BLOCKING CALL.
    bool takePredefinedPosture(std::string posture, float speed);
    /**
     * lookAtPoint - Move robot to point it's main camera to a given point (x,y,z).
     *
     * @param x - X coordination of the point in the global frame.
     * @param y - Y coordination of the point in the global frame.
     * @param z - Z coordination of the point in the global frame.
     *
     * @return call status (false - Failed, true - Success)
     */
    // this is a BLOCKING CALL. 
    bool lookAtPoint(float x, float y, float z);
    /**
     * rest - take given safe posture and remove motors stiffness. If the given posture is not safe - returns False.
     *
     * @param posture - name of the safe posture: "Crouch","Sit","SitRelax","LyingBelly","LyingBack".
     *
     * @return call status (false - Failed, true - Success)
     */
    // This is a BLOCKING CALL
    bool rest(std::string posture);
    /**
     * moveAlongPath - move robot along the given path. It moves with standard velocity, untill the end is reached or any obstacle was met.
     *
     * @param poses - vector of poses that specifies the desired path.
     *
     * @return call status (false - Failed, true - Success)
     */
    // This is a BLOCKING CALL
    bool moveAlongPath(std::vector<rapp::object::PoseStamped> poses);
    /**
     * getRobotPose - returns robot pose given in the global frame.
     *
     *
     * @return current robot pose in the global frame.
     */
    // getRobotPose - returns robot pose given in the map frame.
    rapp::object::PoseStamped getRobotPose();
    /**
     * setGlobalPose - sets new robot pose in the global frame. Usually is used to set new robots pose that was estimated by one of global localization methods (e.g. QR-localization).
     *
     *
     * @return call status (false - Failed, true - Success)
     */
    bool setGlobalPose(rapp::object::Pose rapp_pose);
    /**
     * @brief getTransform - return homogeneous transformation matrix of given chain in the given space.
     *
     * @param chainName - name of the desired chain: 
     * @param space - desired space.
     * @details  Avaliable joints are as follows:
     *       
     *Head      | LArm            | LLeg             | RLeg              | RArm              |
     *--------- | --------------- | ---------------- | ----------------- | ----------------- |
     *HeadYaw   |  LShoulderPitch | LHipYawPitch  !! |  RHipYawPitch  !! |  RShoulderPitch   |
     *HeadPitch |  LShoulderRoll  | LHipRoll         |  RHipRoll         |  RShoulderRoll    |
     *_________ |  LElbowYaw      | LHipPitch        |  RHipPitch        |  RElbowYaw        |
     *_________ |  LElbowRoll     | LKneePitch       |  RKneePitch       |  RElbowRoll       |
     *_________ |  LWristYaw  !   | LAnklePitch      |  RAnklePitch      |  RWristYaw  !     |
     *_________ |  LHand      !   | RAnkleRoll       |  LAnkleRoll       |  RHand  !         |
     * 
     * -> ! - these joints do not exist in the NAO Body type “H21”.
     * -> !! - LHipYawPitch and RHipYawPitch share the same motor so they move simultaneously and symmetrically. In case of conflicting orders, LHipYawPitch always takes the priority.
     *
     * @return homogeneous transformation matrix of given chain in the given space
     */
    std::vector<std::vector<float>> getTransform(std::string chainName, int space);   
  private:
    NavigationImpl * pimpl;
};

} // namespace robot
} // namespace rapp
#endif // RAPP_ROBOT_NAVIGATION
