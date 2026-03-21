<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=26&pause=1000&color=39FF14&center=true&vCenter=true&width=600&lines=%F0%9F%8F%A0+Automated+Data+Entry+Bot;%F0%9F%94%8D+Web+Scraper+%2B+Form+Automation;%E2%8C%9B+Process+Efficiency+Tool" alt="Animated Header" />
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
  <span style="color: #39FF14;">🚀 Project Overview</span><br>
  <img src="https://placehold.co/1000x2/39FF14/39FF14.png" width="100%" height="2" alt="Green Divider"/>
</h3>

A sophisticated automation script designed to streamline real estate data collection. The bot harvests property listings (prices, addresses, and URLs) from a research website and programmatically populates a Google Form, effectively transforming unstructured web data into a structured spreadsheet format.

**Technical Logic (Verified):**
* **🕷️ Data Harvesting:** Utilizes `BeautifulSoup` to parse complex HTML structures, extracting specific real estate metrics through targeted CSS selectors.
* **🧹 String Sanitization:** Implements data cleaning logic during the scraping phase to remove inconsistent formatting and currency symbols before transmission.
* **📋 Form Orchestration:** Leverages `Selenium` to automate the data entry pipeline, managing multiple input fields and form submissions in a continuous loop.
* **⚡ Workflow Integration:** Bridges two distinct web technologies to create a seamless end-to-end automation solution for repetitive research tasks.

<br>

<h3>
  <span style="color: #00E5FF;">📁 Project Structure</span><br>
  <img src="https://placehold.co/1000x2/00E5FF/00E5FF.png" width="100%" height="2" alt="Cyan Divider"/>
</h3>

```text
automated-data-entry-job/
├── main.py                     # Scraper logic and Selenium automation controller
├── requirements.txt            # Project dependencies
└── README.md                   # Documentation
```
<h3>
  <span style="color: #BC13FE;">🧠 Code Review & Complexity</span><br>
  <img src="https://placehold.co/1000x2/BC13FE/BC13FE.png" width="100%" height="2" alt="Purple Divider"/>
</h3>

<div align="center">
  <img src="https://img.shields.io/badge/OVERALL_DIFFICULTY-INTERMEDIATE-FE428E?style=for-the-badge&logoColor=white" height="35">
</div>

<br>

> <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=18&pause=1000&color=39FF14&vCenter=true&width=400&lines=>_ANALYZING_SYSTEM_COMPLEXITY..." alt="Animated Loading" />
> 
> <table>
>   <tr>
>     <td width="260"><b><span style="color: #39FF14;">HTML Parsing (BeautifulSoup)</span></b></td>
>     <td width="200"><img src="https://placehold.co/160x10/39FF14/39FF14.png"/><img src="https://placehold.co/40x10/2F2F2F/2F2F2F.png"/></td>
>     <td width="50"><b><span style="color: #39FF14;">80%</span></b></td>
>   </tr>
>   <tr>
>     <td width="260"><b><span style="color: #00E5FF;">Automation Flow (Selenium)</span></b></td>
>     <td width="200"><img src="https://placehold.co/160x10/00E5FF/00E5FF.png"/><img src="https://placehold.co/40x10/2F2F2F/2F2F2F.png"/></td>
>     <td width="50"><b><span style="color: #00E5FF;">80%</span></b></td>
>   </tr>
>   <tr>
>     <td width="260"><b><span style="color: #BC13FE;">Data Sanitization</span></b></td>
>     <td width="200"><img src="https://placehold.co/120x10/BC13FE/BC13FE.png"/><img src="https://placehold.co/80x10/2F2F2F/2F2F2F.png"/></td>
>     <td width="50"><b><span style="color: #BC13FE;">60%</span></b></td>
>   </tr>
>   <tr>
>     <td width="260"><b><span style="color: #39FF14;">Workflow Synchronization</span></b></td>
>     <td width="200"><img src="https://placehold.co/140x10/39FF14/39FF14.png"/><img src="https://placehold.co/60x10/2F2F2F/2F2F2F.png"/></td>
>     <td width="50"><b><span style="color: #39FF14;">70%</span></b></td>
>   </tr>
> </table>

<br>

**🟢 High-Impact Wins:**
* **Tool Synergy:** Demonstrates the ability to combine different libraries (BS4 for data, Selenium for action) into a single functional unit.
* **Reliable Extraction:** Clean handling of list iterations to ensure no data point is missed during the transfer process.

**🔧 Technical Debt:**
* **Explicit Waits:** Replacing static sleep times with `WebDriverWait` would make the form submission process more resilient to network lag.
* **Headless Mode:** Implementing a headless browser option would allow the bot to run as a background service without a GUI.

<br>

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=16&duration=3000&pause=1000&color=00E5FF&center=true&vCenter=true&width=500&lines=[SYSTEM_SCAN_COMPLETE]----------------------------" alt="Animated Scan Divider" />
</div>
