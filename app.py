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
        ProgressBar["title"].markdown("Normal Computing...")
        ProgressBar["bar"].progress(0/1)
        Data["normal"]["time"]["process"] = time.time()
        Data["normal"]["value"] = USERINPUT_A * USERINPUT_B
        Data["normal"]["time"]["process"] = time.time() - Data["normal"]["time"]["process"]
        ProgressBar["bar"].progress(1/1)

        # Memory Compute
        ## Create Memory
        ProgressBar["title"].markdown("Creating Memory...")
        ProgressBar["bar"].progress(0/2)
        Data["memory"]["time"]["init"] = time.time()
        Memory = CreateMemory_CustomOperation(1 << USERINPUT_N, COMPUTERS["Multiply"]["operation"])
        Data["memory"]["time"]["init"] = time.time() - Data["memory"]["time"]["init"]
        ProgressBar["bar"].progress(1/2)
        ## Compute
        ProgressBar["title"].markdown("Memory Computing...")
        Data["memory"]["time"]["process"] = time.time()
        Data["memory"]["value"] = COMPUTERS["Multiply"]["compute"](USERINPUT_A, USERINPUT_B, Memory, USERINPUT_N)
        Data["memory"]["time"]["process"] = time.time() - Data["memory"]["time"]["process"]
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
        st.markdown("### Overall")
        st.markdown("Answer Match: " + ("✅" if Data["normal"]["value"] == Data["memory"]["value"] else "❌"))

