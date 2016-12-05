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
 * @note This class handles transformation matrices, convertion to rapp::object::pose objects and other localication related methods.
 */
class localization
{
  public:
     /**
     * Create localization module. Handles transformation matrices, convertion to rapp::object::pose objects and other localication related methods.
     */
  	localization(int argc=0, char ** argv = NULL);
    /**
     * Destroy localization module. Implementation object should be destroyed here.
     */
    ~localization();
    /**
     * quaternion_from_euler - convert euler (ZYX) angles to rapp::object::quaternion object.
     *
     * @param roll - angle around X direction.
     * @param pitch - angle around Y direction.
     * @param yaw - angle around Z direction.
     *
     * @return rapp::object::quaternion
     */
    // This is a BLOCKING CALL.
    rapp::object::quaternion quaternion_from_euler(float roll, float pitch, float yaw);
    /**
     * invert_transform - invert transformation matrix.
     *
     * @param matrix_input - input matrix.
     *
     * @return std::vector<std::vector<float>> inverted matrix
     */
    // This is a BLOCKING CALL.
	std::vector<std::vector<float>> invert_transform(std::vector<std::vector<float>> matrix_input);
    /**
     * euler_from_quaternion - convert rapp::object::quaternion object to euler (ZYX) angles.
     *
     * @param rapp_quaternion - input quaternion object.
     *
     * @return std::vector<float> - euler angles: [0] - angle around X direction, [1] - angle around Y direction, [2] - angle around Z direction.
     */
    // This is a BLOCKING CALL.
 const void euler_from_quaternion(const rapp::object::quaternion &rapp_quaternion, std::array<float, 3> &euler);
    /**
     * pose_from_matrix - convert transformation matrix to the rapp::object::pose object.
     *
     * @param matrix - input transformation matrix.
     * @param pose - output rapp::object::pose object.
     *
     */
    // This is a BLOCKING CALL.
    void pose_from_matrix(std::vector<std::vector<float>> &matrix,rapp::object::pose &pose);
    /**
     * multiply_poses - multiply transformation matrices given by rapp::object::pose objects: pose1_matrix * pose2_matrix = end_pose_matrix.
     *
     * @param pose1 - input rapp::object::pose object -> pose1.
     * @param pose2 - input rapp::object::pose object -> pose2.
     * @param end_pose - output rapp::object::pose object.
     *
     */
    // This is a BLOCKING CALL.
    void multiply_poses(rapp::object::pose &pose1, rapp::object::pose &pose2, rapp::object::pose &end_pose);
    /**
     * qr_code_localization - multiply transformation matrices given by rapp::object::pose objects: pose1_matrix * pose2_matrix = end_pose_matrix.
     *
     * @param QRcodes - found QR Codes (using rapp::robot::vision::qr_code_detection method),
     * @param camera_to_robot_matrix - transformation matrix from camera coordination frame to robot coordination frame,
     * @param MapPath - path to the QRcode map (given by .xml file as desribed here: <a href="https://github.com/rapp-project/rapp-robots-api/wiki/localization#create-qr-code-map">QR code map creation tutorial</a> ).
     *
     * @return pose - robot pose in the global coordination frame.
	 *
     */
    // This is a BLOCKING CALL.
    rapp::object::pose qr_code_localization(rapp::object::qr_code_3d QRcodes,std::vector<std::vector<float>> camera_to_robot_matrix, std::string *MapPath);
    /**
     * qr_code_localization - multiply transformation matrices given by rapp::object::pose objects: pose1_matrix * pose2_matrix = end_pose_matrix.
     *
     * @param QRcodes - found QR Codes (using rapp::robot::vision::qr_code_detection method),
     * @param camera_to_robot_matrix - transformation matrix from camera coordination frame to robot coordination frame,
     * @param QRmap - QR code map object, can be loaded using rapp::robot::localization::load_qr_code_map method.
	 *
     * @return pose - robot pose in the global coordination frame.
     *
     */
    // This is a BLOCKING CALL.
    rapp::object::pose qr_code_localization(rapp::object::qr_code_3d QRcodes, std::vector<std::vector<float>> camera_to_robot_matrix,rapp::object::qr_code_map QRmap);
    /**
     * load_qr_code_map - multiply transformation matrices given by rapp::object::pose objects: pose1_matrix * pose2_matrix = end_pose_matrix.
     *
     * @param is - path to the QR code map file (.xml file). Map file shoud be created as desribed here: <a href="https://github.com/rapp-project/rapp-robots-api/wiki/localization#create-qr-code-map">QR code map creation tutorial</a>),
     *
     * @return QRcodeMap - contains poses of all lendmarks in the environment.
     *
     */
    // This is a BLOCKING CALL.
	rapp::object::qr_code_map load_qr_code_map(std::string * is);

  private:
};
} // namespace dynamic
} // namespace rapp
#endif // RAPP_DYNAMIC_LOCALIZATION
