#ifndef RAPP_DYNAMIC_LOCALIZATION
#define RAPP_DYNAMIC_LOCALIZATION
#include "includes.ihh"

namespace rapp {
namespace robot {

/**
 * @class localization
 * @brief Class which defines the interface for Robot localization capabilities
 * @date 10-August-2015
 * @author Wojciech Dudek <wojciechsbox@gmail.com>
 * @note This class uses pimpl pattern to make ABI as stable as possible when deploying new library versions
 */
class localization
{
  public:
  	localization(int argc=0, char ** argv = NULL);

    ~localization();
    /**
     * quaternion_from_euler - move NAO arm to point its fingers to the reqested point given in the global coordinate frame.
     *
     * @param x - X coordination of the requested point.
     * @param y - Y coordination of the requested point.
     * @param z - z coordination of the requested point.
     *
     * @return call status (false - Failed, true - Success)
     */
    // This is a BLOCKING CALL.
    rapp::object::quaternion quaternion_from_euler(float roll, float pitch, float yaw);

    std::vector<float> euler_from_quaternion(rapp::object::quaternion &rapp_quaternion);

    void pose_from_matrix(std::vector<std::vector<float>> matrix,rapp::object::pose &pose);

    void multiply_poses(rapp::object::pose &pose1, rapp::object::pose &pose2, rapp::object::pose &end_pose);
    rapp::object::pose qr_code_localization(rapp::object::qr_code_3d QRcodes,std::vector<std::vector<float>> camera_to_robot_matrix, std::string *MapPath);

    rapp::object::pose qr_code_localization(rapp::object::qr_code_3d QRcodes, std::vector<std::vector<float>> camera_to_robot_matrix,rapp::object::qr_code_map QRmap);

	rapp::object::qr_code_map load_qr_code_map(std::string * is);

  private:
};
} // namespace dynamic
} // namespace rapp
#endif // RAPP_DYNAMIC_LOCALIZATION
