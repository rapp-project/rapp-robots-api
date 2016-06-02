#ifndef RAPP_DYNAMIC_LOCALIZATION
#define RAPP_DYNAMIC_LOCALIZATION
#include "includes.ihh"
/**
 * @class Localization
 * @brief Class which defines the interface for Robot localization capabilities
 * @date 10-August-2015
 * @author Wojciech Dudek <wojciechsbox@gmail.com>
 * @note This class uses pimpl pattern to make ABI as stable as possible when deploying new library versions
 */

namespace rapp {
namespace robot {

class localization
{
  public:
  	localization(int argc=0, char ** argv = NULL);

    ~localization();
	rapp::object::pose qr_code_localization(rapp::object::qr_code_3d QRcodes,std::vector<std::vector<float>> camera_to_robot_matrix, const char* MapPath);

        rapp::object::pose qr_code_localization(rapp::object::qr_code_3d QRcodes, std::vector<std::vector<float>> camera_to_robot_matrix,rapp::object::qr_code_map QRmap);

	rapp::object::qr_code_map load_qr_code_map(std::istream & is);

  private:
};
} // namespace dynamic
} // namespace rapp
#endif // RAPP_DYNAMIC_LOCALIZATION
