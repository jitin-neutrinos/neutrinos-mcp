# Expansion Panel

<https://documentation.neutrinos.com/articles/#!components-guide-8/expansion-panel>

## Expansion Panel

### Overview

The **Expansion Panel **component is used to display data in an expanded view. It is best used for lightweight editing of an element, such as selecting a value for a setting.

Expansion Panels should be used within the [Expansion Panel Outlet](/articles/components-guide-8/expansion-panel-outlet) component. It can contain components such as [Expansion header](/articles/components-guide-8/expansion-panel-header), [Expansion title](/articles/components-guide-8/expansion-panel-title), and [Expansion Panel Description](/articles/components-guide-8/expansion-panel-description).

### Usage

The **Expansion panel **component can be used where the data to be displayed in an expanded view and will be shown and hidden based on the onclick() event. Only the title and description will be shown and other components will be hidden and they will be displayed when the user clicks on it.

### How to use

1. Drag and drop an **Expansion panel** component.
2. Fill in the attributes such as style, class, *ngFor, opened, closed, and expanded.
3. Drag and drop various Expansion components that can be placed inside this.

### Associated Attributes

- **Expansion Panel label: **The display name of the component. This label is only used to uniquely identify the component on the [canvas](/smart/project-concepts/canvas). It does not provide any behavioral difference on the end app.
- Style: It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- **Class: **The class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example-  class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

***ngFor**: Used to iterate through an array of objects to display data. **(opened):** Create a [page flow](/smart/project-sample-how-to-guide/design-page-flows) to define the function that is to be run every time the expansion panel is opened. You can enter the function name of the page flow directly here or click ![flow picker icon](/resources/Storage/components-guide-8/flow_picker_icon.png) and map the function name using the [Flow Picker](/smart/project-sample-how-to-guide/bind-page-flows-to-components) editor.**(closed):** Create a [page flow](/smart/project-sample-how-to-guide/design-page-flows) to define the function that is to be run every time the expansion panel is closed. Inside the function, you can define the actions that should take place when the panel closes. You can enter the function name of the page flow directly here or click ![flow picker icon](/resources/Storage/components-guide-8/flow_picker_icon.png) and map the function name using the [Flow Picker](/smart/project-sample-how-to-guide/bind-page-flows-to-components) editor. **HideToggle: **Used to hide/show the expansion indicator icon expansion icon. Defaults to False. If set to True, hides the icon, else select False.**[expanded]:** Enter True if you want the panel expanded by default. Else, enter False. This filed also accepts any type of value to indicate that the panel is expanded. **(afterCollapse): **Create a [page flow](/smart/project-sample-how-to-guide/design-page-flows) to define the function that is to be run after the expansion panel body's collapse animation happens. You can enter the function name of the page flow directly here or click ![flow picker icon](/resources/Storage/components-guide-8/flow_picker_icon.png) and map the function name using the [Flow Picker](/smart/project-sample-how-to-guide/bind-page-flows-to-components) editor. **(afterExpand): **Create a [page flow](/smart/project-sample-how-to-guide/design-page-flows) to define the function that is to be run after the expansion panel body's expand animation happens. You can enter the function name of the page flow directly here or click ![flow picker icon](/resources/Storage/components-guide-8/flow_picker_icon.png) and map the function name using the [Flow Picker](/smart/project-sample-how-to-guide/bind-page-flows-to-components) editor. **Disabled:** Defaults to False. If set to True, disable the component. A disabled Expansion panel can't be toggled by the user, but can still be manipulated programmatically.**(destroyed):** Create a [page flow](/smart/project-sample-how-to-guide/design-page-flows) to define the function that is to be run when the expansion panel is destroyed. You can enter the function name of the page flow directly here or click ![flow picker icon](/resources/Storage/components-guide-8/flow_picker_icon.png) and map the function name using the [Flow Picker](/smart/project-sample-how-to-guide/bind-page-flows-to-components) editor. **id: **The unique ID for the Expansion Panel. This is used to uniquely identify this expansion panel from the others.

### Examples

To learn how to use this component, see the examples documented in [Expansion Panel Outlet](/articles/components-guide-8/expansion-panel-outlet).
