# Overview

<https://documentation.neutrinos.com/articles/#!components-guide-8/autocomplete>

### Overview

**Autocomplete **is a normal input component that is enhanced by a panel of suggested options. It acts as a real-time suggestion box and displays suggestions as soon as the user types anything in the input area. It helps users avoid spelling errors and speeds up human-computer interactions when it correctly predicts the word a user intends to enter after only a few characters have been typed into a text input field.

### How to use

1. Drag and drop an** Input **component to the canvas.
2. Drag and drop an **Autocomplete** component to the canvas. Define a unique value for the component in the **matAutocomplete **field which can be used as a reference value to bind it to a input components on the page via** [matAutocomplete]** attribute.
    ![matAutocomplete](/resources/Storage/components-guide-8/matAuto.png)
3. Double click the **Input **component to open its attribute window and define a custom property of type **Key&Value** to indicate the unique value of the Autocomplete component is to be mapped to this field:
    ![mapping Autocomplete to Input component](/resources/Storage/components-guide-8/matAuto1.png)

### Associated Attributes

#### Basic Properties

- **Autocomplete label: **The display name for the autocomplete.
- **Style: **It accepts a string value and affects different properties (height, width, color, etc.) of the component based on the values provided as inline styling. For example-(background:orange;height:200px;).
- **Class: **It accepts space-separated class names that are defined in the [Styles](/articles/studio-guide-7/apply-global-styling) editor. For example, if the following CSS classes are defined in the **Styles** editor, then you can select them here to apply to this component. Copy CodeHTML.class1
   {
   border-radius:10px;
   flex-basis:10%;
   height:100px;
   }
   .class2
   {
   border-radius:10px;
   flex-basis:10%;
   height:100px;
   }

- **matAutoComplete:** Enter the unique identity value of the autocomplete component.

| ![Information](/resources/Storage/components-guide-8/project-component-docs-test/info.png) | Make sure you add **matAutoComplete = auto** in the custom property section of the input component that you are attaching the autocomplete component with. |
| --- | --- |

- ***ngFor:** ngFor is used to iterate through the array object and get the data. The syntax of *ngFor is *ngFor="let d of data | async" where d is a loop variable and data is an array or object from which the data will be accessed. Adding async to *ngFor is necessary when the dataset is of type observable.
- **Group options:** If set to True, allows you to set up autocomplete options where options can be grouped into categories. By default, it is set to False. See [Configuring Group Options](/articles/components-guide-8/autocomplete/a/h3_2002773352) to learn more.
- **optionView:** The view value associated with the option selected from the drop-down list. To provide this value, cretae an object reference called **option **in the page flow. Using this object reference, a user can navigate to the object keys inside the array. For example, {{option.viewValue}}.
- **[value]:** Value of the selected object from the array.

### Advanced Properties

- **Auto Active First Option:** Whether the first option should be highlighted when the autocomplete panel is opened. It can be configured globally through the MAT_AUTOCOMPLETE_DEFAULT_OPTIONS token.
- **Disable Ripple:** Whether ripples should be disabled or not.
- **[displayWith]: **To display the value on select.
- **[panelWidth]:** Specify the width of the autocomplete panel. It can be any CSS sizing value, otherwise, it will match the width of its host.
- **(closed):** The event to be emitted when the autocomplete panel is closed.
- **(opened):** The event to be emitted when the autocomplete panel is opened.
- **(optionSelected):** The event to be emitted when an item is selected from the drop-down list of autocomplete options.

### Configuring Group Options

If you set **Group Options** to true, you should configure these fields:

- **optionDatasource: **The options that are to be displayed under each category.
- **[label]:** The label for the group of options.

Before creating a grouped dataset, create an interface to identify a related set of data. You should also create a function called filter to filter the dataset according to the user's input. See **Example 2 **to learn more.

### Example

**Example 1: A simple auto-complete with 3 options**

![Autocomplete example 1](/resources/Storage/components-guide-8/matAuto3.png)

1. Drag and drop a **Form** component to the canvas.
2. Drag and drop an **Input** component inside the **Form** component.
3. Drag and drop an **Autocomplete **component inside the form. Make note of the matAutocomplete property value.
4. Double click the **Input** component and enter the following properties.
  - **Placeholder**: Pick a number
  - Define a custom property of type **Key&Value** to indicate which **Autocomplete** component is to be mapped to this field:
      ![mapping Autocomplete to Input component](/resources/Storage/components-guide-8/matAuto1.png)
  - In the custom properties section, select **Key&Value** and enter [matAutoComplete] in the key field and auto in the value field.
5. Navigate to the [Flow designer](/smart/project-concepts/page-designer/a/h3_520216706) of the page.
6. Update the [On Init flow](/smart/project-page-services-designer-guide/on-init-flow). Add the following page variable to the **Page Variables** node in the **On Init** flow:
    ![page variables node](/resources/Storage/components-guide-8/page_var.png)
7. Drag and drop a **Script **node to the **On Init** flow and add the following code:Copy CodeJavaScriptpage.options = ['One', 'Two', 'Three'];
8. Navigate back to the [UI designer](/smart/project-concepts/page-designer/a/h3__1090805748) of the page. In the properties window of the **Autocomplete** component, set the following attributes.
  - ***ngFo****r**: let option of page.options
  - **optionView**: {{option}}
  - **[value]: **option
