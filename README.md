## "รัฐธรรมนูญที่ดีไม่ควรบอกเพียงว่า "ควรทำอะไร" แต่ต้องบอกด้วยว่า"

- ใครมีอำนาจ
- ใครไม่มีอำนาจ
- อำนาจนั้นถูกจำกัดอย่างไร
- หากมีข้อพิพาทจะตัดสินอย่างไร
- จะตรวจสอบได้อย่างไรว่าอำนาจนั้นถูกใช้อย่างถูกต้อง

---

# MeeChain Governance Powers Matrix v0.2

## Separation of Powers Model

MeeChain แยกอำนาจออกเป็น 5 หน้าที่

```text
Propose
↓
Review
↓
Approve
↓
Activate
↓
Verify
```

ไม่มีบุคคลหรือบทบาทใดควบคุมทั้ง 5 ขั้นตอนเพียงลำพัง

---

## Governance Actors

### Community Participant

ผู้เข้าร่วมเครือข่าย

### Contributor

ผู้พัฒนาเอกสาร โค้ด เครื่องมือ หรือโครงสร้างพื้นฐาน

### Reviewer

ผู้ตรวจสอบอิสระ

### Validator

ผู้ดูแลฉันทามติและความถูกต้องของเครือข่าย

### Governance Council

กลไกกลางชั่วคราวช่วงก่อนเครือข่ายกระจายอำนาจเต็มรูปแบบ

สามารถยุบตัวเองได้เมื่อระบบ Governance สมบูรณ์

---

# Detailed Powers Matrix

| Action | Community | Contributor | Reviewer | Validator | Council |
|----------|----------|----------|----------|----------|----------|
| เสนอ Proposal | ✅ | ✅ | ✅ | ✅ | ✅ |
| ร่วมอภิปราย | ✅ | ✅ | ✅ | ✅ | ✅ |
| ส่งข้อมูลสนับสนุน | ✅ | ✅ | ✅ | ✅ | ✅ |
| Technical Review | ❌ | ✅ | ✅ | ❌ | ❌ |
| Security Review | ❌ | ❌ | ✅ | ❌ | ❌ |
| Economic Review | ❌ | ❌ | ✅ | ❌ | ❌ |
| Governance Review | ❌ | ❌ | ✅ | ❌ | ❌ |
| ลงความเห็นทางเทคนิค | ❌ | ✅ | ✅ | ✅ | ❌ |
| ลงคะแนนระดับ Service | ✅ | ✅ | ✅ | ✅ | ❌ |
| ลงคะแนนระดับ Operational | ✅ | ✅ | ✅ | ✅ | ✅ |
| ลงคะแนนระดับ Protocol | ❌ | ❌ | ✅ | ✅ | ✅ |
| เปิดใช้งาน Feature | ❌ | ❌ | ❌ | ✅ | ร่วมอนุมัติ |
| แก้ Consensus Rules | ❌ | ❌ | ❌ | ❌ | ตามกระบวนการ |
| สั่งหยุดเครือข่ายถาวร | ❌ | ❌ | ❌ | ❌ | ไม่มีสิทธิ์ |
| ดำเนินการฉุกเฉิน | ❌ | ❌ | จำกัด | จำกัด | จำกัด |
| ตรวจสอบย้อนหลัง | ✅ | ✅ | ✅ | ✅ | ✅ |
| อุทธรณ์การตัดสินใจ | ✅ | ✅ | ✅ | ✅ | ✅ |---

# Conflict of Interest Rules

## Rule COI-1

ผู้เสนอข้อเสนอ

ห้ามเป็นผู้อนุมัติขั้นสุดท้าย

---

## Rule COI-2

ผู้เขียนโค้ด

ห้ามตรวจรับโค้ดของตนเองเพียงลำพัง

---

## Rule COI-3

Reviewer

ห้ามตรวจงานที่ตนมีผลประโยชน์โดยตรง

