# Using Constant

<https://documentation.neutrinos.com/articles/#!neutrinos-reels-publication/formula-rule>

The **Formula** rule enables calculations using mathematical or logical expressions. This topic explains how to configure and deploy the Formula rule in the Reels Platform.

Steps to Create, Manage, and Map Data in a Formula Rule:

1. Click the **Rules** button in the left-side navigation bar to open the Rules List page. This page displays a list of rules created in the Reels platform in a tabular format, including details such as the Rule Name, Rule ID, Version, Rule Type, Author, Date of Creation, and Last Updated Date.
2. Click the **Add** button on the top right of the **Rule list** page > Click **Rule** from the dropdown options.
    ![rule-add-button](/resources/Storage/neutrinos-reels-publication/images/rule-add-button.png)
3. In the pop-up window, enter a **Rule Name**, add a description for the rule that describes the purpose of the rule, or its functionality, and select **Formula** as the Rule Type.
    ![fomula-rule](/resources/Storage/neutrinos-reels-publication/images/rule-add-rule-fomula-rule.png)
4. Click the **Create** button to create the rule.
5. When a rule is created, the Rule Details page opens, allowing you to configure the rule. This page displays key information about the rule, including Version, Status, Last Updated date, Created Date, Deployment ID, and more.
    Additionally, the following sections provide further details:
    ![Rule details - formula rule](/resources/Storage/neutrinos-reels-publication/images/rule-details-formula-rule.png)
  - **Description**: Displays the rule description.
  - **Constants**: Lists the constants used in the rule.
  - **Input and Output Editors**: Allows you to define and manage input and output parameters.
6. Navigate to the Rule Designer tab > Double-click the Rule name to open the Rule editor. This page contains 3 tabs, namely Rule, Model Editor, and Constants.
    ![rule-designer-page](/resources/Storage/neutrinos-reels-publication/images/formularule-doubleclick-designer.gif)
  1. Click the Model Editor tab > Add the necessary input and output keys using **Add Root** in both the Input and Output editors as required to construct the formula logic. For example, to calculate a discount on a premium amount, the input must be **premium**, and the output must be **discount**.
      ![formularule-model-editor](/resources/Storage/neutrinos-reels-publication/images/formularule-model-editor.png)
      ![Note](/resources/Storage/neutrinos-reels-publication/project-trailproject/note.png)
      The keys can be of type string, number, boolean, object, or an array of string, number, or object.
  2. After configuring the input-output keys in the **Model Editor** tab, click the **Rule tab** to construct the formula for rule execution. Add the Output Target, which is the output key defined in the previous step.
  3. Define the formula by entering individual operands and operators in the provided input area. You can also drag and drop operators into the formula. When entering an operand, press **Enter** after each entry to confirm it in the formula.
      ![formularule-formula-construct](/resources/Storage/neutrinos-reels-publication/images/formularule-formula-construct.gif)
      Additionally, the **Rule** tab provides the following options:
      ![formularule-rule-tab](/resources/Storage/neutrinos-reels-publication/images/formularule-rule-tab.png)
    1. **Search Bar**: You can search for a specific formula by typing the output target in the search bar.
    2. The **checkbox** in an individual formula row allows you to select and delete a specific formula. The **checkbox** in the table header allows you to select and delete all formulas at once.
    3. The **kebab** icon in the **Action** column allows you to edit or delete a formula.
    4. **Round Result**: If the formula requires rounding, enable the Round Result toggle, set the precision, and choose a rounding method:
      - Round – Rounds the last digit of the fractional part to the nearest number based on the specified precision.
      - Ceil – Rounds the last digit of the fractional part to the next number based on the specified precision.
      - Floor – Rounds the last digit of the fractional part to the previous number based on the specified precision.
  4. Click the **Add** button, to add the formula.
  5. Click the **Save** button, to save the configured rule.
7. Finally, click the **Save and Publish** button to save and deploy the rule. Enter the **Release Notes** to differentiate between the versions of the rules.

The GIF below illustrates how to create a Formula rule to calculate a discount:

