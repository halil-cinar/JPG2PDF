from PIL import Image
from reportlab.lib.pagesizes import letter,A4
from reportlab.pdfgen.canvas import Canvas
import os


path=input("Enter the folder address where the files are located")
path.replace("\\","/" )
path+="/"
print(path)
             


output_filename = "new.pdf"
output_file_path=input("Enter the address where you want the file to be saved, if you leave it blank, it will be saved on the desktop.")
if(output_file_path==""):
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    output_file_path=desktop_path

output_filename = input("name of new file")
output_filename += ".pdf"
output_file_path=output_file_path+"/"+output_filename

def process():
    # Finding .png files in the directory where the files are located
    png_files = [f for f in os.listdir(path) if f.endswith(".png")or f.endswith(".PNG")
                 or f.endswith(".jpg")]

    # Create PDF file and add images
    with open(output_file_path, "wb") as f:
        c = Canvas(f,pagesize=A4)
        width, height = A4
        
        for png in png_files:
            
            image_width,image_height=Image.open(path+png).size
            resize_height=(image_height)*(width/image_width)
            
            c.setPageSize([width,resize_height])
            c.drawImage(path + png, 0, 0, width, resize_height)
            c.showPage()
        c.save()
        print("Saved")


try:
    process()

   
except FileNotFoundError:
    try:
        print("file save path not found saving to desktop")
        output_file_path=os.path.join(os.path.expanduser('~'), 'Desktop')+"/"+output_filename
        print(output_filename)
        process()
    except:
        print("MISTAKE!! Please try again error code: 1")
except:
    print("MISTAKE!! Please try again error code: 2")
