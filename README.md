# 🖼️ Python Asset Optimization Pipeline

[![Project Status](https://img.shields.io/badge/Status-Complete%20%7C%20Automated-28a745?style=for-the-badge)](./resize_images.py)
[![Language](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python)](./resize_images.py)
[![Focus](https://img.shields.io/badge/Focus-Performance%20%7C%20Asset%20Integrity-007bff?style=for-the-badge)]()

---

## 💡 Project Overview: The Image Asset Manager

This repository contains a crucial utility for modern web development, demonstrating automated **batch optimization and resizing of image assets**. The core focus is on establishing a robust **asset pipeline** that ensures consistency and maximal performance gains by targeting high-resolution image bloat.

The script serves as a foundational component for automated workflows in content management and site deployment.

## 🛠️ Engineering Disciplines Demonstrated

This project showcases expertise in several crucial software development areas:

### 1. **Asset Integrity & Aspect Ratio Preservation**
* **Strict Dimensional Control:** Implements a direct ratio calculation (`ratio = original_height / original_width`) to ensure that, regardless of the target width, the image's inherent aspect ratio is **mathematically guaranteed**, preventing visual distortion.
* **Format Consistency:** Uses the `img.format` property when saving, ensuring the output file retains its original file type (JPEG remains JPEG, PNG remains PNG), maintaining expected behavior for downstream systems.

### 2. **Optimized Processing & Flow Control**
* **Performance-Centric Skip Logic:** Includes a defensive check (`original_width <= new_width`) to automatically bypass image files that are already smaller than the target, eliminating unnecessary I/O and CPU cycles. This is a crucial element of an efficient batch process.
* **Robust Exception Handling:** Implements `try...except` blocks for both `FileNotFoundError` and general exceptions, ensuring the batch process continues gracefully even when encountering corrupt or invalid files.

### 3. **Modular and Defensible Architecture**
* **Separation of Concerns (SoC):** The logic is cleanly separated into two single-responsibility functions: `resize_image` (handles one file) and `batch_resize` (handles directory traversal and orchestration).
* **Directory Management:** Includes idempotent logic (`os.makedirs`) to ensure the output directory is created only if it doesn't exist, reflecting professional filesystem management.

---

## ⚙️ Application Structure

The entire application is contained within `resize_images.py` and manages input/output directories configured by global constants.

### Key Code Components:

| Function/Variable | Purpose | Engineering Highlight |
| :--- | :--- | :--- |
| `NEW_WIDTH` | Global constant defining the target output width. | Centralized configuration for easy pipeline adjustment. |
| `Image.open()` | Handles reading image data. | Utilizes the powerful Pillow library for image processing. |
| `batch_resize()` | Orchestrates the entire directory process. | Implements directory traversal and file type filtering
| `if original_width <= new_width:` | Conditional check within the resize function. | The core of the performance-driven skip logic. |

## 🚀 Quick Setup

This application requires only Python 3.x and the Pillow library.

1.  **Install Dependencies:**
    ```bash
    pip install Pillow
    ```
2.  **Prepare Assets:**
    Create a folder named **`input_images`** and place your files inside.
3.  **Execute the Optimizer:**
    ```bash
    python resize_images.py
    ```

## 🎯 Outcome

This project successfully delivered a performance-focused asset processing utility. It validates my ability to implement **robust file handling, mathematical integrity checks, and modular architecture** in a Python environment, showcasing a commitment to producing clean, reliable, and production-ready code.