def mbm_evaluate():
    # Title
    st.header("Memory Based Multiplier - Evaluate")

    # Prereq Loaders
    
    # Load Inputs
    st.markdown("## Memory")
    USERINPUT_N_Range = st.slider("N (Memory Size Range: (2^N, 2^N))", min_value=1, max_value=10, value=(1, 3))
    st.markdown("## Inputs")
    cols = st.columns(2)
    USERINPUT_A_Range = (
        cols[0].number_input("A Start", min_value=0, max_value=1000000, value=22),
        cols[1].number_input("A End", min_value=0, max_value=1000000, value=23),
    )
    cols = st.columns(2)
    USERINPUT_B_Range = (
        cols[0].number_input("B Start", min_value=0, max_value=1000000, value=16),
        cols[1].number_input("B End", min_value=0, max_value=1000000, value=17),
    )

    # Process Inputs
    USERINPUT_StreamProcess = st.checkbox("Stream Process", value=False)
    if USERINPUT_StreamProcess or st.button("Process"):
        # Get Inputs
        USERINPUT_Ns = list(range(USERINPUT_N_Range[0], USERINPUT_N_Range[1]+1))
        USERINPUT_As = list(range(USERINPUT_A_Range[0], USERINPUT_A_Range[1]+1))
        USERINPUT_Bs = list(range(USERINPUT_B_Range[0], USERINPUT_B_Range[1]+1))
        # Init Data
        ProgressBar = {
            "title": st.sidebar.empty(),
            "bar": st.sidebar.empty()
        }
        Data = {
            "normal": {
                "value": np.zeros((len(USERINPUT_As), len(USERINPUT_Bs)), dtype=int),
                "time": {
                    "init": np.zeros((len(USERINPUT_As), len(USERINPUT_Bs)), dtype=float),
                    "process": np.zeros((len(USERINPUT_As), len(USERINPUT_Bs)), dtype=float)
                }
            },
            "memory": {
                "value": np.zeros((len(USERINPUT_Ns), len(USERINPUT_As), len(USERINPUT_Bs)), dtype=int),
                "time": {
                    "init": np.zeros((len(USERINPUT_Ns),), dtype=float),
                    "process": np.zeros((len(USERINPUT_Ns), len(USERINPUT_As), len(USERINPUT_Bs)), dtype=float)
                }
            }
        }

        # Normal Compute
        ## Compute
        ProgressBar["title"].markdown("Normal Computing...")
        ProgressBar["bar"].progress(0)
        for i in range(len(USERINPUT_As)):
            for j in range(len(USERINPUT_Bs)):
                Data["normal"]["time"]["process"][i, j] = time.time()
                Data["normal"]["value"][i, j] = USERINPUT_As[i] * USERINPUT_Bs[j]
                Data["normal"]["time"]["process"][i, j] = time.time() - Data["normal"]["time"]["process"][i, j]
            ProgressBar["bar"].progress((i+1)/len(USERINPUT_As))

        # Memory Compute
        for ni in range(len(USERINPUT_Ns)):
            USERINPUT_N = USERINPUT_Ns[ni]
            ## Create Memory
            ProgressBar["title"].markdown(f"Creating Memory... ({ni+1}/{len(USERINPUT_Ns)})")
            ProgressBar["bar"].progress(0/1)
            Data["memory"]["time"]["init"][ni] = time.time()
            Memory = CreateMemory_CustomOperation(1 << USERINPUT_N, COMPUTERS["Multiply"]["operation"])
            Data["memory"]["time"]["init"][ni] = time.time() - Data["memory"]["time"]["init"][ni]
            ProgressBar["bar"].progress(1/1)
            ## Compute
            ProgressBar["bar"].progress(0)
            ProgressBar["title"].markdown(f"Memory Computing... ({ni+1}/{len(USERINPUT_Ns)})")
            for i in range(len(USERINPUT_As)):
                for j in range(len(USERINPUT_Bs)):
                    USERINPUT_A = USERINPUT_As[i]
                    USERINPUT_B = USERINPUT_Bs[j]
                    Data["memory"]["time"]["process"][ni, i, j] = time.time()
                    Data["memory"]["value"][ni, i, j] = COMPUTERS["Multiply"]["compute"](USERINPUT_A, USERINPUT_B, Memory, USERINPUT_N)
                    Data["memory"]["time"]["process"][ni, i, j] = time.time() - Data["memory"]["time"]["process"][ni, i, j]
                ProgressBar["bar"].progress((i+1)/len(USERINPUT_As))
            ProgressBar["title"].markdown(f"Memory Computed ({ni+1}/{len(USERINPUT_Ns)})")

        # Display Outputs
        st.markdown("## Output")
        ## Normal
        st.markdown("### Normal Computation")
        VisData_Normal = {
            "n_samples": len(USERINPUT_As) * len(USERINPUT_Bs),
            "time": {
                "init": 0,
                "process": {
                    "min": np.min(Data["normal"]["time"]["process"]),
                    "max": np.max(Data["normal"]["time"]["process"]),
                    "mean": np.mean(Data["normal"]["time"]["process"]),
                    "std": np.std(Data["normal"]["time"]["process"]),
                    "total": np.sum(Data["normal"]["time"]["process"])
                }
            }
        }
        st.write(VisData_Normal)
        ## Memory
        ### Overall
        VisData_Memory = {}
        for ni in range(len(USERINPUT_Ns)):
            USERINPUT_N = USERINPUT_Ns[ni]
            matches = (Data["normal"]["value"] == Data["memory"]["value"][ni])
            n_matches = np.sum(matches)
            VisData_Memory[USERINPUT_N] = {
                "n_matches": int(n_matches),
                "accuracy": n_matches / (matches.shape[0]*matches.shape[1]),
                "time": {
                    "init": Data["memory"]["time"]["init"][ni],
                    "process": {
                        "min": np.min(Data["memory"]["time"]["process"][ni]),
                        "max": np.max(Data["memory"]["time"]["process"][ni]),
                        "mean": np.mean(Data["memory"]["time"]["process"][ni]),
                        "std": np.std(Data["memory"]["time"]["process"][ni]),
                        "total": np.sum(Data["memory"]["time"]["process"][ni])
                    }
                }
            }
        st.markdown("### Memory Computation - Overall")
        VisData_Memory_Overall = {
            "n_memories": len(USERINPUT_Ns),
            "n_samples": len(USERINPUT_As) * len(USERINPUT_Bs),
            "n_matches": int(np.sum([VisData_Memory[USERINPUT_N]["n_matches"] for USERINPUT_N in USERINPUT_Ns])),
            "accuracy": np.mean([VisData_Memory[USERINPUT_N]["accuracy"] for USERINPUT_N in USERINPUT_Ns]),
            "time": {
                "init": {
                    "min": np.min([VisData_Memory[USERINPUT_N]["time"]["init"] for USERINPUT_N in USERINPUT_Ns]),
                    "max": np.max([VisData_Memory[USERINPUT_N]["time"]["init"] for USERINPUT_N in USERINPUT_Ns]),
                    "mean": np.mean([VisData_Memory[USERINPUT_N]["time"]["init"] for USERINPUT_N in USERINPUT_Ns]),
                    "std": np.std([VisData_Memory[USERINPUT_N]["time"]["init"] for USERINPUT_N in USERINPUT_Ns]),
                    "total": np.sum([VisData_Memory[USERINPUT_N]["time"]["init"] for USERINPUT_N in USERINPUT_Ns])
                },
                "process": {
                    "min": np.min([VisData_Memory[USERINPUT_N]["time"]["process"]["min"] for USERINPUT_N in USERINPUT_Ns]),
                    "max": np.max([VisData_Memory[USERINPUT_N]["time"]["process"]["max"] for USERINPUT_N in USERINPUT_Ns]),
                    "mean": np.mean([VisData_Memory[USERINPUT_N]["time"]["process"]["mean"] for USERINPUT_N in USERINPUT_Ns]),
                    "std": np.mean([VisData_Memory[USERINPUT_N]["time"]["process"]["std"] for USERINPUT_N in USERINPUT_Ns]),
                    "total": np.sum([VisData_Memory[USERINPUT_N]["time"]["process"]["total"] for USERINPUT_N in USERINPUT_Ns])
                }
            }
        }
        st.write(VisData_Memory_Overall)
        ### Casewise
        if st.checkbox("Show Casewise"):
            for ni in range(len(USERINPUT_Ns)):
                USERINPUT_N = USERINPUT_Ns[ni]
                st.markdown(f"### Memory Computation (N = {USERINPUT_N})")
                st.write(VisData_Memory[USERINPUT_N])
                st.image(np.array(matches, dtype=float), caption="Matches", use_column_width=True)

    
#############################################################################################################################
# Driver Code
if __name__ == "__main__":
    main()