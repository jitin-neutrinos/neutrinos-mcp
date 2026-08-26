# Create Pull Request

<https://documentation.neutrinos.com/articles/#!pulse-publication/pull-requests-ct>

Pull Requests (PRs) are a structured mechanism in a change tracking system used to propose, review, validate, and integrate changes from one branch into another. A pull request represents a formal request to merge a set of tracked changes from a source branch into a target branch. It encapsulates the changes, associated metadata, review feedback, and approval status required to complete the integration.

The Pull Requests page displays the required information in a tabular format, as illustrated in the image below.




 ![alpha-change-tracking-branches-pull-requests-landing-page](/resources/Storage/pulse-publication/images/alpha-change-tracking-branches-pull-requests-landing-page.png)

- **Pull Request Identifier (#)**: A unique, system-generated ID assigned to each pull request.
- **Summary**: A short, descriptive title for the pull request that displays the source-to-target branch mapping.
- **Status**: Indicates the current state of the pull request:
  - **Pending**: Awaiting review, approval, or additional updates.
  - **Merged**: Successfully integrated into the target branch.
  - **Declined**: Rejected or closed without merge.
- **Author**: Identifies the user who created the pull request.
- **Reviewers**: Lists the reviewers assigned to validate the changes. This may include multiple reviewers and approval indicators, enforcing the review and approval workflow.
- **Last Updated**: Displays the most recent update timestamp for the pull request.
- **Actions**: This column contains a kebab icon that allows you to view or edit the pull request.

Additionally, you can filter pull requests based on those created by you, those assigned to you for review, and their status—Open, Merged, or Declined, as illustrated in the image below:




 ![alpha-change-tracking-branches-pull-requests-filter](/resources/Storage/pulse-publication/images/alpha-change-tracking-branches-pull-requests-filter.png)

## Create Pull Request

To create a pull request, follow the steps below:

1. From the Commits landing page, navigate to Pull Requests using the left navigation panel.
2. On the Pull Requests page, click Create Pull Request in the top-right corner.
    ![alpha-change-tracking-branches-pull-requests-pr-button](/resources/Storage/pulse-publication/images/alpha-change-tracking-branches-pull-requests-pr-button.png)
3. On the next page, enter the details for creating the PR as illustrated in the image below:
    ![alpha-change-tracking-branches-pull-requests-create-pr-page](/resources/Storage/pulse-publication/images/alpha-change-tracking-branches-pull-requests-create-pr-page.png)
  - **Source**: Specifies the branch that contains the proposed changes, representing the source of the commits to be reviewed and merged.
  - **Destination Branch**: Specifies the target branch into which the changes will be merged (for example, main or a release branch).
  - **Title**: A mandatory, human-readable summary of the pull request that documents the intent and scope of the proposed changes. This summary is used for search, traceability, and audit purposes.
  - **List of Changes**: Displays the calculated differences between the selected source and target branches, including modified, added, and deleted files along with their changes.
  - **Reviewers**: Allows assignment of one or more reviewers responsible for evaluating the changes.
4. After providing all required details, click the **Create PR** button at the top of the page to create the pull request. Upon successful creation, the pull request appears on the Pull Requests page with a Pending status. After the reviewer completes the review, the status changes to Merged. If the pull request is declined, the status changes to Declined.
