#ifndef RAPP_ROBOT_INFO
#define RAPP_ROBOT_INFO

#include "includes.ihh"

namespace rapp {
namespace robot {

/**
 * Utility class keeping global information about robot.
 */
class info {
public:
    /**
     * Constructor takes command-line arguments and parses them to retrieve 
     * information passed by core-agent during application deployment.
     * Those arguments may be: --base_path
     */
    info(int argc, char * argv[]);

    /**
     * Copy constructor
     */
    info(const info & rhs) = default;

    /**
     * Get path to root folder, from which application is run.
     * 
     * \return absolute path to application directory
     */
    const std::string & base_path() const
    {
        return base_path_;
    }

    /**
     * Get absolute path to the file given its name and relative path.
     *
     * \return absolute path to specified file
     *
     * \note file have to be installed with application (use CMake macro)
     */
    std::string get_path(const std::string & relative_path) const {
        return base_path_ + relative_path;
    }

private:
    /**
     * Default contructor removed 
     */
    info() = delete;

    /// Base path
    std::string base_path_;
};

} // namespace robot
} // namespace rapp

#endif /*RAPP_ROBOT_INFO */
