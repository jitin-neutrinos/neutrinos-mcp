# Image Carousel

<https://documentation.neutrinos.com/articles/#!components-guide/image-carousel5-0>

## Image Carousel

**Overview**The carousel is used to show images in a slideshow. This template is responsive so it will display gorgeously on all screen types including mobiles and computers. Also, our carousel will automatically change its size to fit the image’s size.**Usage**Carousels are often used to display a series of looping images. There are some other popular usages of the carousel. Some of them are:TeasersArticlesEntire sections of web pages
**How to Use**1. Download the carousel template from the Neutrinos store.
2. Install the template into N-Studio.
3. When creating a new app, select the carousel template from the **ENTER APP DETAILS** menu and click on the **create** button.
4.Create a component (Example: carousel)
5.In the TS file
6.Import services: one service based on user requirements (Example: image service) and another, carousel service, which contains observable media- used for tracking the responsiveness.
Copy CodeJavaScriptimport{imageserviceService}from'../../services/imageservice/imageservice.service';
import { carouselserviceService } from '../../services/carouselservice/carouselservice.service';

7.Inject the two services in 'constructor'Copy CodeJavaScript
constructor(private imgService:imageserviceService,private cService:carouselserviceService) {
}

8.Inside class, declare the variables usedCopy CodeJavaScript
imagedata : String ;
limit : any ;

9. In ngOnInit
Copy CodeJavaScriptthis.imageData = this.imgService.getImages();

imagedata - Variable used in imageservice. imgservice - Keyword for the service.

10. write a function
Copy CodeJavaScriptngDoCheck() {
this.limit = this.cService.assignLimit(1, 2, 4);
}
limit - Variable used in carouselservice. cservice - Keyword for the service. ngDoCheck() - Function used for tracking the responsiveness.
11.In HTML file
 Drag and drop a custom HTML to call the child component
Copy CodeJavaScript<bh-carousel [imageData]="imageData"[limitImage]="limit" *ngIf="imageData"></bh-carousel>
carousel- Name of the child component.
**Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
