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
    std::vector<std::string> fake_image_;
    size_t current_id_;
};

vision::vision(int argc, char * argv[]) : pimpl(NULL) 
{
    pimpl = new VisionImpl;
    pimpl->current_id_ = 0;
    std::cout << "Initialized placeholder rapp::robot::vision library" << std::endl;
    po::options_description desc("Allowed options");
    desc.add_options()
    ("fake_image", po::value<std::vector<std::string> >(&pimpl->fake_image_)->multitoken(), "fake image")
    ;

    po::variables_map vm;
    po::store(po::command_line_parser(argc, argv).options(desc).allow_unregistered().run(), vm);
    po::notify(vm);

    if (vm.count("fake_image")) {
        for (auto s: pimpl->fake_image_) {
            std::cout << "Using fake image: " << s << "\n";
            fs::path p = s;
            if (!fs::exists(p)) {
                throw std::runtime_error("rapp::robot::vision: file " + s + " doesn't exist!");
            }
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
    if (pimpl->fake_image_.size() > 0) {
        std::string fname = pimpl->fake_image_[pimpl->current_id_++];
        if (pimpl->current_id_ >= pimpl->fake_image_.size()) pimpl->current_id_ = 0;
        std::cout << "returning " << fname << "\n";
        auto pic = std::make_shared<rapp::object::picture>(fname);
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

rapp::object::qr_code_3d vision::qr_code_detection(rapp::object::picture::Ptr image, std::vector<std::vector<float>> robot_to_camera_matrix, double camera_matrix[][3], float landmark_theoretical_size)
{
    return rapp::object::qr_code_3d();
}

vision::camera_info vision::load_camera_info(int camera_id) {
	vision::camera_info ret;
    ret.K = {1000, 0, 640, 0, 1000, 480, 0, 0, 1};
    ret.D = {0, 0, 0, 0, 0};
    ret.P = ret.K;
	return ret;
}

void vision::save_camera_info(int camera_id, vision::camera_info info) {
	
}

} /* namespace robot */
} /* namespace rapp */
