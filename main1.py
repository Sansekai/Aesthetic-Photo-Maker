from aesthestic.maker import AestheticMaker

# with decoration
maker1 = AestheticMaker("background.jpg", "media/temp/image/hasilremovebg.png")
maker1.create()
maker1.save("media/temp/image/estetik.jpg")
