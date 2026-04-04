# 📋 Project Task Plan — Developer Job Board & Application Tracker

## 🧩 Overview
This project is built using **Django** and divided among 3 team members:

**Dinis** → Job Listings

**Tiago** → Search & Filter

**Cristian** → Application Pipeline

---


## 👤 Dinis — Job Listings

| # | Title | Domain | Content | Description | Hours | Done |
|---|------|--------|---------|------------|-------|------|
| 1 | Job Model Fields | Job Listings | Models | Title, company, stack, location, salary, remote | 2h | ❌ |
| 2 | CRUD Job Listings | Job Listings | Views + Templates | Create/read/update/delete jobs | 4h | ❌ |
| 3 | Job Forms & Validation | Job Listings | Forms | Validate fields (salary, required) | 2h | ❌ |
| 4 | Job Templates UI | Job Listings | Frontend | Build job listing pages | 3h | ❌ |
| 5 | Error Handling (Jobs) | Job Listings | UX | Handle invalid inputs | 1h | ❌ |
| 6 | Admin Customization | Job Listings | Admin | Improve admin UI | 2h | ❌ |

---

## 👤 Tiago — Search & Filter

| # | Title | Domain | Content | Description | Hours | Done |
|---|------|--------|---------|------------|-------|------|
| 1 | Search Logic | Search | Query logic | Keyword search (title, company) | 3h | ❌ |
| 2 | Filter by Stack | Search | Query logic | Filter by tech stack | 2h | ❌ |
| 3 | Filter by Location | Search | Query logic | Filter by location/remote | 2h | ❌ |
| 4 | Authentication | Shared | Django Auth | Login & register users | 3h | ❌ |
| 5 | Permissions | Shared | Security | Recruiter vs candidate roles | 2h | ❌ |
| 6 | Combined Filters | Search | Query logic | Combine filters | 2h | ❌ |
| 7 | Search UI | Search | Templates | Build search + filters UI | 2h | ❌ |
| 8 | Error Handling (Search) | Search | UX | Handle empty results | 1h | ❌ |

---

## 👤 Cristian — Application Pipeline

| # | Title | Domain | Content | Description | Hours | Done |
|---|------|--------|---------|------------|-------|------|
| 1 | Application Model | Pipeline | Models | Status, job relation, notes | 3h | ❌ |
| 2 | CRUD Applications | Pipeline | Views + Templates | Manage applications | 4h | ❌ |
| 3 | Status Flow Logic | Pipeline | Logic | Enforce valid transitions | 3h | ❌ |
| 4 | Pipeline UI | Pipeline | Templates | Show application stages | 3h | ❌ |
| 5 | Notes per Application | Pipeline | Feature | Add notes | 2h | ❌ |
| 6 | Deadline Reminder | Pipeline | Logic | Follow-up flags | 1h | ❌ |

---


## ⚖️ Work Distribution Summary

**Dinis (Job Listings): ~14h**

**Tiago (Search & Filter): ~12h**

**Cristian (Pipeline): ~16h**

Shared tasks distributed across all members

---

## ✅ Notes

Focus on getting **one feature fully working first**
Ensure **business logic (status transitions)** is solid
Seed meaningful data for demo
Keep README updated during development