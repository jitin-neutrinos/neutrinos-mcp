# Button

<https://documentation.neutrinos.com/articles/#!pulse-publication/input-fields-pages-wf-cm>

Input field components allow users to enter and interact with data within a form. These components enable structured data capture and user interaction based on the form’s requirements. Common input field components include buttons, date pickers, checkboxes, radio buttons, tables, text areas, and other controls.

## Button

A Button control allows users to initiate actions within a form. It is commonly used to submit entered data, clear form fields, or trigger other configured operations.




 To add a Button to the form, drag and drop the Button control from the Components panel onto the form canvas. After adding the control, you can configure its properties as required. The following image illustrates the Button control added to a form along with its customizable properties.




 ![button-component-basic-properties](/resources/Storage/pulse-publication/images/button-component-basic-properties.png)




 The following table lists all the customizable properties available for the Button control.

| **Property  ** | **  Value** |
| --- | --- |
| Label | Accepts a string value that is used as the display text (label) of the Button. |
| Style | You can select the Button style from the available options. The supported styles include Primary, Secondary, and Tertiary, which determine the visual appearance of the Button on the user interface. |
| Disabled | Enable this toggle to keep the Button disabled when the form loads. The Button can be enabled dynamically after a specified condition is met. |
| Tooltip | Accepts a string value that is displayed as tooltip text when the mouse pointer hovers over the Button. |
| PrefixIcon | Allows you to select an icon for the Button. The selected icon is displayed before the Button label. You can choose an icon from the dropdown list. |
| SuffixIcon | Allows you to select an icon for the Button. The selected icon is displayed after the Button label. You can choose an icon from the dropdown list. |

Additionally, a Button can be mapped to a CO, Case Instance, Task Instance, or a local object from the Dependency section. You can also define conditions within the Dependency section to control the Button’s visibility, allowing it to be shown or hidden dynamically based on specified criteria.

In addition to the basic configurable properties, a Button control can be associated with a trigger to invoke an **On Click** event. This event is triggered when a user clicks the Button. To configure a trigger for the Button control, navigate to the <b>Trigger</b> tab in the Properties panel and define the required trigger settings.




 For more information about configuring triggers, refer to the [Triggers](/smart/project-alpha-platform/triggers) topic.

## Checkbox

A Checkbox control enables users to select or deselect an option by toggling its state. It is primarily used to capture boolean values or allow users to choose one or more options from a set of independent selections.




 To add a Checkbox to the form, drag and drop the Checkbox control from the Components panel onto the form canvas. After adding the control, you can configure its properties as required. The following image illustrates the Checkbox control added to a form along with its customizable properties.




 ![checkbox-component-basic-properties](/resources/Storage/pulse-publication/images/checkbox-component-basic-properties.png)




 The following table lists all the customizable properties available for the Checkbox control.

| **Property  ** | **  Value** |
| --- | --- |
| Label | Accepts a string value. that is used as a display text (label) of the Checkbox. |
| Multi Select | Enables or disables the option to allow multiple selections for the Checkbox control. When this option is enabled, you can add multiple datasets containing different options for the Checkbox. Click the Plus (+) button to add additional options to the Checkbox control. By default, the multi-select option is disabled. |
| Orientation | Allows you to set the orientation of the Checkbox options. The available orientations are Horizontal and Vertical. |
| Binding | Allows you to bind the Checkbox control to a CO, Case Instance, Task Instance, or a local object. |
| Mandatory | Enable this toggle to make the Checkbox control a mandatory field. By default, this option is disabled. |
| Disabled | Enable this toggle to keep the Checkbox control disabled by default. |
| Read Only | Enable this toggle to make the Checkbox control read-only by default. When enabled, you can specify text that is displayed only when the Checkbox control is in a read-only state. |

Additionally, a Checkbox can be mapped to a CO, Case Instance, Task Instance, or a local object from the **Dependency** section. You can also define conditions within the **Dependency** section to dynamically control the Checkbox’s behavior, such as managing its visibility (show or hide), configuring it as editable, or enabling or disabling it based on specified criteria.

In addition to the basic configurable properties, a Checkbox control can be associated with a trigger to invoke an **On Change** event. This event is triggered whenever the value of the Checkbox changes, that is, when it transitions from checked to unchecked or vice versa. To configure a trigger for the Checkbox control, navigate to the **Trigger** tab in the Properties panel and define the required trigger settings.




 For more information about configuring triggers, refer to the [Triggers](/smart/project-alpha-platform/triggers) topic.

## Radio Button

