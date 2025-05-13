import os
import re
import folder_paths

### SET MAIN CHANNEL NODE

class SetMainChannel:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "channel": ("STRING", {"default": "CH_0001", "multiline":False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("channel output",)
    FUNCTION = "set_mainchannel"
    CATEGORY = "🛡️ NAI Scripting Pipeline"

    def set_mainchannel(self, channel):
        return (channel,)


### SAVE SCRIPT NODE

class SaveScriptToDatabase:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt_title": ("STRING", {"default": "Scene_1/Motion_A/V1", "multiline":False}),
                "prompt_short": ("STRING", {"default": "short", "multiline":True}),
                "prompt_long": ("STRING", {"default": "long", "multiline":True}),
                "project_dir": ("STRING", {"default": "/outputs/project_name...", "multiline":False}),
            }
        }

    RETURN_TYPES = ("STRING","STRING","STRING","STRING",)
    RETURN_NAMES = ("prompt title", "short prompt", "long prompt", "project dir",)
    FUNCTION = "save_script"
    CATEGORY = "🛡️ NAI Scripting Pipeline"

    def save_script(self, prompt_title, prompt_short, prompt_long, project_dir):
        return (prompt_title,prompt_short,prompt_long,project_dir)


### LOAD SCIPTS NODE

class LoadScriptsFromDatabase:
    """
    Loads scripts from Database (csv file), and returns concatenated output string data.
    """
    
    # LOAD AGENTS FROM DATABASE

    @staticmethod
    def load_agents_csv(agents_path: str):
        """Loads AGENTS Database file (CSV). It has three columns. It Ignores the first row (header).
        Returns: List of scripts. Each script is a dict with keys: script_name and value: [short_script, long_script]
        """
        agents = {"Error loading agents.csv, check the console": ["",""]}

        # Verify folder !
        print(f"""YOUR FOLDER: {folder_paths.base_path}""")

        if not os.path.exists(agents_path):
            print(f"""Error. No agents.csv found. Add your own agents.csv in the custom_nodes/ComfyUI-Universal-Styler directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return agents
        try:
            with open(agents_path, "r", encoding="utf-8") as f:    
                agents = [[x.replace('"', '').replace('\n','') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                agents = {x[0]: [x[1],x[2]] for x in agents}
        except Exception as e:
            print(f"""Error loading agents.csv. Make sure it is located into the custom_nodes/ComfyUI-Universal-Styler directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return agents
    
    # LOAD SCENES FROM DATABASE

    @staticmethod
    def load_scenes_csv(scenes_path: str):
        """Loads SCENES Database file (CSV). It has three columns. It Ignores the first row (header).
        Returns: List of scripts. Each script is a dict with keys: script_name and value: [short_script, long_script]
        """
        scenes = {"Error loading scenes.csv, check the console": ["",""]}
        if not os.path.exists(scenes_path):
            print(f"""Error. No scenes.csv found. Add your own scenes.csv in the custom_nodes/ComfyUI-Universal-Styler directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return scenes
        try:
            with open(scenes_path, "r", encoding="utf-8") as f:    
                scenes = [[x.replace('"', '').replace('\n','') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                scenes = {x[0]: [x[1],x[2]] for x in scenes}
        except Exception as e:
            print(f"""Error loading scenes.csv. Make sure it is located into the custom_nodes/ComfyUI-Universal-Styler directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return scenes

    # LOAD MOTION FROM DATABASE
    
    @staticmethod
    def load_motions_csv(motions_path: str):
        """Loads MOTIONS Database file (CSV). It has three columns. It Ignores the first row (header).
        Returns: List of scripts. Each script is a dict with keys: script_name and value: [short_script, long_script]
        """
        motions = {"Error loading motions.csv, check the console": ["",""]}
        if not os.path.exists(motions_path):
            print(f"""Error. No motions.csv found. Add your own motions.csv in the custom_nodes/ComfyUI-Universal-Styler directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return motions
        try:
            with open(motions_path, "r", encoding="utf-8") as f:    
                motions = [[x.replace('"', '').replace('\n','') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                motions = {x[0]: [x[1],x[2]] for x in motions}
        except Exception as e:
            print(f"""Error loading motions.csv. Make sure it is located into the custom_nodes/ComfyUI-Universal-Styler directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return motions
    
    # LOAD LIGHTINGS FROM DATABASE
    
    @staticmethod
    def load_lightings_csv(lightings_path: str):
        """Loads LIGHTINGS Database file (CSV). It has three columns. It Ignores the first row (header).
        Returns: List of scripts. Each script is a dict with keys: script_name and value: [short_script, long_script]
        """
        lightings = {"Error loading lightings.csv, check the console": ["",""]}
        if not os.path.exists(lightings_path):
            print(f"""Error. No lightings.csv found. Add your own lightings.csv in the custom_nodes/ComfyUI-Universal-Styler directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return lightings
        try:
            with open(lightings_path, "r", encoding="utf-8") as f:    
                lightings = [[x.replace('"', '').replace('\n','') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                lightings = {x[0]: [x[1],x[2]] for x in lightings}
        except Exception as e:
            print(f"""Error loading lightings.csv. Make sure it is located into the custom_nodes/ComfyUI-Universal-Styler directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return lightings
    
    # LOAD STYLES FROM DATABASE
    
    @staticmethod
    def load_styles_csv(styles_path: str):
        """Loads STYLES Database file (CSV). It has three columns. It Ignores the first row (header).
        Returns: List of scripts. Each script is a dict with keys: script_name and value: [short_script, long_script]
        """
        styles = {"Error loading styles.csv, check the console": ["",""]}
        if not os.path.exists(styles_path):
            print(f"""Error. No styles.csv found. Add your own styles.csv in the custom_nodes/ComfyUI-Universal-Styler directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return styles
        try:
            with open(styles_path, "r", encoding="utf-8") as f:    
                styles = [[x.replace('"', '').replace('\n','') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                styles = {x[0]: [x[1],x[2]] for x in styles}
        except Exception as e:
            print(f"""Error loading styles.csv. Make sure it is located into the custom_nodes/ComfyUI-Universal-Styler directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return styles
    
    # LOAD CAMERAS FROM DATABASE
    
    @staticmethod
    def load_cameras_csv(cameras_path: str):
        """Loads CAMERAS Database file (CSV). It has three columns. It Ignores the first row (header).
        Returns: List of scripts. Each script is a dict with keys: script_name and value: [short_script, long_script]
        """
        cameras = {"Error loading cameras.csv, check the console": ["",""]}
        if not os.path.exists(cameras_path):
            print(f"""Error. No cameras.csv found. Add your own cameras.csv in the custom_nodes/ComfyUI-Universal-Styler directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return cameras
        try:
            with open(cameras_path, "r", encoding="utf-8") as f:    
                cameras = [[x.replace('"', '').replace('\n','') for x in re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)] for line in f.readlines()[1:]]
                cameras = {x[0]: [x[1],x[2]] for x in cameras}
        except Exception as e:
            print(f"""Error loading cameras.csv. Make sure it is located into the custom_nodes/ComfyUI-Universal-Styler directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return cameras
        
    # CUSTOM NODES SETUP
    
    @classmethod
    def INPUT_TYPES(cls):
        base = os.path.dirname(__file__)
        cls.agents_csv = cls.load_agents_csv(os.path.join(base, "SCRIPTS", "agents.csv"))
        cls.scenes_csv = cls.load_scenes_csv(os.path.join(base, "SCRIPTS", "scenes.csv"))
        cls.motions_csv = cls.load_motions_csv(os.path.join(base, "SCRIPTS", "motions.csv"))
        cls.lightings_csv = cls.load_lightings_csv(os.path.join(base, "SCRIPTS", "lightings.csv"))
        cls.styles_csv = cls.load_styles_csv(os.path.join(base, "SCRIPTS", "styles.csv"))
        cls.cameras_csv = cls.load_cameras_csv(os.path.join(base, "SCRIPTS", "cameras.csv"))
        return {
            "required": {
                "channel_input": ("STRING", {"forceInput": True}),
                "mode": (["normal", "extended", "solo agent output", "experimental"],),
                "agents": (list(cls.agents_csv.keys()),),
                "scenes": (list(cls.scenes_csv.keys()),),
                "script_prefix": ("STRING", {"multiline": False,"default": ""}),
                "cameras": (list(cls.cameras_csv.keys()),),
                "motions": (list(cls.motions_csv.keys()),),
                "styles": (list(cls.styles_csv.keys()),),
                "lightings": (list(cls.lightings_csv.keys()),),
                "channel_follow": ("STRING", {"multiline": False,"default": "#0001"}),
                "channel_encode": ("BOOLEAN", {"default": False}),
            },                
        }

    RETURN_TYPES = ("STRING","STRING",)
    RETURN_NAMES = ("channel output", "script output",)
    FUNCTION = "load_scripts"
    CATEGORY = "🛡️ NAI Scripting Pipeline"   

    def load_scripts(self, script_prefix, channel_input, mode, agents, styles, motions, cameras, lightings, scenes, channel_follow, channel_encode):
            short_compiled_prompt = script_prefix + "" + self.agents_csv[agents][0] + "" + self.motions_csv[motions][0]+ "" + self.cameras_csv[cameras][0] + "" + self.scenes_csv[scenes][0]+ "" + self.styles_csv[styles][0]+ "" + self.lightings_csv[lightings][0]
            
            long_compiled_prompt = script_prefix + "" + self.agents_csv[agents][1] + "" + self.motions_csv[motions][1] + "" + self.cameras_csv[cameras][1]+ "" + self.scenes_csv[scenes][1]+ "" + self.styles_csv[styles][1]+ "" + self.lightings_csv[lightings][1]

            channel_concat = channel_input + "/" + channel_follow

            compiled_prompt_moded = channel_concat + "/ SCE/ " + self.scenes_csv[scenes][0]+ "/ MOT/ " + self.motions_csv[motions][0]+ "/ CAM/ " + self.cameras_csv[cameras][0]+ "/ AGT/ " + self.agents_csv[agents][0]+ "/ STL/ " + self.styles_csv[styles][0]+ "/ LGT/ " + self.lightings_csv[lightings][0]

            solo_agent_script = "AGENT: " +self.agents_csv[agents][0] + "/DETAILS: " + self.agents_csv[agents][1]
            
            if channel_encode == True:
                if mode == "normal":
                    return (channel_concat, short_compiled_prompt)
                elif mode == "extended":
                    return (channel_concat, long_compiled_prompt)
                elif mode == "experimental":
                    return (channel_concat, compiled_prompt_moded)
                elif mode == "solo agent output":
                    return (channel_concat, solo_agent_script)
            else:
                if mode == "normal":
                    return (channel_follow, short_compiled_prompt)
                elif mode == "extended":
                    return (channel_follow, long_compiled_prompt)
                elif mode == "experimental":
                    return (channel_follow, compiled_prompt_moded)
                elif mode == "solo agent output":
                    return (channel_follow, solo_agent_script)
            

# REQUIRED

NODE_CLASS_MAPPINGS = {
    "🛡️ Set Main Channel": SetMainChannel,
    "🛡️ Load Scripts from Database": LoadScriptsFromDatabase,
    "🛡️ Save Script to Database (In progress)": SaveScriptToDatabase,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SetMainChannel": "Set Main Channel",
    "LoadScriptsFromDatabase": "Load Scripts from Database",
    "SaveScriptToDatabase": "Save Script to Database",
}
