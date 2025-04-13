> [!WARNING]
> This file contains multiple guides to help you execute this software properly, but such guides aren't complete.
> Refer to [Official Python Installation Guide](https://www.python.org/downloads/) for step-by-step and more topic-depth instructions.

## String Art Generation

This project creates string art using Python as main language. It leverages **Pillow**, **Imageio**, **Numpy**
to generate and animate circular string patterns, exporting the final result as a sequence of rendered frames with format GIF.

## Description

String Art Generation is a demonstration of algorithmic art generation, where lines connect points around a circle to form evolving predictable patterns. It's a clear example of how code can be transformed into visual creativity.

## Technologies Used

- **Python 3.x**
- **Numpy** - numerical array processing.
- **Pillow (PIL)** - for image processing.
- **Imageio** - for compiling frames into animated GIFs.

## Install Requirements

> [!CAUTION]
> These guides might seem helpful but they don't cover all possible configurations slash preferences.

1. **Download Python 3.13.3 or older from the official website:**

   If you wish to download Python, simply click the following link: [Download Python](https://www.python.org/downloads/)
   This will take you to the official Python website.

   # Python Not Recognized By Default
      If your system doesn't recognize the Python command, it's likely that Python's path hasn't been added to your environment variables.
      To fix this issue, you can run the following commands in your terminal or command prompt:
      ```bash
      where Python # On Windows
      which Python # On macOS/Linux
      ```
      If no path is returned, you may manually add Python to your system's PATH environment variable.

   If you reached this step, ensure that Python has been successfully installed on your system by running the following command in your terminal or command prompt:
   ```bash
   python --version
   ```
   You should see an output similar or identical to:
   ```bash
   Python 3.13.3
   ```

3. **Navigate to the project directory and install the dependencies:**

   > Don't forget to extract the **.zip** folder.

    ```bash
    cd {your_folder}
    cd Generative-String-Art-1.0.0
    pip install -r requirements.txt
    ```

## Run Python Script

Once you have completed all the previous steps and confirmed that Python is installed on your system, you're just one step away to see it in action. To run the project, use the following commands in your terminal or command prompt:
```bash
cd src
python string_art.py
```

## Previews
- The following image belongs to the software's outcome:
  ![Preview Image](output/previews/string_art_animation_modules_60.gif)
