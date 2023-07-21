from fpdf import FPDF

pdf = FPDF(orientation="portrait", unit="mm", format="A4")
def get_minion(pdf):
    pdf.add_font(family="Minion", fname="C:\Fonts\Minion\TTF\MinionProReg.ttf",
                 uni=True)

    pdf.add_font(family="MinionItal", fname="C:\Fonts\Minion\TTF\MinionProItal.ttf",
                 uni=True)

    pdf.add_font(family="MinionBold", fname="C:\Fonts\Minion\TTF\MinionProBold.ttf",
                 uni=True)

    pdf.add_font(family="MinionBoldItal", fname="C:\Fonts\Minion\TTF\MinionProBoldItal.ttf",
                 uni=True)

    pdf.add_font(family="MinionImpact", fname="C:\Fonts\Minion\TTF\MinionProBigBold.ttf",
                 uni=True)

    pdf.add_font(family="MinionImpactItal", fname="C:\Fonts\Minion\TTF\MinionProBigBoldItal.ttf",
                 uni=True)
