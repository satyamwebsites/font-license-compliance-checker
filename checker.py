import os
from fontTools.ttLib import TTFont

def get_font_metadata(file_path):
    font = TTFont(file_path)
    name_table = font['name']

    data = {
        "Font Name": "Unknown",
        "Copyright": "Not found",
        "License": "Not found",
        "License URL": "Not found"
    }

    for record in name_table.names:
        try:
            text = record.toUnicode()
            if record.nameID == 4:
                data["Font Name"] = text
            elif record.nameID == 0:
                data["Copyright"] = text
            elif record.nameID == 13:
                data["License"] = text
            elif record.nameID == 14:
                data["License URL"] = text
        except:
            pass

    return data

def main():
    print("========================================")
    print("  FONT LICENSE COMPLIANCE CHECKER v1.0  ")
    print("========================================\n")
    
    font_folder = "fonts"

    if not os.path.exists(font_folder):
        print(f"Folder '{font_folder}' created successfully!")
        print("Add your .ttf or .otf font files inside the 'fonts' folder and run this again.")
        os.makedirs(font_folder)
        return

    found_fonts = False
    for filename in os.listdir(font_folder):
        if filename.lower().endswith((".ttf", ".otf")):
            found_fonts = True
            file_path = os.path.join(font_folder, filename)
            print(f"Scanning: {filename}...")

            metadata = get_font_metadata(file_path)

            print(f"  -> Font Name:   {metadata['Font Name']}")
            print(f"  -> Copyright:   {metadata['Copyright']}")
            print(f"  -> License:     {metadata['License']}")
            print(f"  -> License URL: {metadata['License URL']}")

            if "OFL" in metadata['License'] or "Open Font" in metadata['License']:
                print("  -> STATUS: Safe for Commercial Use (Open Source / OFL)")
            elif metadata['License'] == "Not found":
                print("  -> STATUS: WARNING! No explicit license data embedded in header.")
            else:
                print("  -> STATUS: Manual Review Required (Check EULA terms)")
            
            print("-" * 40)

    if not found_fonts:
        print(f"No font files found in '{font_folder}'. Add some .ttf files to test!")

if __name__ == "__main__":
    main()