# Using Constants

<https://documentation.neutrinos.com/articles/#!pulse-publication/levenshtein-distance-rule>

The Levenshtein Distance Rule calculates the minimum number of edits needed to transform one string into another. This topic explains configuring and deploying the Levenshtein Distance rule in the Reels Platform.

Steps to Create, Manage, and Map Data in the Levenshtein Distance Rule:

1. Click the **Rules **button in the sub-module navigation bar to open the Rules List page. This page displays a list of rules created in the Reels platform in a tabular format, including details such as the Rule Name, Rule ID, Version, Rule Type, Author, Date of Creation, and Last Updated Date.
2. Click the **Add** button on the top right of the **Rule List** page > Click **Rule** from the dropdown options.
    ![rule-add-button](/resources/Storage/pulse-publication/images/rule-add-button.png)
3. In the pop-up window, enter a **Rule Name**, add a **description** for the rule that describes the purpose of the rule or its functionality, and select **Levenshtein Distance** Rule as the Rule Type.
    ![add-levenshtein-distance-rule](/resources/Storage/pulse-publication/images/rule-add-levenshtein-distance-rule.png)
4. Click the **Create** button to create the rule.
5. When a rule is created, the Rule Details page opens, allowing you to configure the rule. This page displays key information about the rule, including Version, Status, Last Updated date, Created Date, Deployment ID, and more.
    Additionally, the following sections provide further details:
    ![levenshtein-distance-rule-details-page](/resources/Storage/pulse-publication/images/rule-details-levenshtein-distance-rule.png)
  - **Description**: Displays the rule description.
  - **Constants**: Lists the constants used in the rule.
  - **Input and Output Editors**: Allows you to define and manage input and output parameters.
6. Navigate to the Rule Designer tab > Double-click the Rule name to open the Rule editor. This page contains 3 tabs, namely Rule, Model Editor, and Constants.
    ![designer-levenshtein-distance-rule](/resources/Storage/pulse-publication/images/levenshtein-rule-designer-doubleclick.gif)
  1. Navigate to the **Model Editor** tab. Use **Add Root** in both the input and output editors to add the necessary input-output keys. For example, define inputs as **inputText1**, **inputText2** and set the output as **Result**.
      ![levenshtein-rule-roots-modeleditor](/resources/Storage/pulse-publication/images/levenshtein-rule-roots-modeleditor.png)
      ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png)
      The keys can be of type string, number, boolean, object, or an array of string, number, or object.
      The settings icon (![settings-icon](/resources/Storage/pulse-publication/images/configure-icon.png)) in the created input key allows you to configure its behavior during rule testing. Similarly, the toggle (![projection-icon](/resources/Storage/pulse-publication/images/projection-toggle.png)) in the created output key represents projection, allowing you to control whether the key is included as an output in an API call. For more details on configuration and projection, see the [Configurations](/smart/project-neutrinos-reels/configurations)topic.
      ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png)
      The data type for the input-output roots should always be **string**, as the rule works on string data.
      This rule accepts two inputs to compare their similarity and produces a single output: the percentage of similarity between the inputs. The similarity index ranges from 0 to 1, where 0 indicates a complete match and 1 represents entirely dissimilar entries.
  2. Switch back to the **Rule** tab, and map the keys defined in the previous step to the target input and output fields.
  3. Click the **Save** button to save the rule.
7. Finally, click the **Save and Publish** button to save and deploy the rule. Enter the **Release Notes** to differentiate between the versions of the rules.

The GIF below demonstrates how to create a Levenshtein Distance rule to calculate the percentage of similarity between two texts

![levenshtein-distance-rule-gif](/resources/Storage/pulse-publication/images/rule-levenshtein-distance-rule.gif)

## Using Constants

You can add a constant using the Add Constant button in the Constant section on the Rule Details page by specifying a key (constant name) and a value.




 ![levenshtein-rule-add-constant-detailspage](/resources/Storage/pulse-publication/images/levenshtein-rule-add-constant-detailspage.gif)

Alternatively, you can add a Constant tab on the Rule Designer page.




 ![levenshtein-rule-add-constant-desinger](/resources/Storage/pulse-publication/images/levenshtein-rule-add-constant-desinger.gif)

Constants can be mapped to inputs on the Rule Designer page. The GIF below illustrates the use of a constant to match an input text in a rule:




 ![levenshtein-rule-use-constant](/resources/Storage/pulse-publication/images/levenshtein-rule-use-constant.gif)

## Rule illustration

This use case demonstrates how to configure a Levenshtein Distance rule to measure the similarity between two text inputs.

Follow the steps below to configure the Levenshtein Distance rule for the above scenario:

1. Click the Rules button in the navigation bar.
2. In the Rules List page, click the Add button and choose the Rule from the dropdown.
3. In the pop-up screen, enter the Rule Name, provide a Rule Description, select Formula as the rule type, and click the Create button.
    For example:
    ![levenshtein-rule-usercase-createrule](/resources/Storage/pulse-publication/images/levenshtein-rule-usercase-createrule.png)
  - **Rule Name**: Levenshtein Distance Rule Demo
  - **Description**: Levenshtein Distance rule for checking similarity between two strings.
4. On the **Rule Details** page, navigate to the **Rule Designer** tab and double-click the rule name to open the designer and draft the rule. The designer page contains 3 tabs namely, Rule, Model Editor, and Constants.
    ![levenshtein-rule-3-tabs](/resources/Storage/pulse-publication/images/levenshtein-rule-3tabs.gif)
5. Navigate to the **Model** tab and create root nodes for two inputs and one output. The output will return the similarity index for the two inputs.
    ![levenshtein-rule-usercase-addroots](/resources/Storage/pulse-publication/images/levenshtein-rule-usercase-addroots.gif)
6. Once the root nodes are added, navigate to the **Rule** tab and map them to the input source, target text, and output.
    ![levenshtein-rule-usercase-mapping-roots](/resources/Storage/pulse-publication/images/levenshtein-rule-usercase-mapping-roots.gif)
7. Click **Save** button to save the rule.
8. Click the **Save and Publish** button to save and publish the rule.

## Testing Rule

To test the created rule, navigate to the Testing tab from the **Rule Designer** page.

1. Click the **Single** tab in the Testing section, then click the **Add** button in the top-right corner of the page to perform the test. From the dropdown, select **Single**.
2. This rule compares the input text values 'Horse' and 'Rose' and returns a similarity score of 0.4.

The GIF below illustrates the testing of the Excel rule:




 ![levenshtein-distance-testing](/resources/Storage/pulse-publication/images/levenshtein-distance-testing.gif)

For more information on testing, see the [Testing](/smart/project-neutrinos-reels/testing) topic.

[Next Topic](/articles/pulse-publication/phonetics-rule)

[Previous Topic](/articles/pulse-publication/api-rule)
