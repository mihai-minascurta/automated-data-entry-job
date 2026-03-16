<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=26&pause=1000&color=FE428E&center=true&vCenter=true&width=600&lines=%F0%9F%8F%A0+Automated+Data+Entry+Bot;%F0%9F%94%8D+Web+Scraper+%2B+Form+Automation;%E2%8C%9B+Process+Efficiency+Tool" alt="Animated Header" />
</div>

<br>

<div align="center">
  <img src="https://img.shields.io/badge/Python-A9FEF7?style=for-the-badge&logo=python&logoColor=black" height="35">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/BeautifulSoup-FE428E?style=for-the-badge&logo=python&logoColor=white" height="35">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white" height="35">
</div>

<br>

<h3>
  🚀 Project Overview<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

A sophisticated automation script designed to streamline real estate data collection. The bot harvests property listings (prices, addresses, and URLs) from a research website and programmatically populates a Google Form, effectively transforming unstructured web data into a structured spreadsheet format.

**Technical Logic (Verified):**
* **🕷️ Data Harvesting:** Utilizes `BeautifulSoup` to parse complex HTML structures, extracting specific real estate metrics through targeted CSS selectors.
* **🧹 String Sanitization:** Implements data cleaning logic during the scraping phase to remove inconsistent formatting and currency symbols before transmission.
* **📋 Form Orchestration:** Leverages `Selenium` to automate the data entry pipeline, managing multiple input fields and form submissions in a continuous loop.
* **⚡ Workflow Integration:** Bridges two distinct web technologies to create a seamless end-to-end automation solution for repetitive research tasks.

<br>

<h3>
  📁 Project Structure<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

```text
automated-data-entry-job/
├── main.py                     # Scraper logic and Selenium automation controller
├── requirements.txt            # Project dependencies
└── README.md                   # Documentation
```
<h3>
  🧠 Code Review & Complexity<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

<div align="center">
  <img src="https://img.shields.io/badge/OVERALL_DIFFICULTY-INTERMEDIATE-FE428E?style=for-the-badge&logoColor=white" height="35">
</div>

<br>

> **📊 SYSTEM COMPLEXITY RADAR**
>
> 🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛ **80%** | **HTML Parsing (BeautifulSoup)**<br>
> 🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛ **80%** | **Automation Flow (Selenium)**<br>
> 🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛ **60%** | **Data Sanitization**<br>
> 🟪🟪🟪🟪🟪🟪🟪⬛⬛⬛ **70%** | **Workflow Synchronization**

<br>

**🟢 High-Impact Wins:**
* **Tool Synergy:** Demonstrates the ability to combine different libraries (BS4 for data, Selenium for action) into a single functional unit.
* **Reliable Extraction:** Clean handling of list iterations to ensure no data point is missed during the transfer process.

**🔧 Technical Debt:**
* **Explicit Waits:** Replacing static sleep times with `WebDriverWait` would make the form submission process more resilient to network lag.
* **Headless Mode:** Implementing a headless browser option would allow the bot to run as a background service without a GUI.

<br>

<div align="center">
  <img src="https://placehold.co/1000x3/FE428E/FE428E.png" width="100%" height="3" alt="Pink Divider"/>
</div>
