# ASCII-Art-VLM: Enhancing LLM Comprehension of ASCII Art via Vision-Language Models  

This repository implements an inference-time system to improve Large Language Model (LLM) understanding of ASCII art by leveraging Vision-Language Models (VLMs). The pipeline:  
1. **Detects** ASCII art in text inputs.  
2. **Converts** it into an image.  
3. **Routes** the image through a VLM (e.g., GPT-4V) for captioning.  
4. **Injects** the caption back into the LLM prompt for enhanced comprehension.  

## Key Features  
- **No LLM retraining**—works with pretrained models (tested on GPT-4).  
- **ASCII-to-image conversion** for VLM processing.  
- **Benchmarked performance** against text-only baselines.  

## Installation  
```bash
pip install -r requirements.txt  # Includes Pillow, OpenCV, and VLM APIs
