from PyPDF2 import PdfReader, PdfWriter

page0 = [0, 1]
page1 = [2, 3]
page2 = [4, 5]
page3 = [6, 7]
page4 = [8, 9]
page5 = [10, 11]
page6 = [12, 13]
page7 = [14, 15]
page8 = [16, 17]
page9 = [18, 19]
page10 = [20, 21]
page11 = [22, 23]
page12 = [24, 25]
page13 = [26, 27]
page14 = [28, 29]
page15 = [30, 31]
page16 = [32, 33]
page17 = [34, 35]
page18 = [36, 37]
page19 = [38, 39]
page20 = [40, 41]
page21 = [42, 43]
page22 = [44, 45]
page23 = [46, 47]
page24 = [48, 49]
page25 = [50, 51]
page26 = [52, 53]
page27 = [54, 55]
page28 = [56, 57]
page29 = [58, 59]
page30 = [60, 61]
page31 = [62, 63]
page32 = [64, 65]
page33 = [66, 67]
page34 = [68, 69]
page35 = [70, 71]
page36 = [72, 73]
page37 = [74, 75]
page38 = [76, 77]
page39 = [78, 79]
page40 = [80, 81]
page41 = [82, 83]
page42 = [84, 85]
page43 = [86, 87]
page44 = [88, 89]
page45 = [90, 91]
page46 = [92, 93]
#page47 = [94, 95]
#page48 = [96, 97]



FeedYardList = ["p1", "p2", "p3"]

num = 0
arg = "p" + str(num) + "writer.write(f2)"

#THIS NEEDS EDITED

