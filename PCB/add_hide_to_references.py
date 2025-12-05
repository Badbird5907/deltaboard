#!/usr/bin/env python3
"""
Script to add (hide yes) to the Reference property of all 
footprints matching "switches:Hotswap_MX_1.00u"
"""

import re
import sys

def add_hide_to_references(file_path):
    """
    Read the KiCad PCB file and add (hide yes) to Reference properties
    of all footprints matching "switches:Hotswap_MX_1.00u"
    """
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    modified = False
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this is the start of our target footprint
        if re.match(r'\s*\(footprint "switches:Hotswap_MX_1\.00u"', line):
            # Found our target footprint, scan forward for Reference property
            footprint_start = i
            i += 1
            
            # Look for Reference property within this footprint
            while i < len(lines):
                current_line = lines[i]
                
                # Check if we've left the footprint (next footprint starts)
                if re.match(r'\s*\(footprint ', current_line) and i > footprint_start + 1:
                    break
                
                # Check if this is a Reference property
                if re.match(r'\s*\(property "Reference"', current_line):
                    # Found Reference property, check if it already has (hide yes)
                    # Look ahead to find the (layer "F.SilkS") line
                    j = i + 1
                    found_hide = False
                    layer_line_idx = None
                    
                    # Scan forward within the Reference property block
                    paren_count = current_line.count('(') - current_line.count(')')
                    
                    while j < len(lines) and paren_count > 0:
                        scan_line = lines[j]
                        paren_count += scan_line.count('(') - scan_line.count(')')
                        
                        # Check if we found (hide yes)
                        if '(hide yes)' in scan_line:
                            found_hide = True
                        
                        # Track the (layer "F.SilkS") line
                        if re.match(r'\s*\(layer "F\.SilkS"\)', scan_line):
                            layer_line_idx = j
                        
                        j += 1
                    
                    # If we didn't find (hide yes) and found the layer line, add it
                    if not found_hide and layer_line_idx is not None:
                        # Insert (hide yes) after the layer line
                        indent_match = re.match(r'(\s*)', lines[layer_line_idx])
                        indent = indent_match.group(1) if indent_match else '\t\t'
                        lines.insert(layer_line_idx + 1, indent + '\t\t(hide yes)\n')
                        modified = True
                        # Adjust j since we inserted a line
                        j += 1
                    
                    # Move past the Reference property block
                    i = j
                    continue
                
                i += 1
            
            continue
        
        i += 1
    
    # Write back if modified
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"Successfully added (hide yes) to Reference properties in {file_path}")
        return True
    else:
        print("No modifications needed - all Reference properties already have (hide yes)")
        return False


if __name__ == '__main__':
    file_path = 'deltaboard.kicad_pcb'
    
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    
    try:
        add_hide_to_references(file_path)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

