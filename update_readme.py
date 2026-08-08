import re

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Free Tier Limit in SaaS table
saas_table = """| Product | Description | Size (Valuation/Revenue) | Pricing | Free Tier Limit |
|---------|-------------|--------------------------|---------|-----------------|
| **[Deputy](https://www.deputy.com/)** | Flexible workforce management platform offering automated scheduling, time tracking, and multi-location support. | $1.1B Valuation | Starts at $5.00/user/mo | 14-day free trial |
| **[HotSchedules (Fourth)](https://www.fourth.com/)** | Widely adopted hospitality workforce management suite covering scheduling, time & attendance, labor forecasting. | $1.0B Valuation | Custom enterprise pricing | 14-day free trial |
| **[Connecteam](https://connecteam.com/)** | All-in-one employee app with scheduling, time tracking, task management, and communication features. | $800M Valuation | Starts at $29/mo (30 users) | Up to 10 users |
| **[7shifts](https://www.7shifts.com/)** | Restaurant-focused scheduling platform with labor forecasting, POS integrations, tip management. | $500M Valuation | Starts at $29.99/location/mo | 1 location, 30 users |
| **[Homebase](https://www.joinhomebase.com/)** | Simple and affordable scheduling, time clock, and team communication platform. | $300M Valuation | Starts at $24.95/location/mo | 1 location, 20 users |
| **[Planday](https://www.planday.com/)** | Workforce management solution focused on hospitality scheduling. | $185M Valuation (Xero) | Starts at €2.99/user/mo | 30-day free trial |
| **[When I Work](https://wheniwork.com/)** | Popular employee scheduling and time-tracking tool with open shifts, availability management. | $100M Revenue | Starts at $2.50/user/mo | 14-day free trial |
| **[Humanity](https://www.humanity.com/)** | Workforce management platform offering scheduling, time clocks, and attendance features. | $50M Revenue (TCP) | Starts at $3.00/user/mo | 30-day free trial |
| **[Sling](https://getsling.com/)** | Free and paid employee scheduling app with messaging, time tracking, and shift management. | $20M Revenue (Toast) | Starts at $1.70/user/mo | Up to 30 users |
| **[Schedulefly](https://www.schedulefly.com/)** | Restaurant-oriented scheduling tool emphasizing simplicity, employee messaging, and basic shift management. | $2M Revenue | Starts at $30/mo (19 staff) | 30-day free trial |
| **[ZoomShift](https://www.zoomshift.com/)** | Straightforward employee scheduling software with drag-and-drop tools, availability tracking. | $1M Revenue | Starts at $2.00/user/mo | 14-day free trial |"""

content = re.sub(r'\| Product \| Description.*?\| ZoomShift.*?\n', saas_table + '\n', content, flags=re.DOTALL)

# 2. Update Open Source List
os_list = """- **[AutoShiftPlanner](https://github.com/betaiotazeta/AutoShiftPlanner)**  
  Free open-source application for generating detailed employee shift schedules based on rules, preferences, and heuristic algorithms.

- **[DutyDock](https://github.com/dutydock/dutydock)**  
  Open-source shift planning and rostering software designed for teams with complex scheduling constraints.

- **[ERPNext HR / Shift Management](https://github.com/frappe/erpnext)**  
  Open-source ERP suite with human resources and shift scheduling modules that can be adapted for restaurant workforce management.

- **[Harmobot](https://github.com/m-walas/Harmobot)**  
  Intelligent open-source automatic schedule generator using Google OR-Tools for creating optimal work schedules from availability and constraints.

- **[Odoo HR](https://github.com/odoo/odoo)**  
  Comprehensive open-source ERP with integrated HR, time tracking, and shift scheduling functionalities suitable for hospitality.

- **[OptaPlanner](https://github.com/kiegroup/optaplanner)**  
  Powerful open-source constraint satisfaction solver often used as the engine behind complex restaurant staff scheduling and rostering systems.

- **[OR-Tools Nurse/Employee Scheduling Examples](https://github.com/google/or-tools)**  
  Official Google OR-Tools examples and constraint programming models widely adapted for restaurant and shift scheduling problems.

- **[pyworkforce](https://github.com/rodrigo-arenas/pyworkforce)**  
  Practical Python library for workforce management covering shift scheduling, rostering, break placement, and queuing models powered by OR-Tools.

- **[Restaurant / Employee Scheduler Projects](https://github.com/marcpage/scheduling)**  
  Community open-source restaurant staff scheduling prototypes and websites focused on availability and basic roster communication.

- **[Roster Wizard](https://github.com/galojix/roster-wizard)**  
  Automatic rostering system built with Google OR-Tools that handles skill mix requirements, staff requests, shift sequence rules, and leave management.

- **[Schichtplaner](https://github.com/lennystepn-hue/schichtplaner)**  
  Self-hosted open-source shift planning software with real-time collaboration, employee preferences, and AI-assisted optimization.

- **[Shift-Scheduler & Related Scripts](https://github.com/codejudas/Shift-Scheduler)**  
  Open-source Python tools originally designed for scheduling restaurant waiters and similar shift-based roles.

- **[Team Schedule](https://github.com/aleksandrrudenko/team-schedule)**  
  Open-source scheduling system for distributed teams with follow-the-sun coverage, overtime prevention, and on-call rotation support.

- **[TimeTables](https://github.com/dlsnyder8/TimeTables)**  
  Open-source employee shift scheduling and management application with automatic schedule generation using constraint algorithms, availability input, and multi-group support."""

content = re.sub(r'- \*\*\[TimeTables\].*?shift-based roles\.\n', os_list + '\n', content, flags=re.DOTALL)

# SEO text
seo_text = '''
> **SEO Description**: A comprehensive, awesome list of the best restaurant scheduling software, SaaS platforms, and open-source GitHub projects for shift management, time tracking, and labor forecasting. Enhance your workforce operations with these tools.
'''

# 3, 4, 5, 6, 7. Banner, Badges, Emojis, SEO
banner_html = f'''<p align="center">
  <img src="assets/banner.svg" alt="Awesome Restaurant Scheduling Banner" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a>
  <a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>
  <a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>
</p>

{seo_text}

'''

content = content.replace('# Awesome-Restaurant-Scheduling', banner_html + '# 🌟 Awesome-Restaurant-Scheduling')

# Emojis for headings
content = content.replace('## Top Restaurant Scheduling Platforms Ecosystem', '## 🚀 Top Restaurant Scheduling Platforms Ecosystem')
content = content.replace('## Table of Contents', '## 📋 Table of Contents')
content = content.replace('## SaaS/Hosted Platforms', '## 💼 SaaS/Hosted Platforms')
content = content.replace('## Open-Source GitHub Projects', '## 💻 Open-Source GitHub Projects')
content = content.replace('### Additional Strong Open-Source Options', '### 🔧 Additional Strong Open-Source Options')
content = content.replace('## How to Contribute', '## 🤝 How to Contribute')
content = content.replace('## Disclaimer', '## ⚠️ Disclaimer')

# 8. Star History
star_history = """
## 🌟 Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Restaurant-Scheduling&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Restaurant-Scheduling&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Restaurant-Scheduling&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Restaurant-Scheduling&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
content += star_history

# 9. Replace chartrepos with chart?repos
content = content.replace('chartrepos', 'chart?repos')

# 10. Replace https://github.com/sindresorhus/awesome with https://github.com/ishandutta2007/Awesome-Awesome-Awesome
content = content.replace('https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome')

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)