with open("Benchmark_Feedyards_Visualization_2023_June_V1.pdf", "rb") as f:
    reader = PdfReader(f)
    p0writer = PdfWriter()
    p1writer = PdfWriter()
    p2writer = PdfWriter()
    p3writer = PdfWriter()
    p4writer = PdfWriter()
    p5writer = PdfWriter()
    p6writer = PdfWriter()
    p7writer = PdfWriter()
    p8writer = PdfWriter()
    p9writer = PdfWriter()
    p10writer = PdfWriter()
    p11writer = PdfWriter()
    p12writer = PdfWriter()
    p13writer = PdfWriter()
    p14writer = PdfWriter()
    p15writer = PdfWriter()
    p16writer = PdfWriter()
    p17writer = PdfWriter()
    p18writer = PdfWriter()
    p19writer = PdfWriter()
    p20writer = PdfWriter()
    p21writer = PdfWriter()
    p22writer = PdfWriter()
    p23writer = PdfWriter()
    p24writer = PdfWriter()
    p25writer = PdfWriter()
    p26writer = PdfWriter()
    p27writer = PdfWriter()
    p28writer = PdfWriter()
    p29writer = PdfWriter()
    p30writer = PdfWriter()
    p31writer = PdfWriter()
    p32writer = PdfWriter()
    p33writer = PdfWriter()
    p34writer = PdfWriter()
    p35writer = PdfWriter()
    p36writer = PdfWriter()
    p37writer = PdfWriter()
    p38writer = PdfWriter()
    p39writer = PdfWriter()
    p40writer = PdfWriter()
    p41writer = PdfWriter()
    p42writer = PdfWriter()
    p43writer = PdfWriter()
    p44writer = PdfWriter()
    p45writer = PdfWriter()
    p46writer = PdfWriter()
    #p47writer = PdfFileWriter()
    #p48writer = PdfFileWriter()
    

    for page in range(len(reader.pages)):
        if page in page0:
            p0writer.add_page(reader.pages[page])
        elif page in page1:
            p1writer.add_page(reader.pages[page])
        elif page in page2:
            p2writer.add_page(reader.pages[page])
        elif page in page3:
            p3writer.add_page(reader.pages[page])
        elif page in page4:
            p4writer.add_page(reader.pages[page])
        elif page in page5:
            p5writer.add_page(reader.pages[page])
        elif page in page6:
            p6writer.add_page(reader.pages[page])
        elif page in page7:
            p7writer.add_page(reader.pages[page])
        elif page in page8:
            p8writer.add_page(reader.pages[page])
        elif page in page9:
            p9writer.add_page(reader.pages[page])
        elif page in page10:
            p10writer.add_page(reader.pages[page])
        elif page in page11:
            p11writer.add_page(reader.pages[page])
        elif page in page12:
            p12writer.add_page(reader.pages[page])
        elif page in page13:
            p13writer.add_page(reader.pages[page])
        elif page in page14:
            p14writer.add_page(reader.pages[page])
        elif page in page15:
            p15writer.add_page(reader.pages[page])
        elif page in page16:
            p16writer.add_page(reader.pages[page])
        elif page in page17:
            p17writer.add_page(reader.pages[page])
        elif page in page18:
            p18writer.add_page(reader.pages[page])
        elif page in page19:
            p19writer.add_page(reader.pages[page])
        elif page in page20:
            p20writer.add_page(reader.pages[page])
        elif page in page21:
            p21writer.add_page(reader.pages[page])
        elif page in page22:
            p22writer.add_page(reader.pages[page])
        elif page in page23:
            p23writer.add_page(reader.pages[page])
        elif page in page24:
            p24writer.add_page(reader.pages[page])
        elif page in page25:
            p25writer.add_page(reader.pages[page])
        elif page in page26:
            p26writer.add_page(reader.pages[page])
        elif page in page27:
            p27writer.add_page(reader.pages[page])
        elif page in page28:
            p28writer.add_page(reader.pages[page])
        elif page in page29:
            p29writer.add_page(reader.pages[page])
        elif page in page30:
            p30writer.add_page(reader.pages[page])
        elif page in page31:
            p31writer.add_page(reader.pages[page])
        elif page in page32:
            p32writer.add_page(reader.pages[page])
        elif page in page33:
            p33writer.add_page(reader.pages[page])
        elif page in page34:
            p34writer.add_page(reader.pages[page])
        elif page in page35:
            p35writer.add_page(reader.pages[page])
        elif page in page36:
            p36writer.add_page(reader.pages[page])
        elif page in page37:
            p37writer.add_page(reader.pages[page])
        elif page in page38:
            p38writer.add_page(reader.pages[page])
        elif page in page39:
            p39writer.add_page(reader.pages[page])
        elif page in page40:
            p40writer.add_page(reader.pages[page])
        elif page in page41:
            p41writer.add_page(reader.pages[page])
        elif page in page42:
            p42writer.add_page(reader.pages[page])
        elif page in page43:
            p43writer.add_page(reader.pages[page])
        elif page in page44:
            p44writer.add_page(reader.pages[page])
        elif page in page45:
            p45writer.add_page(reader.pages[page])
        elif page in page46:
            p46writer.add_page(reader.pages[page])
        elif page in page47:
            p47writer.add_page(reader.pages[page])
        elif page in page48:
            p48writer.add_page(reader.pages[page])

    with open("BFY.pdf", "wb") as f2:
        p0writer.write(f2)
    with open("BRF.pdf", "wb") as f2:
        p1writer.write(f2)
    with open("BVF.pdf", "wb") as f2:
        p2writer.write(f2)
    with open("CCF.pdf", "wb") as f2:
        p3writer.write(f2)
    with open("CO-E.pdf", "wb") as f2:
        p4writer.write(f2)
    with open("CO-H.pdf", "wb") as f2:
        p5writer.write(f2)
    with open("CO-K.pdf", "wb") as f2:
        p6writer.write(f2)
    with open("CO-L.pdf", "wb") as f2:
        p7writer.write(f2)
    with open("CO-S.pdf", "wb") as f2:
        p8writer.write(f2)
    with open("CO-T.pdf", "wb") as f2:
        p9writer.write(f2)
    with open("DCF.pdf", "wb") as f2:
        p10writer.write(f2)
    with open("DFY-F.pdf", "wb") as f2:
        p11writer.write(f2)
    with open("DFY-P.pdf", "wb") as f2:
        p12writer.write(f2)
    with open("DFY-S.pdf", "wb") as f2:
        p13writer.write(f2)
    with open("DFY-T.pdf", "wb") as f2:
        p14writer.write(f2)
    with open("DHF.pdf", "wb") as f2:
        p15writer.write(f2)
    with open("ELORO.pdf", "wb") as f2:
        p16writer.write(f2)
    with open("FBCC.pdf", "wb") as f2:
        p17writer.write(f2)
    with open("FCN1.pdf", "wb") as f2:
        p18writer.write(f2)
    with open("FCN2.pdf", "wb") as f2:
        p19writer.write(f2)
    with open("FDCF.pdf", "wb") as f2:
        p20writer.write(f2)
    with open("FFFY.pdf", "wb") as f2:
        p21writer.write(f2)
    with open("FLFY.pdf", "wb") as f2:
        p22writer.write(f2)
    with open("FRCF.pdf", "wb") as f2:
        p23writer.write(f2)
    with open("FRON.pdf", "wb") as f2:
        p24writer.write(f2)
    with open("FSCC.pdf", "wb") as f2:
        p25writer.write(f2)
    #with open("H1.pdf", "wb") as f2:
        #p26writer.write(f2)
    with open("HB.pdf", "wb") as f2:
        p26writer.write(f2)
    #with open("HCH.pdf", "wb") as f2:
        #p28writer.write(f2)
    with open("HFC.pdf", "wb") as f2:
        p27writer.write(f2)
    with open("HGFC.pdf", "wb") as f2:
        p28writer.write(f2)
    with open("HGFF.pdf", "wb") as f2:
        p29writer.write(f2)
    with open("HYP.pdf", "wb") as f2:
        p30writer.write(f2)
    with open("MAG.pdf", "wb") as f2:
        p31writer.write(f2)
    with open("NVF.pdf", "wb") as f2:
        p32writer.write(f2)
    with open("OBC.pdf", "wb") as f2:
        p33writer.write(f2)
    with open("OCC.pdf", "wb") as f2:
        p34writer.write(f2)
    with open("OLSO.pdf", "wb") as f2:
        p35writer.write(f2)
    with open("P-MCF.pdf", "wb") as f2:
        p36writer.write(f2)
    with open("PAR4.pdf", "wb") as f2:
        p37writer.write(f2)
    with open("PF-A.pdf", "wb") as f2:
        p38writer.write(f2)
    with open("PF-B.pdf", "wb") as f2:
        p39writer.write(f2)
    with open("PF-P.pdf", "wb") as f2:
        p40writer.write(f2)
    with open("ROG1.pdf", "wb") as f2:
        p41writer.write(f2)
    with open("ROG2.pdf", "wb") as f2:
        p42writer.write(f2)
    with open("ROOD.pdf", "wb") as f2:
        p43writer.write(f2)
    with open("SFI.pdf", "wb") as f2:
        p44writer.write(f2)
    with open("SRC.pdf", "wb") as f2:
        p45writer.write(f2)
    with open("TE.pdf", "wb") as f2:
        p46writer.write(f2)
