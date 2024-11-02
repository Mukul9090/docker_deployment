from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(filename, message):
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, message)
    c.save()

def read_message(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return "No message found in file."

if __name__ == "__main__":
    # Read the message from 'input.txt'
    message = read_message("input.txt")
    create_pdf("hello_world.pdf", message)
    print("PDF generated as 'hello_world.pdf'")
   
