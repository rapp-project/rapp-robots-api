#include <iostream>

#include <rapp-robots-api/navigation/navigation.hpp>

namespace rapp {
namespace robot {

// placeholder class for vision implementation
class NavigationImpl {
};

navigation::navigation(int argc, char * argv[]) : pimpl(NULL) 
{
    std::cout << "Initialized placeholder rapp::robot::navigation library" << std::endl;
}

navigation::~navigation() 
{
    std::cout << "Finished placeholder rapp::robot::navigation library" << std::endl;
}

bool navigation::moveTo(float x, float y, float theta)
{
    return true;
}

bool navigation::moveVel(float x, float y, float theta)
{
    return true;
}

bool navigation::moveVel(float x, float theta)
{
    return true;
}

bool navigation::moveStop()
{
    return true;
}

bool navigation::moveJoint(std::vector<std::string> joint, std::vector<float> angle, float speed)
{
    return true;
}

bool navigation::moveJoint(std::vector<std::string> joint, std::vector<float> angle)
{
    return true;
}

bool navigation::takePredefinedPosture(std::string posture, float speed)
{
    return true;
}

bool navigation::lookAtPoint(float x, float y, float z)\
{
    return true;
}

bool navigation::rest(std::string posture)
{
    return true;
}

bool navigation::moveAlongPath(std::vector<rapp::object::PoseStamped> poses)
{
    return true;
}

rapp::object::PoseStamped navigation::getRobotPose()
{
    return rapp::object::PoseStamped();
}

bool navigation::setGlobalPose(rapp::object::Pose rapp_pose)
{
    return true;
}

std::vector<std::vector<float>> navigation::getTransform(std::string chainName, int space)
{
    return std::vector<std::vector<float>>();
}

} /* namespace robot */
} /* namespace rapp */
