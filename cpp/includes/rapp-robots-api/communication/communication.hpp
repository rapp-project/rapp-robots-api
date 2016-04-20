#ifndef RAPP_ROBOT_COMMUNICATION
#define RAPP_ROBOT_COMMUNICATION
#include "Includes.ihh"

namespace rapp {
namespace robot {

class CommunicationImpl;

/**
 * \class communication
 * \brief Interface class for robot communication module
 * \version 1
 * \date 20-September-2015
 * \author Maksym Figat <m.figat@ia.pw.edu.pl>
 */
class communication
{
public:
	
	/**
	 * Language for text-to-speech module
	 */
	enum class Language {ENGLISH, GREEK};

	/** 
	 * Create communication module. Implementation object (pimpl) should be created here.
	 */
	communication(int argc, char * argv[]);

	/**
	 * Destroy communication module. Implementation object should be destroyed here.
	 */
	~communication();

	/**
	 * Produce Audio from robot's speakers
	 * 
	 * \param file_path path to the audio file
	 * \param position 
	 * \param volume
	 * \param balance
	 * \param play_in_loop
	 * 
	 * \return
	 */
	bool playAudio(const std::string & file_path, double position, double volume, double balance, bool play_in_loop); 

	/** 
	 * Say given sentence in selected language
	 * 
	 * \param str
	 * \param lanugage
	 * 
	 * \return 
	 */
	bool textToSpeech(const std::string & str, Language language = Language::ENGLISH);

	/**
	 * Recognize the word included in the database
	 * 
	 * \param dictionary
	 * \param size
	 * 
	 * \return
	 * 
	 * \todo use vector<string> instead of string[]
	 */
	std::string wordSpotting(std::string dictionary[], int size);

	/**
	 * Record the audio message from the microphones by the desired time
	 * 
	 * \param time
	 * 
	 * \return
	 */
	std::string captureAudio(int time);

	/**
	 * Record the audio message with silence detection
	 * 
	 * \param file_path
	 * \param waiting_time
	 * \param microphone_energy
	 */
	std::string captureAudio(std::string & file_path, float waiting_time, int microphone_energy);

	/**
	 * Return signal energy of the selected microphone
	 * 
	 * \param name
	 * 
	 * \return
	 */
	int microphoneEnergy(std::string & name);

	/**
	 * Record the audio message to the buffer 
	 * 
	 * \param start
	 * \param buffer
	 */
	void voiceRecord(bool start, std::vector< std::vector<unsigned char> > & buffer);

private:
	CommunicationImpl * pimpl;

};

} // namespace robot
} // namespace rapp
#endif
