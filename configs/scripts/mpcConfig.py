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
            content= instruction + soundName
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

if __name__ == "__main__":
    folder_path = "../resources/audio/experiment/"
    pages = []
    pages.append(create_generic_page("generic1", "Welcome Page", "Welcome to the test"))
    pages.append(create_consent_page("consent1", "Consent", "Please give your consent to participate in the test"))
    pages.append(create_volume_page("volume1", "Volume", "Please set the volume", "configs/resources/audio/calibration/volume/pinknoise_minus60db.wav"))
    pages.extend(create_mushra_test_pages(folder_path))
    pages.append(create_finish_page("finish1", "Finish", "Thank you for participating in the test!", True, True))
    config = create_config("MPCBrightness", "mpcBrightness", 1024, True, True, "service/write.php", pages)
    write_config_to_file(config, "mpc_brightness.yaml")





    

