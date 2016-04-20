#ifndef RAPP_ROBOT_NAVIGATION
#define RAPP_ROBOT_NAVIGATION
#include "includes.ihh"

namespace rapp {
namespace robot {

class navigation_impl;

class navigation
{
public:
  
    /// Constructor - create instance of NavigationImpl here
    Navigation(int argc=0, char ** argv = NULL);

    ~Navigation();
    // moveTo - initiate move to specified point given by (x,y,theta) coordinates, with respect to NAO coordination frame.
    // This is a BLOCKING CALL.
    bool moveTo(float x, float y, float theta);
    // moveVel - initiate move with the specified linear velocities in x, y axis direction and angular velocity theta.
    // this is NOT a BLOCKING CALL.
    bool moveVel(float x, float y, float theta);
    // moveStop - Stop robot movement - movement initiated by moveTo, moveVel and moveAlongPath methods.
    // this is NOT a BLOCKING CALL.
    bool moveStop();
    // moveJoint - move given joints to specified angle with specified maximum joint speed fraction.
    // this is a BLOCKING CALL.
    bool moveJoint(std::vector<std::string> joint, std::vector<float> angle, float speed);
    // takePredefinedPosture - Take predefined robot posture (if enabled). 
    // this is a BLOCKING CALL.
    bool takePredefinedPosture(std::string posture, float speed);
    // lookAtPoint - Move robot to point it's main camera to a given point (x,y,z).
    // this is a BLOCKING CALL. 
    bool lookAtPoint(float x, float y, float z);
    // rest - take given safe posture and remove motors stiffness (if enabled). If the given posture is not safe - returns False.
    // This is a BLOCKING CALL
    bool rest(std::string posture);
    // moveAlongPath - move robot along the given path. It moves with standard velocity, untill the end is reached or any obstacle was met.
    // This is a BLOCKING CALL
    bool moveAlongPath(rapp::object::Path path);
    // getRobotPose - returns robot pose given in the map frame.
    rapp::object::PoseStamped getRobotPose();
    // setGlobalPose - sets new robot pose in the map frame. Usually is used to set new robots pose that was estimated by any global localization method (e.g. QR-localization)
    bool setGlobalPose(rapp::object::PoseStamped rapp_pose);

    
private:
    navigation_impl * pimpl;
};

}
}
#endif
