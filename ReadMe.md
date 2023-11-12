# File Converter
This script converts all pdf files to docx format, or converts all jpeg/jpg files to pdf format.

## Steps
0. put source files in the 'input' folder
1. activate virtual environment
2. install packages needed
3. run the script with parameters

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# To convert pdf to docx:
python3 filecovert.py pdf docx

# To convert jpeg or jpg to pdf:
python3 filecovert.py jpeg pdf
# Or
python3 fileconvert.py jpg pdf

deactivate
```
4. collect all converted files in the 'output' folder