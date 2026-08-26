# About the Excel File

<https://documentation.neutrinos.com/articles/#!reels-publication/excel-file>

### About the Excel File

Reels platform leverages conventional spreadsheet files for the representation of business rules. This framework enables users to employ familiar spreadsheet editors like MS Excel™. The actual business users can use MS Excel directly to create and edit business rules spreadsheets.

![](/resources/Storage/reels-publication/decision-table-icons/NewRule.png)

### Defining Rules in Excel

For example, let’s define rules to determine insurance premium discounts based on number of years as a policy holder:

- Customers who are Policy holders from 1-3 years get 5% discount on base premium.
- Customers who are Policy holders from 4-6 years get 10% discount on base premium.
- Customers who are Policy holders for more than or equal to 7 years get 15% discount on base premium.

#### The Excel File

Let’s begin with creating an excel file as per the required structure and keywords defined by the Reels engine:

- **IP_Name ** - The rules engine identifies this as your input field.
- **OP_Name ** - The rules engine identifies this as your output field.

A sample excel sheet is provided below as a reference, which can be used within the Steps to Create a Product using Excel File.

[Sample Excel](/resources/Storage/reels-publication/base%20premium.xlsx)

Steps to Create a Product using Excel File.

1. Login to reels platform using valid credentials.
2. Navigate to Products > Add Product.
    ![Note](/resources/Storage/reels-publication/noteicon.png)
    To import a product, click on the import button and upload a product.
3. Enter the Product name within the Product Info tab.
   ![](/resources/Storage/reels-publication/cookbook_1.png)
4. Click on the Rules flow tab.
5. Click on Rule button to add a new rule.
    ![Note](/resources/Storage/reels-publication/noteicon.png)
    To import a rule, click on the import button and upload a rule.
6. Enter a Rule name, description and click on the Excel File.
7. A node with Rule Type as EXCEL is displayed.
   ![](/resources/Storage/reels-publication/excelruletype.png)
8. Connect the Start and end to the node and click on Rule's Data.
9. Upload the excel document (provided in the previous section).
10. The excel rule config pop-up window is displayed with inputs and outputs as shown below.
   ![](/resources/Storage/reels-publication/decision-table-operators/Xconfig.png)
11. Click Save to save the rule config.
12. After saving the rule config, click on Data Mapping and configure the Input.
13. Click Save.
   The edit product screen is displayed.
14. View the product info details and ensure that the details are accurate.
15. Click on the Deploy toggle button and deploy your product.
   ![](/resources/Storage/reels-publication/Deploy.png)
16. Navigate to Sandbox and validate the configured output.
