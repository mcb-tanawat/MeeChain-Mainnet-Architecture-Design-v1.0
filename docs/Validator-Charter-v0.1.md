# Validator Charter v0.1

Purpose

กำหนดคุณสมบัติ บทบาท และกระบวนการสำหรับ Validator บน MeeChain เพื่อรักษา Integrity, Liveness และ Recoverability ของเครือข่าย

Eligibility & Onboarding

- เกณฑ์พื้นฐาน: uptime, hardware, identity vetting, stake/commitment (ถ้ามี)
- Background checks: security posture, operational competence
- Onboarding process: application → vetting → testnet probation → active validator

Responsibilities

- Participate in consensus และตรวจสอบการเปิดใช้งาน (Activation)
- ลงคะแนนในระดับ Protocol / Operational ตามที่กำหนด
- บันทึกหลักฐานการดำเนินการและเผยแพร่ logs เพื่อให้ตรวจสอบย้อนหลังได้

SLAs & Monitoring

- Uptime target: ระบุเป็นเกณฑ์ (ตัวอย่าง: 99% over 30 days)
- Performance metrics: block propagation latency, validation latency
- Reporting: รายงานเหตุผิดปกติและการเปลียนแปลงด้านการดำเนินงาน

Removal & Dispute

- Removal triggers: โกง, offline ต่อเนื่อง, ขัดกับกติกา security
- Evidence required: เหตุผล + หลักฐาน + สิทธิอุทธรณ์
- Slashing / Penalties: ระบุไว้ใน Protocol Rules หากใช้

Independence & COI

- Validator ต้องไม่มีสิทธิพิเศษเหนือธุรกรรมทั่วไป (COI-4)
- ห้ามมี key sharing ที่ทำให้สิทธิ์รวมศูนย์

Next steps

- ขยายเป็น playbook onboarding และ offboarding
- ระบุ telemetry และ metric export format สำหรับการตรวจสอบ
