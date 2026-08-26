# Create First Global Custom Code

<https://documentation.neutrinos.com/articles/#!pulse-publication/create-global-custom-code>

To create global custom code, follow the steps below:

1. Click the** Custom Code** icon on the top bar, next to the user profile icon, to open the Custom Code page.
2. The **Custom Code** page lists all the available custom codes in the platform in a columnar format, as shown in the image below:
    ![custom-code-landing-page](/resources/Storage/pulse-publication/images/custom-code-landing-page.png)
  - **Name**: Displays the name of the custom code.
  - **Version**: Displays the latest version number of the custom code. A new version is automatically created each time a change is made and saved on the platform. The number displayed in this column represents the most recent version available for that custom code.
  - **Last Update and Time**: Displays the date and timestamp of the most recent edit made to the custom code.
  - **Last Test Execution Time**: Displays the total duration taken by the most recent test cases of the custom code to run to completion.
  - **Last Test Status**: Displays the result of the most recent test executed on the custom code—either Success or Failed.
  - **Release Note**: Displays the release note entered when the custom code was published to the Marketplace.
  - **Action**: Contains a kebab menu that provides options to Clone or Delete the specific custom code.
  - The caret icon at the end of each row expands to display all available versions of the specific custom code. The details of each version are shown in the same columnar format as described above, except for the Name column, which is omitted since the expanded section pertains to the selected custom code.
3. Click the Create button at the top-right corner to start creating a new custom code on the platform.
    ![custom-code-create-new](/resources/Storage/pulse-publication/images/custom-code-create-new.png)
4. By default, a randomly generated name is assigned to every newly created custom code, which you can update as needed. You will be prompted to provide a name to identify the custom code. Enter a meaningful name and click the Save button.
5. The new Custom Code page interface is divided into three sections, as shown in the image below:
    ![custom-code-page-sections](/resources/Storage/pulse-publication/images/up-custom-code-page-sections.png)
    The Code page allows you to write, run, and validate custom code. Usage – Displays the modules and specific components where the custom code is referenced or used. The Plugins tab displays a list of plugins that are supported and can be directly used within the custom code—for example, cms-service, case-services, and others.
6. The code section itself is split into two sections, as shown in the image below:
    ![custom-code-two-sections](/resources/Storage/pulse-publication/images/custom-code-two-sections.png)
  - The left panel, **Code**, is used for writing custom code.
  - The right panel, **Runtime Panel**, displays the output when the custom code is executed.
7. Write a valid JavaScript or TypeScript snippet in the Code section, based on your specific requirements.
8. After writing the code, run and verify the results by clicking the Run button at the top of the Code section on the Custom Code page.
9. You can further test the custom code with a specific project (context) by selecting the desired project from the Project dropdown. Once a project is selected, the Page dropdown becomes enabled, allowing you to associate the custom code with a specific page within that project. If no project is selected, the Page dropdown remains disabled.
    ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png)
    Note: Selecting a project and page within the Custom Code page does not bind the code to the selected project. It is only for testing the custom code before implementing it within the project.
10. Once the required functionality of the custom code is completed, tested, and verified, click the Save button. This creates a new version of the custom code. You can access available versions from the dropdown menu at the top of the page.
11. Click the Save button in the top-right corner to save the custom code. Then click the Publish button at the top-right corner to publish the custom code to the Marketplace. You will be prompted to provide relevant release notes during the publishing process. Once a specific version of the custom code is published, it can be accessed from the Workflow Studio by referencing its name and selecting the published version.

## Create First Global Custom Code

To create your first global custom code, follow the steps below:

1. Click the Custom Code icon on the top bar, next to the user profile icon, to open the Custom Code page. Then, click Create in the upper-right corner of the page..
2. Assign a name to the custom code to identify it on the platform.
3. On the New Custom Code page, use the left panel to write your code as per the requirement. For example, the following code adds two integers.
    ![global-custom-code-add-two-numbers](/resources/Storage/pulse-publication/images/global-custom-code-add-two-numbers.gif)
    The code above defines a function named total that accepts two input values and returns their sum, which is then printed to the console.
4. Once the code is written, click the Save button to save your changes.
    ![global-custom-code-save-sample](/resources/Storage/pulse-publication/images/global-custom-code-save-sample.png)
5. Click the Run button at the top of the code panel to execute the code. The output will be displayed in the Runtime panel on the right.
    ![global-custom-code-run-sample](/resources/Storage/pulse-publication/images/global-custom-code-run-sample.gif)

## Keyboard Shortcuts

The Global Custom Code supports the following keyboard shortcuts:

| **Shortcuts** | **Description** |
| --- | --- |
| c | On the Global Custom Code page, pressing the 'c' key opens a new custom code editor for creating a Global Custom Code. |
| ctrl + / or cmd + / | Opens a list of all available shortcuts for the current page. |
| **Keyboard shortcuts available in the Custom Code Page** |  |
| ctrl + s or cmd + s | Save the custom Code |
| ctrl + shift + s or cmd + shift + s | Publish the Custom Code |
| ctrl + shift + enter or cmd + shift + enter | Execute the Custom Code |
| Esc | Sets focus to the Project Dropdown |
| Enter | Save name and set focus to the editor |
| / | Sets focus to the code editor |
