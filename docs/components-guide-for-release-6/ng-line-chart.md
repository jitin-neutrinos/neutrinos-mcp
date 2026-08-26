# Line Chart

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/ng-line-chart>

## Line Chart

### Overview

**Line Chart** used to display the data points in connected straight line segments. In the chart, the point is plotted in a way that the point has appeared.

### Usage

The **Line Chart** is popularly used to chart out trending data. For instance, in the stock market share charts. Let us consider a scenario where an Insurance Company wants to track the overall performance of the year along with insured clients and the month. The company chart needs to show the performance of the individual months with the number of clients that are insured. The company KPI (Key Performance Indicator) should be able to see the previous data as well as the current data along with the graph indicating the rise or fall of the insured client. In this case, the line chart will successfully provide all of these features. Some of the other popular use cases of line chart are:

- Banking
- Health center
- Retail
- Education
- Product Analysis in Industries
- Climate Change Statistic

### How to Use

1. Open the newly created page.

2. Drag and drop a **Line Chart **from the **Ng Charts **category.

3. Switch to the **Ts** editor of the page and then declare the variable and provide values for the following in the component class:

- A dataset array (contains y-axis values and labels of the legend). For example, Copy CodeJavaScriptpublic lineChartData:Array<any> = [
    {
    data: [
    65,
    59,
    55,
    81,
    56,
    55,
    40
    ],
    label: 'Series A'
    },
    {
    data: [
    28,
    48,
    40,
    19,
    86,
    27,
    90
    ],
    label: 'Series B'
    }
   ];

- A labels array (contains x-axis values). For example, Copy CodeJavaScriptpublic lineChartLabels:Array<any> = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July'
   ];
- Legend value (either true or false). For example, public legend=false;
- Options value. For example, Copy CodeJavaScriptpublic lineChartOptions:any = {
    responsive: true
   };

4. Now switch back to the **Html** editor of the page and provide the dataset array name in the [datasets] attribute. For example, [datasets] = lineChartData.

5. Provide the labels name in** [labels]** attribute. For example, [labels] = lineChartLabels.

6. Provide the options name in** [options] **attribute. For example, [options] = lineChartOptions.

7. Provide the legend name in** [legend] **attribute. For example, [legend] = legend.

8. Save the page and run the application.

### Associated Attributes

- **Label (String Array):** It is a specific name given to the x-axis and y-axis in the line chart. For example, Copy CodeJavaScriptChartLabels:Array<any> = [
    'January',
    ‘February’,
    'March',
    'April',
    'May',
    'June',
    'July'
   ];

- **Datasets (JSON Objects Array):** It is a collection of points which is plotted on the line chart using x-axis and y-axis. For example, Copy CodeJavaScriptlineChartData:Array<any> = [
    {
    data: [
    65,
    59,
    55,
    81,
    56,
    55,
    40
    ],
    label: 'Series A'
    },
    {
    data: [
    28,
    48,
    40,
    19,
    86,
    27,
    90
    ],
    label: 'Series B'
    },
    {
    data: [
    18,
    48,
    77,
    9,
    100,
    27,
    40
    ],
    label: 'Series C'
    }
    declaired
   ];

- **chartHover/chartClick (mouse Events): **It is an event that appears when the mouse is clicked or placed over the line chart. For example, displaying labels and point values when the mouse is clicked on the chart or mouse is moved over the chart.
- **Show Legends (Boolean): **It is a name given to the same category of data that is used in plotting the line chart. If it is true, it shows the legends otherwise it does not show.
- **[colors] (Color/color hexadecimal code):** This property provides the user the desired color to the line chart. For example, backgroundColor: ‘rgba(148,159,177,0.2)’;
- **[data]: **Specify the name of the array in which the custom data is embedded for the Line Chart. For example, [data]= lineChartData.
- **[options]: **Specify the name of an array which is defined in the TS editor from which the drop-down list of options must be displayed.
- **fxflex: **This property should be used on elements within a fxLayout container and identifies the resizing of that element within the flexbox container flow such as **flex-grow, flex basis, flex-shrink,flex-grow**.
- **fxlayout:** Specifies the flex-direction and whether the contents should be wrapped or not. eg. fxLayout=column wrap.
- **Style: **It accepts a string value and affects the different properties (height, width, color etc.) of the component based on the values provided (eg. background: orange; height:200px;).
- **Class: **Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (eg. class1 class2) which are defined in the Style tab as shown below. Copy CodeCSS.class1 {
    border-radius:10px;
    flex-basis:10%;
    height:100px;
   }
   .class2 {
    border-radius:10px;
    flex-basis:10%;
    height:100px;
   }

### Example

Let's take the example of representing the views of a series on each month of the year.

| Months | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Series A | 65 | 59 | 80 | 81 | 56 | 55 | 40 | 10 | 20 | 30 | 40 | 50 |
| Series B | 28 | 48 | 40 | 19 | 86 | 85 | 90 | 11 | 23 | 31 | 42 | 51 |
| Series C | 18 | 42 | 76 | 7 | 100 | 25 | 40 | 12 | 24 | 31 | 43 | 52 |
| Series D | 15 | 45 | 77 | 8 | 105 | 26 | 40 | 12 | 24 | 32 | 43 | 52 |
| Series E | 19 | 48 | 45 | 19 | 103 | 24 | 90 | 12 | 24 | 32 | 43 | 52 |
| Series F | 28 | 43 | 35 | 47 | 86 | 25 | 90 | 11 | 23 | 32 | 42 | 51 |
| Series G | 25 | 41 | 36 | 23 | 85 | 26 | 90 | 111 | 23 | 31 | 42 | 51 |

Perform the following steps:

1. Drag and drop a **Line Chart** to the page container.
2. In the TS editor of the page, enter the following code: Copy CodeJavaScriptlineChartData: Array<any> = [
    { data: [65, 59, 80, 81, 56, 55, 40,10,20,30,40,50], label: 'Series A' },
    { data: [28, 48, 40, 19, 86, 25, 90,11,23,31,42,51], label: 'Series B' },
    { data: [18, 45, 75, 9, 100, 26, 40,12,24,32,43,52], label: 'Series C' },
    { data: [15, 42, 76, 7, 105, 25, 40,12,24,32,43,52], label: 'Series D' },
    { data: [19, 48, 77, 5, 103, 27, 40,12,24,32,43,52], label: 'Series E' },
    { data: [28, 47, 40, 19, 86, 28, 90,11,23,31,42,51], label: 'Series F' },
    { data: [25, 46, 42, 15, 85, 27, 90,11,23,31,42,51], label: 'Series G' },
    ];
    lineChartLabels: Array<any> = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July','Aug','Sep','Oct','nov','dec',];
3. Navigate back to the **HTML** editor. Double-click the chart to open its attributes window.
4. Enter the following values: AttributeValue[labels]
   lineChartLabels [datasets]
   lineChartData [options]lineChartOptions
5. Save and run the page.
