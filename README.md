# Font License Compliance Checker (Prototype) ⚖️🔍

A practical legal-tech prototype designed to bridge the gap between software licensing, copyright compliance, and corporate risk management.

This Python utility extracts embedded End User License Agreement (EULA) metadata and copyright tables directly from OpenType (`.otf`) and TrueType (`.ttf`) font files.

## 🎯 Purpose & Legal Context
In corporate and creative industries, unauthorized use of commercial font software can lead to significant copyright infringement liability. Manually verifying license scopes across digital assets is slow and error-prone. This tool automates first-pass compliance checks.

## ⚙️ Key Technical Features
* **Metadata Extraction:** Reads OpenType `name` tables (`NameID 0`, `NameID 4`, `NameID 13`, `NameID 14`) using `fontTools`.
* **Zero External Dependencies:** Runs 100% locally and offline without third-party API keys or external server calls.
* **Risk Categorization:** Flags fonts as Open Source (SIL OFL) vs. Proprietary / Manual EULA Review required.

## 🚀 How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/font-license-compliance-checker.git](https://github.com/YOUR_USERNAME/font-license-compliance-checker.git)
