# Using Constants

<https://documentation.neutrinos.com/articles/#!neutrinos-reels-publication/decision-table>

**Decision tables** provide a structured way to represent decision-making logic in a tabular format, similar to a truth table. They simplify complex rule management by defining conditions and corresponding actions. This topic explains how to configure and deploy decision table rules in the Reels platform.

Steps to Create, Manage, and Map Data in a Decision Table Rule:

1. Click the **Rules** button in the left-side navigation bar to open the Rules List page. This page displays a list of rules created in the Reels platform in a tabular format, including details such as the Rule Name, Rule ID, Version, Rule Type, Author, Date of Creation, and Last Updated Date.
2. Click the **Add** button on the top right of the **Rule list** page > Click **Rule** from the dropdown options.
    ![rule-add-button](/resources/Storage/neutrinos-reels-publication/images/rule-add-button.png)
3. In the pop-up window, enter a **Rule Name**, add a description for the rule that describes the purpose of the rule or its functionality, and select **Decision Table** as the Rule Type.
    ![rule-add-create-rule-type](/resources/Storage/neutrinos-reels-publication/images/rule-add-create-rule-type.png)
4. Click the **Create** button to create the rule.
5. When a rule is created, the Rule Details page opens, allowing you to configure the rule. This page displays key information about the rule, including Version, Status, Last Updated date, Created Date, Deployment ID, and more.
    Additionally, the following sections provide further details:
    ![rule-details-page](/resources/Storage/neutrinos-reels-publication/images/rule-add-rule-details-page.png)
  - **Description**: Displays the rule description.
  - **Constants**: Lists the constants used in the rule.
  - **Input and Output Editors**: You can define and manage input and output parameters.
6. Navigate to the Rule Designer tab > Double-click the Rule name to open the Rule editor. This page contains 3 tabs, namely Rule, Model Editor, and Constants.
    ![rule-designer-page](/resources/Storage/neutrinos-reels-publication/images/rule-add-rule-designer-page.gif)
  1. Click the **Model Editor** tab and use **Add Root** to add input and output keys in their respective editors. For example, in an age-based eligibility scenario, you can define the input key as **inputAge** and the output key as **Status** as shown in the image below:
      ![decisiontable-addroot](/resources/Storage/neutrinos-reels-publication/images/rule-add-rule-decisiontable-addroot.png)
      ![Note](/resources/Storage/neutrinos-reels-publication/project-trailproject/note.png)
      The keys can be of type string, number, boolean, object, or an array of string, number, or object.
      The settings icon (![](/resources/Storage/neutrinos-reels-publication/images/configure-icon.png)) in the created input key allows you to configure its behavior during rule testing. Similarly, the toggle (![](/resources/Storage/neutrinos-reels-publication/images/projection-toggle.png)) in the created output key represents projection, allowing you to control whether the key is included as an output in an API call. For more details on configuration and projection, see the [Configurations](/articles/neutrinos-reels-publication/configurations)topic.
  2. After configuring the **input** and **output** keys in the **Model Editor** tab, navigate to the **Rule** tab to define rule conditions and expected results. Each condition is defined by an input key used for evaluation, with individual rows representing the values or criteria for evaluation. Additionally, the **Rule** tab provides the following options to enhance rule capabilities:
      Icon
      Description
      ![](/resources/Storage/neutrinos-reels-publication/images/rules-checkbox-action.png)
      **Action Checkbox:** Select all rows in the decision table rule. When ticked, it allows you to delete the selected rows simultaneously.
      ![](/resources/Storage/neutrinos-reels-publication/images/rules-conditions-dropdown.png)
      **Condition**: Specifies the criteria for rule evaluation. Each condition is represented as a separate column containing an input key, a logical operator, and a value used to evaluate the condition. Select an input key from the dropdown below to choose or map input keys to a condition.
      ![](/resources/Storage/neutrinos-reels-publication/images/rules-conditions-dropdown.png)
      The **Kebab Icon** in the conditions section allows you to add conditions, create condition groups, clone conditions, set the date format, or delete conditions.
      ![](/resources/Storage/neutrinos-reels-publication/images/rules-add-conditions.png)
      **Add Condition: **Add multiple conditions in a single row that the rule must adhere to. These conditions can be combined using AND or OR logic.
      ![](/resources/Storage/neutrinos-reels-publication/images/rules-add-group-conditions.png)
      **Add Group Condition**: Add a group of conditions that must be collectively satisfied for the rule to process the result.
      ![](/resources/Storage/neutrinos-reels-publication/images/rules-clone-conditions.png)
      **Clone**: Create an identical replica of the existing condition.
      ![](/resources/Storage/neutrinos-reels-publication/images/rules-date-operations.png)
      **Date**: Enables the condition to perform date-based operations when required. Additionally, select the **Include Time** checkbox to factor in the time during condition evaluation.
      ![](/resources/Storage/neutrinos-reels-publication/images/rules-delete-condition.png)
      **Delete**: Delete a specific condition.
      ![](/resources/Storage/neutrinos-reels-publication/images/rules-conditions-row.png)
      The individual rows represent the criteria used to evaluate the specified key. You can perform the following:
      ![](/resources/Storage/neutrinos-reels-publication/images/rules-row-select.png)
      Select this checkbox to choose a specific criteria row. Once selected, you can delete the corresponding row.
      ![](/resources/Storage/neutrinos-reels-publication/images/rules-row-disable.png)
      Turn off the toggle in an individual criteria row to disable that row.
      ![](/resources/Storage/neutrinos-reels-publication/images/rules-row-kebab-icon.png)
      The kebab icon in each row allows you to perform the following actions:
      **Note**: Criteria rows are added in the order of **execution priority**.
      ![](/resources/Storage/neutrinos-reels-publication/images/rules-row-logical-operator.png)
      Select the logical operator to evaluate the key against the condition criteria for the specified row.
      ![](/resources/Storage/neutrinos-reels-publication/images/rules-row-criteria-value.png)
      The actual value that is used to compare against the key within the condition.
      ![](/resources/Storage/neutrinos-reels-publication/images/rules-result-column.png)
      **Result**: Represents the outcome displayed to the user based on condition evaluation. The kebab icon in the result section provides the same options available in the Conditions section. You can:
      ![](/resources/Storage/neutrinos-reels-publication/images/rules-add-new-row.png)
      **Add Row**: Enables you to add a new condition criteria row.
      ![](/resources/Storage/neutrinos-reels-publication/images/rules-add-new-default-row.png)
      **Add Default Row**: Enables you to add a default row that specifies the result to be returned if all preceding conditions are not met.
      ![Note](/resources/Storage/neutrinos-reels-publication/project-trailproject/note.png)
      Alternatively, you can use the input keys created in the rule by specifying them as '**{IP_keyname}**'. For example, if the input key is 'gender' you can reference it as '**{IP_gender}**'.
  3. Click the **Save** button, to save the configured rule.
