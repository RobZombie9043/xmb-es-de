import re
import os
from pathlib import Path

AUTO_NAME_MAP = {
    "all": "auto-allgames",
    "favorites": "auto-favorites",
    "recent": "auto-lastplayed",
    "collections": "custom-collections"
}

def extract_items_from_log(filepath):
    ordered_items = []
    system_pattern = re.compile(r'ViewController::preload\(\): Populating gamelist for system "([^"]+)"')
    custom_pattern = re.compile(r'ViewController::preload\(\): Populating gamelist for custom collection "([^"]+)"')
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            if system_match := system_pattern.search(line):
                name = system_match.group(1)
                item_type = "auto" if name in AUTO_NAME_MAP else "system"
                ordered_items.append((name, item_type))
                print(f"Extracted: {name}, Type: {item_type}")
            elif custom_match := custom_pattern.search(line):
                name = custom_match.group(1)
                ordered_items.append((name, "custom"))
    return ordered_items

def map_output_name(name, item_type):
    if item_type == "auto":
        return AUTO_NAME_MAP[name]
    return name

def get_wrapped_index(index, offset, list_length):
    return (index + offset) % list_length

def generate_xml(ordered_items, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    total = len(ordered_items)
    for i, (name, item_type) in enumerate(ordered_items):
        filename = map_output_name(name, item_type)
        minus2 = map_output_name(*ordered_items[get_wrapped_index(i, -2, total)])
        minus1 = map_output_name(*ordered_items[get_wrapped_index(i, -1, total)])
        plus1  = map_output_name(*ordered_items[get_wrapped_index(i,  1, total)])
        plus2  = map_output_name(*ordered_items[get_wrapped_index(i,  2, total)])
        plus3  = map_output_name(*ordered_items[get_wrapped_index(i,  3, total)])
        plus4  = map_output_name(*ordered_items[get_wrapped_index(i,  4, total)])
        plus5  = map_output_name(*ordered_items[get_wrapped_index(i,  5, total)])
        plus6  = map_output_name(*ordered_items[get_wrapped_index(i,  6, total)])
        plus7  = map_output_name(*ordered_items[get_wrapped_index(i,  7, total)])
        xml_content = f"""<?xml version="1.0" ?>
<theme>
    <variables>
        <systemMinus2>{minus2}</systemMinus2>
        <systemMinus1>{minus1}</systemMinus1>
        <systemPlus1>{plus1}</systemPlus1>
        <systemPlus2>{plus2}</systemPlus2>
        <systemPlus3>{plus3}</systemPlus3>
        <systemPlus4>{plus4}</systemPlus4>
        <systemPlus5>{plus5}</systemPlus5>
        <systemPlus6>{plus6}</systemPlus6>
        <systemPlus7>{plus7}</systemPlus7>
    </variables>
</theme>"""
        output_path = Path(output_folder) / f"{filename}.xml"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_content)
    print(f"Generated {total} XML files in '{output_folder}'.")

if __name__ == "__main__":
    script_dir = Path(__file__).resolve().parent
    log_file = (script_dir / ".." / ".." / ".." / "logs" / "es_log.txt").resolve()
    output_dir = (script_dir.parent / "theme-customizations" / "gamelist-carousel").resolve()

    ordered_items = extract_items_from_log(log_file)
    generate_xml(ordered_items, output_dir)