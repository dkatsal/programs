import os
from PIL import Image, ImageDraw
for file in os.listdir("1"):
    if file.endswith(".jpg"):
        image = Image.open(os.path.join("1", file)) #Открываем изображение. 
        pix = image.load() #Выгружаем значения пикселей.
        width = image.size[0] #Определяем ширину. 
        height = image.size[1] #Определяем высоту. 
        N=height
        k=[]
        for i in range(0,height,10):
            for j in range(0,width,10):
                a = pix[j, i][0]
                b = pix[j, i][1]
                c = pix[j, i][2]
                area = (0, 0, 0, 0)
                if (a == 255) and (b==255) and (c==255):
                    print(i,j,"White")
        

                elif (a < 250) and (b<250) and (c<250):
                    print(i,j,"Photo")
            
                    for l in range(N):
                        k.append(i)
                    break
        print(k)            
        print(k[0],k[-1])     
        area = (0, k[0]-15, width, k[-1]+16)

        cropped = image.crop(area)
        #cropped.show()
        cropped.save(os.path.join("2", file))


        image = Image.open(os.path.join("2", file)) #Открываем изображение. 
        pix = image.load() #Выгружаем значения пикселей.
        width = image.size[0] #Определяем ширину. 
        height = image.size[1] #Определяем высоту. 
        N=height
        k=[]
        for i in range(0,width,10):
            for j in range(0,height,10):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                area = (0, 0, 0, 0)
                if (a == 255) and (b==255) and (c==255):
                    print(i,j,"White")
        

                elif (a < 250) and (b<250) and (c<250):
                    print(i,j,"Photo")
            
                    for l in range(N):
                        k.append(i)
                    break
        print(k)            
        print(k[0],k[-1])     
        area = (k[0]-4, 0, k[-1]+5, height)

        cropped = image.crop(area)
        #cropped.show()

        cropped.save(os.path.join("2", file))
print("ОБРАБОТАННО")