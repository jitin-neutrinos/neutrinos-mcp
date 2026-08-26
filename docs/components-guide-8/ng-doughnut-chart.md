# Doughnut Chart

<https://documentation.neutrinos.com/articles/#!components-guide-8/ng-doughnut-chart>

## Doughnut Chart

### Overview

The doughnut chart is similar to the pie chart but the difference is that the doughnut chart has a circular hollow gap in the middle of the chart.

### Usage

A Doughnut chart is widely used in the business world, mass media, and institutions. Let us consider a health center scenario where a particular hospital wants to plot a chart to record the number of patients admitted to different wards. The chart should represent the overall hospital and be divided into different sections which represent the wards of the hospital. This can be achieved by using the Doughnut chart where a complete chart represents the hospital and the slices represent the wards of the hospital. There are some other popular use cases as well. Some of them are:

- Pharmaceutical Industries (indicating the different types of drugs)
- Industries (for providing information on different products and services )
- Government offices (like revenue department)
- Retails (for different types of products they provide)

### How to Use

- Drag and drop the **Doughnut Chart** from the Ng Charts category.
- Double click the component to display the list of attributes that can be used with it.
- Fill in the attributes which are needed and save the page.

### Associated Attributes

- **[labels] (String Array): **Labels are the identity of the data series in a doughnut chart. It appears in the legend and tooltips. It gives a specific name to each slice in the doughnut chart. For example, Copy CodeJavaScriptpageXOffset.doughnutChartLabels= [
    'Emergency & Casualty',
    'Labor Ward',
    'Endoscopy Ward',
    'Coronary Ward',
    'Surgical Ward',
    'General Ward'
   ]
   ;

- ** [datasets] (JSON Objects Array):** It is the data of the chart which is framed in a circular slice depending upon the dataset values. For example: Copy CodeJavaScriptpage.doughnutChartData = [
    { data: [65, 59, 80, 81, 56, 55, 40], label: 'Series A' },
    { data: [28, 48, 40, 19, 86, 27, 90], label: 'Series B' }
    ];

- **chartHover** and** chartClick** (mouse Events): It is an event that appears when the mouse is clicked or placed over the slice of the doughnut chart. For example, displaying labels and point values when the mouse is clicked on the slice of the chart or the mouse is moved over it.
- **Show Legends (Boolean):** It is a name given to the same category of data that is used in plotting the doughnut chart. If it is true, it shows the legends otherwise it does not show.
- **[colors] (Color/color hexadecimal code):** This property provides the user's desired color to the doughnut chart. For example: Copy CodeJavaScriptpage.doughnutChartColor = [
    {
    backgroundColor: 'rgba(256, 0, 0, 0.1)',
    borderColor: 'rgba(0, 0, 0, 0.1)',
    color: '#000',
    }
    ]
- **[data]: **Specify the name of the array defined in which the data for the Doughnut Chart is embedded.
- **fxflex: **This property should be used on elements within a fxLayout container and identifies the resizing of that element within the flexbox container flow such as flex-grow, flex-basis, flex-shrink,flex-grow.
- **fxlayout:** Specifies the flex-direction and whether the contents should be wrapped or not. Example, fxLayout=column wrap.
- **[options]: **Specify the name of an array that is defined in the Script node of the page flow from which the drop-down list of options must be displayed. For example, [option]=doughtnutchartOptions.
- **Style:** It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (eg. background:orange;height:200px;).
- **Class:** The Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (eg. class1 class2) which are defined in the Style tab as shown below. Copy CodeCSS.class1 {
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

Consider an example of a hospital that wants to record the percentage of patients admitted to different wards such as emergency & casualty, labor ward, Endoscopy Ward, Coronary Care ward, and Surgical Ward using a Doughnut chart.

| Hospital Wards | Emergency & Casualty | Labor Ward | Endoscopy Ward | Coronary Ward | Surgical Ward | General Ward |
| --- | --- | --- | --- | --- | --- | --- |
| Patients(%) | 25 | 11 | 8 | 9 | 18 | 29 |

To do that, perform the following steps:In the **Page Flow Designer **of the page, add a **Script **node to the** On init **flow and enter the following code:Copy CodeJavaScriptpage.doughnutChartData = [
 { data: [65, 59, 80, 81, 56, 55, 40], label: 'Series A' },
 { data: [28, 48, 40, 19, 86, 27, 90], label: 'Series B' }
 ];

page.doughnutChartLabels = ['2006', '2007', '2008', '2009', '2010', '2011', '2012'];
In the page designer, create a **mycharclick** flow to display an alert pop-up on click of the chart. Drag and drop a **Start **node and name it **mycharclick**.Drag and drop a **Script node and add **alert("chart clicked"); Connect the nodes.Navigate to the UI designer of the page. Drag and drop an **Ng Doughnut Chart** component and set the following properties:[datasets]: page.doughnutChartData [labels]: page.doughnutChartLabels (chartClick): Click the **Pick a Flow** mat chip. Open the **Flow Picker **editor, and select the **mychartclick **flow.fxFlex: 50Save and run the page.
