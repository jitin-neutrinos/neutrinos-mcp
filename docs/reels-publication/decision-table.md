# Decision Table

<https://documentation.neutrinos.com/articles/#!reels-publication/decision-table>

A decision table contains rows and columns that work together to form rules. They contain multiple inputs, and return multiple outputs for values that you specify.

The rules inside decision tables are executed one-by-one in the order they are placed in the table. The execution logic of one rule (row in the vertical table) is the following:

*IF all conditions for a row are satisfied then all the results for the corresponding row will be the output .*

If at least one condition is violated, all other conditions in the same row are ignored and are not evaluated. If the operator of a condition cell is set to "anything" then, condition is always true. Results are evaluated only if all conditions in the same row evaluated to be true.

![](/resources/Storage/reels-publication/product-info/Decision%20Table%20Config.png)

**Use Case**

Let us consider an example where Customers whose policy duration:

- Is Greater than or equal to 3 years are eligible for a discount on base premium.
- Is less than 3 years are not eligible for a discount.

Let us consider this use case and create a product using Decision table as a rule.

1. Navigate to Products > Add Product.
2. Enter the Product name within the Product Info tab.
   ![](/resources/Storage/reels-publication/cookbook_1.png)
3. Click on the Rules flow tab > Rule button and add a new rule.
   Enter the following details:
   - Rule name
   - Description
4. Select the rule as Decision Table.
   ![](/resources/Storage/reels-publication/rule-grouping/NewRule.png)
   A node with Rule Type as Decision_Table is displayed.
   ![](/resources/Storage/reels-publication/rule-grouping/DT.png)
5. Connect the Start and end to the node and click on Rule's Data.
   ![](/resources/Storage/reels-publication/reels-cookbook-dtable-formula/Ruledata.png)
6. The Decision Table Config window is displayed.
   ![](/resources/Storage/reels-publication/rule-grouping/Destab.png)
7. Click on the ![](/resources/Storage/reels-publication/rule-grouping/anything.png) icon.
   The operator select pop-up window is displayed. For more information about all the available decision table operators, refer to [Decision Table Operators](/articles/reels-publication/decision-table-operators).
   ![](/resources/Storage/reels-publication/rule-grouping/Ref1.png)
8. Search for an operator and click on it to add.
   As per our use case, let us search and add the first operator (as a condition) which is **Greater Than or Equal to.
   ![](/resources/Storage/reels-publication/rule-grouping/greaor.png)
   **The second operator will be result of the condition we have added. In this case the operator will be equals to and the result will be yes.
   ![](/resources/Storage/reels-publication/rule-grouping/eligib.png)
9. Let us add a second condition and a result for the added condition**.
   ![](/resources/Storage/reels-publication/rule-grouping/DT-2.png)
   **
10. Click Save to save the decision table config.
11. After saving, click on Data Mapping and configure the Input.
   ![](/resources/Storage/reels-publication/rule-grouping/IDMupdtd.png)
12. Click Save.
13. Click on the Deploy toggle button and deploy your product.
   ![](/resources/Storage/reels-publication/Deploy.png)
14. Navigate to Sandbox and validate the configured output.
   ![](/resources/Storage/reels-publication/decision-table/validate.png)

**View and Download this example**

To view this example, download the

Decision Table Workflow

sample and import it within the Reels platform. For more information about importing, refer to the

Import

feature.
