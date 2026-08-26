# List Page

<https://documentation.neutrinos.com/articles/#!pulse-publication/page-layout>

A Page Layout is a metadata-driven configuration that defines how an object's data is presented and interacted with within the application user interface. While the object itself defines the business entity, its fields, relationships, and underlying data structure, the Page Layout determines how this information is organized, displayed, and managed by end users. It acts as the presentation layer of the object and enables you to configure the user experience without modifying the underlying data model.

In the Page Layout configuration, the object is divided into two primary layout types:

1. List Page
2. Form Page

The List Page controls how multiple records of an object are displayed in a tabular view, whereas the Form Page defines the layout used when viewing, creating, or editing an individual record.

## List Page

The List Page defines the presentation and behavior of the object's record listing screen. Whenever users navigate to an object such as Leads, they are presented with a table containing multiple records. The List Page configuration determines how these records are searched, filtered, sorted, displayed, and navigated.




 ![up-hypha-studio-objects-pages-list-view](/resources/Storage/pulse-publication/images/up-hypha-studio-objects-pages-list-view.png)

### Filters

The Filter section defines the search criteria that users can apply to retrieve specific records from the object. Rather than displaying all available records, filters allow users to narrow the results based on one or more attributes such as identifiers, dates, status values, or numeric ranges. Each filter is configured independently and becomes available as a search control on the List Page. Each filter consists of several properties.

1. **Filter Name**: Specifies the display label of the filter as it appears in the user interface. The filter name should clearly indicate the purpose of the filter, such as **CID**, **Task ID**, **Case Status**, and **Case Created At**, as illustrated in the following screenshot.
2. **Binding Value**: Binding Value defines the relationship between the filter displayed on the user interface and the corresponding field within the object model. It specifies which object and fields should be queried when the filter is applied. For example, the filter CID is bound to the CID field within the Case Instance object. Similarly, Task ID is bound to the Task ID field of the Task Instance object.
3. **Filter Type**: Determines the type of input control displayed to users and defines how the filter processes the selected values.
    For example:
    The filter type therefore determines both the interface component displayed and the query logic executed by the platform.
  - A **Date Range** filter provides two date selectors that enable users to specify a start date and an end date. The system returns records whose date values fall within the selected range.
  - A **Search** filter provides a text input field that allows users to search for a specific value. Depending on the configured search behavior, the search can perform an exact match or a partial match.
  - A **Multi Select** filter displays a list of predefined values from which users can select one or more options. The system returns records that match any of the selected values.
  - A **Range** filter is typically used for numeric values. It allows users to specify minimum and maximum values, and the system returns records whose values fall within the specified range.
4. **Filter Value**: Defines the configuration associated with the selected filter type. Depending on the filter type, it specifies the values, search behavior, or range limits used during filtering.
    For example:
  - A **Date Range** filter specifies the start date and end date displayed when the page is opened.
  - A **Search** filter defines the search behavior, such as **Exact Match** or **Partial Match**, which determines how user-entered values are matched against the available records.
  - A **Multi Select** filter defines the list of values available for selection and can optionally specify one or more selected values.
  - A **Range** filter specifies the minimum and maximum values that define the allowable search range.
5. **Action**: The Action column provides deletion operations for each filter definition. Deleting a filter only removes it from the interface. It does not delete the corresponding object field or stored data.

#### Add Filter

The Add Filter enables you to create new filter definitions for the List Page. When a new filter is added, specify the filter name, binding value, filter type, and any associated configuration values.

#### Save Filter

The Save Filter option determines whether users can save customized search criteria for future use. When enabled, users can define a set of filters and store them as reusable search configurations. For example, a sales manager may save a filter that displays only high-priority leads assigned to a specific region.

#### Table Sort

The Table Sort configuration controls whether users can sort records displayed within the List Page. When sorting is enabled, users can arrange records in ascending or descending order based on one or more columns such as Lead ID, Status, Created Date, or Owner.

#### Column Selection

The Column Selection option determines whether users can customize the columns displayed in the record list. When enabled, users may choose which object field they want to display or hide according to their preferences. For example, one user may prefer to view Lead ID, Owner, and Status, while another may prioritize Created Date, Priority, and Assigned Team.

#### Number of Rows

The Number of Rows setting controls the default number of records displayed on each page of the List Page. Pagination improves navigation by limiting the number of records loaded at one time. Admins can configure a default value based on data volumes and usability requirements.

### Column

The Column section defines which object fields are displayed as columns within the List Page table. While filters determine how records are searched, columns determine what information is presented for each retrieved record.

- **Column Label**: The Column Label defines the header text displayed above each column in the record list. The label provides a business-friendly name for the underlying field.
- **Binding Value**: Similar to the filter configuration, the Binding Value specifies the object field associated with each displayed column. The binding establishes the connection between the presentation layer and the underlying business object. For example, the CID column may be bound to the CID field of the Case Instance object, while the Task ID column is bound to the corresponding field within the Task Instance object.
- **Default**: The Default property specifies whether a column is displayed automatically when users first open the List Page. Columns marked as True appear by default, while columns marked as False remain hidden unless users choose to display them through the Column Selection feature.

