# Column

<https://documentation.neutrinos.com/articles/#!components-guide-8/flex-layout-column>

## Column

### Overview

The **Column** component is used to set the position or flow of the child components vertically. Its main axis is from top to bottom.

We recommend learning about [Flex Layout and it's underlying concepts](/smart/project-concepts/flexbox-layout) before using this component.

To make your app responsive, follow our [Best Practices](/articles/best-practices/best-practices-for-using-responsive-layouts).

### How to use

1. Drag and drop a **Column** component.
2. Set the required attributes such as style, class, fxflex, wrap, fxlayoutgap, layout direction, fxshow and fxhide.
3. Drag and drop any other components inside the **Column** component.

### Associated Attributes

Learn about [Flex layout and flex container](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) before using this component.

- **Column label: **The display name of the component. This label is only used to uniquely identify the component on the [canvas](/smart/project-concepts/studio-application-page/a/h3__2105229662). It does not provide any behavioral difference on the end app.
- Style: It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- Class: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **fxFlex: **Resizes the child components along the main axis of the layout. negative numbers are invalid. This property accepts three parameters:
  - flex-basis: Specifies the initial default size of the flexbox item before it is changed by the flex-grow and flex-shrink properties. Once you specify the initial size, the flex item will not grow or shrink even when we specify the grow and shrink properties.
  - flex-grow: Specifies how much the flexbox item will grow relative to the rest of the flexbox child components inside the same flex container, when there is enough space. it will work only when we add flex-basis value is set to auto.
  - flex-shrink: Specifies how much the flexbox item should shrink relative to the rest of the flexbox child components in the same flex container, when there isn’t enough space.
- **fxLayoutGap:** Specifies margin gaps on child components within a flexbox container. It accepts integer value such as 20px, 5em etc.
- **Wrap: **Choose whether flex child components are forced onto one line or can wrap onto multiple lines.
  - Wrap (default): Flex child components will wrap onto multiple lines, from top to bottom
  - NoWrap: all flex child components will be on one line.
- **Layout Direction: **Specifies how child components should be aligned along the main axis. Select a direction from the drop-down list:
  - none (default): Child components are packed in their default position as if no value was set.
  - start: Child components are packed to the start of the container.
  - end: Child components are packed to the end of the container.
  - center: child components are centered in the container.
  - space-between: Child components are evenly distributed; the first line is at the start of the container while the last one is at the end.
  - space-around: Child components are evenly distributed with equal space around each line.
  - space-evenly: Child components are evenly distributed with equal space around them.
- **Perpendicular Direction:** Specifies how the child components should be aligned along the cross axis. Select a direction from the drop-down list:
  - start: Child components are placed at the start of the cross axis.
  - end: Child components are placed at the end of the cross axis.
  - center: child components are placed at the center of the cross axis.
  - stretch: Child components stretch to fill the container.
  - space-between: Child components are evenly distributed vertically.
  - space-around: Child components are evenly distributed vertically with equal space around them.
  - baseline: Child components are aligned such as their baselines align. Baseline is a line where most letters sit. The child elements are aligned based on that line.
- **fxShow:** Choose whether to dynamically show the element by selecting True or False. Or, click ![flow picker icon](/resources/Storage/components-guide-8/flow_picker_icon.png) and map the field to a [page flow](/smart/project-sample-how-to-guide/design-page-flows) a using the [Flow Picker](/smart/project-sample-how-to-guide/bind-page-flows-to-components) editor.
- **fxHide: **Choose whether to dynamically hide the element by selecting True or False. Or, click ![flow picker icon](/resources/Storage/components-guide-8/flow_picker_icon.png) and map the field to a [page flow](/smart/project-sample-how-to-guide/design-page-flows) a using the [Flow Picker](/smart/project-sample-how-to-guide/bind-page-flows-to-components) editor.

### Examples

**Example 1: ****To display a Column with four buttons**

1. Drag and drop a **Column** component. Double click the column to open its attributes window.
2. Update the following attribute values:
  - Style: width:300px; height:100%;background:#FFEBEE;
  - layout direction: space-around
  - perpendicular direction: center
3. Drag and drop five Buttons inside the **Column **component.
4. Name the buttons as **Button 1**, **Button 2**, **Button 3**, **Button 4**, and** Button 5** respectively.
5. In the [Styles](/smart/project-sample-how-to-guide/apply-global-styling) editor, create a class named .btn-style with the following CSS:Copy CodeJavaScript.btn-style
   {height:100px;background:#E8EAF6;border:1pxsolidblack; width:200px;}
6. Save and run the page.

When the page is loaded, the buttons appear vertically, and are evenly distributed in with equal space around them.

Update the layout direction and perpendicular direction attributes of **Column** and see how the placement of the buttons change. For example, if you choose the layout direction to start and the perpendicular direction to end, this is how the buttons are displayed within the Column.

Update the height of **Button 1, Button 2,** and **Button 5 **to 700px - height:700px; and change the **Column** property from nowrap to wrap. You will see that the height of the buttons exceeds the screen size. Therefore, they are wrapped onto multiple lines, from top to bottom as we set the Column property to wrap.

![column example 3](/resources/Storage/components-guide-8/project-component-docs-test/col_ex_3.png)

Change the **Column** property from wrap to nowrap. The buttons are wrapped into a single line even though their width exceeds the screen size.

**Example 2: ****To demonstrate how to work with flex layout**

1. Add the following CSS to the [Styles](/smart/project-sample-how-to-guide/apply-global-styling) editor on the Neutrinos Application page. Save the changes.  .demo-content{ padding: 25px; margin-bottom: 10px; background:#FFEBEE;  height:100%; width:300px; }
2. Add the Column Label as **Column 1**.
3. Select demo-content for the class attribute drop-down list.
4. Set fxlayoutGap to 20px to add a gap of 20px between the child elements of this column.
5. Drag and drop three **Columns **inside **Column1**. Update the Column labels to **Column2**, **Column3**, and **Column4** respectively.
  - Update the style attribute of each Column to background:#E1BEE7;border: 1px solid;
  - Set fxflex of **Column2** to **70**.
  - Set the fxflex of **Column3** to **20 10 auto**.
  - Set the fxflex of **Column4** to **10 10 3**.
6. Save and run the app.

Because the main axis of a Column runs vertically, you will see that **Column1** will flex up to 70% of the height of the parent Column from left to right. As only flex-grow value is provided, the default values of flex-shrink and flex-basis , that is **1** and **auto **respectively, are assumed. **Column 2** will flex up to 20% of the height of the parent Column and shrinks 10% if necessary. For Column3, even though the flex-grow value is provided as 10, the Column will not flex up as the flex-basis value is set to **1** instead of **auto**. Therefore, by default, it takes flex-basis value and flexes up to 3%.

**Example 3: ****To hide the Column at extra-small screen sizes**

1. Double-click **Column1** from the previous example.
2. Add [fxHide.xs] as the [custom property](/smart/project-component-docs-test/how-to-use-palette-components/a/h4__1320575622) of type **Key & Value **and set it to **true**.
3. Click the **Add** button to add the property.
4. Save and preview the app.

![custom property for a row component](/resources/Storage/components-guide-8/project-component-docs-test/row_cust_prop.png)

If you preview the app in an **iPad** view, you will see **Column1** and its child columns visible. But, if you preview the same app in an **iPhone** view, **Column1** and its child elements are not displayed as they are hidden from extra-small screens using the [fxHide.xs] property.

![iPAd view](/resources/Storage/components-guide-8/project-component-docs-test/col_ipad.png)

![column iphone](/resources/Storage/components-guide-8/project-component-docs-test/col_iphone.png)
