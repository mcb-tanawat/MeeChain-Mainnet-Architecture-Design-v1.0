# Governance Charter v0.1

Purpose

เอกสารนี้กำหนดหลักปฏิบัติ กระบวนการ และกฎการลงมติสำหรับการเปลี่ยนแปลงเชิง Governance ของ MeeChain เพื่อให้การตัดสินใจเป็นไปอย่างโปร่งใส ยุติธรรม และตรวจสอบได้

Scope

- Quorum, Voting thresholds และ Voting workflows
- บทบาท (Roles) และอำนาจ (Authorities)
- Proposal lifecycle (Draft → Review → Vote → Ratify → Implement)
- Conflict of Interest controls

Roles & Authorities

- Community Participant: เสนอ, ร่วมอภิปราย, ส่งข้อมูลสนับสนุน
- Contributor: เสนอ, พัฒนารูปแบบการเปลี่ยนแปลง, ลงความเห็นเชิงเทคนิค
- Reviewer: ตรวจสอ��ด้านเทคนิค ความปลอดภัย ผลกระทบทางเศรษฐกิจ และ Governance Review
- Validator: ตรวจสอบความถูกต้องของการเปิดใช้งาน และลงคะแนนระดับ Protocol / Operational
- Governance Council: กลไกชั่วคราวสำหรับบูตสแตรป พื้นที่ปฏิบัติการเชิงกลไก (มีข้อจำกัดตาม Constitution)

Quorum & Voting

- Quorum: ระบุเปอร์เซ็นต์ขั้นต่ำของผู้มีสิทธิ์ร่วมในการลงคะแนน (ตัวอย่าง: 20–33% ขึ้นกับโดเมน)
- Approval Thresholds:
  - Operational changes: simple majority (50%+1)
  - Service-level changes: qualified majority (e.g., 67%)
  - Protocol / Constitutional changes: supermajority (e.g., 75% or higher)
- Abstain / Reject: นโยบายต้องระบุการนับผลในกรณี abstain
- Time windows: ช่วงเวลาสำหรับการโหวตและการอุทธรณ์ต้องกำหนดชัดเจน

Proposal Lifecycle

1. Draft: ผู้เสนอเตรียม Proposal พร้อมหลักฐานและวัตถุประสงค์
2. Review: Technical / Security / Economic / Governance reviews โดย Reviewer ที่เป็นอิสระ
3. Vote: การลงคะแนนโดยผู้มีสิทธิ์ตามโดเมน
4. Ratify: บันทึกการตัดสินใจ (signed decision) และเชื่อมโยงกับ Proposal ID
5. Implement: การนำไปปฏิบัติ (deployment plan + approvals แยกหน้าที่ชัดเจน)
6. Activate: Activation transaction/operation ที่ Validator ทำการตรวจสอบ
7. Verify: Runtime verification และการบันทึกหลักฐาน

Conflict of Interest

- ผู้เสนอไม่สามารถเป็นผู้อนุมัติขั้นสุดท้าย (COI-1)
- ผู้เขียนโค้ดห้ามตรวจรับโค้ดของตนเองเพียงลำพัง (COI-2)
- Reviewer ห้ามตรวจงานที่ตนมีผลประโยชน์โดยตรง (COI-3)

Audit & Evidence

- ทุก Proposal ต้องมีเลขอ้างอิงเฉพาะ (Proposal ID)
- ทุก Decision ต้องลงนาม/บันทึกหลักฐานและเชื่อมโยงกับ Proposal ID
- การเปิดใช้งานต้องบันทึก activation tx และ metadata ที่จำเป็น

Next steps

- ระบุค่าตัวเลขจริง (quorum, threshold) โดยอ้างอิง Compliance Framework
- กำหนดกฎการนับคะแนนเชิงเทคนิคและ token-based / stake-based voting model