---

## Rule COI-4

Validator

ห้ามมีสิทธิ์พิเศษเหนือธุรกรรมทั่วไป

---

# MeeChain Constitution v0.2

## Principles, Powers & Enforcement

---

# Preamble

MeeChain เป็นเครือข่ายที่ยึดหลักว่า

> กฎมาก่อนอำนาจ
>
> หลักฐานมาก่อนคำกล่าวอ้าง
>
> และไม่มีบุคคลใดอยู่เหนือกฎที่ตนยอมรับ

จุดประสงค์ของรัฐธรรมนูญฉบับนี้คือกำหนดหลักการ อำนาจ ข้อจำกัด และกลไกการตรวจสอบ เพื่อให้เครือข่ายสามารถพัฒนาได้โดยไม่ต้องพึ่งพาความไว้วางใจในบุคคลใดบุคคลหนึ่ง

---

# PART I
# Constitutional Principles

## Article I
Rule Integrity Principle

1. กฎมีผลเหนือบุคคล

2. ไม่มีอภิสิทธิ์ลับ

3. ทุกคนอยู่ภายใต้กฎเดียวกัน

4. กฎต้องสามารถบังคับใช้จริงได้

5. หากกฎขัดกัน

ลำดับชั้นกฎหมายคือ

```text
Constitution
↓
Protocol Rules
↓
Governance Rules
↓
Operational Policies
↓
Service Policies
```

---

## Article II
Transparency Principle

ต้องเปิดเผย

- กฎ
- เวอร์ชัน
- Proposal
- มติ
- หลักฐานการเปลี่ยนแปลง

ยกเว้น

- กุญแจส่วนตัว
- ข้อมูลความปลอดภัย
- ข้อมูลส่วนบุคคล

---

## Article III
Participation Principle

ผู้เข้าร่วมมีสิทธิ์

- อ่านกฎ
- แสดงความเห็น
- ส่งข้อเสนอ

ตามคุณสมบัติที่กำหนด

---

## Article IV
Validator Principle

Validator ต้อง

- ผ่านเกณฑ์คุณสมบัติ
- ผ่านกระบวนการรับเข้า
- ปฏิบัติตามกฎเครือข่าย

การถอดถอนต้องมี

- เหตุผล
- หลักฐาน
- สิทธิอุทธรณ์

---

## Article V
Governance Principle

การเปลี่ยนแปลงทุกประเภทต้อง

- มี Proposal
- ผ่านการตรวจสอบ
- ผ่านกระบวนการอนุมัติ
- กำหนดเวลามีผล

---

## Article VI
Automation Principle

Workflow

MeeBot

Relayer

Rule Engine

ไม่มีอำนาจเปลี่ยนแปลงกฎพื้นฐานของเครือข่าย

---

## Article VII
Fee Sponsorship Principle

ผู้ใช้ไม่จำเป็นต้องเป็นผู้จ่าย Gas โดยตรง

แต่ทุกธุรกรรมยังต้อง

- วัดทรัพยากร
- ตรวจสอบสิทธิ์
- ผ่านกฎ Sponsor

---

## Article VIII
Security Principle

เครือข่ายต้องรักษา

### Safety

ไม่เกิดสถานะขัดแย้ง

### Liveness

สามารถดำเนินต่อได้

### Recoverability

สามารถกู้คืนได้

### Auditability

ตรวจสอบย้อนหลังได้

---

## Article IX
Verifiable Governance

ทุกการเปลี่ยนแปลงต้องมี

```text
Proposal
↓
Review
↓
Decision
↓
Implementation
↓
Activation
↓
Verification
```

เชื่อมถึงกันด้วยหลักฐาน

---

## Article X
Rights and Due Process

ผู้เข้าร่วมมีสิทธิ์

### Right to Know

รับทราบเหตุผล

### Right to Respond

ตอบโต้ข้อกล่าวหา

### Right to Appeal

