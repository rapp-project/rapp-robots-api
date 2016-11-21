info class Reference
=================================

#### Member Data Documentation

#### info::info (int argc, char \*argv\[\])

Constructor takes command-line arguments and parses them to retrieve information passed by core-agent during application deployment. Those arguments may be: –base\_path

#### info::info (const info &rhs)=default

Copy constructor

#### const std::string& info::base\_path () const

Get path to root folder, from which application is run.

**Returns:.**

absolute path to application directory

#### std::string info::get\_path (const std::string &relative\_path) const

Get absolute path to the file given its name and relative path.

**Returns:.**

absolute path to specified file

**Note:.**

file have to be installed with application (use CMake macro)

#### info::info ()=delete

Default contructor removed
