import os
from configGen import create_config, write_config_to_file, create_mushra_page, create_generic_page, create_consent_page, create_volume_page, create_finish_page

def create_file_dict(folder_path):
    file_dict = {}
    for folder_name, subfolders, files in os.walk(folder_path):
        file_dict[folder_name] = files
    return file_dict

def create_mushra_test_pages(folder_path, pages=[]):
    file_dict = create_file_dict(folder_path)

    for subfolder, files in file_dict.items():
        if subfolder != folder_path:
            soundName = subfolder.split("/")[-1]
            subfolder = subfolder.replace("..", "configs")
            instruction = "Rate the brightness of each stimuli compared to the reference "
            refFile = [s for s in files if "+0.000dB" in s][0]
            files.remove(refFile)

            # Create a mushra test page using the sounds inside the subfolder
            id= soundName
            name= soundName
            content= instruction
            showWaveform= True
            enableLooping= True
            strict= False
            reference= os.path.join(subfolder, refFile)
            createAnchor35= False
            createAnchor70= False
            randomize= True
            showConditionNames= False
            stimuli= {"C"+str(index+1): os.path.join(subfolder, item) for index, item in enumerate(files)}
            switchBack= True

            pages.append(create_mushra_page(id, name, content, showWaveform, enableLooping, strict, reference, createAnchor35, createAnchor70, randomize, showConditionNames, stimuli, switchBack))
            print(f"Creating Mushra test page for subfolder: {subfolder}")
    
    return pages

def process_for_html(text):
    text = text.replace("\n", "<br>")
    text = text.replace("'", "&#39;")
    return text

def get_generic_page():
    id= "generic1"
    name= "Brightness Perception Test"
    contentText= "\
            Welcome to our online survey about music perception and thank you very much for participating! \n \n \
            In this survey, we wish to understand the perception of the word brightness when talking about music. \n \
            Brightness is widely used to describe the timbre attributes of a musical instrument, an opera singer's voice or any kind of sound. \n \n \
            With our study, we'd like to find out how you perceive the brightness of multiple song snippets. \n \n \
            We will play you a reference song snippet and then ask you to rate the brightness of 4 other song snippets. \n \
            Please use headphones to participate in this survey. \
            The survey will take approximately 10 minutes. \n \n\
            Please press <b> Next </b> below to proceed to the instructions page \n \
            "
    content = process_for_html(contentText)
    return create_generic_page(id, name, content)

def get_instruction_page(folder_path):
    """
       Create an instructional MUSHRA test to explain the task to the user
    """
    file_dict = create_file_dict(folder_path)
    subfolder = folder_path
    soundName = subfolder.split("/")[-1]
    subfolder = subfolder.replace("..", "configs")
    files = file_dict[folder_path]
    refFile = [s for s in files if "+0.000dB" in s][0]
    files.remove(refFile)

    id= "instruction1"
    name= "Instructions Page"
    contentText= "\
            You will be presented a reference sound and 4 potentially edited versions. \
            If any of the 4 conditions sounds less bright or more bright, you can indicate that by moving the slider down or up. \n \n \
            Although the slider is continuous, we'll assign all ratings to one of the five categories mentioned between the two enclosing markers. \n \
            So, a rating of 63 or 79 will both be assigned to the category <b> More Bright </b>. \
            Similarly, any rating between 0 to 19 will be assigned to the category <b> Least Bright </b>. \n \n\
            For each condition, your rating should be in comparison to the reference sound only. \n \
            When a condition is played using the <b> Play </b> button, its slider becomes active and a rating can be selected. \n \
            You can switch between the reference and condition as many times before selecting the rating. \n \n \
            If you perceive a song snippet as equally bright, that is no change from original, just set the slider at 50 (same brightness). \n \
            Please press <b> Next </b> below to proceed to the test \n \
            "
    content= process_for_html(contentText)
    showWaveform= True
    enableLooping= True
    strict= False
    reference= os.path.join(subfolder, refFile)
    createAnchor35= False
    createAnchor70= False
    randomize= True
    showConditionNames= False
    stimuli= {"C"+str(index+1): os.path.join(subfolder, item) for index, item in enumerate(files)}
    switchBack= True

    return create_mushra_page(id, name, content, showWaveform, enableLooping, strict, reference, createAnchor35, createAnchor70, randomize, showConditionNames, stimuli, switchBack)

if __name__ == "__main__":
    folder_path = "../resources/audio/experiment/"
    pages = []
    pages.append(get_generic_page())
    pages.append(get_instruction_page(os.path.join(folder_path, "Classical_GustavHolst_01_1")))
    # pages.append(create_consent_page("consent1", "Consent", "Please give your consent to participate in the test"))
    # pages.append(create_volume_page("volume1", "Volume", "Please set the volume", "configs/resources/audio/calibration/volume/pinknoise_minus60db.wav"))
    pages.extend(create_mushra_test_pages(folder_path))
    pages.append(create_finish_page("finish1", "Finish", "Thank you for participating in the test!", True, True))
    config = create_config("MPCBrightness", "mpcBrightness", 1024, True, True, "service/write.php", pages)
    write_config_to_file(config, "mpc_brightness.yaml")





    