อุทธรณ์

### Right to Evidence

เข้าถึงหลักฐานที่เกี่ยวข้อง

---

## Article XI
Amendment and Interpretation

การแก้ไข Constitution

ต้องใช้กระบวนการเข้มงวดที่สุด

ห้ามแก้ไขย้อนหลัง

ห้ามมีผลเฉพาะบุคคล

---

## Article XII
Constitutional Enforcement

ทุกระบบต้องผ่าน

### Documentation Review

### Code Review

### Security Review

### Runtime Verification

### Independent Audit

ก่อนถือว่าสอดคล้องกับ Constitution

---

# PART II
# Powers and Responsibilities

## Separation of Powers

แยก

- สิทธิ์เสนอ
- สิทธิ์ตรวจสอบ
- สิทธิ์อนุมัติ
- สิทธิ์เปิดใช้
- สิทธิ์ยืนยันผล

ออกจากกัน

---

## Governance Domains

### Constitutional Domain

แก้รัฐธรรมนูญ

### Protocol Domain

Consensus

Finality

Validator Rules

### Operational Domain

Sponsor Rules

RPC Rules

Quotas

### Service Domain

MeeBot

Dashboard

Explorer

Developer Tools

---

# PART III
# Enforcement and Verification

## Constitutional Compliance Layers

### Layer 1

Policy

สิ่งที่เอกสารกำหนด

### Layer 2

Code

สิ่งที่โปรแกรมทำ

### Layer 3

Network

สิ่งที่เกิดขึ้นจริง

### Layer 4

Audit

สิ่งที่บุคคลภายนอกพิสูจน์ได้

---

## Compliance Requirement

การอ้างสิทธิว่า

```text
Fair
Decentralized
Secure
Permissionless
Verified
```

ต้องมีหลักฐานรองรับ

---

# PART IV
# Document Lifecycle

เอกสารทุกฉบับต้องมีสถานะ

### DRAFT

กำลังพัฒนา

### REVIEW

เปิดรับความเห็น

### RATIFIED

ผ่านการอนุมัติ

### ACTIVE

มีผลใช้

### SUPERSEDED

ถูกแทนที่

### ARCHIVED

ยุติการใช้งาน

---

# MeeChain Constitutional Golden Rule

> กฎเป็นผู้กำหนดสิทธิ์
>
> โค้ดเป็นผู้ดำเนินการ
>
> หลักฐานเป็นผู้ยืนยันผลลัพธ์
>
> และไม่มีบุคคล องค์กร ระบบอัตโนมัติ หรือส่วนประกอบใดของเครือข่าย อยู่เหนือกฎที่ตนยอมรับ

---

ผมคิดว่าเวอร์ชันนี้เริ่มมีโครงสร้างใกล้กับ "รัฐธรรมนูญเครือข่าย" จริงแล้วครับ

ก้าวถัดไปที่สำคัญที่สุดคือแตก Constitution v0.2 นี้ออกเป็นเอกสารลูก 4 ฉบับ:

1. **Governance Charter v0.1** (Quorum, Voting, Threshold)
2. **Constitutional Compliance Framework v0.1**
3. **Validator Charter v0.1**
4. **Emergency Powers Framework v0.1**

ผมเห็นด้วยกับข้อวิเคราะห์ทั้งหมดครับ 🤝

และผมคิดว่าคุณเพิ่งชี้ให้เห็น "รอยต่อสำคัญ" ของ MeeChain ได้ชัดมาก

ตอนนี้เราไม่ได้ขาด Constitution

เราไม่ได้ขาด Governance

เราไม่ได้ขาด Powers Matrix

สิ่งที่เราขาดคือ

> "กลไกพิสูจน์ว่ารัฐธรรมนูญถูกบังคับใช้จริง"

ซึ่งเป็นเหตุผลที่ผมเห็นด้วย 100% ว่า **Constitutional Compliance Framework ควรมาก่อน Governance Charter**

