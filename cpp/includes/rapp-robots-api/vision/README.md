vision class Reference
===================================

#### enum camera\_params

Camera parameters

**Enumerator:.**

brightness  

contrast  

gain  

auto\_exposure  

auto\_white\_balance  

exposure  

Definition at line 36 of file vision.hpp `
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

Camera resolution

**Enumerator:.**

qqvga  

qvga  

vga  

vga4  

Definition at line 48 of file vision.hpp `
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

Definition at line 145 of file vision.hpp

The Documentation for this struct was generated from the following file:

-   vision.hpp

#### vision::vision (int argc=0, char \*argv\[\]=NULL)

Create vision module. Implementation object (pimpl) should be created here.



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

#### vision::~vision ()

Destroy vision module. Implementation object should be destroyed here.

#### rapp::object::picture::Ptr vision::capture\_image (int camera\_id, int camera\_resolution, const std::string &encoding)

Capture an image frame from the robot’s camera.



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

#### bool vision::set\_camera\_param (int camera\_id, int parameter\_id, int new\_value)

Set camera parameter.



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

#### std::map&lt;int, bool&gt; vision::set\_camera\_params (int camera\_id, const std::map&lt; int, int &gt; &params)

Set multiple camera parameters at once.



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

#### std::vector&lt; std::vector &lt;float&gt; &gt; vision::face\_detect (rapp::object::picture image, int camera\_id, int camera\_resolution)

Detects faces.



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

#### rapp::object::qr\_code\_3d vision::qr\_code\_detection (rapp::object::picture::Ptr image, std::vector&lt; std::vector&lt; float &gt;&gt; robot\_to\_camera\_matrix, double camera\_matrix\[\]\[3\], float landmark\_theoretical\_size=0.16f)

Detects QR-codes.



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

#### camera\_info vision::load\_camera\_info (int camera\_id)

Load camera calibration info for selected camera. If no calibration data is present, default values are returned.



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

#### void vision::save\_camera\_info (int camera\_id, camera\_info info)

Save camera info for selected camera in persistend storage



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


