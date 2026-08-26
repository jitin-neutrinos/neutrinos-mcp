# Using Constants

<https://documentation.neutrinos.com/articles/#!neutrinos-reels-publication/script-rule>

The Script rule allows you to create and execute custom code, enabling complex logic beyond standard rule capabilities. This topic explains how to configure and deploy Script rule in the Reels Platform.

Steps to Create, Manage, and Map Data in a Script Rule:

1. Click the **Rules** button in the left-side navigation bar to open the Rules List page. This page displays a list of rules created in the Reels platform in a tabular format, including details such as the Rule Name, Rule ID, Version, Rule Type, Author, Date of Creation, and Last Updated Date.
2. Click the **Add** button on the top right of the **Rule list** page > Click **Rule** from the dropdown options.
    ![rule-add-button](/resources/Storage/neutrinos-reels-publication/images/rule-add-button.png)
3. In the pop-up window, enter a **Rule Name**, add a description for the rule that describes the purpose of the rule or its functionality, and select **Script Rule** as the Rule Type.
    ![add-script-rule](/resources/Storage/neutrinos-reels-publication/images/rule-add-script-rule.png)
4. Click the **Create** button to create the rule.
5. When a rule is created, the Rule Details page opens, allowing you to configure the rule. This page displays key information about the rule, including Version, Status, Last Updated date, Created Date, Deployment ID, and more.
    Additionally, the following sections provide further details:
    ![script-rule-details-page](/resources/Storage/neutrinos-reels-publication/images/add-rule-script-rule-rules-details-page.png)
  - **Description**: Displays the rule description.
  - **Constants**: Lists the constants used in the rule.
  - **Input and Output Editors**: Allows you to define and manage input and output parameters.
6. Navigate to the Rule Designer tab > Double-click the Rule name to open the Rule editor. This page contains 3 tabs, namely Rule, Model Editor, and Constants.
    ![designer-script-rule](/resources/Storage/neutrinos-reels-publication/images/rule-designer-doubleclick-scriptrule.gif)
  1. In the **Rule** tab, write a script to define the rule's execution logic. The script follows JavaScript syntax, where input names must be prefixed with "**IP_**" and output names with "**OP_**" (e.g., **IP_inputAge**,** OP_status**). This tab contains two sections: one for writing the script and another for mapping the inputs and outputs defined in the script to the corresponding keys.
  2. Switch to the Model Editor tab to add the necessary input-output keys using **Add Root** in both input and output editors. For example, in an age-based eligibility scenario, you can define the input key as **inputAge** and the output key as **Status** as shown in the image below:
      ![decisiontable-addroot](/resources/Storage/neutrinos-reels-publication/images/rule-add-rule-decisiontable-addroot.png)
      ![Note](/resources/Storage/neutrinos-reels-publication/project-trailproject/note.png)
      The keys can be of type string, number, boolean, object, or an array of string, number, or object.
      The settings icon (![](/resources/Storage/neutrinos-reels-publication/images/configure-icon.png)) in the created input key allows you to configure its behavior during rule testing. Similarly, the toggle (![](/resources/Storage/neutrinos-reels-publication/images/projection-toggle.png)) in the created output key represents projection, allowing you to control whether the key is included as an output in an API call. For more details on configuration and projection, see the [Configurations](/articles/neutrinos-reels-publication/configurations)topic.
  3. In the **Rule** tab, under the **Mapping** section, map the input and output keys to their corresponding inputs and outputs defined in the script.
      ![rule-input-mapping](/resources/Storage/neutrinos-reels-publication/images/rules-script-rule-input-mapping.png)
  4. Click the **Save** button to save the script.
7. Finally, click the **Save and Publish** button to save and deploy the rule. Enter the **Release Notes** to differentiate between the versions of the rules.

The GIF below illustrates how to create a Script rule:

![rule-script-rule](/resources/Storage/neutrinos-reels-publication/images/rule-script-rule.gif)

## Using Constants

