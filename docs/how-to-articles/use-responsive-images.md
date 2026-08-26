# Use Responsive Images

<https://documentation.neutrinos.com/articles/#!how-to-articles/use-responsive-images>

It’s important to make sure that images display correctly across a wide variety of screen widths and window sizes. One of the easiest techniques for accomplishing this is to set max-width: 100% and height: auto. This will ensure that the image is never too big for its container. When used in conjunction with a flexible grid system, this optimizes the image's display size for various screen widths.

Another way is by using the srcset property to specify multiple sizes of a single image, allowing the browser to select the appropriate image source based on the screen size. The srcset property lets us define a list of images that the browser switches between based on the rendered size and the density of the display.

The srcset property must always be accompanied by the sizes attribute so that the browsers can pick which image to load out of a source set before they layout the page. For example, the media query (max-width: 800px) 100vw indicates that when my viewport is less than 800px wide, my image should take up 100% of the screen.

The browser will :

- Use the number with the w to calculate which image file will best fit within the amount of space we’ve defined in the sizes attribute.
- Consider the vw, so it can pick the right media condition and then use the w value next to the media condition (max-width: 800px) to calculate how many pixels are needed to fill that space.

Let us look at a few examples.

**Example 1: Consuming Images from the Assets editor**

In this example, we will be providing multiple sizes of the same image, allowing the browser to select the appropriate image source based on the screen size. We will be storing these images in the [Assets](/smart/project-sample-how-to-guide/add-assets)[editor](/smart/project-sample-how-to-guide/add-assets) of the application.

1. Drag and drop an **Image** component to the canvas.
2. Download the following Flamingo images of different sizes and upload them to the Web/Icons folder on [assets editor](/smart/project-sample-how-to-guide/add-assets):
  - [flamingo1x](/resources/Storage/how-to-articles/flamingo/flamingo1x.jpg)
  - [flamingo2x](/resources/Storage/how-to-articles/flamingo/flamingo2x.jpg)
  - [flamingo3x](/resources/Storage/how-to-articles/flamingo/flamingo3x.jpg)
  - [flamingo4x](/resources/Storage/how-to-articles/flamingo/flamingo4x.jpg)
  - [flamingo-fallback](/resources/Storage/how-to-articles/flamingo/flamingo-fallback.jpg)
3. Double-click the image component on the canvas to open its attributes window and set the following properties:
  - [src]: 'assets/Web/Icons/flamingo-fallback.jpg'
  - srcset: assets/Web/Icons/flamingo4x.jpg 4025w, assets/Web/Icons/flamingo2x.jpg 2013w, assets/Web/Icons/flamingo1x.jpg 1006w, assets/Web/Icons/flamingo3x.jpg 3019w
  - sizes: 80vw
4. Save and preview the page. Resize the page and inspect the image to learn how the browser picks different images based on the screen size.

**Example 2: Consuming images from a URL**

Configure the following image properties. Here, we are not saving the images in the Assets editor. Instead, we consuming them directly from the address where they are hosted.

[src]= 'https://i.imgur.com/fQ6hsx5.png'

alt= Responsive Images

srcset= https://i.imgur.com/fQ6hsx5.png 600w, https://i.imgur.com/tZ4OOWe.png 1500w, https://i.imgur.com/dTfQlJr.png 3000w

sizes= (max-width: 800px) 100vw

Here, we have specified 3 images in srcset with the w indicating the width of the image. If the viewport is less than 600px in width,** fQ6hsx5.png** will be displayed. If the viewport is larger than 600px in width and less than 1500 w, **tZ4OOWe.png ** will be displayed and if the viewport is larger than 1500px in width, **dTfQlJr.png **will be displayed.
