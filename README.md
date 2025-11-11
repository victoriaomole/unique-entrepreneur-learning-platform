# Unique Entrepreneur Learning Platform

**Organisation:** Unique Entrepreneur Solutions Limited  
**Prepared by:** Omole Victoria Oluwatosin  
**Roles:** Business Analyst · Data Analyst · Data Management Professional · Frontend & Backend Engineer  

---

## 🌍 Overview

The **Unique Entrepreneur Learning Platform** is a full-featured, multi-tenant online learning ecosystem designed to serve both the **public learning marketplace** and **private education groups (organisations, schools, and cooperatives)**.  

It draws inspiration from platforms such as **Udemy**, **Coursera**, and **Skillshare**, while adding deep organisational structure, governance, and integration support for schools and small-scale enterprises — particularly within **agriculture**, **recycling**, and **entrepreneurship education**.

---

## 🎯 Core Vision

Empower learners, instructors, and institutions to **create, manage, and deliver structured digital learning experiences** in a governed, secure, and scalable environment.  
This initiative supports entrepreneurship literacy and cooperative education across the UK and Nigeria.

---

## 🧩 Key Features

| Category | Capabilities |
|-----------|--------------|
| **Multi-Tenancy** | Organisation → School → Class hierarchy, with data isolation and white-labelling |
| **Learning Management** | Courses, quizzes, assignments, live sessions, certificates |
| **Commerce** | Marketplace and organisational subscriptions, coupons, and payouts |
| **Analytics** | Enrolment, completion, and revenue dashboards |
| **Governance** | Role-based access, GDPR compliance, data retention and audit |
| **Integrations** | SSO (Google, Microsoft), Zoom/Teams, Stripe/PayPal, S3 video hosting |
| **Accessibility & Localisation** | WCAG 2.1 AA, multi-language, regional currency support |

---

## 🧱 Technical Stack

| Layer | Technology |
|--------|-------------|
| **Frontend** | Next.js · React · TypeScript · TailwindCSS · shadcn/ui |
| **Backend** | Django REST Framework (Python) |
| **Database** | PostgreSQL (with Row-Level Security) |
| **Cache / Queue** | Redis |
| **Storage** | AWS S3 + CloudFront |
| **Deployment** | Docker · GitHub Actions · Terraform · AWS/Vercel |
| **Analytics** | Power BI · Metabase · Google Analytics (optional) |

---

## 🧭 Project Phases

### **Phase 1 – Discovery & Scoping**
- Stakeholder interview templates generated using `python-docx`
- Personas, user journeys, and discovery interview logs
- Output: `UniqueEntrepreneur_Discovery_Interview_Template.docx`

### **Phase 2 – Requirements & Governance Alignment**
- Business Requirements Document (BRD)
- Data Governance Framework
- Compliance & retention model
- Output: `UniqueEntrepreneur_BRD.docx`, `UniqueEntrepreneur_Data_Governance_Framework.docx`

### **Phase 3 – Architecture & Design**
- System Architecture & ERD documentation
- Data Governance Implementation pack
- Technical integration design
- Output: `UniqueEntrepreneur_Phase3_Architecture_and_ERD.docx`

---

## 🧮 Roles and Contributions

| Role | Description |
|------|--------------|
| **Business Analyst (BA)** | Requirement elicitation, process mapping, stakeholder workshops |
| **Data Analyst (DA)** | KPI definition, data visualisation (Power BI), behavioural insights |
| **Data Management Professional (DMP)** | Data governance, quality, compliance, lineage documentation |
| **Frontend/Backend Engineer** | Full-stack architecture setup, code generation tools, infrastructure automation |

---

## 🧰 Automation Scripts

| Script | Purpose |
|--------|----------|
| `generate_kickoff.py` | Creates project kick-off presentation |
| `generate_discovery_template.py` | Builds stakeholder interview forms |
| `create_discovery_interview_log.py` | Generates the Excel log for interview tracking |
| `generate_brd_template.py` | Builds the BRD template with fillable fields |
| `generate_phase3_architecture_design_doc.py` | Creates system architecture documentation |
| `generate_phase3_data_governance_doc.py` | Outputs the data governance implementation pack |
| `generate_userstories_docs.py` | Generates user story sheets for Jira/Azure import |

---

## 🪄 Usage Example

To generate documentation locally:

```bash
python generate_brd_template.py
python generate_phase3_architecture_design_doc.py
python generate_phase3_data_governance_doc.py
