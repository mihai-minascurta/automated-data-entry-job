<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=26&pause=1000&color=FE428E&center=true&vCenter=true&width=600&lines=%F0%9F%8F%A0+Automated+Data+Entry+Bot;%F0%9F%94%8D+Zillow+Scraper+%2B+Google+Forms;%E2%8C%9B+Time-Saving+Automation" alt="Animated Header" />
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

A powerful data research tool that automates the tedious task of property hunting. The bot scrapes rental listings from a Zillow-like clone (or real Zillow) to extract prices, addresses, and links, and then programmatically populates a Google Form with the collected data to create an organized spreadsheet.

**Key Features:**
* **🕷️ Data Harvesting:** Uses `BeautifulSoup` to parse complex HTML and extract rental information from real estate platforms.
* **📋 Form Automation:** Employs `Selenium` to navigate Google Forms and input the scraped data into specific fields.
* **⚡ Efficiency:** Replaces hours of manual data entry with a script that completes the entire process in seconds.
* **🧹 Data Cleaning:** Cleans and formats scraped strings (like stripping extra symbols from price tags) before submission.

<br>

<h3>
  📁 Project Structure<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

```text
automated-data-entry-job/
├── main.py                     # Scraper logic and Selenium automation
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
> 🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛ **80%** | **Dynamic Form Interaction**<br>
> 🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛ **60%** | **Data Cleaning & Formatting**<br>
> 🟪🟪🟪🟪🟪🟪🟪⬛⬛⬛ **70%** | **Workflow Synchronization**

<br>

**🟢 High-Impact Wins:**
* **Workflow Bridging:** Effectively connecting two different technologies (Scraping + Automation) to solve a real-world problem.
* **Selector Precision:** Using robust CSS selectors/XPaths to handle deeply nested HTML structures.

**🔧 Key Recommendations:**
* **Headless Execution:** Run Selenium in headless mode for a smoother experience if no visual confirmation is needed.
* **JSON Backup:** Save the scraped data into a `data.json` file before submitting it to the form to prevent data loss in case of a crash.

<br>

<div align="center">
  <img src="https://placehold.co/1000x3/FE428E/FE428E.png" width="100%" height="3" alt="Pink Divider"/>
</div>
