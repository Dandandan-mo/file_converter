# File Converter
This script converts all pdf files to docx format, or converts all jpeg/jpg files to pdf format.

## Steps

TODO: add a bash script to create the input and output folder structure
0. create 'input' and 'output' folder:
```bash
chmod +x create_folders.sh

./create_folders.sh
```
1. put source files in the 'input' folder

2. create and activate virtual environment
```bash
python3 -m venv venv

source venv/bin/activate
```
2. install packages needed

```bash
pip install -r requirements.txt
```
3. run the script with parameters
```bash
# To convert pdf to docx:
python3 filecovert.py pdf docx

# To convert jpeg or jpg to pdf:
python3 filecovert.py jpeg pdf
# Or
python3 fileconvert.py jpg pdf

deactivate
```
4. collect all converted files in the 'output' folder