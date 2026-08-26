# Using Constants

<https://documentation.neutrinos.com/articles/#!pulse-publication/decision-tree>

A **Decision Tree** graphically represents decisions and their possible outcomes in a tree-like structure. This rule is useful when multiple decision paths need to be included. This topic explains how to configure and deploy a **Decision Tree** rule in the Reels platform.

Steps to Create, Manage, and Map Data in a Decision Tree Rule:

1. Click the **Rules **button in the sub-module navigation bar to open the Rules List page. This page displays a list of rules created in the Reels platform in a tabular format, including details such as the Rule Name, Rule ID, Version, Rule Type, Author, Date of Creation, and Last Updated Date.
2. Click the **Add** button on the top right of the **Rule list** page > Click **Rule** from the dropdown options.
    ![rule-add-button](/resources/Storage/pulse-publication/images/rule-add-button.png)
3. In the pop-up window, enter a **Rule Name**, add a **description** for the rule that describes the purpose of the rule or its functionality, and select **Decision Tree** Rule as the Rule Type.
    ![decision-tree-rule](/resources/Storage/pulse-publication/images/rule-add-decision-tree-rule.png)
4. Click the **Create** button to create the rule.
5. When a rule is created, the Rule Details page opens, allowing you to configure the rule. This page displays key information about the rule, including Version, Status, Last Updated date, Created Date, Deployment ID, and more.
    Additionally, the following sections provide further details:
    ![decision-tree-rule-details-page](/resources/Storage/pulse-publication/images/rule-add-details-decision-tree-rule.png)
  - **Description**: Displays the rule description.
  - **Constants**: Lists the constants used in the rule.
  - **Input and Output Editors**: Allows you to define and manage input and output parameters.
6. Navigate to the Rule Designer tab > Double-click the Rule name to open the Rule editor. This page contains 3 tabs, namely Rule, Model Editor, and Constants.
    ![designer-decision-tree-rule](/resources/Storage/pulse-publication/images/DecisionTree-dubleclick-designerpage.gif)
  1. Click the **Model Editor** tab > Add necessary input-output keys using **Add Root** in both input and output editors. For example, in an age-based eligibility scenario, you can define the input key as **inputAge** and the output key as **Status** as shown in the image below:
      ![decisiontree-addroot](/resources/Storage/pulse-publication/images/rule-add-rule-decisiontable-addroot.png)
      ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png)
      The keys can be of type string, number, boolean, object, or an array of string, number, or object.
      The settings icon (![config-icon](/resources/Storage/pulse-publication/images/configure-icon.png)) in the created input key allows you to configure its behavior during rule testing. Similarly, the toggle (![projection-icon](/resources/Storage/pulse-publication/images/projection-toggle.png)) in the created output key represents projection, allowing you to control whether the key is included as an output in an API call. For more details on configuration and projection, see the [Configurations](/smart/project-neutrinos-reels/configurations)topic.
  2. After configuring the **input** and **output** keys in the **Model Editor** tab, navigate to the **Rule** tab to add condition blocks that define the decision logic for the rule. You can add multiple test conditions by clicking **'Add Block'**. Each condition block starts with an **IF** statement, and alternative conditions can be added using an **ELSE** block. Within an **IF** block, conditions can be nested using **AND** or **OR** logic. Additional conditions within the same block can be added using **IF**, **ELSE**, or **THEN** condition blocks.
      ![decisiontree-addblocks-condition-logic](/resources/Storage/pulse-publication/images/decisiontree-addblocks-condition-logic.gif)
      Additionally, the **Rule** tab provides the following options to enhance rule capabilities:
      Icon
      Description
      ![](/resources/Storage/pulse-publication/images/6-dots.png)
      Allows you to rearrange or move conditions and condition blocks based on execution priority.
      ![decisiontree-condition-logical-operator](/resources/Storage/pulse-publication/images/decisiontree-condition-logical-operator.png)
      Allows you to select a logical operator to evaluate the condition.
      ![decisiontree-condition-nest-addblock](/resources/Storage/pulse-publication/images/decisiontree-condition-nest-addblock.png)
      Allows you to add another condition within the same block using AND or OR logic. Additionally, you can rearrange conditions based on execution priority.
      ![decisiontree-condition-delete-icon](/resources/Storage/pulse-publication/images/decisiontree-condition-delete-icon.png)
      Allows you to delete the condition row.
      ![decisiontree-condition-kebab-icon](/resources/Storage/pulse-publication/images/decisiontree-condition-kebab-icon.png)
      Allows you to clone or delete a specific condition block.
      ![decisiontree-add-additional-condition-block](/resources/Storage/pulse-publication/images/decisiontree-add-additional-condition-block.png)
      Allows you to add additional condition blocks to structure the decision logic.
      ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png)
      Alternatively, you can use the input keys created in the rule by specifying them as '**{IP_keyname}**'. For example, if the input key is 'gender' you can reference it as '**{IP_gender}**'.
  3. Click the **Save** button to save the rule.
7. Finally, click the **Save and Publish** button to save and deploy the rule. Enter the **Release Notes** to differentiate between the versions of the rules.

The GIF below demonstrates how to create a **Decision Tree** rule to determine a person's eligibility based on age as input.:

![decision-tree-rule-gif](/resources/Storage/pulse-publication/images/rule-decision-tree-rule.gif)

## Using Constants

