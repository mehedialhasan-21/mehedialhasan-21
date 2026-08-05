<div align="center">
  <img src="assets/banner.svg" alt="Profile Banner" width="100%" />
</div>

<br />

<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=24&pause=1000&color=38BDF8&center=true&vcenter=true&width=650&lines=Senior+Cloud+Native+%26+DevOps+Engineer;Kubernetes+%26+GitOps+Architect;Building+Scalable+Cloud+Infrastructure" alt="Typing SVG" />
</div>

<div align="center">

  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)]({{ config.socials.linkedin }})
  [![Twitter](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)]({{ config.socials.twitter }})
  [![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)]({{ config.socials.email }})
  [![Profile Views](https://komarev.com/ghpvc/?username={{ config.username }}&color=38bdf8&style=for-the-badge&label=PROFILE+VIEWS)](https://github.com/{{ config.username }})

</div>

---

### ⚡ Technical Arsenal & Cloud Stack

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" />
  <img src="https://img.shields.io/badge/ArgoCD-EF7B4D?style=for-the-badge&logo=argo&logoColor=white" />
  <img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" />
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" />
</p>

---

### 📊 System Metrics & GitHub Analytics

<div align="center">
  <img src="assets/stats.svg" alt="Native Stats SVG" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={{ config.username }}&layout=compact&theme=tokyonight&hide_border=true" alt="Top Languages" />
</div>

<br/>

<div align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user={{ config.username }}&theme=tokyonight&hide_border=true" alt="GitHub Streak" />
</div>

---

### 📌 Featured Repositories

| Repository | Primary Language | Stars | Link |
| :--- | :--- | :--- | :--- |
{% for repo in pinned_repos -%}
| **{{ repo.name }}** | `{{ repo.primaryLanguage.name if repo.primaryLanguage else "N/A" }}` | ⭐ {{ repo.stargazerCount }} | [Explore Project]({{ repo.url }}) |
{% endfor %}

---

### 🎯 Current Focus & Objectives

- 🔭 **Current Focus:** {{ config.goals.today }}
- 🚀 **Weekly Goal:** {{ config.goals.weekly }}
- 📍 **Location:** {{ config.location }} (`{{ config.timezone }}`)

---

### 💬 Daily Engineering Philosophy

> *"{{ quote.quote }}"*  
> — **{{ quote.author }}**

---

<div align="center">

  **Last Engine Run:** `{{ timestamps.utc_time }}` | **Date:** `{{ timestamps.current_date }}`  
  *Driven by Python 3.12, GraphQL v4, & GitHub Actions Automation* ⚡

</div>