A Radio Button control allows users to select a single option from a predefined group of mutually exclusive options. When multiple radio buttons are grouped, selecting one option automatically deselects any previously selected option within the same group.




 Radio buttons are typically used when users must choose only one value from a limited and clearly defined set of choices.

To add a Radio Button to the form, drag and drop the Radio Button control from the Components panel onto the form canvas. After adding the control, you can configure its properties as required. The following image illustrates the Radio Button control added to a form along with its customizable properties.




 ![radio-button-component-basic-properties](/resources/Storage/pulse-publication/images/radio-button-component-basic-properties.png)

The following table lists all the customizable properties available for the Radio Button control.

| **Property  ** | **  Value** |
| --- | --- |
| Label | Accepts a string value that is displayed as the label text for the Radio Button set. |
| Dataset | Accepts values that are displayed as options in the Radio Button list. Each option consists of a label displayed to the user and a corresponding value used for internal representation. |
| Orientation | Allows you to set the orientation of the Radio Button options. The available orientations are Horizontal and Vertical. |
| Binding | Allows you to bind the Radio Button control to a CO, Case Instance, Task Instance, or a local object. |
| Read Only | Enable this toggle to make the Checkbox control read-only by default. When enabled, you can specify text displayed only when the Radio Button control is read-only. |
| Mandatory | Enable this toggle to make the Radio Button control a mandatory field. By default, this option is disabled. |

Additionally, a Radio Button can be mapped to a CO, Case Instance, Task Instance, or a local object from the **Dependency** section. You can also define conditions within the **Dependency** section to control the Radio Button’s behavior dynamically, such as managing its visibility (show or hide), setting it as required, or configuring it as editable or read-only based on specified criteria.

In addition to the basic configurable properties, a Checkbox control can be associated with a trigger to invoke an **On Change** event. This event is triggered whenever the value of the Radio Button changes, that is, when it transitions from checked to unchecked or vice versa. To configure a trigger for the Radio Button control, navigate to the **Trigger** tab in the Properties panel and define the required trigger settings.




 For more information about configuring triggers, refer to the [Triggers](/smart/project-alpha-platform/triggers) topic.

## Text Area

A Text Area control allows users to enter multi-line textual information. Unlike a standard text field that accepts single-line input, a Text Area provides a larger input region designed to capture detailed or extended content. The Text Area is used when users are required to provide descriptive, explanatory, or long-form input that cannot be effectively captured in single-line fields.

To add a Text Area to the form, drag and drop the Text Area control from the Components panel onto the form canvas. After adding the control, you can configure its properties as required. The following image illustrates the Radio ButtonText Area control added to a form along with its customizable properties.




 ![text-area-component-basic-properties](/resources/Storage/pulse-publication/images/text-area-component-basic-properties.png)

The following table lists all the customizable properties available for the Radio Button control.

| **Property  ** | **  Value** |
| --- | --- |
| Label | Accepts a string value that is displayed as the label text for the Text Area. |
| Placeholder Text | Displays temporary text inside the Text Area as a hint before the user provides any input. The placeholder text appears in a muted (gray) color and is replaced when the user clicks inside the Text Area and begins entering a value. |
| Help Text | Displays contextual help text below the Text Area to provide additional information or guidance about the input that needs to be entered. |
| Binding | Allows you to bind the Checkbox control to a CO, Case Instance, Task Instance, or a local object. |
| MinLength | Accepts an integer value that specifies the minimum number of characters that must be entered in the Text Area. |
| MaxLength | Accepts an integer value that specifies the maximum number of characters allowed in the Text Area. |
| Read Only | Enable this toggle to make the Text Area control read-only by default. When enabled, the Text Area functions as a label and does not accept any user input. |
| Mandatory | Enable this toggle to make the Text Area control a mandatory field. This option is disabled by default. When enabled, you can specify a display text that is shown when no value is provided for this field. |

Additionally, a Text Area can be mapped to a CO, Case Instance, Task Instance, or a local object from the **Dependency **section. You can also define conditions within the **Dependency **section to dynamically control the Text Area’s behavior, such as managing its visibility (show or hide), configuring it as editable, or enabling or disabling it based on specified criteria.

In addition to the basic configurable properties, a Text Area control can be associated with a trigger to invoke an **On Text Change** event. This event is triggered whenever the value in the Text Area changes. To configure a trigger for the Text Area control, navigate to the **Trigger** tab in the Properties panel and define the required trigger settings.




 For more information about configuring triggers, refer to the [Triggers](/articles/pulse-publication/triggers-component-window-wf-cm) topic.
