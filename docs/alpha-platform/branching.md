# Create Branch

<https://documentation.neutrinos.com/articles/#!alpha-platform/branching>

A branch is a logical copy of a baseline (such as the main or master branch) that maintains its own sequence of changes. Each branch tracks a distinct set of modifications while preserving a shared history with the baseline.




 ![alpha-change-tracking-branches-landing-page](/resources/Storage/alpha-platform/images/alpha-change-tracking-branches-landing-page.png)

- **Branch Name**: Displays the logical identifier for each branch, typically the branch name. This column can be sorted in ascending or descending order to help view and navigate specific records, making it easier to locate changes made to a particular branch.
- **Head Commit**: Indicates the most recent commit associated with the branch. Each head commit is represented by a unique commit ID and serves as the current snapshot of changes in that branch.
- **Author**: Identifies the user who last updated the branch, supporting accountability by linking changes to individual contributors.
- **Last Updated**: Displays the date and time when the branch was last modified.
- **Actions**: Contains a kebab icon (three-dots) providing branch-specific operations, such as:
  - Viewing commit history.
  - Comparing changes.
  - Creating a pull request.
- **Supporting Controls**:
  - **Search (Branch Name)**: Filters branches by name to quickly locate a specific branch.
  - **Create Branch**: Enables users to create a new branch from an existing main branch.
  - **Pagination and Row Controls**: Supports navigation between pages and allows you to select the number of rows displayed per page.

## Create Branch

Creating a branch in a change tracking system is the process of establishing a new, independent line of change derived from an existing branch (such as the main or release branch). Branch creation initializes a new branch that inherits the complete state of a selected source branch at a specific commit. All subsequent changes made in the new branch are tracked independently while retaining a shared historical lineage with the source.

To create a new branch, follow the steps below:

1. From the Commits landing page, select Branches from the left navigation panel.
    ![alpha-change-tracking-branches-landing-create-branch-button](/resources/Storage/alpha-platform/images/alpha-change-tracking-branches-landing-create-branch-button.png)
2. On the Branches page, click Create Branch in the top-right corner.
    ![alpha-change-tracking-branches-landing-create-branch-popup](/resources/Storage/alpha-platform/images/alpha-change-tracking-branches-landing-create-branch-popup.png)
3. In the pop-up dialog, enter a name for the new branch and select the parent branch from the available options in the drop-down list.
    ![alpha-change-tracking-branches-landing-create-branch-popup-values](/resources/Storage/alpha-platform/images/alpha-change-tracking-branches-landing-create-branch-popup-values.png)
4. After entering a valid branch name and selecting the main branch as the parent, click Create at the bottom of the pop-up dialog.
    ![alpha-change-tracking-branches-landing-create-branch-create-button](/resources/Storage/alpha-platform/images/alpha-change-tracking-branches-landing-create-branch-create-button.png)
5. A success message is displayed, and the newly created branch is added to the list of branches in the table.
    ![alpha-change-tracking-branches-landing-create-branch-success](/resources/Storage/alpha-platform/images/alpha-change-tracking-branches-landing-create-branch-success.png)

## View Details

After the branch is created from the main branch, you can view the details of the newly created branch. To view the branch details, follow these steps:

1. In the Actions column, click the kebab icon and select View Details from the menu.
    ![alpha-change-tracking-branches-view-details](/resources/Storage/alpha-platform/images/alpha-change-tracking-branches-view-details.png)
2. The next screen displays the details of the selected branch. It lists all branches that were created from the specified parent branch. The page displays the information in a table containing columns to display the commit ID, Message, Branches, Author, Date, and Actions.
    ![alpha-change-tracking-branches-view-details-page](/resources/Storage/alpha-platform/images/alpha-change-tracking-branches-view-details-page.png)
3. From the list, select the newly created branch to view all changes made to that branch. Note that the branch drop-down at the top of the page displays the name of the branch from which you navigated to the details page, as illustrated in the image below:
    ![alpha-change-tracking-branches-view-details-page-changes](/resources/Storage/alpha-platform/images/alpha-change-tracking-branches-view-details-page-changes.png)

On the page that displays information about changes made by a specific commit, the interface allows you to view those changes in multiple ways:

- You can search for a specific change made by a commit in a particular branch using the search bar at the top of the left panel.
   ![alpha-change-tracking-branches-view-details-page-search-bar](/resources/Storage/alpha-platform/images/alpha-change-tracking-branches-view-details-page-search-bar.png)
- You can use the toggle in the left panel to view either all changes or only the changes made to a particular branch by selecting All or Changed.
   ![alpha-change-tracking-branches-view-details-page-view-toggle](/resources/Storage/alpha-platform/images/alpha-change-tracking-branches-view-details-page-view-toggle.png)
- You can view changes in either a unified or side-by-side view to compare modifications to the existing code. You can also switch between light and dark display themes by clicking the theme icon. Additionally, you can choose to view all lines of code or only the modified lines by clicking the eye icon. Navigation controls are provided in the top-right corner to move through each change using the arrow icons displayed next to the total number of changes.
   ![alpha-change-tracking-branches-view-details-page-dark-light-side-unified](/resources/Storage/alpha-platform/images/alpha-change-tracking-branches-view-details-page-dark-light-side-unified.png)
