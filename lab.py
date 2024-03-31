from PIL import Image

img = Image.open("portrait.jpg")
ancho , alto = img.size
pixel_map = img.load() 

n = 100

for j in range(alto):
    for i in range(ancho):
        if i < ancho-n and i%2==0  :
            pixel_map[i,j] = pixel_map[i+n,j]

        if j < alto - n and j%3==0:
            pixel_map[i,j] = pixel_map[i,j+n]
    


img.save("exp2.jpg")