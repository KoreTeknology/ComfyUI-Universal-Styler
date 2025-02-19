# ComfyUI Universal Styler
```py
VERSION: Release 0.5.1 - UPDATED 02/2025 - Licensed under GNU General Public License v3.0
```
Hi, this is a research Node based project on *Artificial Intelligence* using ComfyUI[^1] visual editor with **VRAM Local processing**[^2] focus in mind. This set of custom node is intended to *offer a large palette of prompting scenrarios*, based on your scripting database[^3]. This package also includes a set of workflows[^4], associated with each feature and a database template folder. This last set of files can be replaced by your own CSV files. It will works fine with image and video models like Stable diffusion and LTXV checkpoints. Feel free to accomodate and customize this template for each project.

<img src="https://img.shields.io/badge/ComfyUI-0.3.14+-c11b3f" /> <img src="https://img.shields.io/badge/Image-Video-c9c9c9" /> <img src="https://img.shields.io/badge/Windows-11-purple" /> <img src="https://img.shields.io/badge/Python-3.10-blue" /> <img src="https://img.shields.io/badge/CAN-X.1567D-949565" />

> [!IMPORTANT]
>>> THIS PACKAGE WAS FULLY REBUILD AFTER VERSION 0.5,
>> OLD NODES MAY NOT WORK AS EXPECTED IN YOUR OLD WORKFLOWS! To avoid errors, remplace old nodes by the latest version from the main node menu.

<img alt="mockup" src="/MEDIA/screen_node_03.png">

## :radio_button: Working Features

- **Load script presets from CSV database** (Scene, Camera, Motion, Lighting, Style)
- **Contextual agents included** (Dedicated Agents database file)
- **Prompt sequences compiler (concatenate)** (Optional Prefix, Various options available)
- **Channel drive (Chain-follow)** (Full references register)
- **Prompt build setup** Database model card available as a node

## :radio_button: Features Under Development

- **NEW set of script templates!**
- **Select database folder path in front-end & Update**
- **Seed INT Field with output connector**
- **Metadata read/write**
- Save database new item (same as save text node + options)

---

## :radio_button: ComfyUI Installation and Custom Nodes

After installing [**ComfyUI**](https://github.com/comfyanonymous/ComfyUI) services with your prefered plateform (i am suggesting the use of [**Stability Matrix**](https://github.com/LykosAI/StabilityMatrix) as it is easy to install and give a lot of controls), make sure you install the additional and necessary custom nodes. Then you need to install [GIT software](https://git-scm.com/) (if it is not done already) on your computer. To install these custom nodes, open a CMD window in the \ComfyUI\custom_nodes folder. And "git clone" each one of them. By adding the link after "git clone".

- [ComfyUi-Manager](https://github.com/ltdrdata/ComfyUI-Manager)

---

## :radio_button: Infos

* Author: **Uriel Deveaud** - [Kore Teknology](https://github.com/KoreTeknology)
* Contact: [Linkedin ComfyUI Users Group](https://www.linkedin.com/groups/13109092/)
* License: This project is released under the GPL License.
* This work is dedicated to all ComfyUI users around the world ;)

[^1]: **ComfyUI** is the free and open source AI creation suite. It supports Stable Diffusion 1.5, 2. XL, Flux and video models LTXV, hunhyan, Mochi. Please, visit the [ComfyUI Github page](https://github.com/comfyanonymous/ComfyUI).

[^2]: Large language models (LLM) are very large deep learning models that are pre-trained on vast amounts of data. The underlying transformer is a set of neural networks that consist of an encoder and a decoder with self-attention capabilities.

[^3]: A scripting database can be compared to a storyboard

[^4]: The provided workflows offer the basic festures thry a simple pipeline design
