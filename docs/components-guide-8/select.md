# Select

<https://documentation.neutrinos.com/articles/#!components-guide-8/select>

## Select

### Overview

The **Select** component is used for selecting a value from a set of options. It creates a drop-down list of options for a web form. The select element creates the list and each option element is displayed as an available option on the list.

### How to use

1. Drag and drop the Select component.
2. Double click the component to display the list of attributes that can be used with it.
3. Fill the attributes which are needed and save the page.

### Associated Attributes

- **Style:** It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height: 200px ;).
- **Class**: The Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1, class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **Placeholder**: The display name of the Select component.
- **dataSource**: An Array (which is defined in a user-defined location) from which the drop-down list of options must be displayed. For example: To display the following array options which are defined in the TS editor of a page, you call the array name state in the datasource field.

```javascript
state = [   {value: 'delhi-0', viewValue: 'Delhi'},   {value: 'mumbai-1', viewValue: 'Mumbai'},   {value: 'pune-2', viewValue: 'Pune'} ];
```

- **formControlName**: A directive that assigns a string for the form module to lookup the control by name.
- **Group Options**: If set to True, allows you to set up a complex select field where options can be grouped into categories. The data source array that is used to define the categories has to be a complex JSON object such as:

```json
PokemonGroup = [    {      name: 'Grass',      pokemon: [        {value: 'bulbasaur-0', viewValue: 'Bulbasaur'},        {value: 'oddish-1', viewValue: 'Oddish'},        {value: 'bellsprout-2', viewValue: 'Bellsprout'}      ]    },    {      name: 'Water',      disabled: true,      pokemon: [        {value: 'squirtle-3', viewValue: 'Squirtle'},        {value: 'psyduck-4', viewValue: 'Psyduck'},        {value: 'horsea-5', viewValue: 'Horsea'}      ]    }    ];
```

If this property is set to True, the following fields are displayed and are required to be filled:

- **[groupLabels]**: The name of the categories that you want to show in the drop-down list. The groups from the above example can be inserted by entering option.name in this field.
- **[disableGroup]**: The Boolean value initialized in the complex **JSON** object to enable or disable the respective group. For example, option.disabled.
- **[optionDatasource]**: The options that are to be displayed under each category. The options from the above example can be inserted by entering option.pokemon in this field. On doing this, in the background, an object called subOption will be created which handles the iteration of the values and view values.

| ![Information](/resources/Storage/components-guide-8/info.png) | If Group Options is enabled, the following attributes should be set as follows:optionValue: subOption.valueoptionView: {{subOption.viewValue}} |
| --- | --- |

- **optionValue**: The value associated with the option selected from the drop-down list. From the above example, if you select **Delhi **from the Select list, the value **delhi-0** is selected. This can be achieved by providing **option.value** in this attribute. To provide the option value, in the background, an object reference called **option** is created. Using this object reference, a user can navigate to the object keys inside the array.

- **optionView**: The view value associated with the option selected from the drop-down list. To provide this value, in the background, an object reference called option is created. Using this object reference, a user can navigate to the object keys inside the array. For example, {{option.viewValue}}.
- **[(ngModel)]**: Used for two-way data binding. The ngmodel attribute is used to bind the data in your model to the view presented to the user.

- **[(value)]**: Value of the select control.
- **Required:** Indicate whether the component is required.
- **Form Field Appearance**: Different appearance variants that can be set for the form field. Options include:
  - The **legacy appearance** is the default style that the form-field has traditionally had. It shows the input box with an underlines underneath it.
  - The** standard appearance** is a slightly updated version of the legacy appearance that has spacing that is more consistent with the fill and outline appearances.
  - The **fill appearance** displays the form field with a filled background box in addition to the underline.
  - The **outline appearance** shows the form field with a border all the way around (not just an underline).

- **Float Label**: The label animation in the Select component. The options include:
  - **Auto**
  - **Never**
  - **Always**
- **Disable Ripple**: By default, when a user clicks on the Select component, a ripple animation is shown. This can be disabled by setting this property value to **True**.
- **Multiple Select**: If you choose this option, the app will allow users to select multiple values at once.
  - **CustomTriggerValue**: The custom trigger text that you want to show in the Select list. For example, on selecting multiple options from the toppings list, if you want to show the selected option like the below screenshot, you can use the given code within this attribute.

```html
{{toppings.value ? toppings.value[0] : ''}}      <span *ngIf="toppings.value?.length > 1" class="example-additional-selection">        (+{{toppings.value.length - 1}} {{toppings.value?.length === 2 ? 'other' : 'others'}})      </span>
```

- **(openedChange)**: Event emitted when the select panel has been opened.
- **(selectionChange)**: Event emitted when the selected value has been changed by the user.
- **Add Select Options**: Options that are given by the user dynamically. You cannot categorize the select options using this attribute.
- **Select Style**: The style to be applied to the Select component. You can either select Basic (the Angular design) or Native (the HTML design).
- **panelClass**: The CSS classes to be entered into the selection panel when it is opened. Supports the same syntax as ngClass.
- **Disabled**: If set to True, the component will be disabled.
- **[errorStateMatcher]**: The object which matches user selections to error messages.
- **Errors**: A button used to enter custom error messages.
  - Add an error condition and the message that you want to show the user when such error occurs.
  - Click Save. When you save the page, an error block will be automatically created in Neutrinos Modelr to check for this error condition when the app is deployed.

### Example

1. In the **Page Flow Designer **of the page, add a page variable named **selected **in the Page Variable node of the On Init flow.
2. Navigate to the UI editor of the page, drag and drop the Select component to a page.
3. Double click the **Select **component and set the following properties:
  1. **Place Holder**: Select an option
  2. **[(value)]**: page.selected
  3. **Add Select Options**: Add three options as follows:
  4. Option 1:
    1. **Display name**: Green;
    2. **Value**: Option 1
  5. Option 2:
    1. **Display name**: Yellow
    2. **Value**: Option 2
  6. Option 3:![](/resources/Storage/components-guide-8/title-2021-10-19.png)
    1. **Display name**: Blue8
    2. **Value**: Option 3
4. Drag and drop an HTML 5 component and set the element type as **paragraph**.
5. Double click the HTML editor and enter You selected: {{page.selected}}
6. Save and run the page.
