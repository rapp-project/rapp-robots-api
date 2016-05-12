#include <iostream>

#include <rapp-robots-api/localization/localization.hpp>
// search vector std::find
#include <algorithm>
// inverse matrix etc.
#include <eigen3/Eigen/Core>
//#include <geometry_msgs/Pose.h>
//#include <tinyxml2.h>
#include <eigen3/Eigen/Geometry>
// conversions TF to eigen and eigen to TF
//#include <eigen_conversions/eigen_msg.h>
//#include <tf_conversions/tf_eigen.h>
#include <boost/property_tree/xml_parser.hpp>
#include <boost/property_tree/ptree.hpp>
#include <boost/foreach.hpp>
namespace rapp {
namespace robot {

// placeholder class for vision implementation
  	localization::localization(int argc, char ** argv)
{
    std::cout << "Initialized placeholder rapp::robot::localization library" << std::endl;
}

    localization::~localization()
{
    std::cout << "Finished placeholder rapp::robot::navigation library" << std::endl;
}

	rapp::object::pose localization::qr_code_localization(rapp::object::qr_code_3d QRcodes,std::vector<std::vector<float>> camera_to_robot_matrix, const char* MapPath)
{
	rapp::object::pose pose;
	return pose;
}

        rapp::object::pose localization::qrCodeLocalization(rapp::object::qr_code_3d QRcodes, std::vector<std::vector<float>> camera_to_robot_matrix,rapp::object::qr_code_map QRmap)
{
	rapp::object::pose pose;
	return pose;
}
	rapp::object::qr_code_map localization::load_qr_code_map(std::istream & MapPath)
{
	boost::property_tree::ptree pt;
	boost::property_tree::xml_parser::read_xml(MapPath, pt);
	rapp::object::pose pose;
	rapp::object::qr_code_map qr_map;
	qr_map.labels.clear();
	qr_map.poses.clear();
	BOOST_FOREACH( boost::property_tree::ptree::value_type const& v, pt.get_child("QRcodes") ) {
        if( v.first == "QR" ) {
		pose.position.x = v.second.get<float>("x");
		pose.position.y = v.second.get<float>("y");
		pose.position.z = v.second.get<float>("z");
		pose.orientation.x = v.second.get<float>("ox");
		pose.orientation.y = v.second.get<float>("oy");
		pose.orientation.z = v.second.get<float>("oz");
		pose.orientation.w = v.second.get<float>("ow");
		qr_map.poses.push_back(pose);
		qr_map.labels.push_back(v.second.get<std::string>("label"));
        }
	}

	return qr_map;
}
std::vector<std::vector<double>> MatrixMul(std::vector<std::vector<double>> vectorsA, std::vector<std::vector<double>> vectorsB ,  int size)
{
	double matrixA[size][size];
	double matrixB[size][size];
	double matrixC[size][size];
	std::vector<std::vector<double>> vectorsC;
	vectorsC.clear();
std::vector<double> row;
		for(int i=0; i<size; i++){
			for(int j=0; j<size;j++){
				matrixA[i][j] = vectorsA[i][j];
				matrixB[i][j] = vectorsB[i][j];

			}
		}	
	
    int i, j, k;

    for(i=0; i<size; i++)                                      // liczy wiersze 
    for(j=0; j<size; j++)                                      // liczy kolumny
    matrixC[i][j]=0;   
		

    for(i=0; i<size; i++)
    for(j=0; j<size; j++)
    for(k=0; k<size; k++)
    matrixC[i][j] += matrixA[i][k] * matrixB[k][j]; 

	row.clear();
	for(int i=0; i<size; i++){
		for(int j=0; j<size;j++){
					
			row.push_back(matrixC[i][j]);
		}
			vectorsC.push_back(row);
			row.clear();
	}		

	// std::cout<< "rozmieszczanie:" <<std::endl;
	// 			std::cout<< "vectorC:" <<std::endl;
	// 	for(int i=0; i<size; i++){
	// 		for(int j=0; j<size;j++){
	// 			std::cout<< vectorsC[i][j] << "  ";
	// 		}
	// 		std::cout<< std::endl;
	// 	}	
		return vectorsC;
}

