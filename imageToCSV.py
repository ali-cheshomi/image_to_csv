# Copyright 2021 MR_AC. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


try:
    import subprocess
    p = subprocess.run('pip --version',capture_output=True)
except:
    print("you need to install subprocess library , 'pip install subprocess'")
    exit()
try:
    from pathlib import Path
except:
    
    print("you need to install pathlib library , 'pip install pathlib'")
    installOK = input("Do you want to install pathlib (y/n): ")
    if(installOK != "n"):
        subprocess.run('pip install pathlib')
    exit()
try:
    import csv
except:
    installOK = input("Do you want to install csv (y/n): ")
    if(installOK != "n"):
        subprocess.run('pip install csv')
    print("you need to install csv library , 'pip install csv'")
    exit()
try:
    from PIL import Image
except:
    installOK = input("Do you want to install PIL (y/n): ")
    if(installOK != "n"):
        subprocess.run('pip install PIL')
    print("you need to install PIL library , 'pip install PIL'")
    exit()

'''-------------------------Image To CSV Class----------------------------'''

class ImageToCSV:
    image:Image
    imagePath:str
    imageWidth:int
    imageHeight:int
    imagePixels:list = []
    csvPath:str
    csvName:str
    csvPixelFieldName:str = 'PX'
    csvField:list = []
    csvAdditionalField:dict = {}
    isGrayScale:bool = False
    
    def __init__(self,imagePath,imageWidth:int,imageHeight:int,csvPath:str=".\\",csvName:str="imagePixels.csv",csvAdditionalField:dict={},isGrayScale:bool=False):
        self.imagePath = imagePath
        self.imageWidth = imageWidth
        self.imageHeight = imageHeight
        self.csvPath = Path(csvPath).joinpath(csvName)
        self.csvName = csvName
        self.image = Image.open(imagePath)
        self.isGrayScale = isGrayScale

        self.__imgToPixel__()
        self.csvAdditionalField = csvAdditionalField
        
    def addToCSV(self) -> None:  
        if self.image.size != (self.imageWidth,self.imageHeight):
            self.image = self.image.resize((self.imageWidth,self.imageHeight))
  
        self.__imgToPixel__()
        rows=list(self.imagePixels)
        afv=list(self.csvAdditionalField.values())
        for a in afv:
            rows.append(a)
        field = self.__csvField__()        
        if(not self.__isCsvFileExist__()):
            with open(self.csvPath, 'w+', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(field)
                writer.writerow(rows)      
        else:        
            with open(self.csvPath, 'a+', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(rows)
    
    def __csvField__(self) -> list:   
        field = []
        wh=len(self.imagePixels)
        for i in range(wh):
            field.append(f'{self.csvPixelFieldName}{i}')
        afk=list(self.csvAdditionalField.keys())
        for a in afk:
            field.append(a) 
        return field

    def __isCsvFileExist__(self) -> bool:
        return Path(self.csvPath).exists()

    def __imgToPixel__(self) -> None:
        if(self.isGrayScale):
            # convert image to grayscale image
            self.image=self.image.convert('L')
        w,h=self.image.size
        
        px=[]
        for i in range(w):
            for j in range(h):
                px.append(self.image.getpixel((i,j)))
        self.imagePixels = px

'''---------------------------------Main----------------------------------'''

if __name__ == "__main__":
    print('''
    example:

        # with "img.csvAdditionalField" you can add some field to csv 
        
        imgAddr = "Test_Pictures/3.jpg"
        
        img1 = ImageToCSV(imgAddr,2,2,csvAdditionalField={'test1':1,'test2':'test2'},isGrayScale=False)
        img1.addToCSV()
        
        img2 = ImageToCSV(imgAddr,2,2,csvAdditionalField={'test1':0,'test2':'test2'},isGrayScale=True)
        img2.csvAdditionalField = {'test3':0}
        img2.addToCSV()
    
    ''')
