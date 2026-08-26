# Using Constants

<https://documentation.neutrinos.com/articles/#!pulse-publication/excel-rule>

Excel rules enable seamless data and rule management using the familiar spreadsheet interface. This topic explains configuring and deploying the Excel rule in the Reels Platform.

Steps to Create, Manage, and Map Data in an Excel Rule:

1. Click the **Rules **button in the sub-module navigation bar to open the Rules List page. This page displays a list of rules created in the Reels platform in a tabular format, including details such as the Rule Name, Rule ID, Version, Rule Type, Author, Date of Creation, and Last Updated Date.
2. Click the **Add** button on the top right of the **Rule list** page > Click **Rule** from the dropdown options.
    ![rule-add-button](/resources/Storage/pulse-publication/images/rule-add-button.png)
3. In the pop-up window, enter a **Rule Name**, add a **description** for the rule that describes the purpose of the rule or its functionality, and select **Excel** Rule as the Rule Type.
    ![add-excel-rule](/resources/Storage/pulse-publication/images/rule-add-excel-rule.png)
4. Click the **Create** button to create the rule.
5. When a rule is created, the Rule Details page opens, allowing you to configure the rule. This page displays key information about the rule, including Version, Status, Last Updated date, Created Date, Deployment ID, and more.
    Additionally, the following sections provide further details:
    ![excel-rule-details-page](/resources/Storage/pulse-publication/images/rule-details-excel-rule.png)
  - **Description**: Displays the rule description.
  - **Constants**: Lists the constants used in the rule.
  - **Input and Output Editors**: Allows you to define and manage input and output parameters.
6. Navigate to the Rule Designer tab > Double-click the Rule name to open the Rule editor. This page contains 3 tabs, namely Rule, Model Editor, and Constants.
    ![designer-excel-rule](/resources/Storage/pulse-publication/images/excel-rule-doubleclick-designer.gif)
  1. In the Rule tab, you are prompted to upload an Excel sheet. You can browse and select the file to upload.
  2. After uploading an Excel sheet, click the **Next** button. The inputs and outputs defined in the sheet are populated into the target fields.
  3. Click the Model Editor tab > Add necessary input-output keys using **Add Root** in both input and output editors.
      ![excel-rule-add-roots](/resources/Storage/pulse-publication/images/excel-rule-add-roots.png)
      ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png)
      The keys can be of type string, number, boolean, object, or an array of string, number, or object.
      The settings icon (![](/resources/Storage/pulse-publication/images/configure-icon.png)) in the created input key allows you to configure its behavior during rule testing. Similarly, the toggle (![](/resources/Storage/pulse-publication/images/projection-toggle.png)) in the created output key represents projection, allowing you to control whether the key is included as an output in an API call. For more details on configuration and projection, see the [Configurations](/smart/project-neutrinos-reels/configurations)topic.
  4. Switch back to the **Rule** tab and map the keys defined in the previous step to the target input and output fields.
      ![excel-rule-map-keys](/resources/Storage/pulse-publication/images/excel-rule-map-keys.png)
  5. Click the **Save** button to save the rule.
7. Finally, click the **Save and Publish** button to save and deploy the rule. Enter the **Release Notes** to differentiate between the versions of the rules.

The GIF below demonstrates how to create an **Excel** rule to calculate the total discount and premium discount based on the number of years a policy is taken.:

![excel-rule-gif](/resources/Storage/pulse-publication/images/rule-excel-rule.gif)

## Using Constants

You can add a constant using the **Add Constant** button in the **Constant** section on the **Rule Details** page by specifying a key (constant name) and a value.




 ![excel-rule-add-constant-ruledetails](/resources/Storage/pulse-publication/images/excel-rule-add-constant-ruledetails.gif)

Alternatively, you can add a constant from the Constant tab on the Rule Designer page.




 ![excel-rule-add-constant-designer](/resources/Storage/pulse-publication/images/excel-rule-add-constant-designer.gif)

To use a constant, map the constant created in the platform to the fields declared in the Excel sheet. The GIF below demonstrates how to map a platform-defined constant to a field specified in the Excel sheet.




 ![excel-rule-constant-mapping](/resources/Storage/pulse-publication/images/excel-rule-constant-mapping.gif)

## Rule Illustration

### Prepare Excel Sheet

The first step is to create an Excel sheet for use with the Excel Rule. This section explains how to configure an Excel sheet for integration into the Excel Rule. Follow the steps below to create the sheet:

