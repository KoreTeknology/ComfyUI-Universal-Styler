import os
import re
import folder_paths

#NAIMODS ##########################################################################

class NaiStylerCSVLoader:
    """
    Loads Stylescsv file
    """
    
    @staticmethod
    def load_naistyles_csv(naistyles_path: str):
        """Loads csv file, Ignore the first row (header).
        Returns:
            list: List of naistyles. Each style is a dict with keys: style_name and value: [positive_prompt, negative_prompt]
        """
        naistyles = {"Error loading naimods.csv, check the console": ["",""]}
        if not os.path.exists(naistyles_path):
            print(f"""Error. No naimods.csv found. Put your naimods.csv in the custom_nodes/ComfyUI_NAI-mod/CSV directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return naistyles
        try:
            with open(naistyles_path, "r", encoding="utf-8") as f:    
                naistyles = [[x.replace('"', '').replace('\n','') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                naistyles = {x[0]: [x[1],x[2]] for x in naistyles}
        except Exception as e:
            print(f"""Error loading naimods.csv. Make sure it is in the custom_nodes/ComfyUI_NAI-mod/CSV directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return naistyles
        
    @classmethod
    def INPUT_TYPES(cls):
        cls.naistyles_csv = cls.load_naistyles_csv(os.path.join(folder_paths.base_path, "custom_nodes\\ComfyUI-NAI-styler\\CSV\\naistyles.csv"))
        return {
            "required": {
                "Styles": (list(cls.naistyles_csv.keys()),),
            },                      
        }

    RETURN_TYPES = ("STRING","STRING")
    RETURN_NAMES = ("Full prompt", "Short prompt")
    FUNCTION = "execute"
    CATEGORY = "✴️ Universal NAI Nodes"   

    def execute(self, naistyles):
            return (self.naistyles_csv[naistyles][0], self.naistyles_csv[naistyles][1],)


#exemple ##########################################################################

class Full:
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
                "mix": ("INT", {
                    "default": 50, 
                    "min": 0, #Minimum value
                    "max": 100, #Maximum value
                    "step": 1, #Slider's step
                    "display": "slider" # Cosmetic only: display as "number" or "slider"
                }),
                "float_field": ("FLOAT", {
                    "default": 0.5,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.01,
                    "round": 0.001, #The value represeting the precision to round to, will be set to the step value by default. Can be set to False to disable rounding.
                    "display": "number"}),
                "mute": (["On", "Off"],),
                "string_field": ("STRING", {
                    "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "Define Agent..."
                }),
                "string_field2": ("STRING", {
                    "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "Define Agent2..."
                }), 
                #"clip": ("CLIP", ),
            },
        }

    RETURN_TYPES = ("STRING","STRING","CONDITIONING","INT")
    RETURN_NAMES = ("Value","Value2","Positive Prompt","mix")

    FUNCTION = "test"

    #OUTPUT_NODE = False

    CATEGORY = "✴️ Universal NAI Nodes"

    def test(self, string_field, string_field2, mix, float_field, mute):
        if print_to_screen == "On":
            print(f"""Your input contains:
                string_field aka input text: {string_field}
                int_field: {int_field}
                float_field: {float_field}
            """)

    """
        The node will always be re executed if any of the inputs change but
        this method can be used to force the node to execute again even when the inputs don't change.
        You can make this node return a number or a string. This value will be compared to the one returned the last time the node was
        executed, if it is different the node will be executed again.
        This method is used in the core repo for the LoadImage node where they return the image hash as a string, if the image hash
        changes between executions the LoadImage node is executed again.
    """
    #@classmethod
    #def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):
    #    return ""



#NODE NAMING ##########################################################################

NODE_CLASS_MAPPINGS = {
    "Load Nai Styles CSV": NaiStylerCSVLoader,
    "Universal_Styler_Node": Full,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "Load Nai Styles CSV": "✴️ NAI: STYLER +",
    "Universal_Styler_Node": "✴️ NAI: FULL NODE",
}