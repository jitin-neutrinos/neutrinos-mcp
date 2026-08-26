# Sidenav

<https://documentation.neutrinos.com/articles/#!components-guide/sidenav5>

## Sidenav

OverviewThe sidenav components are designed to add side content to a fullscreen app. Sidenav typically contains the links for different pages in the app or links for different sections on that page. Sidenav is a fixed layout whose slide-in and slide-out activity can be bound to an action (ex. Button press, checkbox, etc.). The Sidenav component has meaning only when it is placed inside the **Sidenav Container** component.**Usage**Sidenav is useful when the user needs to have immediate access to the most used pages/components of an app.How to useDrag the **Sidenav** component from the **Navigation** section and drop it inside the **Sidenav Container** component.Populate the **Sidenav** component with the content that is required in the sidenav of that page.Save the changes.ExampleCreate a page called **page**.Drag and drop the **Sidenav Container**.Drag and drop the **Sidenav** component inside the **Sidenav Container**.Drag and drop an **HTML **component.Write an anchor tag inside that HTML component with the **href** attribute set to [http://www.neutrinos.co](http://www.neutrinos.co) and **target** attribute to **blank**. <a href="http://www.neutrinos.co">neutrinos</a>Save the changes.Now, pressing the button will open the neutrinos website.**Associated Attributes**
**Style:** It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (eg. background: orange; height:200px;).**Class:** **Class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the **Style** side menu. The **Class** attribute accepts space-separated class names (eg. class1 class2) which are defined in the **Style** tab as shown below.Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
 **mode:** Sidenav can render in one of three different ways based on the **mode** property.over - Sidenav floats over the primary content, which is covered by a backdroppush - Sidenav pushes the primary content out of its way, also covering it with a backdropside - Sidenav appears side-by-side with the main content, shrinking the main content's width to make space for the sidenav.**opened:** It decides whether the sidenav is opened. It can be **true** or **false**.**position:** Position can be either **start** or **end** which places the side content on the left or right side. Default is **start**.**fxLayout:** Specifies the flex-direction and whether the contents should be wrapped or not. eg. fxLayout=**column wrap**.**(opened):** Takes function name as the value. This function is defined in Ts file and is executed when the sidenav is opened.**(closed):** Takes function name as the value. This function is defined in Ts file and is executed when the sidenav is closed.**(toggle):** Takes function name as the value. This function is defined in Ts file and is executed when the sidenav is toggled.**Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