You can add a constant using the **Add Constant** button in the **Constant** section on the **Rule Details** page by specifying a key (constant name) and a value.




 ![decisiontree-add-constant-ruledetails-page](/resources/Storage/pulse-publication/images/decisiontree-add-constant-ruledetails-page.gif)




 Alternatively, you can add a constant from the **Constant** tab on the **Rule Designer** page.




 ![decisiontree-add-constant-designerpage](/resources/Storage/pulse-publication/images/decisiontree-add-constant-designerpage.gif)




 To use a constant in the rule, specify its name within curly brackets. For example, to use the constant '**minAge**' in a rule, enter **{minAge}**. The image below illustrates the use of the constants 'minAge' and 'maxAge' in the rule:




 ![decisiontree-constant-usage](/resources/Storage/pulse-publication/images/decisiontree-constant-usage.png)

## Rule Illustration

The use case demonstrates how to create a decision table rule to determine a person’s eligibility based on age and gender.

The rule is designed for the below scenario:

- **Eligible**: The person is eligible if they are 18 years or older and their gender is Male.
- **Not Eligible**: The person is not eligible if they are below 18 years of age and gender is Male.
- **Not Applicable**: For all other cases, the result defaults to "Not Applicable".

Follow the steps below to configure the decision table rule for the above scenario:

1. Click the Rules button in the navigation bar.
2. In the Rules List page, click the **Add** button and choose the Rule from the dropdown.
3. In the pop-up screen, enter the **Rule Name**, provide a **Rule Description**, select **Decision Tree **as the rule type, and click the **Create** button.
    For example:
    ![decisiontree-usercase-create-rule](/resources/Storage/pulse-publication/images/decisiontree-usercase-create-rule.png)
  - **Rule Name**: Decision Tree Demo.
  - **Description**: Decision Tree rule for eligibility check.
4. On the **Rule Details** page, navigate to the **Rule Designer**, tab and double-click the rule name to open the designer and draft the rule. The designer page contains 3 tabs namely, Rule, Model Editor, and Constants.
    ![decisiontree-usercase-designer-tab](/resources/Storage/pulse-publication/images/decisiontree-usercase-designer-tab.gif)
5. Click the **Model Editor** tab and select **Add Root** to add the input and output keys.
    For example:
    ![decisiontree-usercase-add-roots](/resources/Storage/pulse-publication/images/decisiontree-usercase-add-roots.png)
  - **Input Keys**: inputAge and inputGender
  - **Output Keys**: outputStatus
6. Navigate to the **Rule** tab and define the conditions for the decision tree rule. This scenario requires two conditions:
  - Click the '**Add Block**' button to add the first condition and select the '**IF**' condition from the dropdown. Then, click '**Add Block**' within the newly added condition block and choose '**AND**' logic.
      ![decisiontree-usercase-add-block](/resources/Storage/pulse-publication/images/decisiontree-usercase-add-block.gif)
  - In the first dropdown, select the input key as '**inputAge**', choose the logical operator '**greater than or equal to**', and enter the value to compare against the input key. Since this scenario requires two conditions, click '**Add Block**' within the existing condition block to add another condition. Select '**AND**' logic, as the result should be true only if both conditions are met.
  - For the second condition, select the input key as '**inputGender**' in the first dropdown, choose the logical operator '**equal to**', and enter the value as '**Male**' to compare against the input key.
      ![decisiontree-usercase-addinputkeys-and-logic](/resources/Storage/pulse-publication/images/decisiontree-usercase-addinputkeys-and-logic.gif)
  - In the section next to the first condition block, click '**Add Block**' and select '**THEN**' from the dropdown to define the output if both conditions in the first condition block are evaluated to true. Then, click '**Add Result**' to add the output key and display the result.
      ![decisiontree-usercase-add-output](/resources/Storage/pulse-publication/images/decisiontree-usercase-add-output.gif)
  - To add another condition block, click '**Add Block**' at the bottom of the page and select '**IF**' condition.
      ![decisiontree-add-addtion-condition](/resources/Storage/pulse-publication/images/decisiontree-add-addtion-condition.gif)
      Add the condition logic following the steps outlined previously.
      ![decisiontree-additional-condition-logic](/resources/Storage/pulse-publication/images/decisiontree-additional-condition-logic.gif)
  - To handle a non-applicable scenario, click the '**Add Block**' button at the bottom of the page and select the '**ELSE**' block. Then, click '**Add Block**' within the newly added '**ELSE**' block and choose '**THEN**' from the dropdown to define the output. Finally, click the '**Add Result**' button to add the output key and display the result.
      ![decisiontree-usercase-not-applicable](/resources/Storage/pulse-publication/images/decisiontree-usercase-not-applicable.gif)
7. Click the **Save** button.
8. Finally, click the **Save and Publish** button to save and publish the rule.

## Testing Rule

To test the created rule, navigate to the Testing tab from the **Rule Designer** page.

1. Click the **Single** tab in the Testing section, then click the **Add** button in the top-right corner of the page to perform the test. From the dropdown, select **Single**.
2. Test: This rule evaluates the input values and returns 'Eligible' when inputAge is 19 and inputGender is 'Male'.

The GIF below illustrates the testing of Decision Tree rule:




 ![decision-tree-testing](/resources/Storage/pulse-publication/images/decision-tree-testing.gif)

For more information on testing, see the [Testing](/smart/project-neutrinos-reels/testing) topic.

[Next Topic](/articles/pulse-publication/excel-rule)

[Previous Topic](/articles/pulse-publication/formula-rule)
