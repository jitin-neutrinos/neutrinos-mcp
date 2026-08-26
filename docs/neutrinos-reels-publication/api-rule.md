# Using Constants

<https://documentation.neutrinos.com/articles/#!neutrinos-reels-publication/api-rule>

The API rule facilitates integration with external services and systems through an Application Programming Interface (API). It enables seamless interaction with other software, allowing data retrieval and transmission. This topic explains configuring and deploying the API rule in the Reels Platform.

Steps to Create, Manage, and Map Data in an API Rule:

1. Click the **Rules** button in the left-side navigation bar to open the **Rules List** page. This page displays a list of rules created in the Reels platform in a tabular format, including details such as the Rule Name, Rule ID, Version, Rule Type, Author, Date of Creation, and Last Updated Date.
2. Click the **Add** button on the top right of the **Rule List** page > Click **Rule** from the dropdown options.
    ![rule-add-button](/resources/Storage/neutrinos-reels-publication/images/rule-add-button.png)
3. In the pop-up window, enter a **Rule Name**, add a **description** for the rule that describes the purpose of the rule or its functionality, and select **API** Rule as the Rule Type.
    ![add-api-rule](/resources/Storage/neutrinos-reels-publication/images/rule-add-rule-api-rule.png)
4. Click the **Create** button to create the rule.
5. When a rule is created, the Rule Details page opens, allowing you to configure the rule. This page displays key information about the rule, including Version, Status, Last Updated date, Created Date, Deployment ID, and more.
    Additionally, the following sections provide further details:
    ![api-rule-details-page](/resources/Storage/neutrinos-reels-publication/images/rule-designer-api-rule.png)
  - **Description**: Displays the rule description.
  - **Constants**: Lists the constants used in the rule.
  - **Input and Output Editors**: Allows you to define and manage input and output parameters.
6. Navigate to the Rule Designer tab > Double-click the Rule name to open the Rule editor. This page contains 3 tabs, namely Rule, Model Editor, and Constants.
    ![designer-api-rule](/resources/Storage/neutrinos-reels-publication/images/api-rule-doubleclick-designer.gif)
  1. In the Rule tab, select an **HTTP** method, such as **POST**, **GET**, or **PUT**, and enter the API URL. To use dynamic input, enable the **Input** toggle and specify the input source using the defined input key.
  2. Add the **Header**, **Request** **Body**, and **After Response**, as per the requirement.
    - **Header**: Accepts the header parameters required for the API call.
        To add a Header, navigate to the **Rule** tab and go to the **Header** section. Click **Add Header**, then enter the **Key** and **Value** for the header. To use dynamic input, enable the **Input** checkbox and specify the input source using the defined input key. By default, the Input checkbox is disabled.
    - **Request Body**: Defines the request body parameters required for the API call.
        To add a field in the **Request Body**, navigate to the **Rule** tab and go to the **Request Body** section. Click **Add Field**, then enter the **Key** and map the **Input Source** for the request body. To use dynamic input, enable the **Input** checkbox and specify the input source using the defined input key. By default, the Input checkbox is disabled.
    - **After Response**: Define the parameters required to handle the API response.
        To add a field in **After Response**, navigate to the **Rule** tab and go to the **After Response** section. Click **Add Field**, then enter the **Key,** and map the **Output Target **for the after response.
  3. Click the Model Editor tab > Add necessary input-output keys using **Add Root** in both input and output editors. For example, in an API call to add a product, define **inputTitle** for the input parameter and **id** and **outputTitle** for the output parameters as illustrated in the image below:
      ![api-rule-add-input-output-roots](/resources/Storage/neutrinos-reels-publication/images/api-rule-add-input-output-roots.png)
      ![Note](/resources/Storage/neutrinos-reels-publication/project-trailproject/note.png)
      The keys can be of type string, number, boolean, object, or an array of string, number, or object.
      The settings icon (![settings-icon](/resources/Storage/neutrinos-reels-publication/images/configure-icon.png)) in the created input key allows you to configure its behavior during rule testing. Similarly, the toggle (![projection-icon](/resources/Storage/neutrinos-reels-publication/images/projection-toggle.png)) in the created output key represents projection, allowing you to control whether the key is included as an output in an API call. For more details on configuration and projection, see the [Configurations](/articles/neutrinos-reels-publication/configurations)topic.
  4. Switch back to the **Rule** tab and map the keys defined in the previous step to the target input and output fields.
  5. Click the **Save** button to save the rule.
