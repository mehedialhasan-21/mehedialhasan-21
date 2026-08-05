
<div align="center">
  <img src="assets/banner.svg" alt="Profile Banner" width="100%" />
</div>

<br />

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=38BDF8&center=true&vcenter=true&width=600&lines=Senior+Python+%26+DevOps+Engineer;Automating+Cloud+Native+Infrastructure;Building+Scalable+Open+Source+Tools" alt="Typing SVG" />
</div>

<div align="center">

  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)]({{ config.socials.linkedin }})
  [![Twitter](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)]({{ config.socials.twitter }})
  [![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)]({{ config.socials.email }})
  [![Profile Views](https://komarev.com/ghpvc/?username={{ config.username }}&color=38bdf8&style=for-the-badge&label=PROFILE+VIEWS)](https://github.com/{{ config.username }})

</div>

---

### 👨‍💻 About Me

- 🔭 I’m currently working on **Cloud Infrastructure Automation & CI/CD Pipelines**
- 🌍 Located in **{{ config.location }}**
- 🎯 **Today's Goal:** {{ config.goals.today }}
- 🚀 **Weekly Goal:** {{ config.goals.weekly }}
- 💬 Ask me about **Python, Docker, Kubernetes, Terraform, and GitHub Actions**

---

### 🛠 Tech Stack

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" alt="Kubernetes" />
  <img src="https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white" alt="Terraform" />
  <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux" />
</p>

---

### 📊 GitHub Analytics

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username={{ config.username }}&show_icons=true&theme=tokyonight&count_private=true&hide_border=true" alt="GitHub Stats" height="175"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={{ config.username }}&layout=compact&theme=tokyonight&hide_border=true" alt="Top Languages" height="175"/>
</div>

<div align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user={{ config.username }}&theme=tokyonight&hide_border=true" alt="GitHub Streak" height="175"/>
</div>

<div align="center">
  <img src="https://github-profile-trophy.vercel.app/?username={{ config.username }}&theme=tokyonight&column=6&margin-w=15" alt="Trophies" />
</div>

---

### 📈 Live GitHub Metrics

| Metric | Count | Metric | Count |
| :--- | :--- | :--- | :--- |
| 👥 **Followers** | `{{ stats.followers }}` | 👤 **Following** | `{{ stats.following }}` |
| 📦 **Public Repositories** | `{{ stats.public_repos }}` | ⭐ **Total Stars Earned** | `{{ stats.total_stars }}` |
| 🔀 **Total Forks** | `{{ stats.total_forks }}` | 💻 **Total Commits (Est.)** | `{{ stats.total_commits }}` |

---

### 🚀 Pinned & Featured Repositories

| Repository | Description | Primary Language | Stars |
| :--- | :--- | :--- | :--- |
{% for repo in pinned_repos -%}
| [**{{ repo.name }}**]({{ repo.html_url }}) | {{ repo.description or "No description provided." }} | `{{ repo.language or "N/A" }}` | ⭐ {{ repo.stargazers_count }} |
{% endfor %}

---

### ⚡ Recent Public Repositories

{% for repo in latest_repos -%}
- 📌 [**{{ repo.name }}**]({{ repo.html_url }}) - {{ repo.description or "No description." }} (`{{ repo.language or "N/A" }}`)
{% endfor %}

---

### 📜 Recent GitHub Activity

{% if recent_activities -%}
{% for activity in recent_activities -%}
- {{ activity.type }} on [**{{ activity.repo_name }}**](https://github.com/{{ activity.repo_name }}) at `{{ activity.created_at }}`
{% endfor -%}
{% else -%}
- *No recent public activity recorded.*
{% endif %}

{% if external.codeforces.rating -%}
---

### 🏆 Competitive Programming & Integrations

- **Codeforces Rating:** `{{ external.codeforces.rating }}` (Rank: `{{ external.codeforces.rank }}`)
{% endif %}

---

### 💬 Random Developer Quote

> *"{{ quote.quote }}"*
> 
> — **{{ quote.author }}**

---

<div align="center">

  **Last Updated:** `{{ timestamps.utc_time }}` | **Current Date:** `{{ timestamps.current_date }}`

  *Automated with Python 3.12 & GitHub Actions* 🤖

</div>
