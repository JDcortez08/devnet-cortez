"""
Module 2 — Activity: File Sorting with os and shutil
Student: [Cortez, Jerick Daniel S.]
Date: [9/27/2026]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]


I created a simple Python script that automatically cleans up a cluttered folder by sorting files into subfolders based on their extensions.
It loops through everything in the target folder, double-checks that the item is an actual file (rather than a folder), and extracts its extension.
Then, it creates a designated subfolder for that file type—like /txt for text files, /jpg for images, or /pdf for documents—if one doesn't exist already, 
and neatly moves the file right into it.

============================================
KEY VOCABULARY
============================================
- os module:
- shutil module:
- file path:
- directory:
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

# --- paste your existing code here ---
folder = "files" 

for filename in os.listdir(folder): 
  file_path = os.path.join(folder, filename)
  
  if os.path.isfile(file_path):
    extension = os.path.splitext(filename)[1].lower().replace(".", "") 
    
    if extension: destination = os.path.join(folder, extension)
      if not os.path.exists(destination): os.makedirs(destination) 
        
        shutil.move(file_path, os.path.join(destination, filename))

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]

Having issues with the file path was one error I made.
the files folder was not where the program expected it to be, so the script was unable to locate it.
I discovered that the path specified in the script must coincide with the folder name and location.



============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]
"""
