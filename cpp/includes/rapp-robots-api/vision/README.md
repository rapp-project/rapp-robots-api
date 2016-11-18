rapp::robot::vision class Reference
===================================

#### Classes

-   struct [rapp::robot::vision::camera\_info](#structrapp_1_1robot_1_1vision_1_1camera__info)

-   enum [camera\_params](#classrapp_1_1robot_1_1vision_1afc0b42a3dae9b13e241313e082a89ee7) { [brightness](#classrapp_1_1robot_1_1vision_1afc0b42a3dae9b13e241313e082a89ee7ac3d28a7c31d7119b902f13230963bcfa)= 0, [contrast](#classrapp_1_1robot_1_1vision_1afc0b42a3dae9b13e241313e082a89ee7a635e7ca0a51cc711d3e4d9371cd587e9)= 1, [gain](#classrapp_1_1robot_1_1vision_1afc0b42a3dae9b13e241313e082a89ee7aa5b5ffe37852aaf650b3072c40fe7567)= 6, [auto\_exposure](#classrapp_1_1robot_1_1vision_1afc0b42a3dae9b13e241313e082a89ee7a823740f84e71addaa8573e0940f97705)= 11, [auto\_white\_balance](#classrapp_1_1robot_1_1vision_1afc0b42a3dae9b13e241313e082a89ee7a7d262bf9fe9dfa996cfb8595b930bb16)= 12, [exposure](#classrapp_1_1robot_1_1vision_1afc0b42a3dae9b13e241313e082a89ee7a667e9ce517a4d3eeda83027b50b7d5d1)= 17 }

    *Camera parameters.*

<!-- -->

-   enum [camera\_resolution](#classrapp_1_1robot_1_1vision_1a4be2c8c9300958a33bed05b459140fd2) { [qqvga](#classrapp_1_1robot_1_1vision_1a4be2c8c9300958a33bed05b459140fd2a770f3ea726fdbcc7f955eb5ca3f124a5)= 0, [qvga](#classrapp_1_1robot_1_1vision_1a4be2c8c9300958a33bed05b459140fd2aaac4534552eb91762548d637138da71f)= 1, [vga](#classrapp_1_1robot_1_1vision_1a4be2c8c9300958a33bed05b459140fd2adafbdf865accf4d8c0ab524d8d06c4bd)= 2, [vga4](#classrapp_1_1robot_1_1vision_1a4be2c8c9300958a33bed05b459140fd2afa84d160fc0ab01a99aa4f39ea484e23)= 3 }

    *Camera resolution.*

#### Private Attributes

-   VisionImpl \* pimpl

-   [vision](#classrapp_1_1robot_1_1vision_1ab8245d2b51b78fc2191c70445b957de2) ( int argc, char \* argv)

<!-- -->

-   [~vision](#classrapp_1_1robot_1_1vision_1a25da68838b073e853b969881e84797f5) ( )

<!-- -->

-   rapp::object::picture::Ptr [capture\_image](#classrapp_1_1robot_1_1vision_1ac7782beca4726d7331ed842430539177) ( int camera\_id, int camera\_resolution, const std::string & encoding)

<!-- -->

-   bool [set\_camera\_param](#classrapp_1_1robot_1_1vision_1a7a9d77d28e6d783e4c516f5761bccbda) ( int camera\_id, int parameter\_id, int new\_value)

<!-- -->

-   std::map&lt; int, bool &gt; [set\_camera\_params](#classrapp_1_1robot_1_1vision_1a48532e792b5b7238f3d5ca2388236809) ( int camera\_id, const std::map&lt; int, int &gt; & params)

<!-- -->

-   std::vector&lt; std::vector&lt; float &gt; &gt; [face\_detect](#classrapp_1_1robot_1_1vision_1acfbe0a5de02df83f01a693e3defb15d6) ( rapp::object::picture image, int camera\_id, int camera\_resolution)

<!-- -->

-   rapp::object::qr\_code\_3d [qr\_code\_detection](#classrapp_1_1robot_1_1vision_1a69686bb466264298e39f08bf1362a39a) ( rapp::object::picture::Ptr image, std::vector&lt; std::vector&lt; float &gt;&gt; robot\_to\_camera\_matrix, double camera\_matrix, float landmark\_theoretical\_size)

<!-- -->

-   [camera\_info](#structrapp_1_1robot_1_1vision_1_1camera__info) [load\_camera\_info](#classrapp_1_1robot_1_1vision_1a7b5d6368f98412dc380c92e22b5c7fc4) ( int camera\_id)

<!-- -->

-   void [save\_camera\_info](#classrapp_1_1robot_1_1vision_1a85f1c9d384341706e7e356aa86589b86) ( int camera\_id, [camera\_info](#structrapp_1_1robot_1_1vision_1_1camera__info) info)

Interface class for robot vision module.

**Version:.**

1

**Date:.**

20-September-2015

**Author:.**

Maciej Stefańczyk <m.stefanczyk@elka.pw.edu.pl>

Definition at line 19 of file vision.hpp

The Documentation for this struct was generated from the following file:

-   vision.hpp

#### enum camera\_params

**Enumerator:.**

brightness  

contrast  

gain  

auto\_exposure  

auto\_white\_balance  

exposure  

Definition at line 34 of file vision.hpp `
{
brightness= 0, 
contrast= 1, 
gain= 6, 
auto_exposure= 11, 
auto_white_balance= 12, 
exposure= 17, 
}camera_params;
                    `

#### enum camera\_resolution

**Enumerator:.**

qqvga  

qvga  

vga  

vga4  

Definition at line 44 of file vision.hpp `
{
qqvga= 0, 
qvga= 1, 
vga= 2, 
vga4= 3, 
}camera_resolution;
                    `

#### Member Data Documentation

Pointer to implementation class.

**See also:.**

Cheshire Cat (pimpl) programming pattern

Definition at line 141 of file vision.hpp

The Documentation for this struct was generated from the following file:

-   vision.hpp

#### rapp::robot::vision::vision (int argc=0, char \*argv\[\]=NULL)

Create vision module. Implementation object (pimpl) should be created here.

**.**

<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">argc</td>
<td align="left"><p>number of arguments passed from host process</p></td>
</tr>
<tr class="even">
<td align="left">argv</td>
<td align="left"><p>list of arguments passed from host process</p></td>
</tr>
</tbody>
</table>

#### rapp::robot::vision::~vision ()

Destroy vision module. Implementation object should be destroyed here.

#### rapp::object::picture::Ptr rapp::robot::vision::capture\_image (int camera\_id, int camera\_resolution, const std::string &encoding)

Capture an image frame from the robot’s camera.

**.**

<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">camera_id</td>
<td align="left"><p>ID of the camera to be used</p></td>
</tr>
<tr class="even">
<td align="left">camera_resolution</td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left">encoding</td>
<td align="left"><p>output image encoding type (e.g. &quot;png&quot;, &quot;jpg&quot;)</p></td>
</tr>
</tbody>
</table>

**Returns:.**

captured image as raw byte stream

#### bool rapp::robot::vision::set\_camera\_param (int camera\_id, int parameter\_id, int new\_value)

Set camera parameter.

**.**

<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">camera_id</td>
<td align="left"><p>ID of the camera to be used</p></td>
</tr>
<tr class="even">
<td align="left">parameter_id</td>
<td align="left"><p>ID of the parameter to be changed</p></td>
</tr>
<tr class="odd">
<td align="left">new_value</td>
<td align="left"><p>new value for the selected parameter</p></td>
</tr>
</tbody>
</table>

**Returns:.**

true on success, false otherwise

#### std::map&lt;int, bool&gt; rapp::robot::vision::set\_camera\_params (int camera\_id, const std::map&lt; int, int &gt; &params)

Set multiple camera parameters at once.

**.**

<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">camera_id</td>
<td align="left"><p>ID of the camera to be used</p></td>
</tr>
<tr class="even">
<td align="left">params</td>
<td align="left"><p>map of pairs param_id-&gt;new_value</p></td>
</tr>
</tbody>
</table>

**Returns:.**

success flag for each parameter

#### std::vector&lt; std::vector &lt;float&gt; &gt; rapp::robot::vision::face\_detect (rapp::object::picture image, int camera\_id, int camera\_resolution)

Detects faces.

**.**

<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">image</td>
<td align="left"><p>for the face detection</p></td>
</tr>
<tr class="even">
<td align="left">camera_id</td>
<td align="left"><p>ID of the camera to be used</p></td>
</tr>
<tr class="odd">
<td align="left">camera_resolution</td>
<td align="left"><p>map of pairs param_id-&gt;new_value</p></td>
</tr>
</tbody>
</table>

**Returns:.**

vector of informations about the detected face

#### rapp::object::qr\_code\_3d rapp::robot::vision::qr\_code\_detection (rapp::object::picture::Ptr image, std::vector&lt; std::vector&lt; float &gt;&gt; robot\_to\_camera\_matrix, double camera\_matrix\[\]\[3\], float landmark\_theoretical\_size=0.16f)

Detects QR-codes.

**.**

<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">image</td>
<td align="left"><p>image for the QR-code detection</p></td>
</tr>
<tr class="even">
<td align="left">robot_to_camera_matrix</td>
<td align="left"><p>transformation matrix from robot to camera framework</p></td>
</tr>
<tr class="odd">
<td align="left">camera_matrix</td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left">landmark_theoretical_size</td>
<td align="left"></td>
</tr>
</tbody>
</table>

**Returns:.**

QR-codes informations

#### camera\_info rapp::robot::vision::load\_camera\_info (int camera\_id)

Load camera calibration info for selected camera. If no calibration data is present, default values are returned.

**.**

<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">camera_id</td>
<td align="left"><p>selected camera id</p></td>
</tr>
</tbody>
</table>

#### void rapp::robot::vision::save\_camera\_info (int camera\_id, camera\_info info)

Save camera info for selected camera in persistend storage

**.**

<table>
<caption>Parameters</caption>
<colgroup>
<col width="20%" />
<col width="80%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">camera_id</td>
<td align="left"><p>selected caemra id</p></td>
</tr>
<tr class="even">
<td align="left">info</td>
<td align="left"><p>new camera parameters to be stored</p></td>
</tr>
</tbody>
</table>


