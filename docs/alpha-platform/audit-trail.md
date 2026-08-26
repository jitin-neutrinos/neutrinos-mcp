# Purpose

<https://documentation.neutrinos.com/articles/#!alpha-platform/audit-trail>

An audit trail is a system-generated record of all significant actions and changes performed on tracked artifacts such as code, configurations, workflows, cases, or records. It provides a chronological history of who changed what, when, how, and sometimes why, ensuring transparency, traceability, and accountability across the system.

## Purpose

An audit trail serves to:

- Ensure traceability of changes across the lifecycle of an artifact
- Enable accountability by associating actions with authenticated users or system tokens
- Facilitate troubleshooting and root-cause analysis
- Provide historical context for reviews, audits, and incident investigations

The Audit Trail page interface is illustrated in the image below:




 ![alpha-change-tracking-audit-trail-landing-page](/resources/Storage/alpha-platform/images/alpha-change-tracking-audit-trail-landing-page.png)

## Filters

Filters in an audit trail allow users to narrow down audit records based on specific criteria. It helps users efficiently locate relevant events within large volumes of audit data, without altering the underlying audit log. To apply filters in Audit Trail, follow the steps below:

1. From the Commits landing page, use the left navigation panel to access the Audit Trails page.
2. On the Audit Trails page, click the Filters button at the top of the page to access available filters and narrow down the audit records.
3. The available filters include Action Performed, User, Branch, Configuration Type (such as Task Pages, Pop-up Pages, Global Pages, various Inboxes, Environments, Task Distributor, and others), and Date Range. These filters can be used to narrow down the records displayed in the Audit Trail.
   ![alpha-change-tracking-audit-trail-filters-gif](/resources/Storage/alpha-platform/images/alpha-change-tracking-audit-trail-filters-gif.gif)
4. Once the filters are applied, the Audit Trail page displays only the records that match the selected criteria. The image below illustrates a sample filter configuration that includes actions such as Commit and Branch Create, a specific user, and two branches.
   ![alpha-change-tracking-audit-trail-filters-applied](/resources/Storage/alpha-platform/images/alpha-change-tracking-audit-trail-filters-applied.png)
