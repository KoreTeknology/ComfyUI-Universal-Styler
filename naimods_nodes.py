import os
import re
import folder_paths

#NAIPROMPTER ##########################################################################

class NaiPrompter:
    """
    multi selection prompter
    """
    @staticmethod
    def load_naiprompter_csv(naiprompter_path: str):
        """Loads prompt csv file, Ignore the first row (header).
        Returns:
            list: List of naimods. Each style is a dict with keys: style_name and value: [positive_prompt, negative_prompt]
        """
        naiprompter = {"Error loading nai_prompter, check the console": ["",""]}
        if not os.path.exists(naiprompter_path):
            print(f"""Error. No nai_prompter found. Put your nai_prompter.csv in the custom_nodes/ComfyUI_NAI-mod/CSV directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return naiprompter
        try:
            with open(naiprompter_path, "r", encoding="utf-8") as f:    
                naiprompter = [[x.replace('"', '').replace('\n','') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                naiprompter = {x[0]: [x[1],x[2]] for x in naiprompter}
        except Exception as e:
            print(f"""Error loading nai_prompter.csv. Make sure it is in the custom_nodes/ComfyUI_NAI-mod/CSV directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return naiprompter
        
    @classmethod
    def INPUT_TYPES(cls):
        cls.naiprompter_csv = cls.load_naiprompter_csv(os.path.join(folder_paths.base_path, "custom_nodes\\ComfyUI-NAI-mod\\CSV\\nai_prompter.csv"))
        return {
            "required": {
                "option1": (list(cls.naiprompter_csv.keys()),),
            },
                                
        }

    RETURN_TYPES = ("STRING")
    OUTPUT_IS_LIST = (True,)
    RETURN_NAMES = ("positive prompt")
    FUNCTION = "execute_prompt"
    CATEGORY = "👹 Universal Nodes2"   

    def execute_prompt(self, naiprompter):
            return (self.naiprompter_csv[naiprompter][0], self.naiprompter_csv[naiprompter][1],)




#NAIMODS ##########################################################################

class NaimodsCSVLoader:
    """
    Loads csv file with Naimods.
    """
    
    @staticmethod
    def load_naimods_csv(naimods_path: str):
        """Loads csv file, Ignore the first row (header).
        Returns:
            list: List of naimods. Each style is a dict with keys: style_name and value: [positive_prompt, negative_prompt]
        """
        naimods = {"Error loading naimods.csv, check the console": ["",""]}
        if not os.path.exists(naimods_path):
            print(f"""Error. No naimods.csv found. Put your naimods.csv in the custom_nodes/ComfyUI_NAI-mod/CSV directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return naimods
        try:
            with open(naimods_path, "r", encoding="utf-8") as f:    
                naimods = [[x.replace('"', '').replace('\n','') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                naimods = {x[0]: [x[1],x[2]] for x in naimods}
        except Exception as e:
            print(f"""Error loading naimods.csv. Make sure it is in the custom_nodes/ComfyUI_NAI-mod/CSV directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return naimods
        
    @classmethod
    def INPUT_TYPES(cls):
        cls.naimods_csv = cls.load_naimods_csv(os.path.join(folder_paths.base_path, "custom_nodes\\ComfyUI-NAI-mod\\CSV\\naimods.csv"))
        return {
            "required": {
                "Styles": (list(cls.naimods_csv.keys()),),
                "Intensity": ("INT", {
                    "default": 50, 
                    "min": 0, #Minimum value
                    "max": 100, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
            },
                                
        }

    RETURN_TYPES = ("STRING","STRING","STRING")
    RETURN_NAMES = ("positive prompt", "negative prompt", "Agent")
    FUNCTION = "execute"
    CATEGORY = "👹 Universal Nodes"   

    def execute(self, naimods):
            return (self.naimods_csv[naimods][0], self.naimods_csv[naimods][1], self.naimods_csv[naimods][2],)


#my panel ##########################################################################

class MyPanel:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
        """
        return {
            "required": {
                "string_field3": ("STRING", {
                    "multiline": True,
                    "default": "Type any text"
                }), 
            },
        }

    RETURN_TYPES = ("STRING",)
    #RETURN_NAMES = ("String",)
    FUNCTION = "test2"
    #OUTPUT_NODE = False
    CATEGORY = "👹 Universal Nodes"

    def test2(self, string_field3, print_to_screen):
        if print_to_screen == "enable":
            print(f"""Your input contains:
                string_field aka input text: {string_field3}
            """)
        #do some processing on the image, in this example I just invert it

#exemple ##########################################################################

class Example:
    """
    A example node

    Class methods
    -------------
    INPUT_TYPES (dict): 
        Tell the main program input parameters of nodes.
    IS_CHANGED:
        optional method to control when the node is re executed.

    Attributes
    ----------
    RETURN_TYPES (`tuple`): 
        The type of each element in the output tulple.
    RETURN_NAMES (`tuple`):
        Optional: The name of each output in the output tulple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            The type can be a list for selection.

            Returns: `dict`:
                - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
                - Value input_fields (`dict`): Contains input fields config:
                    * Key field_name (`string`): Name of a entry-point method's argument
                    * Value field_config (`tuple`):
                        + First value is a string indicate the type of field or a list for selection.
                        + Secound value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {
            "required": {
                "clip": ("CLIP", ),
                "image": ("IMAGE",),
                "int_field": ("INT", {
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
                "print_to_screen": (["enable", "disable"],),
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

    RETURN_TYPES = ("IMAGE","STRING","STRING","CONDITIONING",)
    RETURN_NAMES = ("image_output_name","Value","Value2","Positive Prompt")

    FUNCTION = "test"

    #OUTPUT_NODE = False

    CATEGORY = "👹 Universal Nodes"

    def test(self, image, string_field, string_field2, int_field, float_field, print_to_screen):
        if print_to_screen == "enable":
            print(f"""Your input contains:
                string_field aka input text: {string_field}
                int_field: {int_field}
                float_field: {float_field}
            """)
        #do some processing on the image, in this example I just invert it
        image = 1.0 - image
        return (image,)

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

#show text ##########################################################################

class MyShowText:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
                "text2": ("STRING", {
                    "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": "Define Agent..."
                }),
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
    CATEGORY = "👹 Universal Nodes"

    def notify(self, text, string_field4, unique_id=None, extra_pnginfo=None):
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


#NODE NAMING ##########################################################################

NODE_CLASS_MAPPINGS = {
    "Nai Prompter": NaiPrompter,
    "Load Nai Mods CSV": NaimodsCSVLoader,
    "Universal_NS1": Example,
    "Universal_NS2": MyPanel,
    "ShowText|Nai Mod": MyShowText,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "Nai Prompter": "☢️ NAI: Prompter",
    "Load Nai Mods CSV": "☢️ NAI: Styler",
    "Universal_NS1": "☢️ NAI:My Panel 1",
    "Universal_NS2": "☢️ NAI:My Panel 2",
    "ShowText|Nai Mod": "☢️ NAI: Show Text",
}