# Data-Processing-Project-with-Pandas-in-Python
This project demonstrates a basic data processing task using the Python Pandas library. The goal is to read data from CSV files, perform some data manipulation, and generate a new CSV file as output.

## Contents

1. [Introduction](#introduction)
2. [Dependencies](#dependencies)
3. [Data Loading](#data-loading)
4. [Data Processing](#data-processing)
5. [Analysis](#analysis)
6. [Results](#results)
7. [Conclusion](#conclusion)

## Introduction
The project deals with processing two CSV files - 'Nodes.csv' and 'Edges.csv'. It loads the data into Pandas DataFrames, performs a join operation, calculates the number of papers associated with each 'Cid', and finally generates a new CSV file named 'Final.csv' containing the results.

## Dependencies

- pandas
- numpy
- csv
- collections

Install the required dependencies using:
```
pip install pandas numpy
```
## Data Loading
The project utilizes Pandas to read the 'Nodes.csv' and 'Edges.csv' files into DataFrames. The data is then combined using a left join operation.

## Data Processing
The project extracts relevant columns ('id' and 'name') from both files and performs a left join based on the 'id' column.
The resulting DataFrame is used to create a dictionary where keys are 'Cid' values, and values are lists of corresponding 'id' values.
The number of papers associated with each 'Cid' is calculated.

## Analysis
The project generates a DataFrame named 'Final', containing 'Cid' and the number of papers associated with it.
The 'Final' DataFrame is sorted in descending order based on the number of papers.

## Results
The project outputs a CSV file named 'Final.csv', which contains the sorted 'Cid' values along with the corresponding number of papers.

## Conclusion
This project showcases a basic data processing pipeline using Pandas, demonstrating how to load, manipulate, and analyze data from CSV files.
