# Use Case

<https://documentation.neutrinos.com/articles/#!reels-publication/formula>

This capability enables you to generate various types of formulas, eliminating the need to directly create the formula within the Rule. Creating rules using Formula empowers you to accomplish the following tasks:

- Construct numerical expressions using all arithmetic operators on fields.
- Generate a formula concerning the columns of an input and output of a previous node.

#### Use Case

Let us consider an example where:

- We calculate the difference in insurance premium from last year to current year.

Let us create a product using the rule type as formula:

#### 

1. Navigate to Products > Add Product.
2. Enter the Product name within the Product Info tab.
   ![](/resources/Storage/reels-publication/cookbook_1.png)
3. Click on the Rules flow tab > Rule button and add a new rule.
   Enter the following details:
   - Rule name
   - Description
4. Enter a Rule name, description and click on Formula.
   ![](/resources/Storage/reels-publication/rule-grouping/Formula1.png)
5. Click Ok.
6. A node with Rule Type as Formula is displayed.
   ![](/resources/Storage/reels-publication/reels-cookbook-dtable-formula/rulename.png)
7. Connect the Start and end to the node and click on Rule's Data.
8. The Formula window is displayed.
   ![](/resources/Storage/reels-publication/rule-grouping/Formune.png)
   Enter the following details:
   - Rule Name
   - Field Name
9. Within the formula field, type your first input value (as per our use case this will be Current Year Premium) and press Enter.
   ![](/resources/Storage/reels-publication/rule-grouping/currentprem.png)
10. The first input value will be added within the formula.
   ![](/resources/Storage/reels-publication/rule-grouping/Enter.png)
11. Select a formula operator ( drag and drop, click on it or type) to add within the formula. Refer to [Formula Operators](/articles/reels-publication/formula-operators) to view information about all the available formula operators.
12. Type the second input value ( in our case Last Year premium) to add the second input value.
   ![](/resources/Storage/reels-publication/rule-grouping/newone.png)
13. After saving the rule config, click on Data Mapping and configure the Input.
   ![](/resources/Storage/reels-publication/rule-grouping/IDM2.png)
14. Click Save.
15. Navigate to Sandbox and validate the configured output.
   ![](/resources/Storage/reels-publication/formula/Amount.png)

**View and Download this example**

To view this example, download the

Formula workflow

sample and import it within the Reels platform. For more information about importing, refer to the

Import

feature.