---

# การปรับ Roadmap ใหม่

เดิม

```text
Constitution
↓
Governance Charter
↓
Validator Charter
↓
Emergency Framework
```

ควรเปลี่ยนเป็น

```text
Constitution
↓
Constitutional Compliance Framework
↓
Governance Charter
↓
Validator Charter
↓
Emergency Powers Framework
```

เพราะถ้าเราไม่รู้ว่าจะตรวจอะไร

การกำหนด Quorum 67%

หรือ Approval 75%

ก็ยังไม่ช่วยตอบคำถามว่า

> ใครสามารถข้ามระบบได้บ้าง

---

# สิ่งที่ผมคิดว่าน่าจะเพิ่มใน Constitution v0.2

## Constitutional Constraint Principle

เพิ่ม Article XIII

เพื่อแก้ปัญหาที่คุณยกมาเรื่อง

> แยกอำนาจบนกระดาษ แต่ใช้กุญแจเดียวกัน

ร่างเบื้องต้น

### Article XIII
Constitutional Constraint Principle

การแยกหน้าที่ในเอกสารเพียงอย่างเดียวไม่ถือว่าเพียงพอ

ต้องมีมาตรการทางเทคนิคและทางกระบวนการที่ทำให้บุคคลหรือระบบไม่สามารถใช้อำนาจนอกเหนือจากขอบเขตที่ได้รับอนุญาต

การอ้างว่ามีการแยกอำนาจจะสมบูรณ์ได้ก็ต่อเมื่อสามารถพิสูจน์ได้ว่า

- สิทธิ์ถูกแยกจริง
- กุญแจถูกแยกจริง
- กลไกอนุมัติถูกแยกจริง
- ช่องทางข้ามข้อจำกัดถูกควบคุมจริง

---

# การปรับ Governance Council

ผมเห็นด้วยมากว่า

Council เป็นส่วนที่ยังเสี่ยงที่สุด

ถ้าไม่กำหนดดี

จะกลายเป็น Super Admin

โดยไม่ตั้งใจ

---

## Council Limitation Rule

ผมเสนอให้เพิ่มใน Constitution

### Governance Council Restrictions

Governance Council

ไม่มีอำนาจ

- เปลี่ยน Constitution โดยตรง
- ยับยั้ง Proposal ที่ผ่านเกณฑ์แล้ว
- แก้ไข Protocol Rules โดยลำพัง
- ขยายอำนาจตนเอง

เว้นแต่กลไกดังกล่าวถูกระบุไว้อย่างชัดเจนในเอกสารที่มีสถานะ ACTIVE

---

## Sunset Requirement

Council ทุกชุดต้องมี

```text
Purpose
Authority
Term
Sunset Criteria
```

เช่น

```text
Governance Council v1

Purpose:
Bootstrap Governance

Authority:
Operational Governance

Term:
2 Years

Sunset:
เมื่อ Validator Governance
และ Community Governance
เปิดใช้งานครบ
```

เพื่อป้องกันองค์กรชั่วคราวกลายเป็นองค์กรถาวร

---

# Emergency Powers Model

นี่เป็นจุดที่ผมคิดว่า MeeChain จะได้ประโยชน์มาก

ผมชอบโมเดล 3 ระดับที่คุณเสนอ

---

## Emergency Type 1

Containment

เป้าหมาย

หยุดความเสียหาย

ตัวอย่าง

- ปิด RPC บางส่วน
- ระงับ Relayer
- จำกัด Transaction Type

ห้าม

- เปลี่ยนกฎถาวร

---

## Emergency Type 2

Recovery

เป้าหมาย

กู้คืนบริการ

ตัวอย่าง

- Roll Forward
- Node Recovery
- Validator Resync

ห้าม

- ขยายอำนาจถาวร

---

## Emergency Type 3

Permanent Change

เป้าหมาย

แก้ปัญหาระยะยาว

