# Pie Chart

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/ng-pie-chart>

## Pie Chart

### Overview

A** Pie Chart** is an excellent chart type for representing the relational proportions between data. It is widely used in the business world as well as in mass media. It represents the data in a pie that is sliced according to the data values.

### Usage

A **Pie Chart **is widely used in the business world and mass media. Consider a health center scenario where a particular hospital wants to plot a chart for the record of its patient admitted to different wards. The chart should indicate the overall hospital and should be divided into different sections which represent the wards of the hospital. This can be achieved using a pie chart where a complete pie represents the hospital and slices of the pie chart represent the wards of the hospital. Some of the other popular use cases of a pie chart are:

- Pharmaceutical Industries (indicating the different types of drugs)
- Industries (for providing information on different products and services)
- Government offices (like revenue department)
- Retail (for different types of products they provide)

### How to Use

1. Open the newly created page.

2. Drag and drop a **Pie Chart** from the **Ng Charts** category.

3. Switch to the **Ts** file of the page and then declare the variable and provide values for the following in the component class:

- A dataset array (contains y-axis values and labels of the legend). For example, Copy CodeJavaScriptpublic pieChartData: Array<any> = [
    {
    data: [
    25,
    11,
    8,
    9,
    18,
    29
    ]
    }
   ];

- A labels array (contains x-axis values). For example, Copy CodeJavaScriptpublic pieChartLabels:string [
   ] = [
    'Emergency & Casualty',
    'Labor Ward',
    'Endoscopy Ward',
    'Coronary Ward',
    'Surgical Ward',
    'General Ward'
   ];

- **Legend value:** Either true or false. For example, public legend=false;.
- Options value. For example, Copy CodeJavaScriptpublic pieChartOptions:any = {
    responsive: true
   };

4. Now switch back to the **Htm**l file of the page and provide the dataset array name in the [datasets] attribute. For example, [datasets] = pieChartData.

5. Provide the labels name in the** [labels] **attribute. For example, [labels] = pieChartLabels.

6. Provide the options name in the** [options] **attribute. For example, [options] = pieChartOptions.

7. Provide the legend name in the **[legend] **attribute. For example, [legend] = legend.

8. Save the page and run the application.

### Associated Attributes

- **[labels] (String Array): **Labels are the identity of the data series in a chart. It appears in the legend and tooltips. It gives a specific name to each slice in the **Pie Chart**. For example, Copy CodeJavaScriptChartLabels:Array<any> = [
    'January',
    ‘February’,
    'March',
    'April',
    'May',
    'June',
    'July'
   ];

- **[datasets] (JSON Objects Array): **It is a data of the chart which is framed in a circular slice whose length depends on the dataset values. For example, Copy CodeJavaScriptpieChartData: Array<any> = [
    {data: [
    69,
    72,
    82,
    79,
    92
    ],
    label: 'Net Profit Margin (%)'
    }
   ];

- **chartHover **and** chartClick** (mouse Events): It is an event that appears when the mouse is clicked or placed over the pie chart. For example, displaying labels and point values when the mouse is clicked on the chart or mouse is moved over the chart.
- **Show Legends (Boolean):** It is a name given to the same category of data that is used in plotting the pie chart. If it is true, it shows the legends otherwise it does not show.
- **[colors] (Color/color hexadecimal code): **This property provides the user with the desired color to the pie chart. For example, background-color: #92a8d1;
- **Value: **It is a value of the key that the user-provided manually.
- **[data]: **Specify the name of the array that is defined in the TS editor which embeds the data for the Pie chart.
- **fxflex:** This property should be used on elements within a fxLayout container and identifies the resizing of that element within the flexbox container flow such as **flex-grow, flex-basis, flex-shrink,flex-grow**.
- **fxlayout: **Specifies the flex-direction and whether the contents should be wrapped or not. eg. fxLayout=column wrap.
- **[options]: **Specify the name of an array which is defined in the TS editor from which the drop-down list of options must be displayed. For example, [options]= piechartOptions.
- **Style: **It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (eg. background: orange; height:200px;).
- **Class:** Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (eg. class1 class2) which are defined in the **Style** tab as shown below. Copy CodeCSS.class1 {
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

Consider an example of a company that wants to plot a chart to record the sales

| Sales | Download Sales | In-Store sales | Mail Sales |
| --- | --- | --- | --- |
| Percentage | 300 | 500 | 100 |

Perform the following steps:

1. Drag and drop a **Pie Chart** to the page container.
2. In the TS editor of the page, enter the following code: Copy CodeJavaScriptpieChartData = [{
    data:[300, 500, 100]}
    ];
   pieChartLabels: string[] = ['Download Sales', 'In-Store Sales', 'Mail Sales'];
   pieChartOptions: any = {
    responsive: true
   }
    mycharclick(){
    alert("chart clicked");
    }
   ]
3. Navigate back to the **HTML** editor. Double-click the chart to open its attributes window.
4. Enter the following values: AttributeValue[labels]
   pieChartLabels [datasets]
   pieChartData [options]pieChartOptions
   (chartClick)mychartclick()
5. Save and run the page.