7. Finally, click the **Save and Publish** button to save and deploy the rule. Enter the **Release Notes** to differentiate between the versions of the rules.

The GIF below demonstrates how to create an API rule to post a product title to a dummy API and receive a response containing the dummy ID and the submitted title:

![api-rule-gif](/resources/Storage/neutrinos-reels-publication/images/rule-api-rule.gif)

## Using Constants

You can add a constant using the **Add Constant** button in the **Constant** section on the Rule Details page by specifying a key (constant name) and a value.




 ![api-rule-add-constant](/resources/Storage/neutrinos-reels-publication/images/api-rule-add-constant.gif)

Alternatively, you can add a **Constant** tab on the **Rule Designer** page.




 ![api-rule-add-constant-designerpage](/resources/Storage/neutrinos-reels-publication/images/api-rule-add-constant-designerpage.gif)

Constants can be used to pass the URL for HTTP methods or as parameters in API calls. The GIF below illustrates using a constant to pass a URL and a request body parameter:




 ![api-rule-use-constant](/resources/Storage/neutrinos-reels-publication/images/api-rule-use-constant.gif)

## Rule Illustration

This use case demonstrates how to configure an API rule to send a POST request to the DummyJSON API, passing the title as a parameter.

Follow the steps below to configure the API rule for the above scenario:

1. Click the Rules button in the navigation bar.
2. In the Rules List page, click the Add button and choose the Rule from the dropdown.
3. In the pop-up screen, enter the Rule Name, provide a Rule Description, select Formula as the rule type, and click the Create button.
    For example:
    ![api-usercase-create-rule](/resources/Storage/neutrinos-reels-publication/images/api-usercase-create-rule.png)
  - **Rule Name**: API Rule Demo.
  - **Description**: API Rule Demo.
4. On the **Rule Details** page, navigate to the **Rule Designer**, tab and double-click the rule name to open the designer and draft the rule. The designer page contains 3 tabs namely, Rule, Model Editor, and Constants.
    ![api-rule-designer-3tabs](/resources/Storage/neutrinos-reels-publication/images/api-rule-designer-3tabs.gif)
5. In the **Rule** tab, under the **Method** section, select an HTTP method such as **POST**, **PUT**, or **GET**. Enter the API URL in the input field. If the **Input** toggle is enabled, select the input source defined by the input key.
    ![api-rule-add-url-postmethod](/resources/Storage/neutrinos-reels-publication/images/api-rule-add-url-postmethod.gif)
6. Add the required parameters for the **Header**, **Request Body**, or **After Response**, as needed.
    Since parameters require input and output keys for mapping, navigate to the **Model Editor** tab and add the necessary roots. Then, go to the** Rule **tab and, under the **Header**, **Request Body**, or **After Response** sections, map the input-output roots created.
    For example, this API call accepts a header parameter **title** and returns a response with **id** and **title**:
    ![api-rule-requestheader-inputkeys](/resources/Storage/neutrinos-reels-publication/images/api-rule-requestheader-inputkeys.gif)
7. Click the **Save** button.
8. Finally, click the **Save and Publish** button to save and publish the rule.

## Testing Rule

To test the created rule, navigate to the Testing tab from the **Rule Designer** page.

1. Click the **Single** tab in the Testing section, then click the **Add** button in the top-right corner of the page to perform the test. From the dropdown, select **Single**.
2. This rule sends the input value 'BMW' to a dummy API, which returns an id of 195 and the title as 'BMW'.

The GIF below illustrates the testing of the Excel rule:




 ![api-rule-testing](/resources/Storage/neutrinos-reels-publication/images/api-rule-testing.gif)

For more information on testing, see the [Testing](/articles/neutrinos-reels-publication/testing) topic.

[Next Topic](/articles/neutrinos-reels-publication/levenshtein-distance-rule)

[Previous Topic](/articles/neutrinos-reels-publication/excel-rule)
