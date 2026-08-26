# Projection

<https://documentation.neutrinos.com/articles/#!neutrinos-reels-publication/configurations>

This topic explains how to configure keys for testing rules, regardless of the rule type. Follow the steps below to configure the keys manually:

1. In the **Model Editor** tab for any rule type, click the **Configure** button (![](/resources/Storage/neutrinos-reels-publication/images/configure-icon.png)) next to the respective input key to open the configuration page:
    ![](/resources/Storage/neutrinos-reels-publication/images/configure-page.png)
2. Enter the below details:
    **Field
    **
    **
    Description**
    Field Name
    Accepts a key name, such as 'Age'.
    Placeholder Text
    Accepts the display text that appears to the user before they enter input.
    Select Field Type
    Allows you to set the type of value to be entered during rule testing. The value can be user input, a default value, a selection from a dropdown, or a date input.
  - **User Input**: Allows the field to be an input type, enabling users to enter a value while testing the rule. The GIF below illustrates the input key’s behavior during rule testing when configured as a user input. By default, it is set to User Input.
      ![user-input](/resources/Storage/neutrinos-reels-publication/images/testing-user-input.gif)
  - **Default**: Accepts a default value that can be set during rule design time and used while testing the rule. The GIF below illustrates the input key's behavior during rule testing when configured as a default input.
      ![default-value](/resources/Storage/neutrinos-reels-publication/images/testing-default-value.gif)
  - **Dropdown**: Accepts a predefined list of options that users can select during rule testing. These options can be specified manually. The GIF below illustrates the input key's behavior during rule testing when configured as a dropdown.
      ![dropdown](/resources/Storage/neutrinos-reels-publication/images/testing-dropdown.gif)
  - **Date**: Accepts a date input from the user. You can specify the required date format. The GIF below illustrates the input key's behavior during rule testing when configured as a date.
      ![date](/resources/Storage/neutrinos-reels-publication/images/testing-date.gif)

## Projection

Projection is a feature that determines which output keys are visible to upstream services. When projection is enabled for an output key, the key becomes available to upstream services. If projection is disabled, the key remains limited to its specific function scope and will not be available to the API.
 By default, the projection toggle is enabled. You can disable projection by turning off the projection toggle. The image below demonstrates how to disable the projection toggle, preventing the key from being available to upstream services.

![projection-disabled](/resources/Storage/neutrinos-reels-publication/images/projection-disabled.png)

For example, in a rule where the outputs are Status and Eligibility, disabling the projection for Status removes it from the output. The image below illustrates how the output appears when projection for the Status key is disabled.




 ![projection-disabled-json](/resources/Storage/neutrinos-reels-publication/images/projection-disabled-json.gif)

The GIF below illustrates the output when projection is enabled for both outputs.




 ![projection-enabled-json](/resources/Storage/neutrinos-reels-publication/images/projection-enabled-json.gif)

[Next Topic](/articles/neutrinos-reels-publication/rule-group)

[Previous Topic](/articles/neutrinos-reels-publication/sentiment-analysis-rule)