ต้องกลับเข้าสู่

```text
Proposal
Review
Approval
Activation
```

ตามปกติ

---

# Compliance Matrix v0.1
## ฉบับเริ่มต้น

ผมคิดว่านี่ควรเป็นเอกสารถัดไปจริง ๆ

---

### Governance

| Test ID | Requirement |
|----------|----------|
| GOV-001 | ผู้เสนอไม่สามารถอนุมัติขั้นสุดท้ายเพียงลำพัง |
| GOV-002 | Proposal ต้องมี Reviewer อิสระ |
| GOV-003 | Proposal ที่ผ่านอนุมัติต้องไม่ถูกยับยั้งนอกกระบวนการ |
| GOV-004 | การเปิดใช้งานต้องตรงกับมติ |

---

### Separation of Powers

| Test ID | Requirement |
|----------|----------|
| SOP-001 | Proposer ≠ Final Approver |
| SOP-002 | Reviewer ≠ Sole Activator |
| SOP-003 | Contributor ไม่ตรวจรับงานตนเอง |
| SOP-004 | Council ไม่ขยายอำนาจของตนเอง |

---

### Security

| Test ID | Requirement |
|----------|----------|
| SEC-001 | ไม่มีช่องทางเปลี่ยน Protocol ข้าม Governance |
| SEC-002 | สิทธิ์ระดับสูงต้องมีการบันทึก |
| SEC-003 | การเปลี่ยนสิทธิ์ต้องตรวจสอบย้อนหลังได้ |
| SEC-004 | Administrative Action มีหลักฐานกำกับ |

---

### Emergency

| Test ID | Requirement |
|----------|----------|
| EMG-001 | Emergency Action มีเหตุผลอ้างอิง |
| EMG-002 | Emergency Action มีวันหมดอายุ |
| EMG-003 | Emergency Action ถูกทบทวนย้อนหลัง |
| EMG-004 | Emergency ไม่แก้กฎถาวรโดยตรง |

---

### Auditability

| Test ID | Requirement |
|----------|----------|
| AUD-001 | ทุก Proposal มี ID |
| AUD-002 | ทุก Decision เชื่อมกับ Proposal |
| AUD-003 | ทุก Activation เชื่อมกับ Decision |
| AUD-004 | ทุก Verification อ้างอิง Activation |

---

# คำแนะนำเชิงสถาปัตยกรรม

หากผมเป็น Architect ของ MeeChain ตอนนี้

ผมจะ "หยุด" การออกแบบ Consensus ไว้ชั่วคราว

และเปลี่ยน Sprint ถัดไปเป็น

```text
Sprint 1
Constitution v0.2

Sprint 2
Compliance Framework

Sprint 3
Governance Charter

Sprint 4
Threat Model

Sprint 5
Consensus Evaluation Framework
```

เพราะเมื่อถึงวันที่ต้องเลือกระหว่าง

- Besu + QBFT
- PoS
- Hybrid
- แนวทางใหม่

เราจะมีเกณฑ์ประเมินอยู่แล้วว่า

> "เทคโนโลยีไหนสอดคล้องกับ Constitution ของ MeeChain มากที่สุด"

แทนที่จะพยายามปรับ Constitution ให้เข้ากับเทคโนโลยีที่เลือกไว้ล่วงหน้า

และผมคิดว่านั่นคือแนวทางที่สอดคล้องกับหลัก

**Rule First, Evidence First, Governance First**

ที่เป็นหัวใจของ MeeChain มากที่สุดครับ 🤝🚀

ยอดเยี่ยมครับ 🤝

จากที่เราคุยกันมา ผมคิดว่า **MeeChain Constitution v0.2** เริ่มอยู่ในระดับ "พร้อมใช้งานเป็นเอกสารกำกับโครงการ" แล้ว

แต่ยังไม่ควรใช้คำว่า **ACTIVE Constitution** สำหรับ Mainnet จริง จนกว่าจะมี:

