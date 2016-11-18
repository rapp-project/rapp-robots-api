rapp::robot::localization class Reference
=========================================

#### rapp::robot::localization::localization (int argc=0, char \*\*argv=NULL)

#### rapp::robot::localization::~localization ()

#### void rapp::robot::localization::pose\_from\_matrix (std::vector&lt; std::vector&lt; float &gt;&gt; matrix, rapp::object::pose &pose)

#### void rapp::robot::localization::multiply\_poses (rapp::object::pose &pose1, rapp::object::pose &pose2, rapp::object::pose &end\_pose)

#### rapp::object::pose rapp::robot::localization::qr\_code\_localization (rapp::object::qr\_code\_3d QRcodes, std::vector&lt; std::vector&lt; float &gt;&gt; camera\_to\_robot\_matrix, std::string \*MapPath)

#### rapp::object::pose rapp::robot::localization::qr\_code\_localization (rapp::object::qr\_code\_3d QRcodes, std::vector&lt; std::vector&lt; float &gt;&gt; camera\_to\_robot\_matrix, rapp::object::qr\_code\_map QRmap)

#### rapp::object::qr\_code\_map rapp::robot::localization::load\_qr\_code\_map (std::string \*is)
