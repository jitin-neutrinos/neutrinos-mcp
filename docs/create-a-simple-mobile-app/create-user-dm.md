# Create the User Data Model

<https://documentation.neutrinos.com/articles/#!create-a-simple-mobile-app/create-user-dm>

1. To create a [Data Model](/articles/project-concepts/legacy-data-model), click the **Add** button from the menu list, and select **Data Model**. Data Model dialog box appears. You can **add** a new data model or** Import** a data model from another app.![](/resources/Storage/create-a-simple-mobile-app/hdfcdatamodels.png)
2. Create the** User** data model with the following description. This data model captures information about the staff of the organization.

### 

After creating the data model, click **Models **in the Menu list and select the **User** data model to design it. Add the following fields to the data model:

| **Name ** | **Type** | **IsArray** |
| --- | --- | --- |
| firstName | string | false |
| lastName | string | false |
| dob | date | false |
| pan | string | false |

After adding the fields, the data model should look like this:
