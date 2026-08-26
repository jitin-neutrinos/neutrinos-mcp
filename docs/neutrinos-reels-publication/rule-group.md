# Integrate with Workflow

<https://documentation.neutrinos.com/articles/#!neutrinos-reels-publication/rule-group>

In the Neutrinos Reels platform, a **Rule Group** is a logical collection of individual rules evaluated collectively to determine outcomes based on defined conditions. It provides a structured approach to managing complex business logic, ensuring that multiple conditions and their corresponding actions are processed systematically.

Follow the steps below to add a Rule Group in reels platform:

1. Click **Rules** from the Navigation bar.
2. In the **Rules List** page, click the **Add** dropdown button > Choose **Rule Group** as shown in the image below:
    ![add-rule-group](/resources/Storage/neutrinos-reels-publication/images/add-rule-group.png)
3. The **Rules Details** page allows you to define a **Rule Group**. By default, the Rule Group is untitled. To rename it, click the **Edit** button next to the default name. This page displays key details about the Rule Group, including its version, status, last updated date, created date, and deployment status. It also provides sections for adding a description, defining constants, and managing input and output keys through input-output editors. The image below illustrates the layout of the Rules details page:
    ![](/resources/Storage/neutrinos-reels-publication/images/rule-designer-rule-group.png)
4. Click the **Rule Designer** tab to open the designer and add decision logic. You can create a new rule logic or import an existing rule or rule group into the designer. To create a rule group, drag and drop a new rule type to define the new rule logic, or drag and drop an existing rule or rule group. The image below illustrates the Rule Designer page for Rule Group:
    ![designer-page-rule-group](/resources/Storage/neutrinos-reels-publication/images/rule-designer-page-rule-group.png)
5. After placing individual rules on the canvas, connect them in the desired execution order using arrows. The GIF below illustrates how to add and link rules within a Rule Group.
    ![rule-group-page](/resources/Storage/neutrinos-reels-publication/images/rule-designer-rule-group-page.gif)
6. After creating the Rule Group logic, configure the input and output keys for each rule:
    Map the input and output targets for the rule. Click **Save** at the individual rule level to apply the changes.
  1. If new rule logic is used, add the required input and output keys.
  2. If existing rule logic is reused, verify the preconfigured input and output keys.
7. Finally, click the **Save**** and Publish** button to save and publish the Rule Group.

The GIF below demonstrates how to add a rule group to check eligibility for a discount. In this example, the rule group returns **Eligible** if the discount is above **500**, the age is above **18**, and the gender is **Male**.

![rule-group-add-rulegroup](/resources/Storage/neutrinos-reels-publication/images/rule-group-add-rulegroup.gif)

| ![Note](/resources/Storage/neutrinos-reels-publication/project-trailproject/note.png) | When you save and publish the Rule Group, you can either create a new version or overwrite the existing one. |
| --- | --- |

## Integrate with Workflow

A Rule Group can be integrated into a workflow. The steps below illustrate how to integrate a Rule Group into workflow:

1. Navigate to the Workflow section. Click the **Add** button to create a new Workflow.
    ![add-new-workflow](/resources/Storage/neutrinos-reels-publication/images/workflow-add-new-workflow.png)
2. Enter a name to the Workflow.
3. Import an existing Rule Group into the workflow, by dragging and dropping it to the workflow.
4. Connect the nodes in the required execution sequence.
5. Configure the input-output model with the proper input-output keys.
6. Click the **Save** button.
7. Finally, click the **Save and Publish **button, to save and publish the Workflow.

The GIF below illustrates how to integrate a Rule Group created in the previous section into a workflow:

![rule-group-with-workflow](/resources/Storage/neutrinos-reels-publication/images/integrate-rul-group-with-workflow.gif)

[Next Topic](/articles/neutrinos-reels-publication/workflow)

[Previous Topic](/articles/neutrinos-reels-publication/configurations)
