# Plate Detector

This repository contains a Python program capable of detecting most vehicle plates from Jalisco, Mexico.

## Requirements

Make sure you have [Python 3](https://www.python.org/downloads/) installed.

## Installation

1. **Install OpenCV**  
   Run the following command in your terminal:
   ```bash
   pip install opencv-python
   ```

2. **Install Tesseract-OCR**  
   Follow the instructions in the [Tesseract GitHub repository](https://github.com/tesseract-ocr/tesseract) to install it for your operating system.

3. **Install pytesseract (Python wrapper for Tesseract)**  
   Run:
   ```bash
   pip install pytesseract
   ```

## Usage

After installation, you can run the script with:

```bash
python main.py
```

Make sure the Tesseract executable is correctly set in your code, for example:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # For Windows
```

or simply use `tesseract` if it's available in your system path (Linux/macOS).

## Notes

- This tool is optimized for Jalisco-style license plates.
- Image quality and lighting affect detection performance.

## License

This project is open-source and available under the [MIT License](LICENSE).

