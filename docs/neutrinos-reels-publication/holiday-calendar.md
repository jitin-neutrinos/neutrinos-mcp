# Illustration

<https://documentation.neutrinos.com/articles/#!neutrinos-reels-publication/holiday-calendar>

The Holiday Calendar Settings page is used to define the operational working hours and time-related configurations for a process calendar. These settings influence how time-dependent activities such as SLAs, task deadlines, and escalations are calculated within the system.




 ![pulse-settings-holiday-calendar-landing-page](/resources/Storage/neutrinos-reels-publication/images/pulse-settings-holiday-calendar-landing-page.png)

- **Working Hours**: Defines the standard business hours during which the process is considered active. All time-based computations (e.g., SLA tracking) are aligned with these configured hours.
  - **Start Time**: Specifies the beginning of the working day.
    - Format: HH:MM AM/PM
    - Example: 09:00 AM
    - This value is used as the reference point for calculating active processing time.
  - **End Time**: Specifies the end of the working day.
    - Format: HH:MM AM/PM
    - Example: 06:00 PM
    - Any time outside the defined range is typically excluded from SLA and processing time calculations.
  - **Timezone**: Defines the time zone used by the calendar.
    - Example: Etc/GMT+5
    - All configured working hours, deadlines, and time-based evaluations are interpreted relative to this timezone.
    - Ensures consistency for geographically distributed users and systems.
- **Daylight Saving Time (DST)**: Determines whether daylight saving adjustments are applied to the calendar.
    **Note**: This setting applies to regions that observe daylight saving time.
  - **Toggle ON**: Automatically adjusts time calculations based on DST changes.
  - **Toggle OFF**: Ignores DST and maintains a fixed time offset throughout the year.
- After configuring all parameters, click Save at the bottom of the page to persist and apply the Holiday Calendar configuration to all the processes within the project.
    ![pulse-settings-holiday-calendar-settings-save](/resources/Storage/neutrinos-reels-publication/images/pulse-settings-holiday-calendar-settings-save.png)

## Illustration

In this scenario, an SLA trigger is configured for a process to execute after 1 minute from the start of the process. The process includes a User Task node.

A Holiday Calendar is configured with defined working hours (start time and end time). If a process is initiated outside the configured working hours, the associated user task is not activated immediately and is instead placed in a Pending state.

In this example, the process is started outside the defined working hours. As a result, the user task remains in the Pending state until the configured working hours begin. The illustration demonstrates the task in its pending state under these conditions.




 ![pulse-settings-holiday-calendar-settings](/resources/Storage/neutrinos-reels-publication/images/pulse-settings-holiday-calendar-settings.gif)

**Note**: If a process is initiated within the configured working hours (unlike the scenario shown above), the SLA is evaluated based on the process completion time. The SLA is triggered only if the process is not completed within the defined SLA duration. If the process is completed within the SLA duration, the SLA is neither triggered nor marked as expired.

## Set Holiday

Along with configuring working hours, you can also define a Holiday Calendar to represent non-working days or project time off. This helps ensure accurate SLA evaluation by preventing unintended SLA expiry or triggering during non-operational periods.

To add a holiday to the Holiday Calendar, follow steps below:

1. In the left navigation panel, navigate to Manage. Hover over Manage to display the available options, and then click Holiday Calendar from the pop-up menu.
    ![pulse-manage-navigation-panel](/resources/Storage/neutrinos-reels-publication/images/pulse-manage-navigation-panel.png)
2. The Holiday Calendar page displays the list of holidays configured for the selected project. Additionally, a separate tab is available to view the days configured as week-offs for the project.
    ![pulse-manage-page-with-holiday-defined](/resources/Storage/neutrinos-reels-publication/images/pulse-manage-page-with-holiday-defined.png)
    When no holidays are configured, the page shows an empty state with the message "Start by adding a holiday."
    ![pulse-manage-page-empty-display](/resources/Storage/neutrinos-reels-publication/images/pulse-manage-page-empty-display.png)
3. On the Holiday Calendar page, click Add at the top of the page to configure a day as a holiday for the project.
    ![pulse-manage-page-new-holiday-add-button](/resources/Storage/neutrinos-reels-publication/images/pulse-manage-page-new-holiday-add-button.png)
4. In the pop-up dialog, specify the holiday name and select the date to be designated as a holiday for the project. In this example, 1st May is configured as a holiday for a specific project.
    ![pulse-manage-page-new-holiday-add](/resources/Storage/neutrinos-reels-publication/images/pulse-manage-page-new-holiday-add.png)
5. After configuring a holiday, you can add additional days in the same manner by clicking Add More, located below the added holiday date row.
    ![pulse-manage-page-new-holiday-add-more](/resources/Storage/neutrinos-reels-publication/images/pulse-manage-page-new-holiday-add-more.png)
6. After configuring all required holidays, click Save at the bottom of the page to save and apply the configuration.
    ![pulse-manage-page-new-holiday-save-button](/resources/Storage/neutrinos-reels-publication/images/pulse-manage-page-new-holiday-save-button.png)

The Weekoffs tab displays the day(s) configured as week-offs for the selected project. By default, no days are selected as week-offs for a project.




 ![pulse-manage-page-with-weekoff-default](/resources/Storage/neutrinos-reels-publication/images/pulse-manage-page-with-weekoff-default.png)

You can select one or more days as week-offs for a specific project. These days are treated as non-working days for that project. When a day is selected as a week-off, a week-off indicator is displayed on the selected days.




 ![pulse-manage-page-with-weekoff-marked](/resources/Storage/neutrinos-reels-publication/images/pulse-manage-page-with-weekoff-marked.png)




 Click Save at the bottom of the page to save and apply the configuration.



![pulse-manage-page-with-weekoff-marked-save](/resources/Storage/neutrinos-reels-publication/images/pulse-manage-page-with-weekoff-marked-save.png)