	rapp::object::pose getRobotPoseFromQRcodeMap(rapp::object::qr_code_3d QRcodes,std::vector<std::vector<float>> camera_to_robot_matrix, rapp::object::qr_code_map QRmap){

		if (QRcodes.number_of_qr_codes > 0){

			// check if one of the detected QRcode is defined in the QRcodeMap

			int k = 0;
			bool QRcode_found_in_map = false;
			int mapped_qrcode_ordinal_nr = -1;
			int found_qrcode_ordinal_nr = -1;
			while ( !QRcode_found_in_map && k < QRcodes.number_of_qr_codes ) {
				std::vector<std::string>::iterator find_iterator;
				find_iterator = std::find(QRmap.labels.begin(), QRmap.labels.end(), QRcodes.qr_message[k]);
				if ( find_iterator != QRmap.labels.end() ){
					QRcode_found_in_map = true;
					found_qrcode_ordinal_nr = k;
					mapped_qrcode_ordinal_nr = std::distance(QRmap.labels.begin(),find_iterator);
				}
				else{
					k += 1;
					QRcode_found_in_map = false;
				}
			}
			//check if any of detected QRcodes is stored in the QRmap
			if (mapped_qrcode_ordinal_nr != -1){

			// compute transformation matrix from map origin to detected QRcode using QRcodeMap
			//geometry_msgs::Pose QRcode_ROS_pose;
			//Eigen::Affine3d map_to_QRcode_transform; 


			// // ... NEW APPROACH

			Eigen::Quaternion<double> map_to_qr_code_quaternion(QRmap.poses[mapped_qrcode_ordinal_nr].orientation.w, QRmap.poses[mapped_qrcode_ordinal_nr].orientation.x, QRmap.poses[mapped_qrcode_ordinal_nr].orientation.y, QRmap.poses[mapped_qrcode_ordinal_nr].orientation.z);
			//Eigen::Matrix3d rotationMatrix = q.matrix();

			Eigen::Translation<double,3> map_to_qr_code_translation;
			Eigen::Transform<double,3,Eigen::Affine>  map_to_QRcode_transform= Eigen::Transform<float,3,Eigen::Affine>::Identity();
			map_to_QRcode_transform.translate(map_to_qr_code_translation);
			map_to_QRcode_transform.rotate(map_to_qr_code_quaternion);
			/*
			 tf::Quaternion q(QR

map.poses[mapped_qrcode_ordinal_nr].orientation.x,QRmap.poses[mapped_qrcode_ordinal_nr].orientation.y, QRmap.poses[mapped_qrcode_ordinal_nr].orientation.z, QRmap.poses[mapped_qrcode_ordinal_nr].orientation.w);
			 tf::Matrix3x3 m(q);
			 double roll, pitch, yaw;
			 m.getRPY(roll, pitch, yaw);
			 // std::cout << "Roll: " << roll << ", Pitch: " << pitch << ", Yaw: " << yaw << std::endl;
			std::vector<std::vector<double>> T_g_qr = computeMatricFromPose(QRmap.poses[mapped_qrcode_ordinal_nr].position.x,QRmap.poses[mapped_qrcode_ordinal_nr].position.y,
			 																		QRmap.poses[mapped_qrcode_ordinal_nr].position.z, roll, pitch, yaw);




			map_to_QRcode_transform.matrix() << T_g_qr[0][0], T_g_qr[0][1], T_g_qr[0][2], T_g_qr[0][3],
												T_g_qr[1][0], T_g_qr[1][1], T_g_qr[1][2], T_g_qr[1][3],
												T_g_qr[2][0], T_g_qr[2][1], T_g_qr[2][2], T_g_qr[2][3],
												T_g_qr[3][0], T_g_qr[3][1], T_g_qr[3][2], T_g_qr[3][3];

			 tf::Quaternion q0(QRmap.poses[0].orientation.x,QRmap.poses[0].orientation.y, QRmap.poses[0].orientation.z, QRmap.poses[0].orientation.w);
			 tf::Matrix3x3 m0(q0);
			 double roll0, pitch0, yaw0;
			 m0.getRPY(roll0, pitch0, yaw0);
			std::vector<std::vector<double>> T_g_qr0 = computeMatricFromPose(QRmap.poses[0].position.x,QRmap.poses[0].position.y,
			 								QRmap.poses[0].position.z, roll0, pitch0, yaw0);
*/
			std::vector<std::vector<double>> T_r_qr;
			T_r_qr = QRcodes.LandmarkInCameraCoordinate[found_qrcode_ordinal_nr];

	
			Eigen::Matrix4d matrix_robot_to_QRcode;
			Eigen::Vector3d translation_robot_to_QRcode( T_r_qr[0][3],T_r_qr[1][3],T_r_qr[2][3]);

			 matrix_robot_to_QRcode << T_r_qr[0][0], T_r_qr[0][1], T_r_qr[0][2],T_r_qr[0][3],
			  			T_r_qr[1][0], T_r_qr[1][1], T_r_qr[1][2],T_r_qr[1][3],
			  			T_r_qr[2][0], T_r_qr[2][1], T_r_qr[2][2],T_r_qr[2][3],
			  			0,0,0,1;
			  Eigen::Affine3d Affine3d_robot_to_QRcode, Affine3d_T_qr_r;

			  Affine3d_robot_to_QRcode.matrix()=matrix_robot_to_QRcode;
			  Affine3d_T_qr_r = Affine3d_robot_to_QRcode.inverse(); 

			  std::vector<std::vector<double>> T_g_r;
			  //MatrixMul( Affine3d_T_qr_r.matrix(),T_g_qr, T_g_r,4);

				// std::cout<< "KONIEC:" <<std::endl;
				// for(int i=0; i<4; i++){
				// 	for(int j=0; j<4;j++){
				// 		std::cout<< T_g_r[i][j] << "  ";
				// 	}
				// 	std::cout<< std::endl;
				// }		

			  //rotation_matrix_robot_to_QRcode;//.toRotationMatrix();//.matrix() = rotation_matrix_robot_to_QRcode//create_rotation_matrix(1.0, 1.0, 1.0);
			  //r.matrix().rightCols<1>() = translation_robot_to_QRcode;//Eigen::Affine3d t(Eigen::Translation3d(Eigen::Vector3d(1,1,2)));

			  //Eigen::Matrix4d m = (t * r).matrix(); // Option 1


			 //Eigen::Matrix3d rotation_matrix_robot_to_QRcode;
			// rotation_matrix_robot_to_QRcode << robot_to_QRcode_vectors[0][0], robot_to_QRcode_vectors[0][1], robot_to_QRcode_vectors[0][2],
			// 									robot_to_QRcode_vectors[1][0], robot_to_QRcode_vectors[1][1], robot_to_QRcode_vectors[1][2],
			// 									robot_to_QRcode_vectors[2][0], robot_to_QRcode_vectors[2][1], robot_to_QRcode_vectors[2][2];

			// Eigen::Quaterniond quaternion_robot_to_QRcode(rotation_matrix_robot_to_QRcode);
			// Eigen::Vector3d translation_robot_to_QRcode( robot_to_QRcode_vectors[0][3],robot_to_QRcode_vectors[1][3],robot_to_QRcode_vectors[2][3]);

			// Eigen::Matrix4d robot_to_QRcode_transform, QRcode_to_robot_transform;
			// robot_to_QRcode_transform.setIdentity();
			// robot_to_QRcode_transform.block<3,3>(0,0) = rotation_matrix_robot_to_QRcode;
			// robot_to_QRcode_transform.rightCols<1>() = translation_robot_to_QRcode;
			// QRcode_to_robot_transform = robot_to_QRcode_transform.inverse(); 


			// compute transformation from map to robot
				// !!!!!!!!!!!!!!!!!!!!!!!!!!!!
			//geometry_msgs::Pose robot_in_map_pose_ROS;
			rapp::object::pose robot_in_map_pose_RAPP;
			Eigen::Affine3d map_to_camera_transform, camera_to_robot_transform, map_to_robot_transform;
			double mT_g_r[4][4];
			for(int i=0; i<4; i++){
			for(int j=0; j<4;j++){
				mT_g_r[i][j] = T_g_r[i][j];

			}
			std::cout<< std::endl;
		} 
		camera_to_robot_transform.matrix() <<  camera_to_robot_matrix[0][0], camera_to_robot_matrix[0][1], camera_to_robot_matrix[0][2],camera_to_robot_matrix[0][3],
			  									camera_to_robot_matrix[1][0], camera_to_robot_matrix[1][1], camera_to_robot_matrix[1][2],camera_to_robot_matrix[1][3],
			  									camera_to_robot_matrix[2][0], camera_to_robot_matrix[2][1], camera_to_robot_matrix[2][2],camera_to_robot_matrix[2][3],
			  									0,0,0,1;
			map_to_camera_transform = map_to_QRcode_transform * Affine3d_T_qr_r;
			map_to_robot_transform = map_to_camera_transform*camera_to_robot_transform;
				// 			std::cout<< "CAMERA:" <<std::endl;
				// for(int i=0; i<4; i++){
				// 	for(int j=0; j<4;j++){
				// 		std::cout<< map_to_camera_transform(i,j) << "  ";
				// 	}
				// 	std::cout<< std::endl;
				// }	
			Eigen::Quaternion end_quat(map_to_robot_transform.matrix());
			Eigen::Translation end_position(map_to_robot_transform.translation());
			robot_in_map_pose_RAPP.orientation.x = end_quat.x;
			robot_in_map_pose_RAPP.orientation.y = end_quat.y;
			robot_in_map_pose_RAPP.orientation.z = end_quat.z;
			robot_in_map_pose_RAPP.orientation.w = end_quat.w;

			robot_in_map_pose_RAPP.position.x = end_position.x;
			robot_in_map_pose_RAPP.position.y = end_position.y;
			robot_in_map_pose_RAPP.position.z = end_position.z;

			//tf::poseEigenToMsg(map_to_robot_transform, robot_in_map_pose_ROS );
			//robot_in_map_pose_RAPP = transform_Pose_to_RAPP(robot_in_map_pose_ROS);

			return robot_in_map_pose_RAPP;
		}else{
				std::cout << "any of detected QRcodes is stored in the QRmap";
		
		}
			// tf::quaternionTFToEigen(&quaternion_robot_to_QRcode)
			// geometry_msgs::Pose QRcode_in_robot_pose;
			// QRcode_in_robot_pose.pose.position.x = robot_to_QRcode_vectors[0][0]

			// Eigen::Matrix4d robot_to_QRcode_matrix;
			// for (int i = 0; i<4;i++){
			// 	for (int j = 0; j<4;j++){
			// 	robot_to_QRcode_matrix(i,j) = robot_to_QRcode_vectors[i][j];
			// 	}
			// }
			
			// QRcode_to_robot_matrix = robot_to_QRcode_matrix.inverse();

			// // compute transformation from map to robot
			// Eigen::Matrix4d map_to_robot_matrix = map_to_QRcode_matrix * QRcode_to_robot_matrix;
		
			// Eigen::Matrix4d robot_to_map_matrix = map_to_robot_matrix.inverse();

			// // ext



		}
		else{
				std::cout << "No QRcodes in passed object";
		}


	}
std::vector<std::vector<double>> computeMatricFromPose(double x,double y,double z,double ox,double oy,double oz){
		
		/*
		# NEW approach
		*/

		std::vector<double> row;

		std::vector<std::vector<double>> Z_c_g;
		row.push_back(cos(oz));
		row.push_back(-sin(oz));
		row.push_back(0);
		Z_c_g.push_back(row);
		row.clear();

		row.push_back(sin(oz));
		row.push_back(cos(oz));
		row.push_back(0);
		Z_c_g.push_back(row);
		row.clear();

		row.push_back(0);
		row.push_back(0);
		row.push_back(1);
		Z_c_g.push_back(row);
		row.clear();

		std::vector<std::vector<double>> Y_c_g;
		row.push_back(cos(oy));
		row.push_back(0);
		row.push_back(sin(oy));
		Y_c_g.push_back(row);
		row.clear();

		row.push_back(0);
		row.push_back(1);
		row.push_back(0);
		Y_c_g.push_back(row);
		row.clear();

		row.push_back(-sin(oy));
		row.push_back(0);
		row.push_back(cos(oy));
		Y_c_g.push_back(row);
		row.clear();

		std::vector<std::vector<double>> X_c_g;
		row.push_back(1);
		row.push_back(0);
		row.push_back(0);
		X_c_g.push_back(row);
		row.clear();

		row.push_back(0);
		row.push_back(cos(ox));
		row.push_back(-sin(ox));
		X_c_g.push_back(row);
		row.clear();

		row.push_back(0);
		row.push_back(sin(ox));
		row.push_back(cos(ox));
		X_c_g.push_back(row);
		row.clear();


std::vector<std::vector<double>>  ZY;
std::vector<std::vector<double>>   R_c_g;
ZY = MatrixMul(Z_c_g, Y_c_g,  3);
	
R_c_g=MatrixMul(ZY, X_c_g,  3);



		std::vector<std::vector<double>> T_c_g;
		row.clear();
		for(int i=0; i<3; i++){
			for(int j=0; j<3;j++){
							

				row.push_back(R_c_g[i][j]);
			}
			if(i==0)
				row.push_back(x);
			if(i==1)
				row.push_back(y);
			if(i==2)
				row.push_back(z);
			if(i==2)
				row.push_back(1);

				T_c_g.push_back(row);
				row.clear();
		}

		for(int j=0; j<3;j++){


			row.push_back(0);
		}
		
		row.push_back(1);
		T_c_g.push_back(row);


		return T_c_g;

	}

} /* namespace robot */
} /* namespace rapp */
