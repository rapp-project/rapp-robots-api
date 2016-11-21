#ifndef RAPP_ROBOT_COMMUNICATION
#define RAPP_ROBOT_COMMUNICATION
#include "includes.ihh"

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
     * \param position starting position
     * \param volume volume level
     * \param balance balance between the speakers
     * \param play_in_loop flag for playing audio file in the loop
     * 
     * \return
     */
    bool play_audio(const std::string & file_path, double position = 0, double volume = 1, double balance = 0, bool play_in_loop = false);

    /** 
     * Say given sentence in selected language
     * 
     * \param str message which will be spoken
     * \param language flag of the language in which the message is given
     * 
     * \return 
     */
    bool text_to_speech(const std::string & str, Language language = Language::ENGLISH);

    /**
     * Recognize the word included in the database
     * 
     * \param dictionary list of short commands
     * 
     * \return
     * 
     * \todo use vector<string> instead of string[]
     */
    std::string word_spotting(const std::vector<std::string> & dictionary);

    /**
     * Record the audio message from the microphones by the desired time
     * 
     * \param time recording time
     * 
     * \return
     */
    std::string capture_audio(int time);

    /**
     * Record the audio message with silence detection
     * 
     * \param file_path path to the audio file, which will be recorded
     * \param waiting_time a desired waiting time in which if silence will not be broken than audio recording will be terminated
     * \param microphone_energy minimal energy for which sillence will occur
     */
    std::string capture_audio(std::string & file_path, float waiting_time, int microphone_energy);

    /**
     * Return signal energy of the selected microphone
     * 
     * \param name microphone's name
     * 
     * \return
     */
    int microphone_energy(std::string & name);

    /**
     * Record the audio message to the buffer 
     * 
     * \param start
     * \param buffer list of buffered messages
     */
    void voice_record(bool start, std::vector< std::vector<unsigned char> > & buffer);

private:
    CommunicationImpl * pimpl;

};

} // namespace robot
} // namespace rapp
#endif
