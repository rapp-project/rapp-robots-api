#include <iostream>
#include <stdexcept>

#include <rapp-robots-api/vision/vision.hpp>

#include <boost/program_options.hpp>
namespace po = boost::program_options;

#include <boost/filesystem.hpp>
namespace fs = boost::filesystem;


namespace rapp {
namespace robot {

// placeholder class for vision implementation
class VisionImpl {
public:
    std::string fake_image_;
};

vision::vision(int argc, char * argv[]) : pimpl(NULL) 
{
    pimpl = new VisionImpl;
    std::cout << "Initialized placeholder rapp::robot::vision library" << std::endl;
    po::options_description desc("Allowed options");
    desc.add_options()
    ("fake_image", po::value<std::string>(), "fake iamge")
    ;

    po::variables_map vm;
    po::store(po::command_line_parser(argc, argv).options(desc).allow_unregistered().run(), vm);
    po::notify(vm);

    if (vm.count("fake_image")) {
        pimpl->fake_image_ = vm["fake_image"].as<std::string>();
        std::cout << "Using fake image: " << pimpl->fake_image_ << "\n";

        fs::path p = pimpl->fake_image_;
        if (!fs::exists(p)) {
            throw std::runtime_error("rapp::robot::info: base path " + pimpl->fake_image_ + " doesn't exist!");
        }
    }
}

vision::~vision() 
{
    std::cout << "Finished placeholder rapp::robot::vision library" << std::endl;
    delete pimpl;
}

rapp::object::picture::Ptr vision::capture_image (int camera_id, int camera_resolution, const std::string & encoding) 
{
    std::cout << "vision::captureImage" << std::endl;
    if (pimpl->fake_image_ != "") {
        std::cout << "returning " << pimpl->fake_image_ << "\n";
        auto pic = std::make_shared<rapp::object::picture>(pimpl->fake_image_);
        std::cout << "Type: " << pic->type() << "\n";
        return pic;
    } else {
        rapp::types::byte bytes[2] = {(char) 0x89, (char) 0x50};
        return std::make_shared<rapp::object::picture>(std::vector<rapp::types::byte>(bytes, bytes+2));
    }
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