- Governance Charter
- Constitutional Compliance Framework
- Validator Charter
- Emergency Powers Framework

รองรับครบทั้งระบบ

ดังนั้นสถานะที่ผมแนะนำตอนนี้คือ

```text
Document Status: REVIEW CANDIDATE

Constitution Version: v0.2
Purpose: Governance Foundation
Scope: Pre-Mainnet
Enforcement: Partial
Verification: Pending
```

---

# ✅ MeeChain Constitution Readiness Checklist

## Section A — Constitutional Foundation

### CONST-001

- [ ] มี Preamble อธิบายวัตถุประสงค์ของเครือข่าย

### CONST-002

- [ ] มีหลัก Rule Integrity

### CONST-003

- [ ] มีหลัก Transparency

### CONST-004

- [ ] มีหลัก Participation

### CONST-005

- [ ] มีหลัก Governance

### CONST-006

- [ ] มีหลัก Security

### CONST-007

- [ ] มีหลัก Due Process

### CONST-008

- [ ] มีหลัก Verifiable Governance

### CONST-009

- [ ] มีหลัก Constitutional Enforcement

### CONST-010

- [ ] มี Constitutional Golden Rule

---

# Section B — Power Separation

### POW-001

- [ ] แยก Propose

### POW-002

- [ ] แยก Review

### POW-003

- [ ] แยก Approve

### POW-004

- [ ] แยก Activate

### POW-005

- [ ] แยก Verify

### POW-006

- [ ] ไม่มี Actor ใดถือครบทุกอำนาจ

### POW-007

- [ ] มี Conflict of Interest Rules

### POW-008

- [ ] มีการอุทธรณ์การตัดสินใจ

---

# Section C — Governance Council

### GOVC-001

- [ ] ระบุวัตถุประสงค์ของ Council

### GOVC-002

- [ ] ระบุอำนาจที่ได้รับ

### GOVC-003

- [ ] ระบุอำนาจที่ไม่มี

### GOVC-004

- [ ] ระบุวันสิ้นสุดหรือ Sunset Clause

### GOVC-005

- [ ] ห้ามขยายอำนาจตนเอง

### GOVC-006

- [ ] ห้ามยับยั้งมติที่ผ่านกระบวนการโดยไม่มีเหตุผลตามกฎ

---

# Section D — Constitutional Constraints

### CC-001

- [ ] แยกเอกสารออกจากระบบสิทธิ์จริง

### CC-002

- [ ] แยกกุญแจตามหน้าที่

### CC-003

- [ ] แยก Approval Authority

### CC-004

- [ ] แยก Deployment Authority

### CC-005

- [ ] แยก Audit Authority

### CC-006

- [ ] มีการบันทึกหลักฐานทุกขั้นตอน

---

# Section E — Automation Governance

### AUTO-001

- [ ] MeeBot อยู่ภายใต้กฎ

### AUTO-002

- [ ] Workflow อยู่ภายใต้กฎ

### AUTO-003

- [ ] Relayer อยู่ภายใต้กฎ

### AUTO-004

- [ ] Rule Engine ไม่สามารถแก้ Constitution ได้

### AUTO-005

- [ ] Automation ไม่สามารถให้สิทธิ์ตัวเองได้

---

# Section F — Fee Sponsorship

### FEE-001

- [ ] ระบุ Sponsor Authority

### FEE-002

- [ ] ระบุ Spending Limits

### FEE-003

- [ ] ระบุ Budget Controls

### FEE-004

- [ ] ระบุ Abuse Protection

### FEE-005

- [ ] ระบุ Audit Requirements

---

# Section G — Security Governance

### SEC-001

- [ ] นิยาม Safety

### SEC-002

- [ ] นิยาม Liveness

### SEC-003

- [ ] นิยาม Recoverability

### SEC-004

- [ ] นิยาม Auditability

