# List Item

<https://documentation.neutrinos.com/articles/#!components-guide-8/list-item>

## List Item

### Overview

The** List Item **component represents an individual data item in a [List](/articles/components-guide-8/list). The data to be displayed in the List Item is stored in an array/object and accessed using the *ngFor attribute. The data can be a string, number, image, etc.

### How to use

1. Drag and drop a **List Item** component inside a **List** component.
2. Set the attributes such as style and class, ngFor, and label.

### Associated Attributes

**List Item label:** The display name for the component. This label is only used to uniquely identify the component on the canvas. It does not provide any behavioral difference on the end app.**Style: **It accepts a string value and affects different properties (height, width, color, etc.) of the component based on the values provided as inline styling. For example-(background:orange;height:200px;). **Class**: It accepts space-separated class names that are defined in the Styles editor. For example, if the following CSS classes are defined in the Styles editor, then you can select them here to apply to this component. ***ngFor:** This property is used to iterate through the array object and get the data. See the [examples](/articles/components-guide-8/list/a/h3_1689083776) to learn more.**Label: **The label of the component that is to be displayed on runtime. Enter a label or provide an extension. If an extension such as {{name}} is provided, the list item will access the list item that you have defined on the page flow and gets the name value of the list item. If you are using any component inside the List Item (for example, if you add an image inside the list item), you should not define this property.ExamplesSee examples in the [List component documentation](/articles/components-guide-8/list/a/h3_1689083776).
