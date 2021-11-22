from PIL import Image
import sys
import pyocr
import pyocr.builders

f = "./ocr_wiki.jpeg"

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))

txt = tool.image_to_string(
    Image.open(f),
    lang="jpn",
    # builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    builder=pyocr.builders.TextBuilder()
)
print(txt)