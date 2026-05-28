# Tài liệu ôn thi: Unified Process (UP)

---

## 1. UP là gì?

**Unified Process Framework (UP)** ra đời vào những năm 1990, đi kèm với sự phát triển của hệ thống hướng đối tượng và ngôn ngữ mô hình hóa chung UML.

- **UP là một framework:** Tức là UP không phải một quy trình cụ thể, cứng nhắc, mà có thể tinh chỉnh tùy theo dự án và tổ chức.
- Các quy trình phần mềm phổ biến dựa trên UP: 
  - **Rational Unified Process (RUP)** – do IBM tạo ra.
  - **OpenUP**.
  - **Agile Unified Process**.

**Đặc trưng của Unified Process (UP):**
1. **Lặp đi lặp lại (Iterative):** Một pha có thể thực hiện lặp đi lặp lại. Ví dụ: trong dự án lớn, pha Construction có thể lặp tới 10 lần.
2. **Tăng dần (Incremental):** Mỗi vòng lặp (iteration) có thể phát hành 1 increment (gồm 1 tập các tính năng).
3. **Tập trung vào thiết kế:** Sử dụng UML với nhiều mô hình thiết kế khác nhau (mỗi mô hình có góc nhìn riêng biệt). Kết hợp lại cho ta cái nhìn tổng thể về hệ thống.
4. **Tập trung vào nhận diện và quản lý rủi ro:** Rủi ro được nhận diện sớm ở pha Inception và làm rõ hơn ở pha Elaboration.

---

## 2. Chu kỳ (Cycle) và 4 pha của UP

- **1 dự án = nhiều cycle.** Output của 1 cycle là 1 bản release hoàn chỉnh cho khách hàng.
- **1 cycle = 4 pha chính:** Inception (bắt đầu), Elaboration, Construction, Transition (kết thúc).
- **1 pha = nhiều vòng lặp (iterations).** Pha nào càng nhiều iteration thì pha đó càng phức tạp hoặc khối lượng công việc càng lớn.

> **Lưu ý về chi phí:** Trong 1 cycle, pha **Construction là pha tốn nhiều chi phí nhất** (resources cao nhất), trong khi pha **Elaboration là quan trọng nhất** (định hình kiến trúc và rủi ro).

### 2.1 Inception (Khởi tạo)

Bản chất của pha Inception là **Giao tiếp với Khách hàng (Communication)** và **Lập kế hoạch (Planning)**. Dựa theo lý thuyết cốt lõi (theo sách Pressman), các công việc chính và ví dụ tương ứng như sau:

**1. Nhận diện các thực thể bên ngoài (Actors) và định nghĩa tương tác (Use cases)**
- **Lý thuyết:** Xác định rõ những ai hoặc hệ thống nào (con người, hệ thống khác) sẽ tương tác với phần mềm. Đồng thời, định nghĩa sơ bộ các tương tác cơ bản (Use cases) mà các thực thể này sẽ thực hiện.
- **Ví dụ (Game MOBA):** 
  - *Nhận diện thực thể (Actors):* Người chơi, Admin game, Cổng thanh toán App Store/Google Play (hệ thống bên thứ 3).
  - *Định nghĩa tương tác:* Người chơi "Đăng nhập", "Tìm trận"; Admin "Khóa tài khoản".
- **Ví dụ (App đặt đồ ăn):** 
  - *Nhận diện thực thể (Actors):* Khách hàng, Nhà hàng, Shipper, Hệ thống cổng thanh toán VNPay.
  - *Định nghĩa tương tác:* Khách hàng thực hiện "Đặt đồ ăn"; Nhà hàng thực hiện "Xác nhận đơn"; VNPay "Xử lý giao dịch".

**2. Đề xuất tài liệu mô tả yêu cầu nghiệp vụ cơ bản**
- **Lý thuyết:** Thu thập các yêu cầu nghiệp vụ cốt lõi từ khách hàng để xác định phạm vi tổng thể, trả lời câu hỏi "Phần mềm giải quyết bài toán gì và giới hạn ở đâu?".
- **Ví dụ (Game MOBA):**
  - *Yêu cầu nghiệp vụ:* Ứng dụng là một game thi đấu đối kháng trực tuyến 5v5 phá hủy nhà chính.
  - *Phạm vi giới hạn:* Chỉ tập trung vào chế độ PvP (người với người), không làm chế độ PvE (đi ải) cốt truyện.
- **Ví dụ (App đặt đồ ăn):**
  - *Yêu cầu nghiệp vụ:* Ứng dụng kết nối khách mua đồ ăn với nhà hàng và tài xế để giao tận nơi.
  - *Phạm vi giới hạn:* Hệ thống chỉ quản lý đơn hàng và theo dõi vận chuyển, KHÔNG bao gồm module quản lý kho nguyên liệu hay quản lý nhân sự của nhà hàng.

