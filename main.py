from aesthestic.maker import AestheticMaker

# with decoration
#maker1 = AestheticMaker("background.jpg", "sansekai.png")
#maker1.create()
#maker1.save("maker1.jpg")
#maker1.showImage()

# without decoration
maker2 = AestheticMaker("background.jpg", "media/temp/image/hasilremovebg.png")
maker2.create(decoration=False)
maker2.save("media/temp/image/estetik.jpg")
