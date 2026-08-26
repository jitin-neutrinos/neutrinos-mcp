# Image

<https://documentation.neutrinos.com/articles/#!components-guide-8/image>

## Image

### Overview

The **Image** component is used to insert an image into an application page. It has two required attributes, [src] and alt. Images are not technically inserted into the page, images are linked to HTML pages. The image component creates a holding space for the referenced image.

### Responsive Images

It’s important to make sure that images display correctly across a wide variety of screen widths and window sizes. One of the easiest techniques for accomplishing this is to set max-width: 100% and height: auto. This will ensure that the image is never too big for its container. When used in conjunction with a flexible grid system, this optimizes the image's display size for various screen widths.

Another way is by using the srcset property to specify multiple sizes of a single image, allowing the browser to select the appropriate image source based on the screen size. The srcset property lets us define a list of images that the browser switches between based on the rendered size and the density of the display.

Let us look at an example. Configure the following image properties:

[src]= 'https://i.imgur.com/fQ6hsx5.png'

alt= Responsive Images

srcset= https://i.imgur.com/fQ6hsx5.png 600w, https://i.imgur.com/tZ4OOWe.png 1500w, https://i.imgur.com/dTfQlJr.png 3000w

sizes= (max-width: 800px) 100vw

Here, we have specified 3 images in srcset with the w indicating the width of the image. If the viewport is less than 600px in width, **space_small.jpg** will be displayed. If the viewport is larger than 600px in width, **space_medium.jpg** will be displayed and if the viewport is larger than 1024px in width, **space_large.jpg** will be displayed.

The srcset property must always be accompanied by the sizes attribute so that the browsers can pick which image to load out of a source set before they layout the page. The media query (max-width: 800px) 100vw indicates that when my viewport is less than 800px wide, my image should take up 100% of the screen.

The browser will :

- Use the number with the w to calculate which image file will best fit within the amount of space we’ve defined in the sizes attribute.
- Consider the vw, so it can pick the right media condition and then use the w value next to the media condition (max-width: 1023px) to calculate how many pixels are needed to fill that space.

### How to use

1. Drag and drop the **Image** component.
2. Double click the component to display the list of attributes that can be used with it.
3. Place the images inside the assets editor and save the image inside one of the folders available inside assets editor, and give the path in the imgsrc attribute.
4. Fill the attributes which are needed and save the page.

### Associated Attributes

- **Image label: **The display name for the component. This label is only used to uniquely identify the component on the [canvas](/smart/project-concepts/studio-application-page/a/h3__2105229662). It does not provide any behavioral difference on the end app.
- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height:200px;).
- **Class**: The class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the **Style** tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **Assets src:** The address of the image present in the [Assets editor](/smart/project-sample-how-to-guide/add-assets). For example, '/Web/Icons/favicon.jpg'. If you want to reference an image from the [assets editor](/smart/project-sample-how-to-guide/add-assets), the image should be uploaded to any of the following folders on the editor:
  - Android
  - MaterialIcons
  - Web
  - iOS
- **alt: **An alternate text to be displayed if the user cannot view the image.
- **[src]: **The source URL of the image. Specify the source URL of the image in single quotes, or design a page flow with the source URL value and map it to this field using the [Flow Picker](/smart/project-sample-how-to-guide/bind-page-flows-to-components) editor. For example, you can directly specify theis value - 'https://www.howtogeek.com/wp-content/uploads/2019/08/img_5d572b6faa204.jpg'.
- **Secure URL:** Set to True if the image is using a secure URL (HTTPS). We recommend that you use secure URLs for your images. If you do not use a secure URL, customers may get warnings that the application contains both secure and insecure data. By default, this attribute is set to False.
- **[collectionName]: ****Deprecated.** A collection of URLs of the images to display dynamically.
- **[imageFilter]:** **Deprecated.** Filter the image from the collection of images.
- **width: **The width of the image. You can specify the width in pixels (for example - 100px), or in percentage (for example - 70%).
- **srcset:** A list of image files to use in different situations. See [Responsive Images](/smart/project-component-docs-test/image/a/h3__1172233646) to learn more. For example - assets/Web/Icons/flamingo4x.jpg 4025w, assets/Web/Icons/flamingo2x.jpg 2013w. Note that the image sizes are specified using w (image width).
- **sizes:** One or more strings separated by commas, indicating a set of source sizes. Source size can be:
  - A media condition. For example - (max-height: 500px) 200px proposes to use a source of 200px width, if the viewport is not higher than 500px.
  - A source size value. For example - 75px, 25,em, 100vw.

| ![Information](/resources/Storage/components-guide-8/info.png) | If the srcset attribute is not given or contains no values with a width descriptor, then the sizes attribute has no effect. |
| --- | --- |

Note that the [HTML image tag](https://www.w3schools.com/tags/tag_img.asp) supports a few more image properties other than the ones listed here. You can add these properties as [custom attributes](/smart/project-component-docs-test/how-to-use-palette-components/a/h4__1320575622) within the **Image** component.

### Examples

**Example 1: To display a simple image**

1. Drag and drop an **image** to the canvas.
2. Download the Neutrinos logo from above and upload it to the Web/Icons folder on [assets editor](/smart/project-sample-how-to-guide/add-assets).
3. Double-click the image to open its attributes window and set the following properties:
  - Style: padding: 25px; margin-bottom: 10px;
  - Assets src: /Web/Icons/NeutrinosLogo.png
  - width: 200px
4. Save and preview the page.

**Example 2: ****Responsive Images**

In this example, we will be providing multiple sizes of the same image, allowing the browser to select the appropriate image source based on the screen size.

1. Drag and drop an **Image** component to the canvas.
2. Download the following Flamingo images of different sizes and upload them to the Web/Icons folder on [assets editor](/smart/project-sample-how-to-guide/add-assets):
  - [flamingo1x](/resources/Storage/components-guide-8/flamingo/flamingo1x.jpg)
  - [flamingo2x](/resources/Storage/components-guide-8/flamingo/flamingo2x.jpg)
  - [flamingo3x](/resources/Storage/components-guide-8/flamingo/flamingo3x.jpg)
  - [flamingo4x](/resources/Storage/components-guide-8/flamingo/flamingo4x.jpg)
  - [flamingo-fallback](/resources/Storage/components-guide-8/flamingo/flamingo-fallback.jpg)
3. Double-click the image component on the canvas to open its attributes window and set the following properties:
  - [src]: 'assets/Web/Icons/flamingo-fallback.jpg'
  - srcset: assets/Web/Icons/flamingo4x.jpg 4025w, assets/Web/Icons/flamingo2x.jpg 2013w, assets/Web/Icons/flamingo1x.jpg 1006w, assets/Web/Icons/flamingo3x.jpg 3019w
  - sizes: 80vw
4. Save and preview the page. Resize the page and inspect the image to learn how the browser picks different images based on the screen size.
