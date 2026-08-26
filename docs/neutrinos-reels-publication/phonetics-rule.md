# Using Constants

<https://documentation.neutrinos.com/articles/#!neutrinos-reels-publication/phonetics-rule>

Phonetic algorithms like Soundex and Metaphone convert words into codes based on sound rather than spelling. This topic explains configuring and deploying the Phonetic rule in the Reels platform.

Steps to Create, Manage, and Map Data in the Phonetic Rule:

1. Click the **Rules** button in the left-side navigation bar to open the **Rules List** page. This page displays a list of rules created in the Reels platform in a tabular format, including details such as the Rule Name, Rule ID, Version, Rule Type, Author, Date of Creation, and Last Updated Date.
2. Click the **Add** button on the top right of the **Rule List** page > Click **Rule** from the dropdown options.
    ![rule-add-button](/resources/Storage/neutrinos-reels-publication/images/rule-add-button.png)
3. In the pop-up window, enter a **Rule Name**, add a **description** for the rule that describes the purpose of the rule or its functionality, and select **Phonetics** Rule as the Rule Type.
    ![add-levenshtein-distance-rule](/resources/Storage/neutrinos-reels-publication/images/rule-add-rule-phonetics-rule.png)
4. Click the **Create** button to create the rule.
5. When a rule is created, the Rule Details page opens, allowing you to configure the rule. This page displays key information about the rule, including Version, Status, Last Updated date, Created Date, Deployment ID, and more.
    Additionally, the following sections provide further details:
    ![levenshtein-distance-rule-details-page](/resources/Storage/neutrinos-reels-publication/images/rule-details-phonetics-rule.png)
  - **Description**: Displays the rule description.
  - **Constants**: Lists the constants used in the rule.
  - **Input and Output Editors**: Allows you to define and manage input and output parameters.
6. Navigate to the Rule Designer tab > Double-click the Rule name to open the Rule editor. This page contains 3 tabs, namely Rule, Model Editor, and Constants.
    ![designer-levenshtein-distance-rule](/resources/Storage/neutrinos-reels-publication/images/phonetics-rule-doubleclick-designer.gif)
  1. Navigate to the **Model Editor** tab. Use **Add Root** in both the input and output editors to add the necessary input-output keys.
      ![phonetics-rule-add-roots](/resources/Storage/neutrinos-reels-publication/images/phonetics-rule-add-roots.png)
      ![Note](/resources/Storage/neutrinos-reels-publication/project-trailproject/note.png)
      The keys can be of type string, number, boolean, object, or an array of string, number, or object.
      The settings icon (![settings-icon](/resources/Storage/neutrinos-reels-publication/images/configure-icon.png)) in the created input key allows you to configure its behavior during rule testing. Similarly, the toggle (![projection-icon](/resources/Storage/neutrinos-reels-publication/images/projection-toggle.png)) in the created output key represents projection, allowing you to control whether the key is included as an output in an API call. For more details on configuration and projection, see the [Configurations](/articles/neutrinos-reels-publication/configurations)topic.
      This rule takes two text inputs, compares their similarity based on sound, and returns either **true** or **false**. If the inputs sound similar, the rule returns **true**; otherwise, it returns **false**.
  2. In the **Rule** tab, select either the **Soundex** or **Metaphone** as an algorithm. Then, map the previously defined keys to their corresponding **input** and **output** fields.
  3. Click the **Save** button to save the rule.
7. Finally, click the **Save and Publish** button to save and deploy the rule. Enter the **Release Notes** to differentiate between the versions of the rules.

The GIF below demonstrates how to create a Levenshtein Distance rule to calculate the percentage of similarity between two texts

![phonetic-rule-gif](/resources/Storage/neutrinos-reels-publication/images/rule-phonetic-rule.gif)

## Using Constants

You can add a constant using the Add Constant button in the Constant section on the Rule Details page by specifying a key (constant name) and a value.




 ![phonetics-rule-add-constant-detailspage](/resources/Storage/neutrinos-reels-publication/images/phonetics-rule-add-constant-detailspage.gif)

Alternatively, you can add a Constant tab on the Rule Designer page.




 ![phonetics-rule-add-constant-designer](/resources/Storage/neutrinos-reels-publication/images/phonetics-rule-add-constant-designer.gif)

To use a constant, map it to the inputs in the rule. The GIF below illustrates the use of a constant in the rule.




 ![phonetics-rule-use-of-constant](/resources/Storage/neutrinos-reels-publication/images/phonetics-rule-use-of-constant.gif)

## Rule Illustration

This use case demonstrates how to configure a Phonetics rule to measure the similarity between two text inputs. The rule returns true if the two words sound similar and false if they do not.

Follow the steps below to configure the Phonetics rule for the above scenario:

1. Click the Rules button in the navigation bar.
2. In the Rules List page, click the Add button and choose the Rule from the dropdown.
3. In the pop-up screen, enter the Rule Name, provide a Rule Description, select Formula as the rule type, and click the Create button.
    For example:
    ![phonetics-rule-usercase-createrule](/resources/Storage/neutrinos-reels-publication/images/phonetics-rule-usercase-createrule.png)
  - **Rule Name**: Phonetics Rule Demo
  - **Description**: Phonetics Rule Demo
4. On the **Rule Details** page, navigate to the **Rule Designer** tab and double-click the rule name to open the designer and draft the rule. The designer page contains 3 tabs namely, Rule, Model Editor, and Constants.
    ![phonetics-rule-usercase-doubleclick](/resources/Storage/neutrinos-reels-publication/images/phonetics-rule-usercase-doubleclick.gif)
5. Navigate to the **Model** tab and create two input roots and one output root. The output will return the similarity index for the two inputs.
    ![phonetics-rule-usercase-add-roots](/resources/Storage/neutrinos-reels-publication/images/phonetics-rule-usercase-add-roots.gif)
6. Once the roots are added, navigate to the **Rule** tab and select the algorithm to be used by the rule. The algorithm can be either **Soundex** or **Metaphone**. Map the input roots to the input source, target text, and output.
    ![phonetics-rule-usercase-maproots](/resources/Storage/neutrinos-reels-publication/images/phonetics-rule-usercase-maproots.gif)
7. Click the **Save** button to save the rule.
8. Click the **Save and Publish** button to save and publish the rule.

## Testing Rule

To test the created rule, navigate to the Testing tab from the **Rule Designer** page.

1. Click the **Single** tab in the Testing section, then click the **Add** button in the top-right corner of the page to perform the test. From the dropdown, select **Single**.
2. This rule compares the input text values 'Bear' and 'Bare' and returns true, as both words have similar phonetic sounds.

The GIF below illustrates the testing of the Excel rule:




 ![phonetic-rule-testing](/resources/Storage/neutrinos-reels-publication/images/phonetic-rule-testing.gif)

For more information on testing, see the [Testing](/articles/neutrinos-reels-publication/testing) topic.

[Next Topic](/articles/neutrinos-reels-publication/sentiment-analysis-rule)

[Previous Topic](/articles/neutrinos-reels-publication/levenshtein-distance-rule)
