import tinify

tinify.key = "zdlkFgyg1F24M5hnXLFD3jX9kXngCznx"
source = tinify.from_file("resim.jpg")
source.to_file("optimizeresim.jpg")

with open("resim.jpg", "rb") as source:
    source_data = source.read()
    result_data = tinify.from_buffer(source_data).to_buffer()

source = tinify.from_file("resim.jpg")
resized = source.resize(method="fit", width=150, height=100)
resized.to_file("resim.jpg")


source = tinify.from_file("resim.jpg")
converted = source.convert(type=["image/webp", "image/png"])
extension = converted.result().extension
converted.to_file("resim.jpg." + extension)