![formula-rule - gif](/resources/Storage/neutrinos-reels-publication/images/rule-formula-rule.gif)

## Using Constant

You can add a constant using the **Add Constant** button in the **Constant** section on the **Rule Details** page by specifying a key (constant name) and a value.

![formularule-add-constant-details-page](/resources/Storage/neutrinos-reels-publication/images/formularule-add-constant-details-page.gif)

Alternatively, you can add a constant from the **Constant** tab on the **Rule Designer** page.




 ![formularule-add-constant-designerpage](/resources/Storage/neutrinos-reels-publication/images/formularule-add-constant-designerpage.gif)

To use a constant in a rule, enter its name in the formula and select it. For example, to use the constant '**dis**', enter dis in the rule. The GIF below illustrates how to use the constant '**dis**' in a rule.




 ![formularule-use-constant](/resources/Storage/neutrinos-reels-publication/images/formularule-use-constant.gif)

## Multiple Formula

The formula rule supports adding multiple formulae within the same rule node. For example, one formula can calculate the sum of a set of numbers, while another can calculate their average. The image below illustrates how multiple formulae can be added to a rule node to perform these calculations.




 ![formula-rule-multiple-formula](/resources/Storage/neutrinos-reels-publication/images/formula-rule-multiple-formula.gif)

| ![Note](/resources/Storage/neutrinos-reels-publication/project-trailproject/note.png) | The output of one formula can be used as an input in another formula if multiple formulas exist in a rule. |
| --- | --- |

## Rule Illustration

The use case demonstrates how to create a formula rule to calculate discount.

The rule is designed to calculate the discount for the base premium entered by the user.

Follow the steps below to configure the decision table rule for the above scenario:

1. Click the Rules button in the navigation bar.
2. In the Rules List page, click the Add button and choose the Rule from the dropdown.
3. In the pop-up screen, enter the Rule Name, provide a Rule Description, select Formula as the rule type, and click the Create button.
    For example:
    ![formularule-usercase-createrule.png](/resources/Storage/neutrinos-reels-publication/images/formularrule-usercase-createrule.png)
  - **Rule Name**: Formula Rule Demo.
  - **Description**: Formula rule to calculate discount.
4. On the **Rule Details** page, navigate to the **Rule Designer**, tab and double-click the rule name to open the designer and draft the rule. The designer page contains 3 tabs namely, Rule, Model Editor, and Constants.
    ![formularule-usercase-designertab](/resources/Storage/neutrinos-reels-publication/images/formularule-usercase-designertab.gif)
5. Click the **Model Editor** tab and select **Add Root** to add the input and output keys.
    For example:
    ![formularule-modeleditor-keys](/resources/Storage/neutrinos-reels-publication/images/formularule-modeleditor-keys.png)
  - **Input Keys**: basePremium
  - **Ouput Keys**: Discount
6. Navigate to the Rule tab and define the formula for the Formula rule. Define the formula by entering individual operands and operators in the provided input area. You can also drag and drop operators into the formula. When entering an operand (value), press **Enter** after each entry to confirm it in the formula. The GIF below illustrates how to add a formula to calculate a discount for an input premium.
    ![formularule-usercase-add-formula](/resources/Storage/neutrinos-reels-publication/images/formularule-usercase-add-formula.gif)
7. Click the **Save** button.
8. Finally, click the **Save and Publish** button to save and publish the rule.

## Testing Rule

To test the created rule, navigate to the Testing tab from the **Rule Designer** page.

1. Click the **Single** tab in the Testing section, then click the **Add** button in the top-right corner of the page to perform the test. From the dropdown, select **Single**.
2. This rule evaluates the input basePremium amount and returns 'Discount'.

The GIF below illustrates the testing of the Formula rule:




 ![formula-rule-testing](/resources/Storage/neutrinos-reels-publication/images/formula-rule-testing.gif)

For more information on testing, see the [Testing](/articles/neutrinos-reels-publication/testing) topic.

[Next Topic](/articles/neutrinos-reels-publication/decision-tree)

[Previous Topic](/articles/neutrinos-reels-publication/script-rule)
