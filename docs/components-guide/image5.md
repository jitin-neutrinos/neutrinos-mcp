# Image

<https://documentation.neutrinos.com/articles/#!components-guide/image5>

## Image

OverviewThe image component is used to insert an image into a page.**Usage**Used to display an image on a page. The image has two required attributes- src and alt. Images are not technically inserted into the page, images are linked to HTML pages. The image component creates a holding space for the referenced image. How to useDrag and drop the component. Double click the component to display the list of attributes that can be used with it.Place the images inside the assets editor and save the image inside one of the folders available inside assets editor, and give the path in imgsrc attribute.Fill the attributes which are needed and save the page.ExampleInput the component field(s) with the attribute value(s): `imgsrc = /home/prashanth/Documents/neutrinos.png ` `Alt = Neutrinos`Save it and run.When the page is loaded **imgsrc = /home/prashanth/Documents/neutrinos.png** will display the image that is specified in the path and the **alt = Neutrinos** will display the text Neutrinos if the image cannot be loaded or is not found.Associated Attributes**Style:** It accepts a string value and affects the different properties (height, width, color etc.) of the component based on the values provided (eg. background:orange;height:200px;).**Class:** **Class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the **Style** side menu. The **Class** attribute accepts space separated class names (eg. class1 class2) which are defined in the **Style** tab as shown below.Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
} **Imgsrc:** The src attribute specifies the URL (web address) of the image. Images should be saved inside assets editor and placed within the Android or MaterialIcons or Web or iOS folders and the appropriate path should be given.**Alt:** The alt attribute provides an alternate text for an image if the user cannot view it.**Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