7. Finally, click the **Save and Publish** button to save and deploy the rule. Enter the **Release Notes** to differentiate between the versions of the rules.

The GIF below illustrates how to create a Decision Table rule:

![add-rule-gif](/resources/Storage/neutrinos-reels-publication/images/rule-add-rule-gif.gif)

## Using Constants

You can add a constant using the **Add Constant** button in the **Constant** section on the **Rule Details** page by specifying a key (constant name) and a value.




 ![decisiontable-constant-use](/resources/Storage/neutrinos-reels-publication/images/decisiontable-constant-use.gif)




 Alternatively, you can add a constant from the **Constant** tab on the **Rule Designer** page.




 ![decisiontable-use-constant-constanttab](/resources/Storage/neutrinos-reels-publication/images/decisiontable-use-constant-constanttab.gif)




 To use a constant in the rule, specify its name within curly brackets. For example, to use the constant '**pi**' in a rule, enter **{pi}**. The image below illustrates the use of the constant 'pi' in the rule:




 ![use-of-constant](/resources/Storage/neutrinos-reels-publication/images/rule-use-of-constant.png)

## Rule Illustration

The use case demonstrates how to create a decision table rule to determine a person’s eligibility based on age and gender.

The rule is designed for the below scenario:

- **Eligible**: The person is eligible if they are 18 years or older and their gender is Male.
- **Not Eligible**: The person is not eligible if they are below 18 years of age and gender is Male.
- **Not Applicable**: For all other cases, the result defaults to "Not Applicable".

Follow the steps below to configure the decision table rule for the above scenario:

1. Click the Rules button in the navigation bar.
2. In the Rules List page, click the Add button and choose the Rule from the dropdown.
3. In the pop-up screen, enter the **Rule Name**, provide a **Rule Description**, select **Decision Table** as the rule type, and click the **Create** button.
    For example:
    ![usercase-createrule](/resources/Storage/neutrinos-reels-publication/images/decisiontable-usercase-createrule.png)
  - **Rule Name**: Decision Table Demo.
  - **Description**: Decision Table rule for eligibility check.
4. On the **Rule Details** page, navigate to the **Rule Designer**, tab and double-click the rule name to open the designer and draft the rule. The designer page contains 3 tabs namely, Rule, Model Editor, and Constants.
    ![usercase-doubleclick](/resources/Storage/neutrinos-reels-publication/images/rule-usercase-doubleclick.gif)
5. Click the **Model Editor** tab and select **Add Root** to add the input and output keys.
    For example:
    ![](/resources/Storage/neutrinos-reels-publication/images/decisiontable-usercase-input-output-keys.png)
  - **Input Keys**: inputAge and inputGender
  - **Output Keys**: outputStatus
6. Navigate to the **Rule** tab and define the conditions for the decision table rule. This scenario requires two conditions:
    ![](/resources/Storage/neutrinos-reels-publication/images/decisiontable-usercase-add-conditions.gif)
    You can optionally add a default row to display the result as **Not Applicable** if neither of the specified conditions is met. To add a default row, click the **Add Default Row** button.
    ![](/resources/Storage/neutrinos-reels-publication/images/decisiontable-usercase-defaultrow.gif)
  - Click the Kebab icon next to the first condition and select Add Condition. Add Conditions with **AND** Logic.
  - Add multiple criteria rows as needed.
  - To add a new condition row, click the Add Row button.
7. Click the **Save** button.
8. Finally, click the **Save and Publish** button to save and publish the rule.

## Testing Rule

To test the created rule, navigate to the Testing tab from the **Rule Designer** page.

1. Click the **Single** tab in the Testing section, then click the **Add** button in the top-right corner of the page to perform the test. From the dropdown, select **Single**.
2. Test: This rule evaluates the input values and returns 'Eligible' when inputAge is 19 and inputGender is 'Male'.

The GIF below illustrates the testing of Decision Table rule:




 ![decision-table-testing](/resources/Storage/neutrinos-reels-publication/images/decision-table-testing.gif)

For more information on testing, see the [Testing](/articles/neutrinos-reels-publication/testing) topic.

[Next Topic](/articles/neutrinos-reels-publication/script-rule)

[Previous Topic](/articles/neutrinos-reels-publication/rules)
