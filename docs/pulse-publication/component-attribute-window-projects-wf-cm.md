# Basic Attributes

<https://documentation.neutrinos.com/articles/#!pulse-publication/component-attribute-window-projects-wf-cm>

Components are UI controls used to structure and design a form layout. Each component includes a set of attributes that can be customized.

## Basic Attributes

To access the attribute double-click the component. The table below outlines the available components and their supported attributes.

| **  Component   ** | **   Attribute   ** | **   Description  ** |
| --- | --- | --- |
| Panel | Panel Properties |  |
| Title Text | The **Title Text** dropdown indicates whether the Title Text field accepts a **String **or **Language **value. If Language is selected, the value entered in the Value textbox can be translated into multiple languages.     **Value**: The Value text box accepts the string displayed as the Panel's name. |  |
| Select Icon | You can select an icon to display alongside the component's name. This enhances the component's visual presentation, making it more engaging and visually meaningful. |  |
| Additional Properties |  |  |
| Collapsible | An additional property enables the panel to have collapsible behavior, minimizing the space it occupies on the screen. When the **Collapsible **toggle is enabled, users can minimize and maximize the panel at runtime. By default, this is turned off.      **Note**: Collapsible behavior is unique to the Panel component, providing a distinctive way to manage screen space. |  |
| Collapsed | You can set the panel to load in a collapsed state by enabling the **Collapsed **toggle. When this option is enabled, the panel is initially collapsed, and users must expand it to access the controls.      **Note**: This collapsed behavior is unique to the Panel component. |  |
| Dependencies | Comparison operators allow you to evaluate the **Mapping Type** and its **Value **against a check value. Depending on the result, you can configure the Panel or Column to either be hidden or visible.     **Note**: You can multiple dependencies using the **Plus** icon. |  |
| Column | Section Properties |  |
| Title Text | The **Title Text** dropdown indicates whether the Title Text field accepts a **String **or **Language **value. If Language is selected, the value entered in the Value textbox can be translated into multiple languages.      **Value**: The Value text box accepts the string displayed as the Column's name. |  |
| Select Icon | You can select an icon to display alongside the component's name. This enhances the component's visual presentation, making it more engaging and visually meaningful. |  |
| Dependencies | Comparison operators allow you to evaluate the **Mapping Type** and its **Value **against a check value. Depending on the result, you can configure the Column to either be **hidden **or **visible**.     **Note**: You can multiple dependencies using the **Plus** icon. |  |
| Document Viewer | Label Properties |  |
| Label | The **Label** dropdown indicates whether the **Label **field accepts a **String** or **Language** value. If **Language** is selected, the value entered in the Value textbox can be translated into multiple languages.    **Value**: The Value text box accepts the string displayed as the Document Viewer's name. |  |
| Additional Properties |  |  |
| Enable Toolbar (Top) | Enable the toggle to display the Toolbar at the top of the Document Viewer. By default, this toggle is disabled. |  |
| Display Single Document | This toggle allows a user to view a single document or file in isolation, rather than viewing multiple documents or items simultaneously. When this option is enabled, only one document will be shown at a time in the viewer interface, making it easier for the user to focus on or interact with that specific document. By default, this toggle is disabled. |  |
| Display Metadata | Displays the metadata for the file provided during the file upload process in DMS. The metadata displayed in the Document Viewer can be configured by adding a column name and its value in the columns section. |  |
| Source Properties |  |  |
| Data Source | Select a **Data Source** from the dropdown to bind the Document Viewer component to display at runtime.    After selecting a Data Source, the **Select Operation** dropdown is shown. Choose the operation the end user will perform using the component.    **Note**: This is a **mandatory **field for Document Viewer component. |  |
| Dependencies | Comparison operators allow you to evaluate the **Mapping Type** and its **Value **against a check value. Depending on the result, you can configure the Document Viewer to either Show, Hide, Editable, Enabled, Disabled, Required, or Readonly.      **Note**: You can multiple dependencies using the **Plus** icon. |  |
| Button | Button Properties |  |
| Label | The **Label** dropdown indicates whether the **Label **field accepts a **String** or **Language** value. If **Language** is selected, the value entered in the Value textbox can be translated into multiple languages.    **Value**: The Value text box accepts the string displayed as the Button's name. |  |
| Style | Select a style for the button from the available options in the **Style **dropdown: **Primary**, **Secondary**, or **Tertiary**. |  |
| Additional Properties |  |  |
| Disabled | The button on the form can be disabled by toggling the Disabled option. By default, this toggle is off. |  |
| Tooltip | A **tooltip** is a hint text displayed when the user hovers the mouse over the button. You can set the tooltip value to either String or Language from the Label dropdown. If 'Language' is selected, the value entered in the Value textbox can be translated into multiple languages.      **Value**:  The Value text box accepts the string displayed as the tooltip. |  |
| PrefixIcon | Select an icon to be displayed before the text on the button. |  |
| sufixIcon | Select an icon to be displayed after the text on the button. |  |
| Dependencies | Comparison operators allow you to evaluate the **Mapping Type** and its **Value **against a check value. Depending on the result, you can configure the Button to either **Show**, **Hide**, **Enabled**, or **Disabled**.      **Note**: You can multiple dependencies using the **Plus** icon. |  |
| Checkbox | Label Properties |  |
| Label | The **Label** dropdown indicates whether the **Label **field accepts a **String** or **Language** value. If **Language** is selected, the value entered in the Value textbox can be translated into multiple languages.    **Value**: The Value text box accepts the string displayed as the Checkbox's name. |  |
| Checkbox Properties |  |  |
| Multi Select | A toggle that enables the addition of multiple options and the selection of multiple values under the same component name. By default, the Multi Select toggle is disabled, allowing only one checkbox to be available for selection. When enabled, the Multi Select toggle allows users to choose from multiple values in the component. |  |
| Dataset | If the **Multi Select** toggle is enabled, you can define multiple options by specifying a display label and value for each option, which users can choose from. |  |
| Options |  |  |
| orientation | Select the orientation from the dropdown for displaying the checkbox. By default, it is Horizontal. |  |
| Binding Variable | Bind the checkbox component to an option from available list in the **Select **dropdown.    Enter the value to bind the checkbox in the provided text box. |  |
| Validation |  |  |
| Mandatory | Enable the Mandatory toggle to require the user to select a value in the checkbox. By default, the toggle is disabled.     When enabled, specify an error message in the textbox to inform users. |  |
| Additional Properties |  |  |
| Disabled | The Disabled toggle disables the checkbox component, making it unavailable for use. By default, the toggle is disabled. |  |
| Read Only | The Read Only toggle removes the tick box option from the checkbox component, making it appear as a simple label. By default, the toggle is disabled. |  |
| Dependencies | Comparison operators allow you to evaluate the **Mapping Type** and its **Value **against a check value. Depending on the result, you can configure the **Checkbox **to either **Hide**, **Show**, **Editable**, **Enabled**, **Disabled**, **Required**, or **Readonly**.    **Note**: You can multiple dependencies using the **Plus** icon. |  |
| Date Picker | Label Properties |  |
| Label | The **Label** dropdown indicates whether the **Label **field accepts a **String** or **Language** value. If **Language** is selected, the value entered in the Value textbox can be translated into multiple languages.      **Value**: The Value text box accepts the string displayed as the Date Picker's name. |  |
| Date Picker Properties |  |  |
| Date Format | Configure the date format displayed by the Date Picker by choosing an option from the dropdown. The default format is `DD{s}MM{s}YYYY`, where `{s}` indicates the separator character.      **Note**: The selected date is saved as an ISO string. |  |
| Time Format | Configure the time format displayed by the Date Picker by choosing from the available options in the dropdown. By default, the format is `HH:MM` (12-hour format).      **Note**: The final value is saved as an ISO string. |  |
| Separator | Choose a separator character for the format from the available options in the dropdown. The default separator is a hyphen. |  |
| Help Text | Help text appears below the component to guide users in providing the correct value format.       The **help text **dropdown indicates whether the **help text **field accepts a **String** or **Language** value. If **Language** is selected, the value entered in the Value textbox can be translated into multiple languages.         You can define the hint format in the **Value **field. |  |
| Days not allowed | Specify the days that the user cannot select in the component. By default, Saturday and Sunday are selected. |  |
| Binding Variable | Select the value to bind the component. Choose the type available in the list of option of binding values.       Enter the value to bind the Date Picker in the provided text box. |  |
| Enable Time | To display time in the Date Picker component, enable the **Enable Time** toggle. The toggle is disabled by default. |  |
| Start week on Monday | Enable the **Start week on Monday** toggle to set the week to start from Monday in the component. The toggle is enabled by default. |  |
| Future Dates | Enable this toggle to display future dates in the Date Picker component. If disabled, future dates will not be visible to the end user. The toggle is enabled by default. |  |
| Past Dates | Enable this toggle to display past dates in the Date Picker component. If disabled, past dates will not be visible to the end user. The toggle is enabled by default. |  |
| Allow Input | Enable this toggle to let users manually input a date in the Date Picker component. By default, this toggle is disabled. |  |
| Readonly | Enable this toggle to set the Date Picker component to Readonly. When enabled, the user can not select the dates using this component. By default, the toggle is disable. |  |
| Mandatory | Enable the **Mandatory** toggle to make selecting a value in the Date Picker mandatory. By default, the toggle is disabled. When enabled, specify an error message in the textbox to inform users. |  |
| Dependencies | Comparison operators allow you to evaluate the **Mapping Type** and its **Value **against a check value. Depending on the result, you can configure the **Checkbox **to either **Show**, **Hide**, **Editable**, **Required**, or **Readonly**.    **Note**: You can multiple dependencies using the **Plus** icon. |  |
| Dropdown | Label Properties |  |
| label | The **label** dropdown indicates whether the **label **field accepts a **String** or **Language** value. If **Language** is selected, the value entered in the Value textbox can be translated into multiple languages.        **Value**: The Value text box accepts the string displayed as the Dropdown's name. |  |
| Dropdown Properties |  |  |
| placeholder | A placeholder displays text within a control when no value is selected or entered, and it disappears as soon as a value is input.      The **placeholder **dropdown indicates whether the **placeholder **field accepts a **String** or **Language** value. If **Language** is selected, the value entered in the Value textbox can be translated into multiple languages.        **Value**: The Value text box accepts the string displayed as the Dropdown's placeholder text. |  |
| help text | Help text is displayed beneath the component to guide the user in entering the correct value format. Help text is always visible, regardless of whether a value has been entered in the component.      The **help text **dropdown indicates whether the **help text **field accepts a **String** or **Language** value. If **Language** is selected, the value entered in the Value textbox can be translated into multiple languages.        **Value**: The Value text box accepts the string displayed as the Dropdown's help text. |  |
| Options | Select a data source for the dropdown from the list of available options. Note: A data source must be specified for this component to function. |  |
| Binding Variable | Select the value to bind the component. Choose the type available in the available list of option of binding values.       Enter the value to bind the Dropdown in the provided text box. |  |
| Additional Properties |  |  |
| Mandatory | Enable the **Mandatory** toggle to make selecting a value in the Date Picker mandatory. By default, the toggle is disabled. When enabled, specify an error message in the textbox to inform users. |  |
| Multi Select | Enable the **Multi Select** toggle to allow users to select multiple values from the dropdown. By default, this toggle is disabled, restricting the dropdown to a single selection. |  |
| Dropdown Search | Enable the **Dropdown Search** toggle to let users search for values in the dropdown. By default, the toggle is disabled, limiting the dropdown to a standard selection without search functionality. |  |
| Readonly | Enable this toggle to set the Dropdown component to Readonly. When enabled, the user can not select the options available in this component. By default, the toggle is disable. |  |
| Dependencies | Comparison operators allow you to evaluate the **Mapping Type** and its **Value **against a check value. Depending on the result, you can configure the **Dropdown **to either **Show**, **Hide**, **Editable**, **Required**, or **Readonly**.    **Note**: You can multiple dependencies using the **Plus** icon. |  |
| Dynamic Input | Label Properties |  |
| Label | The **Label** dropdown indicates whether the **label **field accepts a **String** or **Language** value. If **Language** is selected, the value entered in the Value textbox can be translated into multiple languages.    **Value**: The Value text box accepts the string displayed as the Dynamic Input's name. |  |
| Dynamic Input Properties |  |  |
| Placeholder Text | A placeholder displays text within a control when no value is selected or entered, and it disappears as soon as a value is input.   The **placeholder **dropdown indicates whether the **placeholder **field accepts a **String** or **Language** value. If **Language** is selected, the value entered in the Value textbox can be translated into multiple languages.     **Value**: The Value text box accepts the string displayed as the Dynamic Input's placeholder text. |  |
| Binding Variables | Select the value to bind the component by choosing a binding type from the available options. Then, enter the binding value for the **Dynamic Input** in the provided text box. |  |
| Validations |  |  |
| MinLength | Set the minimum number of characters required in the Dynamic Input component. If the user input does not meet this requirement, an error message is shown. You can specify the error message in the provided text box. |  |
| MaxLength | Specify the maximum number of characters allowed in the Dynamic Input component. If the user input exceeds this limit, an error message will be displayed. Enter the error message in the provided text box. |  |
| MinItems | Set the minimum number of inputs required for the Dynamic Input component. If the user fails to meet the specified requirement, an error message will be displayed. You can define the error message in the provided text box. |  |
| Additional Properties |  |  |
| MaxItems | Restrict the user by specifying a maximum number of inputs that can be added for the Dynamic Input component. You can set the maximum number of inputs allowed by entering a value in the specified text box. For example, if you set the maximum to 3, the user cannot add more than 3 inputs to the component. |  |
| Readonly | Enable this toggle to set the Dynamic Input component to Readonly. When enabled, the user can not enter in the component. By default, the toggle is disable. |  |
| Disabled | Enable this toggle to make the Dynamic Input component disabled. |  |
| Mandatory | Enable the **Mandatory** toggle to make entering value in the Dynamic Input component mandatory. By default, the toggle is disabled. When enabled, specify an error message in the textbox to inform users. |  |
| Dependencies | Comparison operators allow you to evaluate the **Mapping Type** and its **Value **against a check value. Depending on the result, you can configure the **Dynamic Input **to either **Show**, **Hide**, **Editable**, **Enabled**, or **Disabled**.    **Note**: You can multiple dependencies using the **Plus** icon. |  |
| Radio Button | Label Properties |  |
| Label | The **Label** dropdown indicates whether the **label **field accepts a **String** or **Language** value. If **Language** is selected, the value entered in the Value textbox can be translated into multiple languages.     **Value**: The Value text box accepts the string displayed as the Radio Button's name. |  |
| Radio Button Properties |  |  |
| Dataset | Add the Dataset using the **Plus **icon. You can enter the label and value for each dataset item in their respective text boxes. |  |
| Options |  |  |
| orientation | You can choose between **Horizontal** and **Vertical** orientations. |  |
| Binding Variables | Select the value to bind the component by choosing a binding type from the available options. Then, enter the binding value for the **Radio Button **in the provided text box. |  |
| Additional Properties |  |  |
| Readonly | Enable this toggle to set the Radio Button component to Readonly. When enabled, the user can not select using the component. By default, the toggle is disable. |  |
| Mandatory | Enable the **Mandatory** toggle to make selecting value from the Radio Button component mandatory. By default, the toggle is disabled. When enabled, specify an error message in the textbox to inform users. |  |
| Dependencies | Comparison operators allow you to evaluate the **Mapping Type** and its **Value **against a check value. Depending on the result, you can configure the **Radio Button **to either **Show**, **Hide**, **Required**, **Editable**, or **Readonly**.    **Note**: You can multiple dependencies using the **Plus** icon. |  |
| Table | Additional Properties |  |
| Enable Refresh Icon | Enable this toggle to display a **Refresh** icon at the top of the table.   By default, this option is disabled. |  |
| Data Source | Select a data source for the **Table** from the list of available options.   **Note:** A data source must be specified for this component to function.    After selecting a data source, additional options will be available depending on the type of data source chosen. Configure these options to reflect the data in the table.    **Note**: If the data source is CO, you can add Columns based on the values retrieved from CO. |  |
| Actions | Enable the **Action** toggle to configure specific actions for the **Table **component. For each listed action, you can specify a value and select an icon. Additionally, you can add triggers to define how the actions should be executed.   **Note**: The action is added for each row in the table. |  |
| Pagination | You can enable the Pagination toggle to divide large datasets into smaller, manageable chunks (pages) for display in a table. |  |
| Dependencies | Comparison operators allow you to evaluate the **Mapping Type** and its **Value **against a check value. Depending on the result, you can configure the **Table **to either **Show **or **Hide**.    **Note**: You can multiple dependencies using the **Plus** icon. |  |
| Text Area | Label Properties |  |
| Label | The **Label** dropdown indicates whether the **label **field accepts a **String** or **Language** value. If **Language** is selected, the value entered in the Value textbox can be translated into multiple languages.     **Value**: The Value text box accepts the string displayed as the Text Area's name. |  |
| Text Area Properties |  |  |
| Placeholder Text | A placeholder displays text within a control when no value is selected or entered, and it disappears as soon as a value is input. The **placeholder **dropdown indicates whether the **placeholder **field accepts a **String** or **Language** value. If **Language** is selected, the value entered in the Value textbox can be translated into multiple languages.      **Value**: The Value text box accepts the string displayed as the **Text Area's** placeholder text. |  |
| Help Text | Help text is displayed beneath the component to guide the user in entering the correct value format. Help text is always visible, regardless of whether a value has been entered in the component.      The **help text **dropdown indicates whether the **help text **field accepts a **String** or **Language** value. If **Language** is selected, the value entered in the Value textbox can be translated into multiple languages.        **Value**: The Value text box accepts the string displayed as the **Text Area's** help text. |  |
| Binding Variables | Select the value to bind the component by choosing a binding type from the available options. Then, enter the binding value for the **Text Area **in the provided text box. |  |
| Validations |  |  |
| MinLength | Set the minimum number of characters required in the **Text Area** component. If the user input does not meet this requirement, an error message is shown. You can specify the error message in the provided text box. |  |
| MaxLength | Specify the maximum number of characters allowed in the **Text Area** component. If the user input exceeds this limit, an error message will be displayed. Enter the error message in the provided text box. |  |
| Additional Properties |  |  |
| Readonly | Enable this toggle to set the Text Area component to Readonly. When enabled, the user can not enter in the component. By default, the toggle is disable. |  |
| Mandatory | Enable the **Mandatory** toggle to enter value from the **Text Area** component mandatory. By default, the toggle is disabled. When enabled, specify an error message in the textbox to inform users. |  |
| Dependencies | Comparison operators allow you to evaluate the **Mapping Type** and its **Value **against a check value. Depending on the result, you can configure the **Text Area **to either **Show,** **Hide**, **Editable**, **Enabled**, or **Disabled**.    **Note**: You can multiple dependencies using the **Plus** icon. |  |
| Input Field | Label Properties |  |
| Label | The **Label** dropdown indicates whether the **label **field accepts a **String** or **Language** value. If **Language** is selected, the value entered in the Value textbox can be translated into multiple languages.       **Value**: The Value text box accepts the string displayed as the Input Field's name. |  |
| Input Field Properties |  |  |
| Placeholder Text | A placeholder displays text within a control when no value is selected or entered, and it disappears as soon as a value is input. The **placeholder **dropdown indicates whether the **placeholder **field accepts a **String** or **Language** value. If **Language** is selected, the value entered in the Value textbox can be translated into multiple languages.        **Value**: The Value text box accepts the string displayed as the **Input Field's** placeholder text. |  |
| Help Text | Help text is displayed beneath the component to guide the user in entering the correct value format. Help text is always visible, regardless of whether a value has been entered in the component.    The **help text **dropdown indicates whether the **help text **field accepts a **String** or **Language** value. If **Language** is selected, the value entered in the Value textbox can be translated into multiple languages.       **Value**: The Value text box accepts the string displayed as the **Input Field's** help text. |  |
| Field Type | Set the type of data that Input Field component accepts from the user. Choose the available option from the dropdown. |  |
| Binding Variables | Select the value to bind the component by choosing a binding type from the available options. Then, enter the binding value for the **Input Field **in the provided text box. |  |
| Validation |  |  |
| Minimum | Set the minimum value the component can accept. If the value fails to match, you can display an error message to the user by specifying the message in the text box provided. |  |
| Maximum | Set the maximum value the component can accept. If the user exceeds this, an error message is displayed. You can set the error message in the text box provided. |  |
| MinLength | Set the minimum number of characters required for the Input Field component. If the user input does not meet this requirement, an error message will be displayed. You can define the error message in the provided text box. |  |
| MaxLength | Specify the maximum number of characters allowed in the Input Field component. If the user input reaches this limit they are restricted from entering in the component. |  |
| Regex Pattern | Set the regular expression pattern to validate the user input in the component. If the input does not match the pattern, an error message can be displayed. Enter the error message in the provided text box. |  |
| Additional Properties |  |  |
| PrefixIcon | Select an icon to be displayed at the start of **Input Field** component. |  |
| suffixIcon | Select an icon to be displayed at the end of **Input Field** component. |  |
| Readonly | Enable this toggle to set the Input Field component to Readonly. When enabled, the user can not enter in the component. By default, the toggle is disable. |  |
| Mandatory | Enable the **Mandatory** toggle to enter value from the **Input Field** component mandatory. By default, the toggle is disabled. When enabled, specify an error message in the textbox to inform users. |  |
| Dependencies | Comparison operators allow you to evaluate the **Mapping Type** and its **Value **against a check value. Depending on the result, you can configure the **Input Field **to either **Show,** **Hide**, **Editable**, **Enabled**, **Disabled**, **Required**, or **Readonly**.      **Note**: You can multiple dependencies using the **Plus** icon. |  |

[Go to Top](/articles/pulse-publication/component-attribute-window-projects-wf-cm/a/Top)
