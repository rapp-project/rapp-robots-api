#include <iostream>

#include <rapp-robots-api/communication/communication.hpp>

namespace rapp {
namespace robot {

// placeholder class for vision implementation
class CommunicationImpl {
};

communication::communication(int argc, char * argv[]) : pimpl(NULL) 
{
	std::cout << "Initialized placeholder rapp::robot::communication library" << std::endl;
}

communication::~communication() 
{
	std::cout << "Finished placeholder rapp::robot::communication library" << std::endl;
}

bool communication::playAudio(const std::string & file_path, double position, double volume, double balance, bool play_in_loop) 
{
	std::cout << "communication::playAudio: " << file_path << std::endl;
	return false;
}

bool communication::textToSpeech(const std::string & str, Language language)
{
	std::cout << "communication::textToSpeech: " << str << std::endl;
	return false;
}

std::string communication::wordSpotting(std::string dictionary[], int size)
{
	std::cout << "communication::wordSpotting" << std::endl;
	return "";
}

std::string communication::captureAudio(int time)
{
	std::cout << "communication::captureAudio" << std::endl;
	return "";
}

std::string communication::captureAudio(std::string & file_path, float waiting_time, int microphone_energy)
{
	std::cout << "communication::captureAudio" << std::endl;
	return "";
}

int communication::microphoneEnergy(std::string & name)
{
	std::cout << "communication::microphoneEnergy" << std::endl;
	return -1;
}

void communication::voiceRecord(bool start, std::vector< std::vector<unsigned char> > & buffer)
{
	std::cout << "communication::voiceRecord" << std::endl;
}


} /* namespace robot */
} /* namespace rapp */
