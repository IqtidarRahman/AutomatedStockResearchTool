# AutomatedStockResearchTool
Automated Stock Research Tool
This tool aims to automate the process of collating news and financial information related to a particular company/stock. Given a company name and market this application will analyse articles, derive a collection of top topics, descriptive bullet points relating to news and info related to the topic, and will export this data to a table.


This application has X parts.

a)
The first part takes an input which is a list of strings related to the company's name and market it operates in (e.g. ASX or US) then scrapes websites for news/financial data relating to the company.

b) Google Gemini API
To use this get an [API key](https://aistudio.google.com/u/1/apikey). Once created input this into sentiment.py where marked #YOUR_API_KEY