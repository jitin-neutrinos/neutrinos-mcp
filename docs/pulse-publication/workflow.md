# Workflow

<https://documentation.neutrinos.com/articles/#!pulse-publication/workflow>

In the Neutrinos Reels platform, a **Workflow** is a logical collection of multiple **Rules** and/or **Rule Groups**, and/or **Sub Workflows** evaluated collectively to determine outcomes based on defined conditions. It provides a structured approach to managing complex business logic, ensuring that multiple conditions and their corresponding actions are processed systematically.

Follow the steps below to add a Workflow in the reels platform:

1. Click **Workflow** from the Navigation bar.
2. In the **Workflow List **page click the **Add** dropdown button > Click **New** as shown in the image below:
    ![add-new-workflow](/resources/Storage/pulse-publication/images/workflow-add-new-workflow.png)
3. The **Workflow details** page allows you to define a Workflow. By default, the Workflow is untitled. To rename it, click the **Edit** button next to the default name. This page displays key details about the **Workflow**, including its version, status, last updated date, created date, and deployment status. It also provides sections for adding a description, defining constants, and managing input and output keys through input-output editors. The layout of this page is similar to the **Rule** or **Rule Group** details page. The image below illustrates the Workflow Details page layout:
    ![workflow-details](/resources/Storage/pulse-publication/images/workflow-details.png)
4. Click the **Rule Designer** tab to open the designer and add decision logic. You can create a new rule logic or import an existing rule, rule group, or workflow into the designer. To create a Workflow, drag and drop a new rule type to define new rule logic, or drag and drop an existing rule or rule group. The image below illustrates the Rule Designer page for Workflow:
    ![workflow-designer](/resources/Storage/pulse-publication/images/workflow-designer.png)
5. After placing rules, rule groups, or workflows on the canvas, connect them in the desired execution order using arrows. The GIF below illustrates how to add and link rules or rule groups within a workflow:
    ![workflow-rules-connect](/resources/Storage/pulse-publication/images/workflow-rules-connect.gif)
6. After creating the Workflow logic, configure the input and output keys for each rule:
    Map the input and output targets for the rule. Finally, click **Save** at the individual rule level to apply the changes.
  1. If new rule logic is used, add the required input and output keys.
  2. If existing rule logic is reused, verify the preconfigured input and output keys.
7. Finally, click the **Save**** and Publish** button to save and publish the Workflow.

The GIF below demonstrates how to create a workflow with two rules and a sub-workflow to determine eligibility. The workflow returns **Eligible** if the person's age is **above 18** and the place is **India**.




 ![add-workflow](/resources/Storage/pulse-publication/images/workflow-add-workflow.gif)

| ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png) | When you save and publish the Workflow, you can either create a new version or overwrite the existing one. |
| --- | --- |

If a subflow is added, you can establish its dependency on the main flow by selecting the **Dependency Flows** checkbox within the subflow settings. To establish the dependency, follow the steps below:

1. Double-click the subflow within a main workflow.
2. Select the **Dependency Flow** checkbox and click **Save**.

The image below highlights the checkbox used to create the dependency:




 ![workflow-dependency-checkbutton](/resources/Storage/pulse-publication/images/workflow-dependency-checkbutton.png)

[Next Topic](/articles/pulse-publication/master-data-management)

[Previous Topic](/articles/pulse-publication/rule-group)
