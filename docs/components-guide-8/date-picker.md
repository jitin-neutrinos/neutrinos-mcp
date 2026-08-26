# Date Picker

<https://documentation.neutrinos.com/articles/#!components-guide-8/date-picker>

## Date Picker

### Overview

The Datepicker component is used to present an interface that makes it easy for users to select the date. Tapping on the component will display a picker interface that can be used to select a date.

### Usage

Datepicker component is used to select the date easily instead of entering it manually.

### How to use

1. Drag and drop the **Date Picker **component.
2. Double click the component to display the list of attributes that can be used with it.
3. Fill the attributes which are needed and save the page.

### Associated Attributes

- **style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height:200px;).
- **class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the** Style** tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **placeholder**: Used to hold the defined text value. Example “Calendar” holds the value Calendar for the field.
- **Form Field Appearance**: Different appearance variants that can be set for the form field. **Options include**:
  - The legacy appearance is the default style that the form-field has traditionally had. It shows the Date Picker with an underline underneath it.
  - The standard appearance is a slightly updated version of the legacy appearance that has spacing that is more consistent with the fill and outline appearances.
  - The fill appearance displays the form field with a filled background box in addition to the underline.
  - The outline appearance shows the form field with a border all the way around (not just an underline).
- **Color**: A theme palette color for the component.
- **[dateClass]**: A function that is used to add custom CSS classes to dates.
- **panelClass**: CSS Classes to be passed to change the date picker panel style.
- **value**: Specify the new value for the target date picker input. Value has to be either null or the letter “D”.
- **[min]**: Specify the minimum valid date. The value should be either null or the letter “D”.
- **[max]**: Specify the maximum valid date. The value should be either null or the letter “D”.
- **[startAt]**: Specify the initial date to open the calendar. It should be in the format: D | null.
- **[calenderHeaderComponent]**: The header section of the calendar can be replaced with a custom component if desired. This is accomplished by using the calendarHeaderComponent property. This property takes a component class and constructs an instance of the component to use as the header.

- **Start View:** Specify the view that the calendar should start in. It should be in the format: 'month' | 'year'.
- **Touch UI:** Specify whether the calendar UI is in touch mode. In touch mode, the calendar opens in a dialog rather than a popup and elements have more padding to allow for bigger touch targets.
- **id**: Specify the id for the date picker calendar. The value should be a string.
- **(dateChange)**: An event emitted when the date is changed.
- **(dateInput)**: An event emitted when the user inputs the date.
- **Opened**: Specify whether the calendar is opened or not.
- **Disabled Datepicker**: This will disable the date picker component.
- **Disabled Icon**: Set to True to disable the Icon click. The date can be entered manually.
- **Disabled Input**: This will disable the input field. The date can be selected using icons.
- **(opened)**: An event called when the calendar is opened.
- **(closed)**: An event called when the calendar is closed.
- **[matDatepickerFilter]**: A function that can be used to filter dates within the date picker. The value should be given in this format: (date: D | null) => boolean(true or false) .
- **formControlName**: A directive that assigns a string for the form module to lookup the control by name.
- **[(ngModel)]**: Used for two-way data binding. The ng-model attribute is used to bind the data in your model to the view presented to the user.
- **name**: Specify the name for the date picker.
- **picker**: A custom reference ID for the date picker which can be used to access the component at a user-defined place. Example: click on the input field of the component
- **ngModel**: A component reference that is used for reading and writing control for components such as error, hint, state, etc of the date picker.
- **Required**: Indicate whether the component is required.
- **(yearSelected)**: An Event emitted when the year is selected.
- **(monthSelected):** An Event emitted when the month is selected.
- **customIcon**: The icon name given to the component.
- **Icon Position**: This defines the position of the Icon in the component.
  - **Prefix**: The icon is positioned to the left.
  - **Suffix**: The icon is positioned to the right. By default, the position of the icon is set to suffix.
- **(click)**: Event emitted when the date picker is clicked.
- **readonly**: Prevents the user from editing the date field.
- **Errors**: A button used to enter custom error messages.
  - Add an error condition and the message that you want to show the user when such error occurs.
  - Click Save. When you save the page, an error block will be automatically created in Neutrinos Modelr to check for this error condition when the app is deployed.
- **Hints**: These are additional descriptive text messages that appear below the form field's underline. Enter a Hint Condition and a Hint Message. An Input component can have up to two hint labels. Therefore, choose Start or End as the position of the hint element. Attempting to add multiple hints to the same side will raise an error.

### Example

1. In the **Page Flow Designer **of the page, create an **Events **flow. This flow displays events of the date picker component.
2. Update the **On Init** flow. Add the following page variable to the Page Variables node in the On Init flow:
3. Create another flow named **Events **flow. This flow displays events of the date picker component.
4. Drag and drop a **Start **node to the canvas and set the following properties:
  1. Enter the name of the node as **Events**.
  2. Add the following input variables:
5. Drag and drop a **Script node** and connect it to the Start node. Add the following code:
6. Navigate to the **UI designer** of the page.
7. Drag and drop a **Date Picker** component. Set the following properties:
  1. **Place Holder**: Choose a date
  2. **Color**: Primary
  3. **(dateChange)**: Click** Pick the Flow** button to open the Flow Picker editor. Select the **events **flow. Enter **'change'** for** type1** variable and **$event** for **event **variable. Save the settings.
  4. **(dateInput)**: Click** Pick the Flow** button to open the Flow Picker editor. Select the **events **flow. Enter **'input' ** for** type1** variable and **$event** for **event **variable. Save the settings.
  5. **customIcon**: keyboard_arrow_down
8. drag and drop the** HTML 5** component. Set the Element Type as **div**. In the custom properties add the following:
  1. ***ngFor**: let e of page.events
9. In the HTML editor, enter **{{e}}**
10. Save and run the page.
