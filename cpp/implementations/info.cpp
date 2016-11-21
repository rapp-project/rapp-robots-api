#include <rapp-robots-api/info/info.hpp>

#include <boost/program_options.hpp>
namespace po = boost::program_options;

#include <boost/filesystem.hpp>
namespace fs = boost::filesystem;

#include <stdexcept>

namespace rapp {
namespace robot {

info::info(int argc, char * argv[])
{
    po::options_description desc("Allowed options");
    desc.add_options()
    ("base_path", po::value<std::string>(), "base path")
    ;

    po::variables_map vm;
    po::store(po::command_line_parser(argc, argv).options(desc).allow_unregistered().run(), vm);
    po::notify(vm);

    if (vm.count("base_path")) {
        base_path_ = vm["base_path"].as<std::string>();
    } else {
        throw std::runtime_error("rapp::robot::info: no base_path set when calling rapp");
    }

    if (base_path_.empty()) {
        throw std::runtime_error("rapp::robot::info: empty base_path passed when calling rapp");
    }

    fs::path p = base_path_;
    if (!fs::exists(p)) {
        throw std::runtime_error("rapp::robot::info: base path " + base_path_ + " doesn't exist!");
    }

    if (base_path_.back() != '/')
        base_path_ += '/';
}

} // namespace robot
} // namespace rapp