**3. Đề xuất bản thiết kế hệ thống ở mức sơ khai (Rough Architecture)**
- **Lý thuyết:** Phác thảo cấu trúc tổng thể bằng việc chỉ ra các hệ thống con (sub-systems) hoặc chức năng cơ bản nhất cấu thành nên sản phẩm, chưa đi vào chi tiết kỹ thuật sâu hay lớp (class).
- **Ví dụ (Game MOBA):** Kiến trúc sơ khai gồm Client Game (chạy trên thiết bị người chơi), Dedicated Match Server (xử lý logic trận đấu), và Database Server (lưu trữ tài khoản, lịch sử đấu).
- **Ví dụ (App đặt đồ ăn):** Kiến trúc sơ khai được chia làm 3 hệ thống con: Mobile App (giao diện cho Khách và Shipper), Web Portal (giao diện cho Nhà hàng), và Central Server (Backend trung tâm điều phối dữ liệu).

**4. Lập kế hoạch dự án và Đánh giá tính khả thi (Feasibility & Planning)**
- **Lý thuyết:** Đánh giá tính khả thi của dự án (kinh doanh, kỹ thuật). Ước lượng tài nguyên (nhân sự, thời gian, chi phí) và nhận diện các rủi ro tiềm ẩn lớn nhất có thể ảnh hưởng đến lịch trình phát hành.
- **Ví dụ (Game MOBA):**
  - *Khả thi & Tài nguyên:* Cần team 50 người (Dev, Artist, Game Designer) làm trong 2 năm, chi phí 20 tỷ VNĐ.
  - *Nhận diện rủi ro:* Rủi ro kỹ thuật lớn nhất là giật lag (latency) khi có 10 người chơi đồng thời ở các quốc gia khác nhau.
  - *Lịch trình (Schedule):* Cuối năm 1 ra mắt tướng cơ bản, giữa năm 2 test nội bộ, cuối năm 2 release.
- **Ví dụ (App đặt đồ ăn):**
  - *Khả thi & Tài nguyên:* Đánh giá khả thi với chi phí 2 tỷ VNĐ, team 10 người phát triển trong 6 tháng.
  - *Nhận diện rủi ro:* Rủi ro kỹ thuật lớn nhất là làm sao tracking định vị Shipper realtime mà không làm hao pin điện thoại quá nhanh.
  - *Lịch trình (Schedule):* Cuối tháng 2 xong bản Demo luồng đặt hàng, tháng 6 release bản chính thức.

---

### 2.2 Elaboration (Làm mịn)

Bản chất của pha Elaboration là **Lập kế hoạch và Mô hình hóa (Planning & Modeling)** để làm mịn yêu cầu và chốt kiến trúc. 

**1. Làm mịn các nghiệp vụ và mở rộng yêu cầu (Refine Requirements)**
- **Lý thuyết:** Phân tích sâu hơn các yêu cầu đã đề xuất ở Inception, làm rõ tất cả các kịch bản ngoại lệ (alternative flows) và chi tiết hóa các luồng nghiệp vụ.
- **Ví dụ (Game MOBA):**
  - *Làm mịn nghiệp vụ:* Chi tiết hóa luồng ghép trận (Matchmaking). Khi người chơi ấn "Tìm trận", hệ thống quét 9 người khác có rank chênh lệch không quá 1 bậc. Nếu 1 người từ chối, 9 người kia trở lại hàng chờ ưu tiên.
- **Ví dụ (App đặt đồ ăn):**
  - *Làm mịn nghiệp vụ:* Chi tiết hóa luồng hủy đơn. Nếu khách hủy khi nhà hàng chưa nhận đơn -> hoàn tiền ngay. Nếu hủy khi shipper đang giao -> khách chịu phí 100%.

**2. Thiết kế và làm mịn kiến trúc (Refine Architecture)**
- **Lý thuyết:** Thiết kế kiến trúc phần mềm chi tiết ra thành nhiều khung nhìn khác nhau và tạo ra 5 loại mô hình UML (Use case model, Requirements model, Design model, Implementation model, Deployment model).
- **Ví dụ (Game MOBA):**
  - *Thiết kế kiến trúc:* Quyết định dùng Unity Engine cho Client, Node.js + WebSocket cho Real-time Server. Thiết kế Data model gồm bảng `Player`, `MatchHistory`, `HeroStats`.
- **Ví dụ (App đặt đồ ăn):**
  - *Thiết kế kiến trúc:* Mobile App dùng Flutter, Backend REST API dùng Spring Boot, Database dùng PostgreSQL kết hợp Redis để cache danh mục món ăn.

