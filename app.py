"""
Stream lit GUI for hosting MemoryBasedComputation
"""

# Imports
import os
import json
import time
import streamlit as st

from MemoryBasedComputation import *

# Main Vars
config = json.load(open("./StreamLitGUI/UIConfig.json", "r"))

# Main Functions
def main():
    # Create Sidebar
    selected_box = st.sidebar.selectbox(
    "Choose one of the following",
        tuple(
            [config["PROJECT_NAME"]] + 
            config["PROJECT_MODES"]
        )
    )
    
    if selected_box == config["PROJECT_NAME"]:
        HomePage()
    else:
        correspondingFuncName = selected_box.replace(" ", "_").lower()
        if correspondingFuncName in globals().keys():
            globals()[correspondingFuncName]()
 

def HomePage():
    st.title(config["PROJECT_NAME"])
    st.markdown("Github Repo: " + "[" + config["PROJECT_LINK"] + "](" + config["PROJECT_LINK"] + ")")
    st.markdown(config["PROJECT_DESC"])

    # st.write(open(config["PROJECT_README"], "r").read())

#############################################################################################################################
# Repo Based Vars
CACHE_PATH = "StreamLitGUI/CacheData/Cache.json"

# Util Vars
CACHE = {}

# Util Functions
def LoadCache():
    global CACHE
    CACHE = json.load(open(CACHE_PATH, "r"))

def SaveCache():
    global CACHE
    json.dump(CACHE, open(CACHE_PATH, "w"), indent=4)

# Main Functions


# UI Functions


# Repo Based Functions
def mbm():
    # Title
    st.header("Memory Based Multiplier")

    # Prereq Loaders
    
    # Load Inputs
    st.markdown("## Memory")
    USERINPUT_N = st.number_input("N (Memory Size: (2^N, 2^N))", min_value=1, max_value=10, value=2)
    st.markdown("## Inputs")
    USERINPUT_A = st.number_input("A", min_value=0, max_value=1000000, value=23)
    USERINPUT_B = st.number_input("B", min_value=0, max_value=1000000, value=17)

    # Process Inputs
    USERINPUT_StreamProcess = st.checkbox("Stream Process", value=False)
    if USERINPUT_StreamProcess or st.button("Process"):
        ProgressBar = {
            "title": st.sidebar.empty(),
            "bar": st.sidebar.empty()
        }
        Data = {
            "normal": {
                "value": 0,
                "time": {
                    "init": 0,
                    "process": 0
                }
            },
            "memory": {
                "value": 0,
                "time": {
                    "init": 0,
                    "process": 0
                }
            }
        }

        # Normal Compute
        ## Compute
        Data["normal"]["time"]["init"] = time.time_ns()
        Data["normal"]["value"] = USERINPUT_A * USERINPUT_B
        Data["normal"]["time"]["init"] = time.time_ns() - Data["normal"]["time"]["init"]

        # Memory Compute
        ## Create Memory
        ProgressBar["title"].markdown("Creating Memory...")
        ProgressBar["bar"].progress(0/2)
        Data["memory"]["time"]["init"] = time.time_ns()
        Memory = CreateMemory_CustomOperation(1 << USERINPUT_N, COMPUTERS["Multiply"]["operation"])
        Data["memory"]["time"]["init"] = time.time_ns() - Data["memory"]["time"]["init"]
        ProgressBar["bar"].progress(1/2)
        ## Compute
        ProgressBar["title"].markdown("Computing...")
        Data["memory"]["time"]["process"] = time.time_ns()
        Data["memory"]["value"] = COMPUTERS["Multiply"]["compute"](USERINPUT_A, USERINPUT_B, Memory, USERINPUT_N)
        Data["memory"]["time"]["process"] = time.time_ns() - Data["memory"]["time"]["process"]
        ProgressBar["bar"].progress(2/2)
        ProgressBar["title"].markdown("Computed")

        # Display Outputs
        st.markdown("## Output")
        st.markdown("### Normal Computation")
        st.latex(f"A \\times B = {USERINPUT_A} \\times {USERINPUT_B} = {Data['normal']['value']}")
        st.write(Data["normal"])
        st.markdown("### Memory Computation")
        st.latex(f"A \\times B = {USERINPUT_A} \\times {USERINPUT_B} = {Data['memory']['value']}")
        st.write(Data["memory"])
    
#############################################################################################################################
# Driver Code
if __name__ == "__main__":
    main()