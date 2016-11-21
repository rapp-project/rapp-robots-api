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

bool navigation::point_arm(float x, float y, float z)
{
    return true;
}

bool navigation::move_to(float x, float y, float theta)
{
    return true;
}

bool navigation::move_vel(float x, float y, float theta)
{
    return true;
}

bool navigation::move_vel(float x, float theta)
{
    return true;
}

bool navigation::move_stop()
{
    return true;
}

bool navigation::move_joint(std::vector<std::string> joint, std::vector<float> angle, float speed)
{
    return true;
}

bool navigation::move_joint(std::vector<std::string> joint, std::vector<float> angle)
{
    return true;
}

bool navigation::take_predefined_posture(std::string posture, float speed)
{
    return true;
}

bool navigation::look_at_point(float x, float y, float z)\
{
    return true;
}

bool navigation::rest(std::string posture)
{
    return true;
}

bool navigation::move_along_path(std::vector<rapp::object::pose_stamped> poses)
{
    for (auto p : poses) {
        std::cout << "Go to " << p.pose.position.x << "," << p.pose.position.y << "\n";
    }
    return true;
}

rapp::object::pose_stamped navigation::get_global_pose()
{
    return rapp::object::pose_stamped();
}

bool navigation::set_global_pose(rapp::object::pose rapp_pose)
{
    return true;
}

std::vector<std::vector<float>> navigation::get_transform(std::string chainName, int space)
{
    return std::vector<std::vector<float>>();
}

} /* namespace robot */
} /* namespace rapp */
