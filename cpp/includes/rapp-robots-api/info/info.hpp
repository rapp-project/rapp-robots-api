#ifndef RAPP_ROBOT_INFO
#define RAPP_ROBOT_INFO

#include "includes.ihh"

namespace rapp {
namespace robot {

/**
 * \class
 */
class info {
public:
    /**
     *
     */
    info(int argc, char * argv[]);

    /**
     *
     */
    info() = delete;

    /**
     *
     */
    info(const info & rhs) = default;

    /**
     *
     */
    const std::string & base_path() const
    {
        return base_path_;
    }

    std::string get_path(const std::string & relative_path) const {
        return base_path_ + relative_path;
    }

private:
    /// Base path
    std::string base_path_;
};

} // namespace robot
} // namespace rapp

#endif /*RAPP_ROBOT_INFO */