**3. Hoàn thiện bản kế hoạch và xác nhận tính khả thi (Finalize Plan)**
- **Lý thuyết:** Dựa trên kiến trúc chi tiết, cập nhật lại bản kế hoạch dự án. Xử lý hoặc đưa ra giải pháp kỹ thuật cho các rủi ro lớn đã nhận diện ở Inception. Nếu không khả thi thì phải điều chỉnh hoặc hủy dự án.
- **Ví dụ (Game MOBA):**
  - *Giải quyết rủi ro:* Để giải quyết rủi ro giật lag, quyết định sử dụng thuật toán dự đoán chuyển động (Client-side prediction) thay vì chờ server phản hồi.
- **Ví dụ (App đặt đồ ăn):**
  - *Giải quyết rủi ro:* Để tránh hao pin Shipper do bật GPS liên tục, quyết định giảm tần suất update location xuống 10 giây/lần.

---

### 2.3 Construction (Xây dựng)

*Đây là pha tốn nhiều Resources (chi phí) nhất trong toàn bộ Cycle.* Bản chất của pha là **Viết mã nguồn (Coding)** và **Kiểm thử (Testing)**.

**1. Viết mã nguồn (Coding / Implementation)**
- **Lý thuyết:** Lập trình viên tiến hành viết code để tạo ra các tính năng. Thường chia thành các vòng lặp nhỏ (iterations), mỗi vòng lặp phát hành 1 phần mềm có thêm tính năng chạy được (Increment).
- **Ví dụ (Game MOBA):**
  - *Code chức năng:* Vòng lặp 1 (C1) code hệ thống đăng nhập và di chuyển cơ bản. Vòng lặp 2 (C2) code hệ thống tính sát thương và kỹ năng tướng.
- **Ví dụ (App đặt đồ ăn):**
  - *Code chức năng:* Vòng lặp 1 (C1) code API đăng nhập và giỏ hàng. Vòng lặp 2 (C2) code giao diện bản đồ theo dõi shipper.

**2. Kiểm thử đơn vị và Kiểm thử tích hợp (Unit & Integration Testing)**
- **Lý thuyết:** Kiểm thử đơn vị (Unit Test) để đảm bảo từng hàm, class, package hoạt động đúng độc lập. Kiểm thử tích hợp (Integration Test) kiểm tra tính tương thích giữa các thành phần khi ghép nối.
- **Ví dụ (Game MOBA):**
  - *Unit test:* Test hàm `TakeDamage(100)`: HP của Hero phải giảm đúng 100 trừ đi điểm giáp bảo vệ hiện có.
  - *Integration test:* Client gửi lệnh dùng kỹ năng -> Server nhận, tính toán -> Server broadcast lại cho 9 Client khác hiển thị hiệu ứng.
- **Ví dụ (App đặt đồ ăn):**
  - *Unit test:* Test hàm tính tổng tiền giỏ hàng bao gồm cả thuật toán áp mã giảm giá 20%.
  - *Integration test:* Khách bấm "Đặt hàng" trên App -> Backend lưu Database -> Bắn Notification sang máy tính bảng của Nhà hàng thành công.

**3. Kiểm thử chấp nhận (Acceptance Testing)**
- **Lý thuyết:** Đánh giá phần mềm dựa trên các yêu cầu nghiệp vụ đã chốt với khách hàng từ pha Elaboration xem có đáp ứng đúng mong đợi không.
- **Ví dụ (Game MOBA):**
  - *Test chấp nhận:* Đưa cho Game Tester chơi thử 1 trận 5v5 đầy đủ từ lúc tìm trận đến khi phá nhà chính để xem nhịp độ trận đấu có đúng thiết kế không.
- **Ví dụ (App đặt đồ ăn):**
  - *Test chấp nhận:* Đưa app cho nhân viên Business dùng điện thoại cá nhân thử đặt 1 ly trà sữa thật để kiểm tra toàn bộ luồng.

---

### 2.4 Transition (Chuyển giao / Deployment)

Bản chất của pha Transition là **Đưa sản phẩm đến tay người dùng thực tế (Deployment)**.

**1. Thực hiện kiểm thử Beta (Beta Testing)**
- **Lý thuyết:** Phát hành phần mềm trong một môi trường thực tế (giới hạn) cho người dùng thật sử dụng. Việc này giúp tìm ra những lỗi ẩn mà đội ngũ test nội bộ (Alpha) không phát hiện được.
- **Ví dụ (Game MOBA):**
  - *Beta test:* Phát hành bản Closed Beta cho 10,000 người chơi. Qua đó phát hiện ra lỗi server bị sập khi cả 10 người cùng dùng chiêu cuối (Ultimate) tại 1 vị trí.
