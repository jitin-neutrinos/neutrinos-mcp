# Carousel

<https://documentation.neutrinos.com/articles/#!components-guide-8/carousel>

## Carousel

### Overview

The Carousel component is used to show images in a slideshow. It works with a series of images, images with captions. It also includes support for previous/next controls and indicators. This component is responsive to render well on a variety of devices with different screen sizes that include mobiles and computers. Also, this carousel will automatically change its size to fit the image’s size.

### How to use

1. Drag and drop a Carousel component to the page container.
2. Optionally add columns, drop columns, paginator, and filter components.
3. Double click the carousel component to display the list of attributes that can be used with it.
4. Double click the column, drop a column, paginator, and filter components added within the table, and set its attributes.
5. Save and run the page.

### Associated Attributes

**Basic Properties**

- **label**: The display name for the carousel component.
- **style**:  It accepts a string value and affects different properties (height, width, color, etc.) of the component based on the values provided (example- background: orange; height:200px;).
- **class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.CSS.class1 {
    border-radius:10px;
    flex-basis:10%;
    height:100px;
   }
   .class2 {
    border-radius:10px;
    flex-basis:10%;
    height:100px;
   }
- **width**: The width of the Carousel.
- **height**: The height of the Carousel.
- **images**: The images to be displayed in the Carousel. Add the images as an array object.

#### Advanced Properties

- **StartIndex (number)**: The index of the image which is to be displayed when the Carousel is previewed.
- **PreviewLeftArrow (String)**: The Angular material icon to be displayed as the left arrow in preview mode.
- **PreviewRightArrow (String)**: The Angular material icon to be displayed as the right arrow in preview mode.
- **CarouselLeftArrow (String)**: The Angular material icon to be displayed as the left arrow in the Carousel.
- **CarouselRightArrow (String)**: The Angular material icon to be displayed as the right arrow in the Carousel.
- **Change (Event Emitter)**: Event emitted on change of the image
- **PreviewOpen (Event Emitter)**: Event emitted once the preview opens up.
- **PreviewClose (Event Emitter)**: Event emitted once the preview is closed.
- **PreviewChange (Event Emitter)**: Event emitted once the preview image has changed.
- **ImageAutoPlayInterval (Number)**: Set the time in milliseconds after which the next image has to be displayed.
- **ShowImageDescription (Boolean)**: Set to TRUE if you want to display the image description.
- **ShowNavigator (Boolean)**: Set to TRUE if you want to show navigator in the Carousel.
- **ImageArrows (Boolean)**: Set to TRUE if you want to show arrows for image navigation in the Carousel
- **ImageSwipe (Boolean)**: Set to TRUE if you want the user to be able to swipe the images. This effect of this feature can be observed only on touch screen devices.
- **ImageAutoPlay (Boolean)**: Set to TRUE if you want the images to keep changing without user navigation.
- **ImageInfinityMove (Boolean)**: Set to TRUE if you want to slide through images in a loop.
- **ShowPreview (Boolean)**: Set to TRUE if you want the user to click on a Carousel image to preview the image.
- **ShowPreviewArrows (Boolean)**: Set to TRUE if you want to show arrows when the user is previewing the image.
- **EnablePreviewSwipe (Boolean):** Set to TRUE if you want to enable swiping of images while previewing on Touch screen devices.
- **PauseOnHover (Boolean)**: Set to TRUE if you want the auto-play to pause on hover.

### Example

