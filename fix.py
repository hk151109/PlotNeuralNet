import os
import re

# Path to your PlotNeuralNet Diagrams folder
folder = r"C:\Users\DELL\Desktop\Sem6\hari\PlotNeuralNet\PlotNeuralNet\Diagrams"

# Regex pattern: match shift=(...), but do NOT touch at(...)
shift_pattern = re.compile(r'shift=\(([^)]*)\)')

for filename in os.listdir(folder):
    if filename.endswith(".tex"):
        filepath = os.path.join(folder, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Replace shift=(...) with shift={(...)}
        fixed_content = shift_pattern.sub(r'shift={(\1)}', content)

        # Backup original file
        backup_path = filepath + ".bak"
        if not os.path.exists(backup_path):
            os.rename(filepath, backup_path)

        # Write fixed content
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(fixed_content)

        print(f"Fixed {filename}, backup saved as {backup_path}")

print("All .tex files in the folder are fixed!")
