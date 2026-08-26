# Create Project

<https://documentation.neutrinos.com/articles/#!pulse-publication/get-started-wf-cm>

Login into the Workflow Studio using Neutrinos IDS Credentials. Developers are presented with a list of projects. They can open existing projects, create new ones, or import project from a ZIP file. The image below showcases the Projects page, which displays details of the projects in a tabular form.

![workflow-studio-projects page](/resources/Storage/pulse-publication/images/workflow-studio-projectspage.png)

The table consists of the following details:

1. **Project Name**: Displays the name of the project.
2. **Description**: Displays the description of the Project.
3. **Case Type**: Displays the Case Type. It is the same as the case type from Case Service. To know more on Case Onboarding, see [Onboarding](/articles/pulse-publication/onboard-process-and-case-wf-cm) topic.
4. **Created Date**: Displays the date when the project was created.
5. **Last Updated**: Displays the last updated date of the project.
6. **Status**: Displays the status of a project. For example, Draft or Published.
7. **Action**: Click on the kebab icon in the action column, which displays the option to delete the project.

| ![Note](/resources/Storage/pulse-publication/note.png) | Developers can search or filter the projects in the Workflow Studio using the search or filter options that is available in the UI. |
| --- | --- |

## Create Project

A project in Workflow Studio is essentially a business application designed for a specific scenario. To create a new project in Workflow Studio, follow the steps below:

1. Click the **Create** button on the top-right corner of the Workflow Studio.
2. Select **New Project** option from the dropdown.
3. In the pop-up screen, enter the following details
    ![Note](/resources/Storage/pulse-publication/note.png)
    To know more on creating case in BPM, see Case Manager topic.
  1. **Project Name**: Specify the name of the project.
  2. **Case Type**: Specify the Case Type to be linked to the project. This Case Type should be the same as the one used during Case Onboarding.
      ![Warning](/resources/Storage/pulse-publication/warning.png)
      Accessing the Workbench will not be possible without onboarding the Case Type in the Case Service.
  3. **Description**: Provide a brief description of the project.
  4. **Select Icon**: Select an appropriate icon for the project.
4. Click the **Create** button in the Pop-up screen.

Ensure all fields are filled accurately to proceed with the creation of Project in the Workflow Studio. The GIF below illustrates the process of creating a New Project "TestDemo1" in the Workflow Studio:

![workflow-studio-create-project-gif](/resources/Storage/pulse-publication/images/workflow-studio-create-project-gif.gif)

| ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png) | A single Case Type can be linked to multiple projects. |
| --- | --- |

# Dev Mode

Dev mode is a boolean flag that can be enabled by developers by updating the environment variable. When enabled, it alters the behavior of the workbench.

1. When Dev mode is enabled, regardless of the environment, any changes made in the Workflow Studio—whether on the task page, global page, or even minor updates—are directly reflected in the Workbench.
2. When Dev mode is disabled, regardless of the environment, any changes made in the Workflow Studio are not reflected for Workbench users. To preview these changes in the Workbench, the updated version must be published and tagged as Current. Only the version tagged as Current is visible in the Workbench.

The image below illustrates the Workbench when the Dev mode is active:

![alpha-dev-mode-active-screen-shot](/resources/Storage/pulse-publication/images/alpha-dev-mode-active-screen-shot.png)
