import os
import time
from pdf2docx import Converter
import img2pdf


def convert_files(input_type, output_type):
    current_dir = os.getcwd()
    input_dir = current_dir + "/input/"
    input_files = os.listdir(input_dir)

    cond1 = input_type == "pdf" and output_type == "docx"
    cond2 = input_type in ["jpeg", "jpg"] and output_type == "pdf"

    for file in input_files:
        input_path = input_dir + file
        output_filename = file.replace(f".{input_type}", f".{output_type}")
        output_path = current_dir + "/output/" + output_filename

        if cond1 and file.endswith(".pdf"):
            cv = Converter(input_path)
            cv.convert(output_path)
            cv.close()

        elif cond2 and file.endswith(".jpeg") or file.endswith(".jpg"):
            print(f"Sart to convert {input_path}")
            t1 = time.perf_counter()

            with open(output_path,"wb") as f:
                f.write(img2pdf.convert(input_path))
                t2 = time.perf_counter()
                print(f"Terminated in {t2 - t1:0.2f}s.")

    if cond1 or cond2:
        print(f"All {input_type} files converted to {output_type} format.")


if __name__ == "__main__":
    import sys

    params = sys.argv
    source_type = params[1]
    target_type = params[2]
    convert_files(source_type, target_type)

    # python3 fileconvert.py pdf docx
    # python3 fileconvert.py jpeg pdf
