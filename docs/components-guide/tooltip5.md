# Tooltip

<https://documentation.neutrinos.com/articles/#!components-guide/tooltip5>

## Tooltip

OverviewThe tooltip displays information about an element; above, below, to the left of, or to the right of the element. By default, the position it takes will be below the element. But this can be configured using the matTooltipPosition input. If the tooltip is required to switch left/right positions, then the position values before and after should be used instead of left and right respectively.**Usage**Tooltip is used to display text (or other content) when you hover over an HTML element.How to useDrag and drop the component. Double click the component to display the list of attributes that can be used with it.Fill the attributes which are needed and save the page.ExampleInput the component field(s) with the attribute value(s):  `matTooltip = This is tooltip ` `tooltip text = tooltip`Save it and run.When the page is loaded the value **matTooltip = This is tooltip** is the text that will be displayed when the mouse hovers over the tooltip area and **tooltip text = tooltip** is the text that is displayed on the tooltip field when the page is loaded.**Associated Attributes**
**Style:** It accepts a string value and affects the different properties (height, width, color etc.) of the component based on the values provided (eg. background: orange; height:200px;).**Class:** **Class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the **Styl****e** side menu. The **Class** attribute accepts space separated class names (eg. class1 class2) which are defined in the **Style** tab as shown below.Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
} **Tooltip text:** Specifies the text that has to be displayed when the application is run.**Mattooltip:** It specifies the message to be displayed in the tooltip. Value has to be a string. Example:- message: string.**Mattooltipposition:** Allows the user to define the position of the tooltip relative to the parent element. Example:- position: left | right | above | below | before | after.**Mattooltipshowdelay:** Specifies the default delay in ms before showing the tooltip after show method is called.**Mattooltiphidedelay:** The default delay in ms before hiding the tooltip after hide method is called.**Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