#### Action

The Action column provides operations for each column definition. Deleting a column removes it from the page layout configuration but does not affect the object's schema or stored data.

### Edit Filter

To edit the name of a filter, follow the steps below:

1. Navigate to the required object, and then click the object to open it.
2. From the left navigation pane, click Page Layouts.
3. On the Filters list page, click the name of the filter that you want to edit. In the filter details section, click the Edit icon to modify the filter configuration as illustrated in the image below:
    ![up-hypha-studio-objects-pages-list-view-edit-filter](/resources/Storage/pulse-publication/images/up-hypha-studio-objects-pages-list-view-edit-filter.png)
4. The next step is to modify the filter properties as required, such as the filter name, binding values, and filter type. For example, the following image illustrates how to edit the filter name:
    ![up-hypha-studio-objects-pages-list-view-edit-filter-save](/resources/Storage/pulse-publication/images/up-hypha-studio-objects-pages-list-view-edit-filter-save.png)
5. After making the required changes to the filter, click Save to save the filter configuration to the platform.

## Form Page

The Form Page is a metadata-driven configuration that defines how individual records of an object are viewed and edited within the application. While the List Page displays multiple records in a tabular format, the Form Page focuses on presenting the complete details of a single object record in a structured and user-friendly manner.

A Form Page acts as a template for an object. It specifies how business data should be organized on the screen, how users interact with each field, and how information is grouped into logical sections. Like other metadata configurations within the platform, the Form Page does not alter the underlying object schema or stored data. Instead, it defines the presentation layer, allowing admins to configure and customize the user experience without modifying the object itself.

Multiple Form Pages can be created for the same object to support different business processes, departments, user roles, or languages. For example, a Customer Service team may require a simplified form that focuses on case details, while an Operations team may need additional operational fields and workflow controls. Since the layout is metadata-driven, each form can present the same underlying object differently while maintaining a consistent data model.




 ![up-hypha-studio-objects-pages-form-page](/resources/Storage/pulse-publication/images/up-hypha-studio-objects-pages-form-page.png)

- **Search**: The Search bar enables administrators to quickly locate existing Form Pages configured for the selected object. As organizations create multiple form layouts for different use cases, the number of configured pages may increase significantly. The search functionality allows you to retrieve a specific page by entering all or part of its name, reducing the time required to navigate through the list.
- **Filter By**: The Filter By option allows you to organize and narrow the displayed list of Form Pages based on criteria.
- **Sort by Category/ Page**: The Sort by Category option controls how Form Pages are ordered within the list. Sorting enables you to organize page layouts alphabetically or according to their assigned category, making navigation more efficient when managing a large number of configurations.
- The central table itself displays all Form Pages configured for the selected object. Each row represents an independent page definition stored as metadata within the platform.
  - **Page Name**: The Page Name uniquely identifies the Form Page within the object. It serves as the primary identifier used while selecting, editing, or assigning page layouts. The Page Name should clearly describe the intended purpose of the layout. Examples might include: Lead Registration, Customer Verification, and so on.
  - **Page Type**: The Page Type identifies the functional purpose of the configured layout.
  - **Type**: The Type column categorizes the Form Page according to its logical implementation.
  - **Category/ Language**: The Category/Language column associates each Form Page with either a business category or a language definition. For example, the Account Name Form Page is associated with the Case Instance category, indicating that it belongs to a specific functional grouping within the application.
  - **Last Updated**: The Last Updated column records the most recent date and time when the Form Page metadata was modified.
  - **Action**: Contains a kebab (⋮) icon that provides page-specific actions. Click the icon to view the available options, such as Edit and Delete.
- **Show By**: The Show By option determines the number of Form Page records displayed on each page.
- **Pagination**: The pagination controls located in the lower-right corner enable you to navigate through multiple pages of Form Page configurations.

Additionally, you can organize fields into the appropriate categories or pages based on the records to which they belong. The following image illustrates fields grouped under their respective categories.




 ![up-hypha-studio-objects-pages-form-page-sorted-categories](/resources/Storage/pulse-publication/images/up-hypha-studio-objects-pages-form-page-sorted-categories.png)

Further, you can edit the category name and assign a color to each category. Color coding helps distinguish categories, making them easier to identify and navigate as illustrated in the image below:




 ![up-hypha-studio-objects-pages-form-page-sorted-categories-edit-color-name](/resources/Storage/pulse-publication/images/up-hypha-studio-objects-pages-form-page-sorted-categories-edit-color-name.png)

The following image shows a sample page layout for the Account Name form page, illustrating its fields and associated details.



![up-hypha-studio-objects-pages-form-page-sample-page-account-name](/resources/Storage/pulse-publication/images/up-hypha-studio-objects-pages-form-page-sample-page-account-name.png)
