import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch


def Generate_PDF(first_name, last_name, id_emp, age, sex):
    request_time = time.time()
    file_name = "id_card_" + first_name + "_" + str(request_time) + ".pdf"
    doc = SimpleDocTemplate(file_name,pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)
    Story=[]
    #logo = "python_logo.png"
    #im = Image(logo, 1*inch, 1*inch)
    #Story.append(im)
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '<font size=12>ID: %s</font>' % id_emp
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size=12>Name: %s</font>' % first_name + last_name
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size=12>Age: %s</font>' % age
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    ptext = '<font size=12>Sex: %s</font>' % sex
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))
    doc.build(Story)

    return file_name
