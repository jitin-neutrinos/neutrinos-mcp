# Create Template

<https://documentation.neutrinos.com/articles/#!neutrinos-reels-publication/content-repository>

The Content Repository in the Neutrinos Reels platform provides a centralized space for creating and managing templates for various use cases, such as broadcast messages and email templates. It allows users to define a schema, which serves as a blueprint for building templates that can be utilized through API calls across different use cases.

![reels-content-repository-landing-page](/resources/Storage/neutrinos-reels-publication/images/reels-content-repository-landing-page.png)

The platform organizes all available content templates (schema) in a tabular format, displaying relevant information across multiple columns.

- **Name**: Specifies the name of the template (schema) defined during template creation, which is used to identify the template within the platform. If any tag was associated with the template during creation, it is also displayed next to the template name.
- **Author**: Displays the user ID of the person who created the template (schema) within the platform.
- **Version**: Displays the latest version of the template (schema) available within the platform. To view all available versions, click the caret icon at the end of the row to expand the row. This displays all other versions of the same template (schema) available in the platform.
- **Last Modified Date and Time**: Displays the date and timestamp of the most recent changes made to the template (schema).
- **Available From**: Displays the date and timestamp when the template (schema) was created.
- **Actions**: This column contains a kebab icon, which allows you to delete the template (schema) from the platform when clicked.
- A caret icon at the end of each row allows you to expand the row to view the different versions of the template (schema) created within the platform.

You can search for a template (schema) using the search bar on the page. Additionally, the pagination options allow you to select the number of visible rows and navigate between pages using the arrow buttons.

## Create Template

Follow the steps below to create a template (schema) within the platform:

1. Access the Content Repository using the left-hand navigation panel.
    ![reels-content-repository-navigate](/resources/Storage/neutrinos-reels-publication/images/reels-content-repository-navigate.png)
2. Click the New dropdown button at the top-right corner of the page to access options for creating a new template or importing an existing template into the platform.
    ![reels-content-repository-navigate-add-new](/resources/Storage/neutrinos-reels-publication/images/reels-content-repository-navigate-add-new.png)
3. The next page allows you to add variables that will be used in the template (schema). The page is divided into two sections: the Details section and the Add Content section, where you can design the template according to your requirements.
    ![reels-content-repository-create-new](/resources/Storage/neutrinos-reels-publication/images/reels-content-repository-create-new.png)
  - The Details page displays all information related to the template, including the template name, creation date, and available versions (a hyphen is displayed if no previous versions exist). It also allows you to add a brief description and provides a section at the bottom to define the schema, including the variables that will be used within the template.
      ![reels-content-repository-create-new-details-section](/resources/Storage/neutrinos-reels-publication/images/reels-content-repository-create-new-details-section.png)
      ![Note](/resources/Storage/neutrinos-reels-publication/project-trailproject/note.png)
      Note: Save the template on the platform before adding content, as saving the template is mandatory. You can also provide tags while saving the template.
  - The Add Content page allows you to design and add content to the template (schema) according to your requirements.
      ![reels-content-repository-create-new-add-content-section](/resources/Storage/neutrinos-reels-publication/images/reels-content-repository-create-new-add-content-section.png)
4. Once the input variables are added, navigate to the Add Content section and add the required content for the template. In the example below, two input keys — age and name — are used in the schema. These keys act as user inputs for the template, which is then created in the Add Content section, as shown in the GIF below.
    ![reels-content-repository-add-schema-details](/resources/Storage/neutrinos-reels-publication/images/reels-content-repository-add-schema-details.gif)
    ![Note](/resources/Storage/neutrinos-reels-publication/project-trailproject/note.png)
    Note: In the Add Content section, the variables age and name enclosed within {{ and }} are treated as user inputs.
