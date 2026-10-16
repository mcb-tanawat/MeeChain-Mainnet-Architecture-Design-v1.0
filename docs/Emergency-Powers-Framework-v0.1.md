# Emergency Powers Framework v0.1

Purpose

นิยามประเภทการดำเนินการฉุกเฉิน ขอบเขต เวลา และกระบวนการทบทวนย้อนหลัง (post-incident review) เพื่อให้ตอบสนองต่อเหตุการณ์ได้เร็ว แต่ไม่ก่อให้เกิดการเปลี่ยนแปลงถาวรโดยไม่ผ่านกระบวนการ Governance ปกติ

Emergency Types

- Type 1 — Containment
  - เป้าหมาย: หยุดความเสียหายทันที
  - ตัวอย่าง: ปิด RPC บางส่วน, ระงับ relayer, จำกัดประเภทธุรกรรม
  - ข้อจำกัด: ห้ามเปลี่ยนกฎถาวร
  - Expiry: ระบุเวลาหมดอายุอัตโนมัติ

- Type 2 — Recovery
  - เป้าหมาย: กู้คืนบริการให้กลับมาทำงาน
  - ตัวอย่าง: Roll forward, node recovery, validator resync
  - ข้อจำกัด: ไม่ขยายอำนาจถาวร
  - Expiry + Review: ต้องมี Post-Mortem และการอนุมัติย้อนหลัง

- Type 3 — Permanent Change
  - เป้าหมาย: แก้ปัญหาระยะยาวที่จำเป็นต้องเปลี่ยนแปลงถาวร
  - กระบวนการ: ต้องเข้าสู่ Proposal → Review → Approval → Activation → Verification ปกติ

Authority & Limits

- ระบุผู้มีอำนาจทำ Emergency action แต่ละประเภท (roles limited)
- ทุกการกระทำฉุกเฉินต้องมี: เหตุผล, ระยะเวลา, รายชื่อผู้อนุมัติ, หลักฐานการตัดสินใจ
- การกระทำฉุกเฉินมีวันหมดอายุอัตโนมัติและต้องผ่าน Post-Incident Review

Audit & Transparency

- บันทึกเหตุผลและหลักฐานทุกขั้นตอน
- รายงาน Post-Mortem เปิดเผยต่อชุมชน (เว้นข้อมูลความปลอดภัยที่เป็นความลับ)

Next steps

- กำหนด escalation path และ automation killswitch ที่ชัดเจน
- สร้าง test drills และ runbooks สำหรับแต่ละ Type
