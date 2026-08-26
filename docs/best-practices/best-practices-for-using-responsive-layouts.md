# Best Practices for using Responsive Layouts

<https://documentation.neutrinos.com/articles/#!best-practices/best-practices-for-using-responsive-layouts>

# Best Practices for using Responsive Layouts

---

Responsive web design is an approach that suggests that design and development should respond to the user’s behavior and environment based on screen size, platform, and orientation. Follow these best practices and conventions while using responsive layouts in Neutrinos Studio:

### Design for Mobile First

![Platform](/resources/Storage/best-practices/responsive_layouts.jpg)

- **Design for thumbs:** Try to limit all user actions for easy thumb reachability.
- **Design testing for keyboard overflow: **All input actions will trigger keyboard open, re-aligning, or pushing the layout. Test the layout when the keyboard opens to ensure that the keyboard push doesn’t break the layout. Also, make sure that the focus of the input field doesn’t overflow out of the screen.

### Use UI Components to Implement Angular Flex Layouts

Neutrinos Platform supports Angular flex layouts and recommends that you use them to build responsive app pages. You can use the UI components in the Layout section of Neutrinos Studio to achieve this.

![](/resources/Storage/best-practices/row_col.png)

Use the following directives in the UI components to make them responsive:

**fxFlex **

The fxFlex directive identifies the resizing of an element within the flexbox container flow. It also identifies the resizing of elements in horizontal or vertical stacks. Some of the options of this directive include:

- flex-grow **: **defines how much a flexbox item should grow (proportional to the others) if there's space available. The **flex-**grow value overrides the width.
- flex-shrink **:** defines how much a flexbox item should shrink if there is not enough space available.
- flex-basis : controls the default size of an element, before it is manipulated by other Flexbox properties.

Template:

```html
<div fxFlex=”<grow> <shrink> <basis>”></div>;
```

- Flex-wrap: defines whether the flex items are forced in a single line or can be flowed into multiple lines. If set to multiple lines, it also defines the cross-axis which determines the direction new lines are stacked in.
- Flex-basis: specifies the initial size of the flex item, before any available space is distributed according to the flex factors.

The aliases used to quickly specify Flexbox styling:

**Alias**


 **Equivalent CSS**






 grow


 Flex: 1 1 100%








 initial



 Flex: 0 1 auto







 auto


 Flex:   100%




 none


 Flex: 0 0 auto







 nogrow



 Flex: 0 1 auto





 noshrink


 Flex: 1 0 auto

**fxLayoutGap**


 This directive defines the gap between the child items within a flexbox container. Some of the features of this directive include:



 margin-right: which is used when the parent container flex-direction == "row".


 margin-bottom: which is used when the parent container flex-direction == "column".






 ![Information](/resources/Storage/best-practices/info.png)


  While using wrap with fxLayout , you should account for the gap sizes when specifying the child item sizes (using fxFlex).








 **fxFlexFill**


 This directive identifies the element whose width and height should be maximized. It should be used on elements within a fxLayout container. Example:


 Copy CodeHTML<div fxFlexFill>
 <div>1. One</div> <div>2. Two</div> <div>3. Three</div> <div>4. Four</div>
</div>


 This directive takes no arguments and populates its host element with the following inline CSS styling:








 **Key**


 **Alias**






 margin


 0








 width



 100%







 height


 100%




 min-width


 100%







 min-height


 100%








 **Other Directives**


 Apart from the ones discussed above, you can use the following directives with UI components:


 fxFlexOrder: defines the order of a flexbox child item.


 ngStyle in flex layout: Enhances the Angular ngStyle directive with style updates based on mediaQuery activations. For example, use ngStyle.xs for extra-small screens.

 ngClass in flex layout: Enhances the Angular ngClass directive with class changes based on mediaQuery activations.


 fxHide: This markup specifies if its host element should not be displayed. It takes a boolean value which can be queried for different screens using breakpoints.

 fxShow: This markup specifies if its host element should be displayed (or not).


 fxLayoutAlign: defines the alignment of children element within the flexbox parent container. You can align both the main-axis and the cross axis.





 fxFlexAlign: Works like fxLayoutAlign, but applies only to a single flexbox item, instead of all items.


 fxFlexOffset: dictates the margin between elements. This directive should be used on elements within a fxLayout container.



 In Neutrinos Studio, some of these directives are already available in the component's attributes window. You can set them by passing a value to the attribute. For the rest of the components, you should create a custom property to set the value. For example:
 ![Row attributes](/resources/Storage/best-practices/row_directives.png)


 ![custom attributes](/resources/Storage/best-practices/fxhide_config.png)






 Breakpoint



 These are the breakpoint aliases and their media query values that you can use with flex layouts:For example, if you set the fxHide.xs of a component to '**true**' , the component will be hidden (not displayed) in an extra small screen. Similarly, all of the directives can query different breakpoints (screen-sizes) to achieve all kinds of layouts.








 **Breakpoint**


 **media query**






 xs


 screen and (max-width: 599px)








 sm



 screen and (min-width: 600px) and (max-width: 959px)







 md


 screen and (min-width: 960px) and (max-width: 1279px)




 lg


 screen and (min-width: 1280px) and (max-width: 1919px)







 xl


 screen and (min-width: 1920px) and (max-width: 5000px)




 lt-sm


 screen and (max-width: 599px)






 lt-md


 screen and (max-width: 959px)






 lt-lg


 screen and (max-width: 1279px)






 lt-xl


 screen and (max-width: 1919px)






 gt-xs


 screen and (min-width: 600px)






 gt-sm


 screen and (min-width: 960px)






 gt-md


 screen and (min-width: 1280px)






 gt-lg


 screen and (min-width: 1920px)
