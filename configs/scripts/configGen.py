import os
import yaml

def create_config(testname, testId, bufferSize, stopOnErrors, showButtonPreviousPage, remoteService, pages):
    config = {
        "testname": testname,
        "testId": testId,
        "bufferSize": bufferSize,
        "stopOnErrors": stopOnErrors,
        "showButtonPreviousPage": showButtonPreviousPage,
        "remoteService": remoteService,
        "pages": pages
    }
    return config

def write_config_to_file(config, filename):
    with open(os.path.join("../", filename), 'w') as file:
        yaml.dump(config, file)

# Generic Page
def create_generic_page(id, name, content):
    generic_page = {
        "type": "generic",
        "id": id,
        "name": name,
        "content": content
    }
    return generic_page

# Consent Page
def create_consent_page(id, name, content):
    consent_page = {
        "type": "consent",
        "id": id,
        "name": name,
        "content": content
    }
    return consent_page

# Volume Page
def create_volume_page(id, name, content, stimulus):
    volume_page = {
        "type": "volume",
        "id": id,
        "name": name,
        "content": content,
        "stimulus": stimulus,
        "default": 0.5
    }
    return volume_page

# MUSHRA Page
def create_mushra_page(id, name, content, showWaveform, enableLooping, strict, reference, createAnchor35, createAnchor70, randomize, showConditionNames, stimuli, switchBack):
    mushra_page = {
        "type": "mushra",
        "id": id,
        "name": name,
        "content": content,
        "showWaveform": showWaveform,
        "enableLooping": enableLooping,
        "strict": strict,
        "reference": reference,
        "createAnchor35": createAnchor35,
        "createAnchor70": createAnchor70,
        "randomize": randomize,
        "showConditionNames": showConditionNames,
        "stimuli": stimuli,
        "switchBack": switchBack
    }
    return mushra_page

# BS.1116 Page
def create_bs1116_page(id, name, content, showWaveform, enableLooping, reference, createAnchor35, createAnchor70, randomize, showConditionNames, stimuli, switchBack):
    bs1116_page = {
        "type": "bs1116",
        "id": id,
        "name": name,
        "content": content,
        "showWaveform": showWaveform,
        "enableLooping": enableLooping,
        "reference": reference,
        "createAnchor35": createAnchor35,
        "createAnchor70": createAnchor70,
        "randomize": randomize,
        "showConditionNames": showConditionNames,
        "stimuli": stimuli,
        "switchBack": switchBack
    }
    return bs1116_page

# Paired Comparison Page
def create_paired_comparison_page(id, name, unforced, content, showWaveform, enableLooping, reference, stimuli):
    paired_comparison_page = {
        "type": "paired_comparison",
        "id": id,
        "name": name,
        "unforced": unforced,
        "content": content,
        "showWaveform": showWaveform,
        "enableLooping": enableLooping,
        "reference": reference,
        "stimuli": stimuli
    }
    return paired_comparison_page

# Finish Page
def create_finish_page(id, name, content, showResults, writeResults):
    finish_page = {
        "type": "finish",
        "id": id,
        "name": name,
        "content": content,
        "showResults": showResults,
        "writeResults": writeResults
    }
    return finish_page

def __main__():
    print("This is the configScript.py file. It is not meant to be run as a standalone script.")
    pass




