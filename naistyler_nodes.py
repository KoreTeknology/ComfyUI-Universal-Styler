import os
import re
import folder_paths

from pathlib import Path

#DEBUG pathlib (to replace folder_path from OS)
print(Path.cwd())
print("############################################")
BASE_DIR = Path.cwd()
DATAPATH = BASE_DIR.joinpath("custom_nodes","ComfyUI-Universal-Styler","CSV")
print(DATAPATH)
print("############################################")
my_database = [str(file) for file in DATAPATH.glob("*.csv")]
print(my_database)
print("############################################")


################
# NAI Show text v0.3 ##########################################################################
################

class ShowText:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    FUNCTION = "notify"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)

    CATEGORY = "✴️ Universal NAI Nodes"

    def notify(self, text, unique_id=None, extra_pnginfo=None):
        if unique_id is not None and extra_pnginfo is not None:
            if not isinstance(extra_pnginfo, list):
                print("Error: extra_pnginfo is not a list")
            elif (
                not isinstance(extra_pnginfo[0], dict)
                or "workflow" not in extra_pnginfo[0]
            ):
                print("Error: extra_pnginfo[0] is not a dict or missing 'workflow' key")
            else:
                workflow = extra_pnginfo[0]["workflow"]
                node = next(
                    (x for x in workflow["nodes"] if str(x["id"]) == str(unique_id[0])),
                    None,
                )
                if node:
                    node["widgets_values"] = [text]

        return {"ui": {"text": text}, "result": (text,)}


################
# NAI STYLER v0.3 ##########################################################################
################

