# Interface

<https://documentation.neutrinos.com/articles/#!pulse-publication/rules>

Rules are the fundamental unit of Reels, representing a single business entity that determines the outcome of a business event based on incoming data. Rules encapsulate specific logic, driving decisions across various business scenarios.

## Interface

![up-reels-landing-rules-page2](/resources/Storage/pulse-publication/images/up-reels-landing-rules-page2.png)

1. The leftmost navigation pane displays all the modules available for the selected project. Use this pane to navigate between modules such as Case Manager, Rules Engine, Process, Tokens, and others.
2. The inner left navigation pane lists all the submodules available within the selected module. The currently selected submodule is highlighted to indicate your current location within the module.
3. This option toggles the visibility of the left navigation pane, allowing you to increase the available workspace. Hiding the navigation pane provides more space to work on the canvas or view tables in full width.
4. This bar displays all the tabs that are currently open on the platform. Each tab represents an open module or submodule, allowing you to switch between different pages without losing your current context.
5. The search bar lets you find items within the currently selected module. The search is limited to the active tab.
6. This option allows you to switch between the Rules and Rule Groups tabs. The selected tab displays the corresponding list of rules or rule groups available on the platform.
7. The Add button allows you to create a new rule or rule group.
8. The Show by and pagination controls allow you to navigate through multiple pages of the rules table when the table contains more records than can be displayed on a single page. Use the Show by option to specify the number of records displayed per page.
9. The table displays the list of rules or rule groups, depending on the selected tab. When the Rules tab is selected, the table lists all the available rules. When the Rule Groups tab is selected, it lists all the available rule groups. The table includes the following information for each rule or rule group:
  - **Name**: Displays the name of the rule or rule group.
  - **ID**: Displays the unique identifier assigned to the rule or rule group.
  - **Version**: Displays the current version of the rule or rule group.
  - **Rule Type**: Displays the type of the rule.
  - **Author**: Displays the name of the user who created the rule or rule group.
  - **Available From**: Displays the date and time from which the rule or rule group is available.
  - **Last Updated**: Displays the date and time when the rule or rule group was last modified.

## Types of Rules

In the Reels platform, rules are classified into two types: Basic and NLP-based.

### Basic Rule Type

The Basic rule type includes decision tables, formulas, Excel rules, decision trees, APIs, and script rules.

| **Rule Type  ** | **  Description  ** |
| --- | --- |
| Decision Table | Decision tables provide a structured way to represent decision-making logic in a tabular format. They help manage complex rules by specifying various conditions and their corresponding actions. Decision tables are ideal for scenarios where decisions depend on multiple input combinations. For more information, see [Decision Table](/articles/pulse-publication/decision-table) topic. |
| Excel Rule | Excel rules enable seamless data and rule management using the familiar spreadsheet interface. They provide data manipulation and rule execution capabilities within a well-known environment. Excel rules are ideal for handling large data volumes, performing calculations, and applying rule logic directly in a spreadsheet format, making them especially useful for spreadsheet users. For more information, see [Excel Rule](/articles/pulse-publication/excel-rule) topic. |
| Formula Rule | The Formula rule enables calculations using mathematical or logical expressions. It is designed to compute values based on given inputs, automating tasks such as totals, averages, date differences, and date-based calculations. Formula rules are particularly useful in scenarios requiring dynamic numerical processing. For more information, see [Formula Rule](/articles/pulse-publication/formula-rule) topic |
| API Rule | The API rule facilitates integration with external services and systems through an Application Programming Interface (API). It enables seamless interaction with other software, allowing data retrieval and transmission. API rules can connect to third-party services, access external data sources, and integrate with other applications. For more information, see [API Rule](/articles/pulse-publication/api-rule) topic. |
| Script Rule | The Script rule allows you to create and execute custom code, enabling complex logic beyond standard rule capabilities. It is used to develop custom functions, automate processes, and perform advanced operations. Script rules are ideal for users with coding experience. For more information, see [Script Rule](/articles/pulse-publication/script-rule) topic. |
| Decision Tree | A Decision Tree graphically represents decisions and their possible outcomes in a tree-like structure. It helps visualize decision-making processes by outlining various decision paths and their corresponding results. Decision trees are useful when decisions involve multiple branching conditions. For more information, see [Decision Tree](/articles/pulse-publication/decision-tree) topic. |

### NLP Rule Types

Natural Language Processing (NLP) Rule Types process and interpret user inputs in conversational AI applications. These include the Levenshtein Distance Rule, Phonetics Rule, and Sentiment Analysis Rule.

| **  Rule Type  ** | **  Description** |
| --- | --- |
| Levenstein Distance Rule | The Levenshtein Distance Rule calculates the minimum number of edits—insertions, deletions, or substitutions—needed to transform one string into another. It is commonly used in:      Spell checkers.      Autocorrect systems.      Fuzzy matching processes to find words that have similar spellings.     For more information, see [Levenshtein Distance Rule](/articles/pulse-publication/levenshtein-distance-rule) topic. |
| Phonetics Rule | Phonetic algorithms like Soundex and Metaphone convert words into codes based on sound rather than spelling. These rules are useful for:      Matching similar-sounding words.      Aid in tasks like search optimization.      Aid in tasks like data deduplication.     For more information, see [Phonetics Rule](/articles/pulse-publication/phonetics-rule) topic. |
| Sentiment Analysis Rule | This rule determines the emotional tone (positive, negative, neutral) of the user's text. It is commonly used in:      Analyzing customer feedback.      Social media posts.      Reviews to gauge public opinion and sentiment.     For more information, see [Sentiment Analysis Rule](/articles/pulse-publication/sentiment-analysis-rule) topic. |

[Next Topic](/articles/pulse-publication/decision-table)

[Previous Topic](/articles/pulse-publication/basic-concepts-reels)
