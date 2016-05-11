#include <iostream>

#include <rapp-robots-api/vision/vision.hpp>

namespace rapp {
namespace robot {

// placeholder class for vision implementation
class VisionImpl {
};

vision::vision(int argc, char * argv[]) : pimpl(NULL) 
{
    std::cout << "Initialized placeholder rapp::robot::vision library" << std::endl;
}

vision::~vision() 
{
    std::cout << "Finished placeholder rapp::robot::vision library" << std::endl;
}

rapp::object::picture::Ptr vision::capture_image (int camera_id, int camera_resolution, const std::string & encoding) 
{
    std::cout << "vision::captureImage" << std::endl;
	rapp::types::byte bytes[2] = {0x89, 0x50};
    return std::make_shared<rapp::object::picture>(std::vector<rapp::types::byte>(bytes, bytes+2));
}

bool vision::set_camera_param(int camera_id, int parameter_id, int new_value) 
{
    std::cout << "vision::setCameraParam" << std::endl;
    return true;
}

std::map<int, bool> vision::set_camera_params(int camera_id, const std::map<int, int> & params) 
{
    std::cout << "vision::setCameraParams" << std::endl;
    return std::map<int, bool>();
}

rapp::object::qr_code_3d qr_code_detection(rapp::object::picture image, std::vector<std::vector<float>> robot_to_camera_matrix, double camera_matrix[][3], float landmark_theoretical_size)
{
    return rapp::object::qr_code_3d();
}

} /* namespace robot */
} /* namespace rapp */
