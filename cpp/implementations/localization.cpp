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

    rapp::object::quaternion localization::quaternion_from_euler(float roll, float pitch, float yaw){
    	rapp::object::quaternion rapp_quaternion;
        Eigen::AngleAxisf rollAngle((roll*M_PI) / 180, Eigen::Vector3f::UnitX());
        Eigen::AngleAxisf yawAngle((yaw*M_PI) / 180, Eigen::Vector3f::UnitZ());
        Eigen::AngleAxisf pitchAngle((pitch*M_PI) / 180, Eigen::Vector3f::UnitY());

        Eigen::Quaternionf q_eigen = yawAngle *  pitchAngle * rollAngle;
        
        rapp_quaternion.x = q_eigen.x();
        rapp_quaternion.y = q_eigen.y();
        rapp_quaternion.z = q_eigen.z();
        rapp_quaternion.w = q_eigen.w();

        return rapp_quaternion;

    }
    
    std::vector<float> localization::euler_from_quaternion(rapp::object::quaternion &rapp_quaternion){

        Eigen::Quaternionf q_eigen(rapp_quaternion.w,rapp_quaternion.x,rapp_quaternion.y,rapp_quaternion.z);

		Eigen::Vector3f euler_eigen = q_eigen.toRotationMatrix().eulerAngles(2, 1, 0);
		//yaw = euler[0]; pitch = euler[1]; roll = euler[2];
		static const float arr[] = {euler_eigen[2],euler_eigen[1],euler_eigen[0]};
    	std::vector<float> euler(arr, arr + sizeof(arr) / sizeof(arr[0]) );
    	return euler;

    }



	rapp::object::pose rapp_pose_fromeigen_matrix(Eigen::Matrix4f &eigen_matrix){
		rapp::object::pose end_pose;
		Eigen::Matrix3f mat_rot3 = eigen_matrix.block<3,3>(0,0);
        Eigen::Quaternion<float> q3(mat_rot3);
        Eigen::Vector4f t3;
        t3 = eigen_matrix.rightCols<1>();
        end_pose.position.x = t3(0);
        end_pose.position.y = t3(1);
        end_pose.position.z = t3(2);
        end_pose.orientation.x = q3.x();
        end_pose.orientation.y = q3.y();
        end_pose.orientation.z = q3.z();
        end_pose.orientation.w = q3.w();
        return end_pose;
	}

    void localization::pose_from_matrix(std::vector<std::vector<float>> matrix,rapp::object::pose &pose){
//Eigen::IOFormat OctaveFmt(Eigen::StreamPrecision, 0, ", ", ";\n", "", "", "[", "]");
	    Eigen::Matrix4f eigen_matrix;
	    Eigen::Vector4f eigen_vector;

		for (int i = 0; i < 4; i++){
			
// 			eigen_vector(0) = matrix[0];
			for (int k = 0; k < 4; k++){
//				eigen_vector = Eigen::Vector4f::Map(&matrix[k][0],k);
                        	eigen_vector(k) = matrix[i][k];

	 		}
	 		eigen_matrix.row(i) = eigen_vector;

		}
       		//std::cout << "eigen_matrix: \n"<<eigen_matrix.format(OctaveFmt) << std::endl;

	    	pose = rapp_pose_fromeigen_matrix(eigen_matrix);

    }


	void localization::multiply_poses(rapp::object::pose &pose1, rapp::object::pose &pose2, rapp::object::pose &end_pose)
    {
        Eigen::IOFormat OctaveFmt(Eigen::StreamPrecision, 0, ", ", ";\n", "", "", "[", "]");
        Eigen::Matrix4f Trans1;
        Eigen::Matrix4f Trans2;
        Eigen::Matrix4f Trans3;
        Eigen::Quaternion<float> q1(pose1.orientation.w, pose1.orientation.x, pose1.orientation.y, pose1.orientation.z);
        Eigen::Matrix3f orient1 = q1.toRotationMatrix();
        Eigen::Quaternion<float> q2(pose2.orientation.w, pose2.orientation.x, pose2.orientation.y, pose2.orientation.z);
        Eigen::Matrix3f orient2 = q2.toRotationMatrix();
        Eigen::Vector3f t1(pose1.position.x, pose1.position.y, pose1.position.z);
        Eigen::Vector3f t2(pose2.position.x, pose2.position.y, pose2.position.z);
        Trans1.setIdentity();
        Trans2.setIdentity();
        Trans1.block<3,3>(0,0) = orient1;
        Trans1.rightCols<1>().head(3) = t1;
        std::cout << "pose_1: \n"<<Trans1.format(OctaveFmt) << std::endl;

        Trans2.block<3,3>(0,0) = orient2;
        Trans2.rightCols<1>().head(3) = t2;
         std::cout << "pose_2: \n"<<Trans2.format(OctaveFmt) << std::endl;
       
        Trans3 = Trans1*Trans2;
        std::cout << "multipl_result_pose: \n"<<Trans3.format(OctaveFmt) << std::endl;
        Eigen::Matrix3f mat_rot3 = Trans3.block<3,3>(0,0);
        Eigen::Quaternion<float> q3(mat_rot3);
        Eigen::Vector4f t3;
        t3 = Trans3.rightCols<1>();
        end_pose.position.x = t3(0);
        end_pose.position.y = t3(1);
        end_pose.position.z = t3(2);
        end_pose.orientation.x = q3.x();
        end_pose.orientation.y = q3.y();
        end_pose.orientation.z = q3.z();
        end_pose.orientation.w = q3.w();
    }


	rapp::object::pose getRobotPoseFromQRcodeMap(rapp::object::qr_code_3d QRcodes,std::vector<std::vector<float>> camera_to_robot_matrix, rapp::object::qr_code_map QRmap){
		rapp::object::pose robot_in_map_pose_RAPP;

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
			//Eigen::Affine3f map_to_QRcode_transform; 


			// // ... NEW APPROACH
Eigen::IOFormat OctaveFmt(Eigen::StreamPrecision, 0, ", ", ";\n", "", "", "[", "]");
			Eigen::Quaternion<float> map_to_qr_code_quaternion(QRmap.poses[mapped_qrcode_ordinal_nr].orientation.w, QRmap.poses[mapped_qrcode_ordinal_nr].orientation.x, QRmap.poses[mapped_qrcode_ordinal_nr].orientation.y, QRmap.poses[mapped_qrcode_ordinal_nr].orientation.z);
			//Eigen::Matrix3d rotationMatrix = q.matrix();

			Eigen::Translation<float,3> map_to_qr_code_translation;
			map_to_qr_code_translation.x() = QRmap.poses[mapped_qrcode_ordinal_nr].position.x;
			map_to_qr_code_translation.y() = QRmap.poses[mapped_qrcode_ordinal_nr].position.y;
			map_to_qr_code_translation.z() = QRmap.poses[mapped_qrcode_ordinal_nr].position.z;

			Eigen::Transform<float,3,Eigen::Affine>  map_to_QRcode_transform= Eigen::Transform<float,3,Eigen::Affine>::Identity();
			map_to_QRcode_transform = map_to_qr_code_translation*map_to_qr_code_quaternion;

std::cout<<"map to QRcode matrix: \n"<<map_to_QRcode_transform.matrix().format(OctaveFmt)<<std::endl;

			//map_to_QRcode_transform.rotate(map_to_qr_code_quaternion);
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
			T_r_qr = QRcodes.landmark_in_camera_coordinate[found_qrcode_ordinal_nr];

	
			Eigen::Matrix4f matrix_robot_to_QRcode;
			Eigen::Vector3f translation_robot_to_QRcode((float) T_r_qr[0][3], (float) T_r_qr[1][3], (float) T_r_qr[2][3]);

			 matrix_robot_to_QRcode << (float) T_r_qr[0][0],(float) T_r_qr[0][1],(float) T_r_qr[0][2], (float) T_r_qr[0][3],
			  			(float) T_r_qr[1][0], (float) T_r_qr[1][1], (float) T_r_qr[1][2], (float) T_r_qr[1][3],
			  			(float) T_r_qr[2][0],(float) T_r_qr[2][1],(float) T_r_qr[2][2],(float)T_r_qr[2][3],
			  			0,0,0,1;
			  Eigen::Affine3f Affine3f_robot_to_QRcode, Affine3f_T_qr_r;

			  Affine3f_robot_to_QRcode.matrix() = matrix_robot_to_QRcode;
			  Affine3f_T_qr_r = Affine3f_robot_to_QRcode.inverse(); 

			  std::vector<std::vector<double>> T_g_r;
			  //MatrixMul( Affine3f_T_qr_r.matrix(),T_g_qr, T_g_r,4);

				// std::cout<< "KONIEC:" <<std::endl;
				// for(int i=0; i<4; i++){
				// 	for(int j=0; j<4;j++){
				// 		std::cout<< T_g_r[i][j] << "  ";
				// 	}
				// 	std::cout<< std::endl;
				// }		

			  //rotation_matrix_robot_to_QRcode;//.toRotationMatrix();//.matrix() = rotation_matrix_robot_to_QRcode//create_rotation_matrix(1.0, 1.0, 1.0);
			  //r.matrix().rightCols<1>() = translation_robot_to_QRcode;//Eigen::Affine3f t(Eigen::Translation3d(Eigen::Vector3d(1,1,2)));

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
			
			Eigen::Affine3f map_to_camera_transform, camera_to_robot_transform, map_to_robot_transform;
			/*float mT_g_r[4][4];
			for(int i=0; i<4; i++){
			for(int j=0; j<4;j++){
				mT_g_r[i][j] = T_g_r[i][j];

			}
			std::cout<< std::endl;
		} */
		camera_to_robot_transform.matrix() <<  (float) camera_to_robot_matrix[0][0],(float) camera_to_robot_matrix[0][1],(float) camera_to_robot_matrix[0][2], (float) camera_to_robot_matrix[0][3],
			  									(float) camera_to_robot_matrix[1][0], (float) camera_to_robot_matrix[1][1], (float) camera_to_robot_matrix[1][2], (float) camera_to_robot_matrix[1][3],
			  									(float) camera_to_robot_matrix[2][0], (float) camera_to_robot_matrix[2][1], (float) camera_to_robot_matrix[2][2], (float) camera_to_robot_matrix[2][3],
			  									0,0,0,1;
			map_to_camera_transform = map_to_QRcode_transform * Affine3f_T_qr_r;
			map_to_robot_transform = map_to_camera_transform*camera_to_robot_transform;
				// 			std::cout<< "CAMERA:" <<std::endl;
				// for(int i=0; i<4; i++){
				// 	for(int j=0; j<4;j++){
				// 		std::cout<< map_to_camera_transform(i,j) << "  ";
				// 	}
				// 	std::cout<< std::endl;
				// }	
			Eigen::Quaternion<float> end_quat(map_to_robot_transform.rotation());
			Eigen::Translation<float,3> end_position(map_to_robot_transform.translation());
			robot_in_map_pose_RAPP.orientation.x = end_quat.x();
			robot_in_map_pose_RAPP.orientation.y = end_quat.y();
			robot_in_map_pose_RAPP.orientation.z = end_quat.z();
			robot_in_map_pose_RAPP.orientation.w = end_quat.w();

			robot_in_map_pose_RAPP.position.x = end_position.x();
			robot_in_map_pose_RAPP.position.y = end_position.y();
			robot_in_map_pose_RAPP.position.z = end_position.z();

			//tf::poseEigenToMsg(map_to_robot_transform, robot_in_map_pose_ROS );
			//robot_in_map_pose_RAPP = transform_Pose_to_RAPP(robot_in_map_pose_ROS);

			return robot_in_map_pose_RAPP;
		}else{
				std::cout << "any of detected QRcodes is stored in the QRmap";
		
		}
			return robot_in_map_pose_RAPP;
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
			return robot_in_map_pose_RAPP;
		}


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

    rapp::object::pose localization::qr_code_localization(rapp::object::qr_code_3d QRcodes,std::vector<std::vector<float>> camera_to_robot_matrix, std::string *MapPath)
{
		rapp::object::qr_code_map QRmap = localization::load_qr_code_map(MapPath);
  		rapp::object::pose pose;
		pose = getRobotPoseFromQRcodeMap(QRcodes, camera_to_robot_matrix, QRmap);
  		return pose;
}

        rapp::object::pose localization::qr_code_localization(rapp::object::qr_code_3d QRcodes, std::vector<std::vector<float>> camera_to_robot_matrix,rapp::object::qr_code_map QRmap)
{
  		rapp::object::pose pose;
		pose = getRobotPoseFromQRcodeMap(QRcodes, camera_to_robot_matrix, QRmap);
  		return pose;
}
	rapp::object::qr_code_map localization::load_qr_code_map(std::string *MapPath)
{
	boost::property_tree::ptree pt;
	boost::property_tree::xml_parser::read_xml(*MapPath, pt);
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




} /* namespace robot */
} /* namespace rapp */
