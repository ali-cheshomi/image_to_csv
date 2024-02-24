import os
import csv
try:
    from PIL import Image
except:
    print("you should install PIL library , 'pip install PIL'")
    exit()

def csv_field(wh,additionalField,pixelFieldName='px'):   
    field = []
    for i in range(wh):
        field.append(f'{pixelFieldName}{i}')
    afk=list(additionalField.keys())
    for a in afk:
        field.append(a) 

    return field

def is_File_Exist(path,filename):
    lst= os.listdir(path)
    for f in lst:
        if(filename ==f):
            return True
    return False

def add_to_csv(pixels,additionalField):  
    global csv_path,csv_name
    wh=len(pixels)
    rows=pixels
    afv=list(additionalField.values())
    for a in afv:
        rows.append(a)

    field = csv_field(wh,additionalField)
    if(is_File_Exist(csv_path,csv_name)==False):

        with open(csv_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(field)
    else:        
        with open(csv_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(rows)

def img_to_pixel(img,mode='G'):
    if(mode=='G'):
        # convert image to grayscale image
        img=img.convert('L')
    w,h=img.size
    px=[]
    for i in range(w):
        for j in range(h):
            px.append(img.getpixel((i,j)))
    return px

def path_to_list(path,format='.jpg'):
    lstdir= os.listdir(path)
    lst=[]
    for l in lstdir:
        if l.find(format)!=-1:
            lst.append(l)
    return lst

def pics_to_csv(lst,path,additionalField):
    global imageWidth,imageHight
    for i in lst:
        imgpath =f'{path}{i}'
        img =Image.open(imgpath)
        '''--- width=imageWidth ,hight=imageHight ---'''
        if img.size!=(imageWidth,imageHight):
            img=img.resize((imageWidth,imageHight))
        lstnp=img_to_pixel(img)
        add_to_csv(lstnp,additionalField)

def create_csv(path,group,imagesFormat='.jpg'):
    lst=path_to_list(path=path,format=imagesFormat)
    '''whit "additionalField" you can add some field to csv '''
    additionalField={'group':group }
    pics_to_csv(lst=lst,path=path,additionalField=additionalField)
'''-------------------------main----------------------------'''

# global value
imageWidth=48
imageHight=48

csv_path='.\\'
csv_name='test.csv'

# example 
'''You can repeat this step to add another image path'''
testPath1='Test_Pictures\\'
# testPath2='Test_Pictures_1\\'

create_csv(path=testPath1,group=0)
# create_csv(path=testPath2,group=1)







