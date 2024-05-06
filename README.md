# ComfyUI Universal Styler
 
A research Node based on *Artificial Intelligence* for ComfyUI[^1], this is a multi-steps development project, with **SD Local System**[^2] focus in mind. This script/custom node is intended to serve the purpose to *generate unique images and video sequences*, within **ComfyUI Editor** and based on Public Checkpoint Models[^3] OR/AND **Private custom Models and LoRas**[^4]. It includes an integrated learning machine process as well as a workflows exporter script.

<img src="https://img.shields.io/badge/Comfy-UI-c11b3f" /> <img src="https://img.shields.io/badge/Windows-11-purple" /> <img src="https://img.shields.io/badge/Python-3.10-blue" /> <img src="https://img.shields.io/badge/Kore-Technology-yellow" /> <img src="https://img.shields.io/badge/CAN-X.1567D-949565" />

```diff
!!! This documentation is in progress !!!
the code release will be uploaded as soon as the complete package is ready, stay tuned...
```

## :radio_button: Acknowledgments

```py
NOTE: 
Release: 0.2.1 - Licensed under GNU General Public License v3.0
```

*"I decided to re-write some custom nodes for several reasons. The first was to keep my workflow as fast s possible. The second was that the interface deserved to be redesigned to integrate into my actual workflow. The third was that I wanted to add functions for animation and the video sequencer. And the last because I haven't found yet a way to get in touch with other developers and offer my collaboration."* :raising_hand:

---

## :radio_button: Objectives

The objectives of this project are to offer different digital creation tools, using Blender as the main platform and only in local environment. At a time when Blender 4x is in the process of being officially released, the main goal is to deliver this addon as soon as this new version of our favorite software is released. Here is a non-exhaustive list of planned features:

- **Create images from prompts (background image, textures, hdri, titles)**
- **Create images from images (styles, tones, themes)**
- **Create 3D Models from images (DMTet integration)**
- **Create texts from prompts (subtitles)**
- **Create images sequences from prompts/images (video strips, animations)**
- **Create audio strips from prompts/images (voices, music themes)**

---





<img alt="preview_v135" src="/media/addon_preview_v125.png">

---

## :radio_button: ComfyUI Installation and Modules

After installing [**ComfyUI**](https://github.com/comfyanonymous/ComfyUI) services with your prefered plateform (i am suggesting the use of [**Stability Matrix**](https://github.com/LykosAI/StabilityMatrix) as it is easy to install for beginners), make sure you install the additional modules. Then you need to install [GIT software](https://git-scm.com/) (if it is not done already) on your computer. To install these modules, open a CMD window in the \ComfyUI\custom_nodes folder. And "git clone" each one of them. By adding the link after "git clone".

- [ComfyUi-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
- [ComfyUI-Impact](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
- [ComfyUI-Inspire](https://github.com/ltdrdata/ComfyUI-Inspire-Pack)
- [WAS Nodes Suite](https://github.com/WASasquatch/was-node-suite-comfyui)
- [Animate Diff](https://github.com/ArtVentureX/comfyui-animatediff)
- [Prompt-Expansion](https://github.com/meap158/ComfyUI-Prompt-Expansion)
- [Derfuu-ComfyUI_ModdedNodes](https://github.com/Derfuu/Derfuu_ComfyUI_ModdedNodes)

---

## :radio_button: Presets, Templates and Snippets

The addon offers 2 types of presets, full nodetrees and node groups. When the user saves a preet, it is automatically kept in specific folders. This allows, among other things, to share your “workflows” or nodetrees with other users. Here is the list of presets provided in this addon and their usage:

- **Basic setups**
  - Simple text-2-image
  - Advanced text-2-image
  - Simple image-2-image
  - Advanced image-2-image
- **Advanced setups**
  - LoRas Merging
  - VAEs Merging
  - Complex text-2-image
  - Complex image-2-image
- **Animation setups**
  - Basic images Sequence
  - Advanced images sequence
- **Film making setups**
  - VFX movie (Inpaint)

---

## :radio_button: Learning from users, training from experience

Objectives: Collecting user data and processing it locally allows you to create personalized artistic and technical models, ready to be used in a new nodetree.
- Many options: Structural, Lineal, Hierachical...
- Json files storage path


<table>
<tr>
<th align="center", width="100%">Data Types</th>
</tr>
</table>

<ul>
      <li><b>Actions History</b>
        <ul>
          <li>What is the last action done by a specific user?</li>
          <li>What is the most repeating actions?</li>
        </ul>
      </li>
      <li><b>Space Orbits</b>
        <ul>
          <li>What is the mid distance from the object origin in edit mode?</li>
          <li>What is the mid distance of action from the world origin?</li>
        </ul>
      </li>
      <li><b>Time Sequences</b>
        <ul>
          <li>What is the mid time between same actions?</li>
          <li>What is the time between same files edition?</li>
        </ul>
  </li>
      <li><b>User Types</b>
        <ul>
          <li>What is the skills level of a specific user?</li>
          <li>What is the most needed skill by user type</li>
        </ul>
      </li>
       <li><b>user Project Types</b>
        <ul>
          <li>What is the project types? Architecture, Industrial Design, etc...</li>
          <li>What is graphical type associated with the project? Realistic scene, cartoon, etc...</li>
        </ul>
      </li>
</ul>

---

## :radio_button: LLM Structure

The addon has 3 modes: Analyse/Prepare/Write, external file from session start.

- ANALYSE: write an external file
- PREPARE: images data
- WRITE: .ckpt/tensors

```diff
- NOTE: ...
```


<table>
<tr>
<th align="center", width="880">Data Processing</th>
</tr>
</table>

<ul>
      <li><b>Real-time Support</b>
        <ul>
          <li>Suggest a serie of optional processes and combos</li>
          <li>Suggest a serie of optional Shortcuts</li>
          <li>Suggest a serie of optional parametric objects</li>
          <li>Suggest a serie of optional Texturing processes</li>
        </ul>
      </li>
      <li><b>Real-time Auto-Correct</b>
        <ul>
          <li>Show errors based on 3 main error types*</li>
        </ul>
      </li>
</ul>

<table>
<tr>
<th align="center", width="880">Data Backend</th>
</tr>
</table>

<ul>
      <li><b>Local Files</b>
        <ul>
          <li>Write data as text file (txt, Json, Xml)</li>
          <li>Write data as new file (.bai) aka csv alternate</li>
        </ul>
      </li>
  <li><b>Temporary Files</b>
        <ul>
          <li>Realize 3 reality states A-X-B (data morphing)</li>
          <li>Compare 2 states A/B</li>
        </ul>
      </li>
</ul>

---

## :radio_button: Infos

* Author: **Uriel Deveaud** - [Kore Teknology](https://github.com/KoreTeknology) 
* License: This project is released under the GPL License.
* This work is dedicated to all ComfyUI users around the world ;)

[^1]: **ComfyUI** is the free and open source 3D creation suite. It supports Stable Diffusion 1.5, 2. XL. Please, visit the [ComfyUI Github age](https://github.com/comfyanonymous/ComfyUI).

[^2]: Large language models (LLM) are very large deep learning models that are pre-trained on vast amounts of data. The underlying transformer is a set of neural networks that consist of an encoder and a decoder with self-attention capabilities.
