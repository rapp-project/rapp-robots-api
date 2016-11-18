rapp::robot::info class Reference
=================================

#### Private Attributes

-   std::string base\_path\_

    *Base path.*

-   [info](#classrapp_1_1robot_1_1info_1a5e3f46a38e36600addacabbb8e9af829) ( int argc, char \* argv)

<!-- -->

-   [info](#classrapp_1_1robot_1_1info_1aed2e1a70d20f64bbfda9fd35b3e4e1b7) ( const [info](#classrapp_1_1robot_1_1info) & rhs)

<!-- -->

-   const std::string & [base\_path](#classrapp_1_1robot_1_1info_1a30c45439de36d4d3187d7d7ae21c528a) ( )

<!-- -->

-   std::string [get\_path](#classrapp_1_1robot_1_1info_1ad657d8eae976052591dba213d4820795) ( const std::string & relative\_path)

-   [info](#classrapp_1_1robot_1_1info_1ae2bfeea89bac81a9647888593032ace1) ( )

Utility class keeping global information about robot.

Definition at line 12 of file info.hpp

The Documentation for this struct was generated from the following file:

-   info.hpp

#### Member Data Documentation

#### rapp::robot::info::info (int argc, char \*argv\[\])

Constructor takes command-line arguments and parses them to retrieve information passed by core-agent during application deployment. Those arguments may be: –base\_path

#### rapp::robot::info::info (const info &rhs)=default

Copy constructor

#### const std::string& rapp::robot::info::base\_path () const

Get path to root folder, from which application is run.

**Returns:.**

absolute path to application directory

#### std::string rapp::robot::info::get\_path (const std::string &relative\_path) const

Get absolute path to the file given its name and relative path.

**Returns:.**

absolute path to specified file

**Note:.**

file have to be installed with application (use CMake macro)

#### rapp::robot::info::info ()=delete

Default contructor removed
