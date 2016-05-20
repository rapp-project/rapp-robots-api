rapp::robot::vision class Reference
===================================

#### enum camera\_params

brightness  

contrast  

gain  

auto\_exposure  

auto\_white\_balance  

exposure  

Definition at line 21 of file vision.hpp

    {
    brightness== 0, 
    contrast== 1, 
    gain== 6, 
    auto_exposure== 11, 
    auto_white_balance== 12, 
    exposure== 17, 
    }camera_params;
                        

#### enum camera\_resolution

qqvga  

qvga  

vga  

vga4  

Definition at line 30 of file vision.hpp

    {
    qqvga== 0, 
    qvga== 1, 
    vga== 2, 
    vga4== 3, 
    }camera_resolution;
                        

Pointer to implementation class.

*See Also:*.
Cheshire Cat (pimpl) programming pattern

Definition at line 111 of file vision.hpp

The Documentation for this struct was generated from the following file:

-   vision.hpp

#### rapp::robot::vision::vision (int argc=0, char \*argv[]=NULL)

Create vision module. Implementation object (pimpl) should be created here.


| Argument | Description |
|---|---|
|argc|number of arguments passed from host process|
|argv|list of arguments passed from host process|

#### rapp::robot::vision::\~vision ()

Destroy vision module. Implementation object should be destroyed here.

#### rapp::object::picture::Ptr rapp::robot::vision::capture\_image (int camera\_id, int camera\_resolution, const std::string &encoding)

Capture an image frame from the robot’s camera.


| Argument | Description |
|---|---|
|camera\_id|ID of the camera to be used|
|camera\_resolution||
|encoding|output image encoding type (e.g. "png", "jpg")|

*Returns:*.
captured image as raw byte stream

#### bool rapp::robot::vision::set\_camera\_param (int camera\_id, int parameter\_id, int new\_value)

Set camera parameter.


| Argument | Description |
|---|---|
|camera\_id|ID of the camera to be used|
|parameter\_id|ID of the parameter to be changed|
|new\_value|new value for the selected parameter|

*Returns:*.
true on success, false otherwise

#### std::map\<int, bool\> rapp::robot::vision::set\_camera\_params (int camera\_id, const std::map\< int, int \> &params)

Set multiple camera parameters at once.


| Argument | Description |
|---|---|
|camera\_id|ID of the camera to be used|
|params|map of pairs param\_id
* new\_value|

*Returns:*.
success flag for each parameter

#### std::vector\< std::vector \<float\> \> rapp::robot::vision::face\_detect (rapp::object::picture image, int camera\_id, int camera\_resolution)

Detects faces.


| Argument | Description |
|---|---|
|image|for the face detection|
|camera\_id|ID of the camera to be used|
|camera\_resolution|map of pairs param\_id
* new\_value|

*Returns:*.
vector of informations about the detected face

#### rapp::object::qr\_code\_3d rapp::robot::vision::qr\_code\_detection (rapp::object::picture::Ptr image, std::vector\< std::vector\< float \>\> robot\_to\_camera\_matrix, double camera\_matrix[][3], float landmark\_theoretical\_size=0.16f)

Detects QR-codes.


| Argument | Description |
|---|---|
|image|image for the QR-code detection|
|robot\_to\_camera\_matrix|transformation matrix from robot to camera framework|
|camera\_matrix||
|landmark\_theoretical\_size||

*Returns:*.
QR-codes informations
