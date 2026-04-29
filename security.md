# 🔐 Security Policy

## 📌 Project Overview
This project is an AI-based chatbot web application built using Flask, HTML, CSS, JavaScript, and external AI APIs. This document outlines OWASP Top 10 risks and tool-specific threats along with their attack scenarios, damage potential, and mitigation strategies.

---

# ⚠️ OWASP Top 10 Risks

## 1. Broken Access Control
- **Attack Scenario:**  
  Unauthorized users access restricted endpoints or admin features.
- **Damage Potential:**  
  Data theft, modification, or deletion.
- **Mitigation:**  
  - Implement role-based access control (RBAC)  
  - Enforce authentication checks  
  - Secure session handling  

---

## 2. Cryptographic Failures
- **Attack Scenario:**  
  Sensitive data is transmitted without encryption.
- **Damage Potential:**  
  Data leaks and privacy breaches.
- **Mitigation:**  
  - Use HTTPS  
  - Encrypt sensitive data  
  - Avoid storing plain-text credentials  

---

## 3. Injection Attacks
- **Attack Scenario:**  
  Malicious input executes unintended queries or commands.
- **Damage Potential:**  
  Database compromise or system control.
- **Mitigation:**  
  - Validate and sanitize inputs  
  - Use parameterized queries  

---

## 4. Security Misconfiguration
- **Attack Scenario:**  
  Debug mode or default settings expose system vulnerabilities.
- **Damage Potential:**  
  Unauthorized system access.
- **Mitigation:**  
  - Disable debug mode  
  - Configure security headers  
  - Regular system audits  

---

## 5. Authentication Failures
- **Attack Scenario:**  
  Weak passwords or poor session handling allow account takeover.
- **Damage Potential:**  
  Unauthorized user access.
- **Mitigation:**  
  - Strong password policies  
  - Multi-factor authentication (MFA)  
  - Secure session tokens  

---

# ⚠️ Tool-Specific Security Threats

## 1. Prompt Injection Attack
- **Attack Vector:**  
  Malicious prompts manipulate AI behavior.
- **Damage Potential:**  
  Exposure of sensitive data or incorrect outputs.
- **Mitigation Plan:**  
  - Input sanitization  
  - Use controlled prompts  
  - Apply moderation filters  

---

## 2. API Key Exposure
- **Attack Vector:**  
  Keys exposed in code or repositories.
- **Damage Potential:**  
  Unauthorized API usage and financial loss.
- **Mitigation Plan:**  
  - Store keys in `.env`  
  - Do not push secrets to GitHub  
  - Rotate keys regularly  

---

## 3. Cross-Site Scripting (XSS)
- **Attack Vector:**  
  Script injection via user inputs.
- **Damage Potential:**  
  Session hijacking and data theft.
- **Mitigation Plan:**  
  - Escape inputs/outputs  
  - Use Content Security Policy (CSP)  

---

## 4. Denial of Service (DoS)
- **Attack Vector:**  
  Flooding server with requests.
- **Damage Potential:**  
  Service downtime.
- **Mitigation Plan:**  
  - Rate limiting  
  - Traffic monitoring  

---

## 5. Data Leakage
- **Attack Vector:**  
  Improper handling of sensitive data.
- **Damage Potential:**  
  Privacy breaches.
- **Mitigation Plan:**  
  - Avoid logging sensitive data  
  - Use HTTPS  
  - Implement access control  

---

## 📢 Reporting a Vulnerability
If you find a security issue, report it responsibly:

**Email:** deepikachavan511@gmail.com  

---

## 📅 Last Updated
April 2026