You can add a constant using the **Add Constant** button in the **Constant** section on the **Rule Details** page by specifying a key (constant name) and a value.




 ![scriptrule-add-constant-details-page](/resources/Storage/neutrinos-reels-publication/images/scriptrule-add-constant-details-page.gif)




 Alternatively, you can add a constant from the **Constant** tab on the Rule Designer page.




 ![scriptrule-add-constant-designer](/resources/Storage/neutrinos-reels-publication/images/scriptrule-add-constant-designer.gif)




 An input variable must be declared in the script to handle the constant and later mapped in the **Mapping** section. The GIF below illustrates how to create a constant and use it in the script:




 ![scriptrule-constant-usage](/resources/Storage/neutrinos-reels-publication/images/scriptrule-constant-usage.gif)

## Rule Illustration

The use case demonstrates how to create a decision table rule to determine a person’s eligibility based on age and gender.

The rule is designed for the below scenario:

- **Eligible**: The person is eligible if they are 18 years or older and their gender is Male.
- **Not Eligible**: The person is not eligible if they are below 18 years of age and gender is Male.
- **Not Applicable**: For all other cases, the result defaults to "Not Applicable".

Follow the steps below to configure the Script rule for the above scenario:

1. Click the Rules button in the navigation bar.
2. In the Rules List page, click the Add button and choose the Rule from the dropdown.
3. In the pop-up screen, enter the Rule Name, provide a Rule Description, select Decision Table as the rule type, and click the Create button.
    For example:
    ![scriptrule-usercase-createrule](/resources/Storage/neutrinos-reels-publication/images/scriptrule-usercase-createrule.png)
  - **Rule Name**: Script Rule Demo.
  - **Description**: Script Rule for eligibility check.
4. On the **Rule Details** page, navigate to the **Rule Designer**, tab and double-click the rule name to open the designer and draft the rule. The designer page contains 3 tabs namely, Rule, Model Editor, and Constants.
    ![scriptrule-designer-doubleclick](/resources/Storage/neutrinos-reels-publication/images/scriptrule-designer-doubleclick.gif)
    In the **Rule** tab, write a script to define the rule's execution logic. The script follows JavaScript syntax. Since the decision logic requires two inputs—age and gender, declare these inputs and implement the script accordingly.
    ![scriptrule-decision-logic](/resources/Storage/neutrinos-reels-publication/images/scriptrule-decision-logic.gif)
5. Switch to **Model Editor** tab, click **Add Root** to add input and output keys.
    For example:
    ![scriptrule-usercase-input-output-keys](/resources/Storage/neutrinos-reels-publication/images/scriptrule-usercase-input-output-keys.png)
  - **Input Keys**: inputAge and inputGender
  - **Output Keys**: outputStatus
6. In the **Rule** tab, under the **Mapping** section, map the input and output keys to their corresponding inputs and outputs defined in the script.
    ![scriptrule-usercase-inputoutput-map](/resources/Storage/neutrinos-reels-publication/images/scriptrule-usercase-inputoutput-map.png)
7. Click the **Save** button to save the script.
8. Finally, click the **Save and Publish** button to save and publish the rule.

To test the created rule, navigate to the Testing tab from the **Rule Designer** page. For more details, see the [Testing](/articles/neutrinos-reels-publication/testing) topic.

## Testing Rule

To test the created rule, navigate to the Testing tab from the **Rule Designer** page.

1. Click the **Single** tab in the Testing section, then click the **Add** button in the top-right corner of the page to perform the test. From the dropdown, select **Single**.
2.
3. Test: This rule evaluates the input values and returns 'Eligible' when inputAge is 19 and inputGender is 'Male'.

The GIF below illustrates the testing of the Script rule:




 ![script-rule-testing](/resources/Storage/neutrinos-reels-publication/images/script-rule-testing.gif)

For more information on testing, see the [Testing](/articles/neutrinos-reels-publication/testing) topic.

[Next Topic](/articles/neutrinos-reels-publication/formula-rule)

[Previous Topic](/articles/neutrinos-reels-publication/decision-table)