1. **Open Excel and Create a New Worksheet**:
  - In any cell, say A5, add the input BasePremium.
  - In cell A6, add the input YearsOfPolicyHolder.
  - Add the outputs PremiumDiscount and TotalDiscount in the consecutive cells.
2. **Define Name Ranges**:
  - For the BasePremium value in cell B5, define the named range as IP_Base_Premium.
  - For the YearsOfPolicyHolder value in cell B6, define the named range as IP_YearsOfPolicy.
  - For the PremiumDiscount value in cell B7, define the named range as OP_PremiumDiscount.
  - For the TotalDiscount value in cell B8, define the named range as OP_TotalDiscount.
3. **Enter Input Values**:
  - Enter the value for Base Premium in cell B5 (e.g., 1000).
  - Enter the value for YearsOfPolicyHolder in cell B6 (e.g., 3, 5, or 10 years).
4. ** Apply Formulae**:
  - Insert a formula in cell B7 to calculate the Premium Discount based on the Policy Duration:
    - If B6, YearsOfPolicyHolder is less than or equal to 3, then the PremiumDiscount percentage will be 5% (0.05).
    - If the YearsOfPolicyHolder is less than or equal to 6, then the PremiumDiscount will be 10% (0.1).
    - If YearsOfPolicyHolder is greater than or equal to 7, then the PremiumDiscount percentage will be 15% (0.15).
    - In cell B6, enter the formula : =IFS(IP_YearOfPolicy<=3, 0.05, IP_YearOfPolicy<=6, 0.1, IP_YearOfPolicy>=7, 0.15).
5. ** Calculate Total Discount**:
  - Calculate the TotalDiscount based on the BasePremium and PremiumDiscount:
    - In cell B13, enter the formula: =B5 * B7.

The GIF below illustrates how to configure an Excel worksheet to compute the premium discount and total discount for an Excel rule.

![configure-excel](/resources/Storage/pulse-publication/images/configure-excel-excel-rule.gif)

The configured Excel sheet can now be integrated for use in the Excel Rule. Click [here](/resources/Storage/pulse-publication/Excel-Rule-excelsheet/ExcelRuleSheet-Sample.xlsx) to download the Excel file created in the above steps.

### Integrate Excel Sheet into Excel Rule

Follow the steps below to integrate the excel sheet into the Excel Rule:

1. Click the **Rules** button in the left-side navigation bar to open the **Rules List** page.
2. Click the **Add** button on the top right of the **Rule list** page > Click **Rule** from the dropdown options.
3. In the pop-up window, enter a **Rule Name**, add a **description** for the rule that describes the purpose of the rule or its functionality, and select **Excel** Rule as the Rule Type.
4. Click the **Create** button to create the rule.
5. After creating the rule, the Rule Details page is displayed.
6. Navigate to the Rule Designer tab > Double-click the Rule name to open the Rule editor.
  1. In the Rule tab, you are prompted to upload an Excel sheet. Upload the Excel sheet created using the steps outlined in the previous section.
  2. After uploading an Excel sheet, click the **Next** button. The inputs and outputs defined in the sheet are populated into the target fields.
  3. Click the Model Editor tab > Add necessary input-output keys using **Add Root** in both input and output editors.
  4. Switch back to the **Rule** tab and map the keys defined in the previous step to the target input and output fields.
  5. Click **Save** to save the rule
7. Finally, click **Save and Publish** to save and publish the rule.

The GIF below illustrates how to integrate the Excel sheet into the Excel Rule to calculate the total discount and premium discount for an input base premium.




 ![excel-rule-integrate-excel-to-rule](/resources/Storage/pulse-publication/images/excel-rule-integrate-excel-to-rule.gif)

## Testing Rule

To test the created rule, navigate to the Testing tab from the **Rule Designer** page.

1. Click the **Single** tab in the Testing section, then click the **Add** button in the top-right corner of the page to perform the test. From the dropdown, select **Single**.
2. This rule calculates the total discount and premium discount based on a base premium of 1000 and a policy duration of 3 years. It returns the total discount as 50 and the premium discount as 0.05.

The GIF below illustrates the testing of the Excel rule:




 ![excel-rule-testing](/resources/Storage/pulse-publication/images/excel-rule-testing.gif)

For more information on testing, see the [Testing](/smart/project-neutrinos-reels/testing) topic.

[Next Topic](/articles/pulse-publication/api-rule)

[Previous Topic](/articles/pulse-publication/decision-tree)
