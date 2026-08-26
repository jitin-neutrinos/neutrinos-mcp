# Image

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/image>

## Image

### Overview

The **Image** component is used to insert an image into a page.

### Usage

Used to display an image on a page. The image has two required attributes- src and alt. Images are not technically inserted into the page, images are linked to HTML pages. The image component creates a holding space for the referenced image.

### How to use

1. Drag and drop the **Image** component.
2. Double click the component to display the list of attributes that can be used with it.
3. Place the images inside the assets editor and save the image inside one of the folders available inside assets editor, and give the path in the imgsrc attribute.
4. Fill the attributes which are needed and save the page.

### Associated Attributes

- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height:200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the **Style** tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **Assets src**: The src attribute specifies the URL (web address) of the image. Images should be saved inside assets editor and placed within the Android or MaterialIcons or Web or iOS folders and the appropriate path should be given.
- **Alt**: The alt attribute provides an alternate text for an image if the user cannot view it.
- **[src]**: Specify the image src URL which needs to be displayed.
- **Secure URL**: Specify the URLs of the images to control how they are displayed.
- **[collectionName]**: A collection of URLs of the images to display dynamically.
- **[imageFilter]**: Filter the image from the collection of images.
- **width**: Specify the width of the image.
- **srcset**: Used to define a set of multiple images.
- **sizes**: Specify the size of the images.

### Example

1. Input the component field(s) with the attribute value(s):

**imgsrc** = /home/prashanth/Documents/neutrinos.png

**Alt **= Neutrinos

1. Save it and run.
2. When the page is loaded the image that is specified in the path will be displayed and the **alt = Neutrinos** will display the text Neutrinos if the image cannot be loaded or is not found.
