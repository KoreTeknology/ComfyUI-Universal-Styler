# ComfyUI Universal Styler
```py
VERSION: Release 0.5.1 - UPDATED 02/2025 - Licensed under GNU General Public License v3.0
```
Hi, this is a research Node based project on *Artificial Intelligence* using ComfyUI[^1] visual editor with **VRAM Local processing**[^2] focus in mind. This set of custom node is intended to *offer a large palette of prompting scenrarios*, based on your scripting database[^3]. This package also includes a set of workflows[^4], associated with each feature and a database template folder. This last set of files can be replaced by your own CSV files. Feel free to accomodate and customize this template for each project.

<img src="https://img.shields.io/badge/ComfyUI-0.2.3+-c11b3f" /> <img src="https://img.shields.io/badge/Image-Video-c9c9c9" /> <img src="https://img.shields.io/badge/Windows-11-purple" /> <img src="https://img.shields.io/badge/Python-3.10-blue" /> <img src="https://img.shields.io/badge/CAN-X.1567D-949565" />

> [!IMPORTANT]
> THIS PACKAGE WAS FULLY REBUILD AFTER VERSION 0.5, OLD NODES MAY NOT WORK ON YOUR OLD WORKFLOW!
>> To avoid errors, remplace old nodes by the last version from the main node menu.

<img alt="mockup" src="/MEDIA/screen_node_02.png">

## :radio_button: Working Features

- **Load prompt presets from CSV database** (Scene, ccamera, motion, light, as well as negative and agent)
- **Prompt sequences compile (concatenate)** (Various options available)
- **Contextual agents included** (Dedicated Agents database file)
- **Channel drive (Chain-follow)** (Full references register)
- **Prompt build setup** Database model card available as a node

## :radio_button: Features Under Development

- NODE A
  - **Select database folder path in front-end**
  - **Seed INT Field with output connector**
- NODE B
  - **Metadata read/write**
  - Save database new item

---

## :radio_button: Objectives

The objectives of this project are to offer different digital creation tools, using ComfyUI as the main platform and only in local environment. Here is a non-exhaustive list of planned features:

- **Image Nai-Filter (parametric)**
- **Image Nai-Tonemapper (parametric)**
- **Image Nai-transformer overlayer**
- **Image 2 text (prompt, neg, metadata)**
- **Text Nai-Prompter load/concat csv**

utils:

- Text 2 string (with preview)
- String 2 text
- load image +
- compare slider preview images
- metadata constructor

---

## :radio_button: ComfyUI Installation and Custom Nodes

After installing [**ComfyUI**](https://github.com/comfyanonymous/ComfyUI) services with your prefered plateform (i am suggesting the use of [**Stability Matrix**](https://github.com/LykosAI/StabilityMatrix) as it is easy to install and give a lot of controls), make sure you install the additional and necessary custom nodes. Then you need to install [GIT software](https://git-scm.com/) (if it is not done already) on your computer. To install these custom nodes, open a CMD window in the \ComfyUI\custom_nodes folder. And "git clone" each one of them. By adding the link after "git clone".

- [ComfyUi-Manager](https://github.com/ltdrdata/ComfyUI-Manager)

---

## :radio_button: Infos

* Author: **Uriel Deveaud** - [Kore Teknology](https://github.com/KoreTeknology) 
* License: This project is released under the GPL License.
* This work is dedicated to all ComfyUI users around the world ;)

[^1]: **ComfyUI** is the free and open source AI creation suite. It supports Stable Diffusion 1.5, 2. XL, Flux and video models LTXV, hunhyan, Mochi. Please, visit the [ComfyUI Github page](https://github.com/comfyanonymous/ComfyUI).

[^2]: Large language models (LLM) are very large deep learning models that are pre-trained on vast amounts of data. The underlying transformer is a set of neural networks that consist of an encoder and a decoder with self-attention capabilities.

[^3]: A scripting database can be compared to a storyboard

[^4]: The provided workflows offer the basic festures thry a simple pipeline design
