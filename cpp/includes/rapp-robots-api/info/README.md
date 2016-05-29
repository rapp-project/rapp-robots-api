rapp::robot::info class Reference
=================================

#### rapp::robot::info::info (int argc, char \*argv[])

Constructor takes command-line arguments and parses them to retrieve information passed by core-agent during application deployment. Those arguments may be: –base\_path

#### rapp::robot::info::info (const info &rhs)=default

Copy constructor

#### const std::string& rapp::robot::info::base\_path () const

Get path to root folder, from which application is run.

*Returns:*.
absolute path to application directory

#### std::string rapp::robot::info::get\_path (const std::string &relative\_path) const

Get absolute path to the file given its name and relative path.

*Returns:*.
absolute path to specified file

*Note:*.
file have to be installed with application (use CMake macro)
