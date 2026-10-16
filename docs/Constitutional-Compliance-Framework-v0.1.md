# Constitutional Compliance Framework v0.1

Purpose

เอกสารนี้เป็นเฟรมเวิร์กสำหรับพิสูจน์และตรวจสอบว่า MeeChain Constitution ถูกบังคับใช้จริง (evidence-first). เป็นชุดข้อกำหนดและชุดทดสอบ (compliance tests) ที่ทีมออกแบบ ระบบ และผู้ตรวจสอบอิสระใช้เป็นเกณฑ์ยืนยันความสอดคล้องของระบบกับรัฐธรรมนูญ

Scope

- การเชื่อมโยง Proposal → Review → Decision → Implementation → Activation → Verification
- การตรวจสอบ Separation of Powers แบบเทคนิคและกระบวนการ
- ข้อกำหนดสำหรับ Emergency Actions และการทบทวนย้อนหลัง
- ข้อกำหนดด้านการบันทึกหลักฐานและการตรวจสอบย้อนหลัง

Compliance Matrix v0.1

### Governance

| Test ID | Requirement |
|----------|----------|
| GOV-001 | ผู้เสนอไม่สามารถอนุมัติขั้นสุดท้ายเพียงลำพัง |
| GOV-002 | Review ต้องมาจากผู้มีสิทธิ์ |
| GOV-003 | Activation ตรงกับ Approval |
| GOV-004 | Proposal มีเลขอ้างอิงเฉพาะ |
| GOV-005 | มีประวัติการเปลี่ยนแปลงครบถ้วน |

### Separation of Powers

| Test ID | Requirement |
|----------|----------|
| SOP-001 | Proposer ≠ Final Approver |
| SOP-002 | Reviewer ≠ Sole Activator |
| SOP-003 | Developer ≠ Sole Reviewer |
| SOP-004 | Council ≠ Unlimited Authority |
| SOP-005 | Verify Layer แยกจาก Activate Layer |

### Security

| Test ID | Requirement |
|----------|----------|
| SEC-001 | Protocol Change ต้องผ่าน Governance |
| SEC-002 | ไม่มีช่องทางข้าม Approval Flow |
| SEC-003 | สิทธิ์ Admin ถูกบันทึก |
| SEC-004 | สิทธิ์ระดับสูงตรวจสอบย้อนหลังได้ |
| SEC-005 | Runtime ตรงกับ Configuration ที่อนุมัติ |

### Auditability

| Test ID | Requirement |
|----------|----------|
| AUD-001 | Proposal ↔ Review เชื่อมโยงได้ |
| AUD-002 | Review ↔ Approval เชื่อมโยงได้ |
| AUD-003 | Approval ↔ Activation เชื่อมโยงได้ |
| AUD-004 | Activation ↔ Verification เชื่อมโยงได้ |
| AUD-005 | ตรวจย้อนเส้นทางหลักฐานได้ครบ |

### Emergency

| Test ID | Requirement |
|----------|----------|
| EMG-001 | Emergency Action มีเหตุผล |
| EMG-002 | มีผู้อนุมัติ |
| EMG-003 | มีวันหมดอายุ |
| EMG-004 | มี Post-Mortem |
| EMG-005 | ไม่ทำให้เกิดสิทธิ์ถาวร |

Definition of Ready (DoR)

MeeChain Constitution v0.2 จะถือว่า "พร้อมอ้างอิงในการออกแบบ Mainnet" เมื่อรายการต่อไปนี้ครบ:

- Constitution v0.2
- Governance Powers Matrix
- Constitutional Compliance Matrix
- Document Lifecycle
- Separation of Powers
- Governance Council Rules
- Emergency Governance Rules
- Evidence Chain Model

---

Notes / Next steps

- รายการทดสอบด้านบนเป็นเวอร์ชันเริ่มต้น (v0.1) — ควรแปลงเป็นชุดทดสอบแบบเครื่องมือ (automated checks) และ QA playbook
- ควรกำหนดรูปแบบหลักฐาน (evidence artifacts) เช่น Proposal ID, signed decisions, activation tx และ verification reports
