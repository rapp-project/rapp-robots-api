#ifndef RAPP_ROBOT_VISION
#define RAPP_ROBOT_VISION

#include "includes.ihh"

namespace rapp {
namespace robot {

class VisionImpl;

/**
 * \class vision
 * \brief Interface class for robot vision module. 
 * \version 1
 * \date 20-September-2015
 * \author Maciej Stefańczyk <m.stefanczyk@elka.pw.edu.pl>
 */
class vision
{
public:
     enum camera_params {
          brightness = 0,
          contrast = 1,
          gain = 6,
          auto_exposure = 11,
          auto_white_balance = 12,
          exposure = 17
     };
     
     enum camera_resolution {
          qqvga = 0,
          qvga = 1,
          vga = 2,
          vga4 = 3
     };

    /**
     * Create vision module. Implementation object (pimpl) should be created here.
     * 
     * \param argc number of arguments passed from host process
     * \param argv list of arguments passed from host process
     */
    vision(int argc = 0, char * argv[] = NULL);

    /**
     * Destroy vision module. Implementation object should be destroyed here.
     */
    ~vision();

    /**
     * Capture an image frame from the robot’s camera.
     *
     * \param camera_id ID of the camera to be used
     * \param camera_resolution
     * \param encoding output image encoding type (e.g. "png", "jpg")
     *
     * \return captured image as raw byte stream
     */
    rapp::object::picture::Ptr capture_image (int camera_id, int camera_resolution, const std::string & encoding);

    /**
     * Set camera parameter.
     *
     * \param camera_id ID of the camera to be used
     * \param parameter_id ID of the parameter to be changed
     * \param new_value new value for the selected parameter
     *
     * \return true on success, false otherwise
     */
    bool set_camera_param(int camera_id, int parameter_id, int new_value);

    /**
     * Set multiple camera parameters at once.
     *
     * \param camera_id ID of the camera to be used
     * \param params map of pairs param_id->new_value
     *
     * \return success flag for each parameter
     */
    std::map<int, bool> set_camera_params(int camera_id, const std::map<int, int> & params);
    
    /**
     * Detects faces.
     *
     * \param image for the face detection
     * \param camera_id ID of the camera to be used
     * \param camera_resolution map of pairs param_id->new_value
     *
     * \return vector of informations about the detected face
     */
    std::vector< std::vector <float> > face_detect(rapp::object::picture image, int camera_id, int camera_resolution);
    
    /**
     * Detects QR-codes.
     *
     * \param image image for the QR-code detection
     * \param robot_to_camera_matrix transformation matrix from robot to camera framework
     * \param camera_matrix
     * \param landmark_theoretical_size
     *
     * \return QR-codes informations
     */
    rapp::object::qr_code_3d qr_code_detection(rapp::object::picture::Ptr image, std::vector<std::vector<float>> robot_to_camera_matrix, double camera_matrix[][3], float landmark_theoretical_size = 0.16f);

private:
    /**
     * Pointer to implementation class. 
     * 
     * \see Cheshire Cat (pimpl) programming pattern
     */
    VisionImpl * pimpl;
};

} /* namespace robot */
} /* namespace rapp */
#endif