- **Ví dụ (App đặt đồ ăn):**
  - *Beta test:* Thử nghiệm app giới hạn tại 1 quận nội thành. Phát hiện ra lỗi định vị bản đồ bị lệch so với số nhà thực tế 20 mét trong hẻm sâu.

**2. Cập nhật và chuyển giao tài liệu cho Khách hàng**
- **Lý thuyết:** Cung cấp tài liệu hướng dẫn sử dụng, đào tạo người dùng cách dùng phần mềm và chuyển giao hệ thống.
- **Ví dụ (Game MOBA):**
  - *Tài liệu & Chuyển giao:* Tạo phần chơi Hướng dẫn tân thủ (Tutorial) tích hợp trong game. Phát hành bản Patch Notes liệt kê các tướng được thay đổi sức mạnh.
- **Ví dụ (App đặt đồ ăn):**
  - *Tài liệu & Chuyển giao:* Soạn file PDF tài liệu HDSD và tổ chức buổi training trực tiếp cho các chủ nhà hàng cách dùng máy POS để nhận đơn.

---

## 3. 6 hoạt động (Disciplines/Workflows) trong 1 Iteration

1 vòng lặp (iteration) thường có các hoạt động con (diễn ra xuyên suốt dự án nhưng mức độ tập trung thay đổi theo thời gian):

1. **Business Modeling (Mô hình hóa nghiệp vụ):** Hiểu tổ chức/doanh nghiệp đang hoạt động thế nào.
2. **Requirements (Yêu cầu):** Thu thập, phân tích và đặc tả yêu cầu.
3. **Analysis & Design (Phân tích & thiết kế):** Chuyển yêu cầu thành kiến trúc và các mô hình UML.
4. **Implementation (Cài đặt):** Viết code.
5. **Test (Kiểm thử):** Kiểm thử đơn vị, tích hợp, hệ thống, chấp nhận, beta, v.v.
6. **Deployment (Triển khai):** Đưa sản phẩm ra môi trường thật.

*(Lưu ý: 5 hoạt động Communication, Planning, Modeling, Construction, Deployment có thể dùng để mô tả mọi quy trình PTPM, kể cả UP).*

---

## 4. Đồ thị của 6 hoạt động

Đồ thị thể hiện **mức độ tập trung công việc (effort)** của mỗi hoạt động qua 4 pha.

```
Effort
   ^
   |   BM    REQ    A&D    IMP    TEST    DEPL
   |
I  |   ****   ****   **     *      *       .
E  |   ***    ***    ****   ***    **      .
C  |   **     *      **     *****  ****    **
T  |   *      .      *      **     ****    ****
   +------------------------------------------> Time
     I       E       C                T
```

### 4.1 Business Modeling & Requirements
- **Cao nhất ở Inception và Elaboration**, giảm mạnh sau đó. Phải khảo sát kỹ doanh nghiệp và chốt yêu cầu ở đầu dự án.

### 4.2 Analysis & Design
- **Bắt đầu ở Inception, cao nhất ở Elaboration**, giảm dần. Elaboration là pha chính để thiết kế kiến trúc nền tảng và các mô hình UML.

### 4.3 Implementation
- **Ít ở đầu, đỉnh điểm ở Construction, giảm ở cuối.** Construction là pha viết code hàng loạt.

### 4.4 Test
- **Có từ đầu, tăng dần, cao nhất ở Construction và Transition.** Đầu dự án test đơn vị/prototype, cuối dự án test tích hợp/beta/chấp nhận.

### 4.5 Deployment
- **Tăng dần, cao nhất ở Transition.** Sản phẩm gần hoàn chỉnh mới deploy lên môi trường thật.

---

## 5. Tóm tắt dễ nhớ — Mẹo ôn thi

### Chu kỳ và 4 pha — "I E C T"

| Pha | Bản chất & Key idea | Output chính |
|-----|-------------------|--------------|
| **I**nception | Giao tiếp & Lập KH (Làm hay không?) | Kế hoạch sơ bộ, yêu cầu sơ bộ |
| **E**laboration | Lập KH & Mô hình hóa (Kiến trúc?) | 5 Mô hình UML, Plan hoàn chỉnh |
| **C**onstruction| Viết code & Test (Tốn chi phí nhất) | Mã nguồn, sản phẩm chạy được |
| **T**ransition  | Beta test & Release | Phản hồi KH, HDSD |

### Key insight — Xu hướng trên đồ thị

```
BM & REQ          → Giảm dần (đầu nhiều, cuối ít)
A&D               → Đỉnh ở Elaboration
IMP               → Đỉnh ở Construction (tốn Resource nhất)
TEST & DEPL       → Tăng dần (cuối nhiều nhất)
```