1. Create a page named **carousel**. Open the created page.
2. Drag and drop a row component to the canvas.
3. Drag and drop a column component inside the row component.
4. Drag and drop a carousel component inside the column. Double click the carousel component and enter the following properties:
  1. Basic Properties:
    - **Width**: imageObject.width
    - **Height**: imageObject.height
    - **images**: imageObject.images
  2. Advanced Properties:
    - **Startindex**:imageObject.startIndex
    - **PreviewLeftArrow**: imageObject.previewLeftArrow
    - **PreviewRightArrow**: imageObject.previewRightArrow
    - **CarouselLeftArrow**: imageObject.carouselLeftArrow
    - **CarouselRightArrow**: imageObject.carouselRightArrow
    - **Change**: change()
    - **PreviewOpen**: previewOpen()
    - ** PreviewClose**: previewClose()
    - **PreviewChange**: previewChange()
    - **imageAutoPlayInterval**: 2000
  3. After adding the properties, replace the TS editor of the page with the following code:
  4. Copy CodeCode/*DEFAULT GENERATED TEMPLATE. DO NOT CHANGE SELECTOR TEMPLATE_URL AND CLASS NAME*/
     import { Component, OnInit } from '@angular/core'
     import { NBaseComponent } from '../../../../../app/baseClasses/nBase.component';
     import { NgxGalleryImage } from 'neo-carousel';
     /*
     Client Service import Example:
     import { servicename } from 'app/sd-services/servicename';
     */
     /*
     Legacy Service import Example :
     import { HeroService } from '../../services/hero/hero.service';
     */
     @Component({
      selector: 'bh-carousel',
      templateUrl: './carousel.template.html'
     })
     export class carouselComponent extends NBaseComponent implements OnInit {
     images: NgxGalleryImage[] = [
      {
      small: 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg' ,
      medium: 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg' ,
      big: 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg',
      description: "sfdsfdsdf"
      },
      {
      small: 'https://cdn.pixabay.com/photo/2013/10/15/09/12/flower-195893_150.jpg',
      medium: 'https://cdn.pixabay.com/photo/2013/10/15/09/12/flower-195893_150.jpg',
      big: 'https://cdn.pixabay.com/photo/2013/10/15/09/12/flower-195893_150.jpg',
      description: "Test description"
      },
      {
      small: 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg' ,
      medium: 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg' ,
      big: 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg'
      },
      {
      small: 'https://cdn.pixabay.com/photo/2013/10/15/09/12/flower-195893_150.jpg',
      medium: 'https://cdn.pixabay.com/photo/2013/10/15/09/12/flower-195893_150.jpg',
      big: 'https://cdn.pixabay.com/photo/2013/10/15/09/12/flower-195893_150.jpg',
      description: "Test carousel preview"
      },
      {
      small: 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg' ,
      medium: 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg' ,
      big: 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg',
      description: "asdcasc"
      },
      {
      small: 'https://cdn.pixabay.com/photo/2013/10/15/09/12/flower-195893_150.jpg',
      medium: 'https://cdn.pixabay.com/photo/2013/10/15/09/12/flower-195893_150.jpg',
      big: 'https://cdn.pixabay.com/photo/2013/10/15/09/12/flower-195893_150.jpg',
      description: "Test preview"
      },
      {
      small: 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg' ,
      medium: 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg' ,
      big: 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg'
      },
      {
      small: 'https://cdn.pixabay.com/photo/2013/10/15/09/12/flower-195893_150.jpg',
      medium: 'https://cdn.pixabay.com/photo/2013/10/15/09/12/flower-195893_150.jpg',
      big: 'https://cdn.pixabay.com/photo/2013/10/15/09/12/flower-195893_150.jpg',
      description: "Test carousel"
      },
      ];
      imageObject = {
      width: '650px',
      height: '650px',
      startIndex: 0,
      previewLeftArrow: 'home',
      previewRightArrow: 'home',
      carouselLeftArrow: 'info',
      carouselRightArrow: 'info',
      interval: 2000,
      images: this.images,
      shownav: true,
      showImageDesc: true,
      imageArrows: true,
      imageSwipe: true,
      imageAutoPlay: true,
      imageInfinityMove: true,
      showPreview: true,
      showPreviewArrows: true,
      enablePreviewSwipe: true,
      pauseOnHover: true,
      }
      constructor() {
      super();
      }
      ngOnInit() {
      }
      change() {
      console.log("change called")
      }
      previewChange() {
      console.log("Test preview")
      }
      previewOpen() {
      console.log("Test preview open")
      }
      previewClose() {
      console.log("Test preview close")
      }
      onChange() {
      console.log('onChange called');
      }
     }
  5. Save and run the app.