class NaiStylerComplexCSVLoader:

    # Part 1
    
    @staticmethod
    def load_naistyles_csv(naistyles_path: str):
        """Loads csv file, Ignore the first row (header).
        Returns:
            list: List of naistyles. Each style is a dict with keys: style_name and value: [positive_prompt, negative_prompt]
        """
        naistyles = {"Error loading naistyles.csv, check the console": ["",""]}
        if not os.path.exists(naistyles_path):
            print(f"""Error. No naistyles.csv found. Put your naistyles.csv in the custom_nodes/ComfyUI-Universal-Styler/CSV directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return naistyles
        try:
            with open(naistyles_path, "r", encoding="utf-8") as f:    
                naistyles = [[x.replace('"', '').replace('\n','') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                naistyles = {x[0]: [x[1],x[2]] for x in naistyles}
        except Exception as e:
            print(f"""Error loading naistyles.csv. Make sure it is in the custom_nodes/ComfyUI-Universal-Styler/CSV directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return naistyles
    
    # part 2

    @staticmethod
    def load_naifilters_csv(naifilters_path: str):
        """Loads filtercsv file, Ignore the first row (header).
        Returns:
            list: List of naistyles. Each style is a dict with keys: style_name and value: [positive_prompt, negative_prompt]
        """
        naifilters = {"Error loading naistyles.csv, check the console": ["",""]}
        if not os.path.exists(naifilters_path):
            print(f"""Error. No naistyles.csv found. Put your naistyles.csv in the custom_nodes/ComfyUI-Universal-Styler/CSV directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return naifilters
        try:
            with open(naifilters_path, "r", encoding="utf-8") as f:    
                naifilters = [[x.replace('"', '').replace('\n','') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                naifilters = {x[0]: [x[1],x[2]] for x in naifilters}
        except Exception as e:
            print(f"""Error loading naistyles.csv. Make sure it is in the custom_nodes/ComfyUI-Universal-Styler/CSV directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return naifilters
    
    # part 3

    @staticmethod
    def load_naitypes_csv(naitypes_path: str):
        """Loads filtercsv file, Ignore the first row (header).
        Returns:
            list: List of naistyles. Each style is a dict with keys: style_name and value: [positive_prompt, negative_prompt]
        """
        naitypes = {"Error loading naistyles.csv, check the console": ["",""]}
        if not os.path.exists(naitypes_path):
            print(f"""Error. No naistyles.csv found. Put your naistyles.csv in the custom_nodes/ComfyUI-Universal-Styler/CSV directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return naitypes
        try:
            with open(naitypes_path, "r", encoding="utf-8") as f:    
                naitypes = [[x.replace('"', '').replace('\n','') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                naitypes = {x[0]: [x[1],x[2]] for x in naitypes}
        except Exception as e:
            print(f"""Error loading naistyles.csv. Make sure it is in the custom_nodes/ComfyUI-Universal-Styler/CSV directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return naitypes
        
    # Data
    
    @classmethod
    def INPUT_TYPES(cls):
        cls.naistyles_csv = cls.load_naistyles_csv(os.path.join(folder_paths.base_path, "custom_nodes\\ComfyUI-Universal-Styler\\CSV\\naifilters.csv"))
        cls.naifilters_csv = cls.load_naifilters_csv(os.path.join(folder_paths.base_path, "custom_nodes\\ComfyUI-Universal-Styler\\CSV\\naistyles.csv"))
        cls.naitypes_csv = cls.load_naitypes_csv(os.path.join(folder_paths.base_path, "custom_nodes\\ComfyUI-Universal-Styler\\CSV\\naitypes.csv"))
        return {
            "required": {
                #"mute": (["On", "Off"],),
                "naifilters": (list(cls.naistyles_csv.keys()),),
                "naistyles": (list(cls.naifilters_csv.keys()),),
                "naitypes": (list(cls.naitypes_csv.keys()),),
                #"clip": ("CLIP", ),
            },                      
        }

    RETURN_TYPES = ("STRING","STRING")
    RETURN_NAMES = ("Full prompt","Short prompt")
    FUNCTION = "execute"
    CATEGORY = "✴️ Universal NAI Nodes"   

    def execute(self, naistyles, naifilters, naitypes):
            return str(self.naistyles_csv[naistyles][0], self.naistyles_csv[naistyles][1],self.naifilters_csv[naifilters][0], self.naifilters_csv[naifilters][1],self.naitypes_csv[naitypes][0], self.naitypes_csv[naitypes][1],)

################
# NAI STYLER v0.1 ##########################################################################
################

class NaiStyler:
    """
    A new custom node
    """

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        """
            All param and values
        """
        return {
            "required": {
                "clip": ("CLIP", ),
                "mute": (["On", "Off"],),
                "mix": ("INT", {
                    "default": 50, 
                    "min": 0, 
                    "max": 100, 
                    "step": 1,
                    "display": "slider" #"number" or "slider"
                }),
                "float_field": ("FLOAT", {
                    "default": 0.5,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.01,
                    "round": 0.001,
                    "display": "slider"}),
                "string_field": ("STRING", {
                    "multiline": True,
                    "default": "Define Object"
                }),
                "string_field2": ("STRING", {
                    "multiline": True, 
                    "default": "Define Background"
                }), 
            },
        }

    RETURN_TYPES = ("CONDITIONING","STRING","STRING","INT")
    RETURN_NAMES = ("Compiled prompt","Value","Value2","mix")
    FUNCTION = "test"
    #OUTPUT_NODE = False
    CATEGORY = "✴️ Universal NAI Nodes"

    def test(self, string_field, string_field2, mix, float_field, mute):
        if mute == "On":
            print(f"""Your input contains:
                string_field aka input text: {string_field}
                int_field: {mix}
                float_field: {float_field}
            """)

################
# NAI concat v0.1 ##########################################################################
################

class ConcatenateFields:     

    @classmethod
    def INPUT_TYPES(cls):
               
        return {"required": {       
                    "text1": ("STRING", {"multiline": False, "default": "Hello"}),
                    "text2": ("STRING", {"multiline": False, "default": "World"}),
                    }
                }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "concatenate_text"
    CATEGORY = "✴️ Universal NAI Nodes"

    def concatenate_text(self, text1, text2):

        text_out = text1 + " " + text2
        
        return (text_out,)

################
# NODES MAPPING ##########################################################################
################

NODE_CLASS_MAPPINGS = {
    "ShowText|pysssss": ShowText,
    "Load Nai Styles Complex CSV": NaiStylerComplexCSVLoader,
    "Universal_Styler_Node": NaiStyler,
    "concat": ConcatenateFields,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "ShowText|pysssss": "✴️ U-NAI Get Text",
    "Load Nai Styles Complex CSV": "✴️ U-NAI Styles Launcher",
    "Universal_Styler_Node": "✴️ U-NAI Styler - v0.2.1",
    "concat": "✴️ U-NAI Fields Concatenate",
}
