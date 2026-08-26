# Illustration

<https://documentation.neutrinos.com/articles/#!neutrinos-reels-publication/error-queue>

An Error Queue is a mechanism for capturing and isolating transactions that fail to process successfully. It serves as a dedicated list for messages or process instances that encounter errors during execution, such as validation failures, external dependency issues, or unexpected exceptions. Rather than discarding failed items, the system redirects them to the Error Queue, enabling traceability, supporting reprocessing, and enhancing overall system resilience.




 ![pulse-settings-error-queue-landing](/resources/Storage/neutrinos-reels-publication/images/pulse-settings-error-queue-landing.png)

The Error Queue configuration is determined by the defined retry attempts and retry intervals. To configure these settings, follow the steps below:

- Select the gear icon located at the top of the page to access the Settings page. By default, the Error Queue configuration page is displayed upon navigation.
    ![pulse-settings-error-queue](/resources/Storage/neutrinos-reels-publication/images/pulse-settings-error-queue.png)
- **Retry Attempts**: This parameter determines the number of retry attempts performed before a message is moved to the Error Queue.
- **Retry Interval**: This parameter defines the interval between retry attempts before a message is moved to the Error Queue. The interval is measured in seconds.
- The dropdown next to the interval defines how the retry interval grows between attempts.
    ![pulse-settings-error-queue-interval-behavior](/resources/Storage/neutrinos-reels-publication/images/pulse-settings-error-queue-interval-behavior.png)
  - Linear Retry: The delay between each retry remains constant.
  - Exponential Retry: The delay increases exponentially after each failure.
- After configuring all parameters, click Save at the bottom of the page to persist and apply the Error Queue configuration to all the processes within the project.
    ![pulse-settings-error-queue-configuration-save](/resources/Storage/neutrinos-reels-publication/images/pulse-settings-error-queue-configuration-save.png)

## Illustration

When a process encounters an error during execution, the associated error logs are recorded under the respective process in the Error Queue. You can access these logs by navigating to Manage > Error Queue.




 ![pulse-settings-error-queue-listing-navigate](/resources/Storage/neutrinos-reels-publication/images/pulse-settings-error-queue-listing-navigate.png)

In this example, a Formula Rule is configured to calculate a person’s age, with the input date expected in DD/MM/YYYY format. When this rule is applied to a Business Node within a process, any invalid input (for example, an incorrectly formatted date) triggers a process error. The resulting error is captured and recorded in the Error Queue, as illustrated in the GIF below.




 ![pulse-settings-error-queue-demo](/resources/Storage/neutrinos-reels-publication/images/pulse-settings-error-queue-demo.gif)