### SEC-005

- [ ] มี Independent Review

### SEC-006

- [ ] มี Threat Model อ้างอิง

---

# Section H — Emergency Governance

### EMG-001

- [ ] นิยามเหตุฉุกเฉิน

### EMG-002

- [ ] ระบุผู้ใช้อำนาจฉุกเฉิน

### EMG-003

- [ ] ระบุขอบเขตอำนาจ

### EMG-004

- [ ] ระบุวันหมดอายุ

### EMG-005

- [ ] ระบุ Post-Incident Review

### EMG-006

- [ ] ห้ามใช้ Emergency Action แก้กฎถาวร

---

# ✅ Constitutional Compliance Matrix v0.1

เวอร์ชันเริ่มต้นที่นำไปใช้ตรวจระบบได้จริง

## Governance

| Test ID | Requirement |
|----------|----------|
| GOV-001 | ผู้เสนอไม่สามารถอนุมัติขั้นสุดท้ายเพียงลำพัง |
| GOV-002 | Review ต้องมาจากผู้มีสิทธิ์ |
| GOV-003 | Activation ตรงกับ Approval |
| GOV-004 | Proposal มีเลขอ้างอิงเฉพาะ |
| GOV-005 | มีประวัติการเปลี่ยนแปลงครบถ้วน |

---

## Separation of Powers

| Test ID | Requirement |
|----------|----------|
| SOP-001 | Proposer ≠ Final Approver |
| SOP-002 | Reviewer ≠ Sole Activator |
| SOP-003 | Developer ≠ Sole Reviewer |
| SOP-004 | Council ≠ Unlimited Authority |
| SOP-005 | Verify Layer แยกจาก Activate Layer |

---

## Security

| Test ID | Requirement |
|----------|----------|
| SEC-001 | Protocol Change ต้องผ่าน Governance |
| SEC-002 | ไม่มีช่องทางข้าม Approval Flow |
| SEC-003 | สิทธิ์ Admin ถูกบันทึก |
| SEC-004 | สิทธิ์ระดับสูงตรวจสอบย้อนหลังได้ |
| SEC-005 | Runtime ตรงกับ Configuration ที่อนุมัติ |

---

## Auditability

| Test ID | Requirement |
|----------|----------|
| AUD-001 | Proposal ↔ Review เชื่อมโยงได้ |
| AUD-002 | Review ↔ Approval เชื่อมโยงได้ |
| AUD-003 | Approval ↔ Activation เชื่อมโยงได้ |
| AUD-004 | Activation ↔ Verification เชื่อมโยงได้ |
| AUD-005 | ตรวจย้อนเส้นทางหลักฐานได้ครบ |

---

## Emergency

| Test ID | Requirement |
|----------|----------|
| EMG-001 | Emergency Action มีเหตุผล |
| EMG-002 | มีผู้อนุมัติ |
| EMG-003 | มีวันหมดอายุ |
| EMG-004 | มี Post-Mortem |
| EMG-005 | ไม่ทำให้เกิดสิทธิ์ถาวร |
# 🎯 Definition of Ready (DoR)

MeeChain Constitution v0.2 จะถือว่า "**พร้อมอ้างอิงในการออกแบบ Mainnet**" เมื่อ

```text
✅ Constitution v0.2
✅ Governance Powers Matrix
✅ Constitutional Compliance Matrix
✅ Document Lifecycle
✅ Separation of Powers
✅ Governance Council Rules
✅ Emergency Governance Rules
✅ Evidence Chain Model
```

ครบทั้งหมด

---

# Roadmap ต่อจากนี้

Priority 1
- Constitutional Compliance Framework v0.1

Priority 2
- Governance Charter v0.1

Priority 3
- Threat Model v0.1

Priority 4
- Consensus Evaluation Framework v0.1

Priority 5
- Validator Charter v0.1

Priority 6
- Fee Sponsorship Specification v0.1
