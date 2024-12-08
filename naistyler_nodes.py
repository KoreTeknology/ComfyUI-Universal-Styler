import re
from pathlib import Path

BASE_DIR = Path.cwd()
DATAPATH = BASE_DIR / "custom_nodes" / "ComfyUI-Universal-Styler" / "CSV"

################
# NAI Show text v0.3 ##########################################################################
################


class ShowText:
    @classmethod
    def INPUT_TYPES(cls):
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

    @staticmethod
    def load_naistyles_csv(naistyles_path: Path):
        """Loads csv file, Ignore the first row (header).
        Returns:
            dict: List of naistyles. Each style is a dict with keys: style_name and value: [positive_prompt, negative_prompt]
        """
        naistyles = {"Error loading naistyles.csv, check the console": ["", ""]}
        if not naistyles_path.exists():
            print(
                f"""Error. No naistyles.csv found. Put your naistyles.csv in the custom_nodes/ComfyUI-Universal-Styler/CSV directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {Path.cwd()}
            """
            )
            return naistyles
        try:
            with naistyles_path.open("r", encoding="utf-8") as f:
                naistyles = [
                    [
                        x.replace('"', "").replace("\n", "")
                        for x in re.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
                    ]
                    for line in f.readlines()[1:]
                ]
                naistyles = {x[0]: [x[1], x[2]] for x in naistyles}
        except Exception as e:
            print(
                f"""Error loading naistyles.csv. Make sure it is in the custom_nodes/ComfyUI-Universal-Styler/CSV directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {Path.cwd()}
                    Error: {e}
            """
            )
        return naistyles

    @staticmethod
    def load_naifilters_csv(naifilters_path: Path):
        """Loads filter csv file, Ignore the first row (header).
        Returns:
            dict: List of naistyles. Each style is a dict with keys: style_name and value: [positive_prompt, negative_prompt]
        """
        naifilters = {"Error loading naistyles.csv, check the console": ["", ""]}
        if not naifilters_path.exists():
            print(
                f"""Error. No naistyles.csv found. Put your naistyles.csv in the custom_nodes/ComfyUI-Universal-Styler/CSV directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {Path.cwd()}
            """
            )
            return naifilters
        try:
            with naifilters_path.open("r", encoding="utf-8") as f:
                naifilters = [
                    [
                        x.replace('"', "").replace("\n", "")
                        for x in re.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
                    ]
                    for line in f.readlines()[1:]
                ]
                naifilters = {x[0]: [x[1], x[2]] for x in naifilters}
        except Exception as e:
            print(
                f"""Error loading naistyles.csv. Make sure it is in the custom_nodes/ComfyUI-Universal-Styler/CSV directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {Path.cwd()}
                    Error: {e}
            """
            )
        return naifilters

    @staticmethod
    def load_naitypes_csv(naitypes_path: Path):
        """Loads types csv file, Ignore the first row (header).
        Returns:
            dict: List of naistyles. Each style is a dict with keys: style_name and value: [positive_prompt, negative_prompt]
        """
        naitypes = {"Error loading naistyles.csv, check the console": ["", ""]}
        if not naitypes_path.exists():
            print(
                f"""Error. No naistyles.csv found. Put your naistyles.csv in the custom_nodes/ComfyUI-Universal-Styler/CSV directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {Path.cwd()}
            """
            )
            return naitypes
        try:
            with naitypes_path.open("r", encoding="utf-8") as f:
                naitypes = [
                    [
                        x.replace('"', "").replace("\n", "")
                        for x in re.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
                    ]
                    for line in f.readlines()[1:]
                ]
                naitypes = {x[0]: [x[1], x[2]] for x in naitypes}
        except Exception as e:
            print(
                f"""Error loading naistyles.csv. Make sure it is in the custom_nodes/ComfyUI-Universal-Styler/CSV directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {Path.cwd()}
                    Error: {e}
            """
            )
        return naitypes

    @classmethod
    def INPUT_TYPES(cls):
        cls.naistyles_csv = cls.load_naistyles_csv(DATAPATH / "naistyles.csv")
        cls.naifilters_csv = cls.load_naifilters_csv(DATAPATH / "naifilters.csv")
        cls.naitypes_csv = cls.load_naitypes_csv(DATAPATH / "naitypes.csv")
        return {
            "required": {
                "naifilters": (list(cls.naistyles_csv.keys()),),
                "naistyles": (list(cls.naifilters_csv.keys()),),
                "naitypes": (list(cls.naitypes_csv.keys()),),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("Full prompt", "Short prompt")
    FUNCTION = "execute"
    CATEGORY = "✴️ Universal NAI Nodes"

    def execute(self, naistyles, naifilters, naitypes):
        return (
            self.naistyles_csv[naistyles][0],
            self.naistyles_csv[naistyles][1],
            self.naifilters_csv[naifilters][0],
            self.naifilters_csv[naifilters][1],
            self.naitypes_csv[naitypes][0],
            self.naitypes_csv[naitypes][1],
        )


################
# Other Nodes ##########################################################################
################

# Include unchanged node classes like `ConcatenateFields` and `ShowText`

################
# NODES MAPPING ##########################################################################
################

NODE_CLASS_MAPPINGS = {
    "ShowText|pysssss": ShowText,
    "Load Nai Styles Complex CSV": NaiStylerComplexCSVLoader,
    # Add other mappings here
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ShowText|pysssss": "✴️ U-NAI Get Text",
    "Load Nai Styles Complex CSV": "✴️ U-NAI Styles Launcher",
    # Add other display name mappings here
}
