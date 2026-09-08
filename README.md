# ImageToCSV

 A lightweight Python utility for converting images into pixel data and saving them as CSV files.

 ## Features

 - Convert images to pixel data
- Resize images to a custom width and height
- Optional grayscale conversion
- Save pixel data to CSV
- Add custom fields to CSV rows
- Customize pixel column names
- Append multiple images to the same CSV file

 ## Installation

 Python 3.x and [Pillow](<https://pypi.org/project/Pillow/>) are required.

```
pip install Pillow
```

 > `csv`, `pathlib`, and `subprocess` are part of Python's standard library and do not need to be installed separately.

 ## Usage

```
from image_to_csv import ImageToCSV

image = ImageToCSV(
    imagePath="image.jpg",
    imageWidth=48,
    imageHeight=48
)

image.addToCSV()
```

 By default, the output will be saved as:

```
imagePixels.csv
```

 in the current directory.

 ## Parameters

```
ImageToCSV(
    imagePath,
    imageWidth,
    imageHeight,
    csvPath=".",
    csvName="imagePixels.csv",
    csvAdditionalField={},
    isGrayScale=False,
    csvPixelFieldName="PX"
)
```

 | Parameter | Description |
| --- | --- |
| `imagePath` | Path to the input image |
| `imageWidth` | Target image width |
| `imageHeight` | Target image height |
| `csvPath` | Output directory |
| `csvName` | Output CSV filename |
| `csvAdditionalField` | Additional CSV columns and values |
| `isGrayScale` | Convert the image to grayscale |
| `csvPixelFieldName` | Prefix for pixel column names |

 ## Resize Image

 The image is automatically resized if its dimensions don't match the specified width and height.

```
image = ImageToCSV(
    "image.jpg",
    48,
    48
)

image.addToCSV()
```

 A `48 × 48` image produces **2304 pixel values**.

 ## Grayscale

 Set `isGrayScale=True` to convert the image to grayscale:

```
image = ImageToCSV(
    "image.jpg",
    48,
    48,
    isGrayScale=True
)

image.addToCSV()
```

 Grayscale pixel values range from:

```
0   = Black
255 = White
```

 ## Custom CSV Fields

 Additional information can be added to each image using `csvAdditionalField`:

```
image = ImageToCSV(
    "cat.jpg",
    48,
    48,
    csvAdditionalField={
        "label": 0,
        "class": "cat"
    },
    isGrayScale=True
)

image.addToCSV()
```

 The CSV will contain:

```
PX0,PX1,PX2,...,PX2303,label,class
```

 with the corresponding pixel values and metadata.

 This is useful for creating datasets for **machine learning and image classification**.

 ## Custom Pixel Column Names

 The default pixel prefix is `PX`:

```
PX0,PX1,PX2,...
```

 You can change it with `csvPixelFieldName`:

```
image = ImageToCSV(
    "image.jpg",
    48,
    48,
    csvPixelFieldName="pixel"
)
```

 Result:

```
pixel0,pixel1,pixel2,...
```

 ## Multiple Images

 If the CSV file already exists, new images are appended as additional rows.

```
from image_to_csv import ImageToCSV

images = [
    ("cat.jpg", 0),
    ("dog.jpg", 1),
]

for path, label in images:
    image = ImageToCSV(
        imagePath=path,
        imageWidth=48,
        imageHeight=48,
        csvPath="./data",
        csvName="dataset.csv",
        csvAdditionalField={
            "label": label
        },
        isGrayScale=True
    )

    image.addToCSV()
```

 The first image creates the CSV header; subsequent images are appended to the same file.

 ## Example

```
from image_to_csv import ImageToCSV

image = ImageToCSV(
    imagePath="Test_Pictures/3.jpg",
    imageWidth=48,
    imageHeight=48,
    csvPath="./data",
    csvName="dataset.csv",
    csvAdditionalField={
        "label": 1,
        "class": "example"
    },
    isGrayScale=True,
    csvPixelFieldName="PX"
)

image.addToCSV()
```

 ## Output

 For a `48 × 48` grayscale image:

```
48 × 48 = 2304 pixels
```

 The resulting CSV will have:

```
PX0,PX1,PX2,...,PX2303,label,class
```

 Each image is stored as **one row**.

 ## License

 Copyright © 2021 MR\_AC.

 Licensed under the **Apache License, Version 2.0**.

 See the `LICENSE` file for the complete license text.
