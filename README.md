# Unit Converter Calculator Project

A modular GUI application built using Python, `tkinter`, and `pygubu` for bidirectional conversions between **grams** and **ounces**. 

The application can be run either as a unified tabbed application or as standalone micro-modules for individual conversion utilities.

---

## Features

- **Bidirectional Unit Conversion:**
  - Grams to Ounces (`1 g ≈ 0.03527 Oz`)
  - Ounces to Grams (`1 Oz = 28.3495 g`)
- **Flexible UI Architecture:** Run the entire suite using a tabbed `ttk.Notebook` container or launch specific converter screens independently.
- **Robust Input Validation:** Displays user-friendly error popups for non-numeric or invalid decimal entries.
- **Separation of Concerns:** UI designs are built and stored declaratively using XML (`.ui` files built with Pygubu Designer) and bound dynamically to Python logic handlers.

---

## Project Structure

```text
.
├── main.py                 # Application entry point (Tabbed Container)
├── AboutApp.py             # About tab module & standalone launcher
├── GramsToOuncesApp.py     # Grams to Ounces converter & standalone launcher
├── OuncesToGramsApp.py     # Ounces to Grams converter & standalone launcher
├── about.ui                # Pygubu UI XML for the About view
├── grams_to_ounces.ui      # Pygubu UI XML for Grams to Ounces view
└── ounces_to_grams.ui      # Pygubu UI XML for Ounces to Grams view