9. Save and run the app.

**Example 2: Autocomplete with Grouped options and filters**

![Autocomplete example 2](/resources/Storage/components-guide-8/matAuto4.png)![Autocomplete example 2](/resources/Storage/components-guide-8/matAuto5.png)

1. Drag and drop a **Form** component to the canvas.
2. Drag and drop an **Input** component inside the **Form** component.
3. Drag and drop an **Autocomplete **component inside the form. Update the matAutocomplete property value to **auto2**.
4. Double click the **Input** component and enter the following properties.
  - **Placeholder**: state
  - Define a custom property of type **Key&Value** to indicate which **Autocomplete** component is to be mapped to this field. Select **Key&Value** and enter [matAutoComplete] in the key field and auto2 in the value field.
5. Navigate to the [Flow designer](/smart/project-concepts/page-designer/a/h3_520216706) of the page and design the following flows:
    ![Page flows for the Autocomplete component example](/resources/Storage/components-guide-8/autocomplete_flows.png)
6. Update the [On Init flow](/smart/project-page-services-designer-guide/on-init-flow). Add the following page variables to the **Page Variables** node in the **On Init** flow:
    ![page variables node](/resources/Storage/components-guide-8/page_var2.png)
  - The stateGroups page variable is used to define an array object for *ngFor to loop through.
  - The filteredOptions page variable is required to find the filtered option with the page.StateGroups value when you reload or filter the app.
7. Drag and drop a **Script **node to the **On Init** flow and add the following code:Copy CodeJavaScriptpage.stateGroups= [{
    letter: 'A',
    names: ['Alabama', 'Alaska', 'Arizona', 'Arkansas']
    }, {
    letter: 'C',
    names: ['California', 'Colorado', 'Connecticut']
    }, {
    letter: 'D',
    names: ['Delaware']
    }, {
    letter: 'F',
    names: ['Florida']
    }, {
    letter: 'G',
    names: ['Georgia']
    }, {
    letter: 'H',
    names: ['Hawaii']
    }, {
    letter: 'I',
    names: ['Idaho', 'Illinois', 'Indiana', 'Iowa']
    }, {
    letter: 'K',
    names: ['Kansas', 'Kentucky']
    }, {
    letter: 'L',
    names: ['Louisiana']
    }, {
    letter: 'M',
    names: ['Maine', 'Maryland', 'Massachusetts', 'Michigan',
    'Minnesota', 'Mississippi', 'Missouri', 'Montana']
    }, {
    letter: 'N',
    names: ['Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
    'New Mexico', 'New York', 'North Carolina', 'North Dakota']
    }, {
    letter: 'O',
    names: ['Ohio', 'Oklahoma', 'Oregon']
    }, {
    letter: 'P',
    names: ['Pennsylvania']
    }, {
    letter: 'R',
    names: ['Rhode Island']
    }, {
    letter: 'S',
    names: ['South Carolina', 'South Dakota']
    }, {
    letter: 'T',
    names: ['Tennessee', 'Texas']
    }, {
    letter: 'U',
    names: ['Utah']
    }, {
    letter: 'V',
    names: ['Vermont', 'Virginia']
    }, {
    letter: 'W',
    names: ['Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
    }];
   // To find the filtered option with the page.StateGroups value when you reload or filter the app.
   page.filteredOptions = page.stateGroups;
8. Create another page flow to filter the dataset according to the user's input. For example, if the user types **F **in the input field, only state names starting from **F** are displayed in the drop-down list. Drag and drop a Start node to the canvas and set the following properties:
  1. Enter the name of the node as** filterdata**.
  2. Add an** input variable** called** filter **of type **any**.
      ![the start node to filter data](/resources/Storage/components-guide-8/start_node.png)
9. Drag and drop a **Script** node and connect it to the **Start** node. Add the following code:Copy CodeJavaScriptconsole.log(bh.input.filter.target.value);
   page.filteredOptions = page.stateGroups.filter(el=>el.letter === bh.input.filter.target.value);
10. Save the changes.
11. Navigate back to the [UI designer](/smart/project-concepts/page-designer/a/h3__1090805748) of the page. In the properties window of the **Autocomplete** component, set the following attributes.
  - ***ngFo****r**: let group of page.filteredOptions
  - **Group Options:** True
  - **optionView**: {{option}}
  - **[value]: **option
  - **[optionDatasource]:** group.names
  - **[label]: **group.letter
12. Open the properties window of the** Input** component and add a custom property of type **Key&Value**. Enter the key as (input) and the value as **filter**. Click **![](/resources/Storage/components-guide-8/flow_picker_icon.png)** to open the [Flow Picker](/smart/project-sample-how-to-guide/bind-page-flows-to-components) editor. Select the filterdata flow and enter $event in the **Enter value for filter** field to the right. Save the settings.
    ![](/resources/Storage/components-guide-8/filter_data.png)
13. Navigate back to the app and save the app.
14. Preview the app.
