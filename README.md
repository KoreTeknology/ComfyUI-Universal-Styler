# ComfyUI Universal Styler
```py
VERSION: Pre-Alpha Release: 0.2.1 - Licensed under GNU General Public License v3.0
```
Hi, this is my first try with comfyUI custom nodes. It is a research Node based project on *Artificial Intelligence* using ComfyUI[^1] visual editor with **Stable diffusion Local processing**[^2] focus in mind. This custom node is intended to serve the purpose to *offer a large palette of prompting scenrarios*, based on Public Checkpoint Models[^3] OR/AND **Private custom Models and LoRas**[^4]. It includes an integrated learning machine process as well as a set of workflows.

<img src="https://img.shields.io/badge/ComfyUI-0.2.3+-c11b3f" /> <img src="https://img.shields.io/badge/Stable Diffusion-XL/2.0/1.5-c9c9c9" /> <img src="https://img.shields.io/badge/Windows-11-purple" /> <img src="https://img.shields.io/badge/Python-3.10-blue" /> <img src="https://img.shields.io/badge/CAN-X.1567D-949565" />

```diff
!!! This project and its documentation are (always) in progress !!! stay tuned...
- You may find some errors, please report the issue in the dedicated section, thx
```


<img alt="mockup" src="/MEDIA/screen_node_02.png">

## :radio_button: Working Features

- **Load prompt presets from CSV personal database**
- **Prompt sequences concatenate**
- **Object and background contextual edition**
- **Clip input, Condition output + Extras**

## :radio_button: Features Under Development

- NODE A
  - **Select database folder path in front-end**
  - **Single database column per category**
  - **All Fields concatenate**
  - **Seed INT Field with output connector**
- NODE B
  - **Model image-2-text to include**
  - **Metadata read/write**

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

[^1]: **ComfyUI** is the free and open source AI creation suite. It supports Stable Diffusion 1.5, 2. XL. Please, visit the [ComfyUI Github age](https://github.com/comfyanonymous/ComfyUI).

[^2]: Large language models (LLM) are very large deep learning models that are pre-trained on vast amounts of data. The underlying transformer is a set of neural networks that consist of an encoder and a decoder with self-attention capabilities.

[^3]: Public Checkpoint Models

[^4]: Private custom Models and LoRas
