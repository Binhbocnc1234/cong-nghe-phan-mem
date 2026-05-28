# Tài liệu ôn thi: Quy trình Thu thập và Phân tích Yêu cầu

---

## 1. Khung nhìn xoắn ốc của Quy trình Kỹ nghệ Yêu cầu (Spiral View)

*Quy trình xoắn ốc: [Không có trong sách]*

- **Lý thuyết:** Quy trình kỹ nghệ yêu cầu không phải là một chuỗi các bước tuyến tính mà là một tiến trình lặp qua nhiều vòng (loops) từ trong ra ngoài. Qua mỗi vòng lặp, tài liệu yêu cầu sẽ có mức độ chi tiết và hoàn thiện tăng dần.
  - **Các phân vùng (Sectors):** Vòng xoắn ốc đi qua 4 phân vùng hoạt động chính:
    1. *Khám phá yêu cầu (Requirements elicitation):* Tìm hiểu nhu cầu của các bên liên quan.
    2. *Đặc tả yêu cầu (Requirements specification):* Chuyển các yêu cầu thành văn bản/mô hình đặc tả chính thống.
    3. *Thẩm định yêu cầu (Requirements validation):* Kiểm tra tính đúng đắn và khả thi của yêu cầu.
    4. *Quản lý yêu cầu (Requirements management):* Kiểm soát và theo dõi các thay đổi yêu cầu (xuyên suốt vòng đời dự án).
  - **Các vòng xoáy lặp lại (Loops):**
    - *Vòng 1 (Feasibility Study):* Khảo sát và đánh giá dự án có khả thi hay đáng làm không. Đầu ra là Báo cáo khả thi (Feasibility report).
    - *Vòng 2 (User Requirements Elicitation & Specification):* Thu thập và viết đặc tả yêu cầu mức người dùng (User requirements document).
    - *Vòng 3 (System Requirements Elicitation, Specification & Modeling):* Thu thập, mô hình hóa và viết đặc tả chi tiết mức hệ thống. Đầu ra cuối cùng là Tài liệu yêu cầu phần mềm hoàn chỉnh (Software Requirements Document/SRS).
- **Ví dụ (Game MOBA):**
  - *Vòng 1 (Khảo sát khả thi):* Nhà phát hành thực hiện nghiên cứu: "Có khả thi không khi phát triển một game MOBA đồ họa 3D chạy trực tiếp trên trình duyệt WebGL với ngân sách 500k USD?". Kết quả chỉ ra dự án khả thi nếu giới hạn số lượng hiệu ứng ánh sáng phức tạp.
  - *Vòng 2 (Yêu cầu người dùng):* Đội ngũ phát triển gặp gỡ game thủ để lấy yêu cầu mức cao bằng ngôn ngữ tự nhiên: "Game thủ muốn có tính năng xem lại trận đấu (Replay) để học hỏi kỹ năng".
  - *Vòng 3 (Yêu cầu hệ thống):* Team Dev tiến hành phân tích kỹ thuật, mô hình hóa sơ đồ dữ liệu lưu trữ các gói tin di chuyển trong trận đấu, thiết kế cơ chế tua nhanh/chậm video replay ở Client và Server, từ đó viết thành đặc tả chi tiết và xuất bản tài liệu SRS chính thức của game.

---

## 2. Bảy nhiệm vụ cốt lõi của Quy trình Kỹ nghệ Yêu cầu (Theo giáo trình Pressman)

Khác với mô hình 4 bước trên slide, sách giáo trình (Software Engineering A Practitioner's Approach) định nghĩa quy trình kỹ nghệ yêu cầu bao gồm 7 nhiệm vụ (tasks) khác biệt. Dưới đây là chi tiết và các kỹ thuật liên quan:

**1. Khởi đầu (Inception)**
- **Lý thuyết:** Quá trình thiết lập sự hiểu biết cơ bản về vấn đề, xác định những người liên quan (stakeholders), hiểu bản chất vấn đề cần giải quyết và thiết lập giao tiếp ban đầu.
- **Ví dụ (Game MOBA):** Nhà phát hành game tổ chức cuộc họp ban đầu với đội ngũ Dev và các game thủ chuyên nghiệp để xác định nhu cầu cơ bản: "Chúng ta cần làm một chế độ chơi 3v3 trên một bản đồ nhỏ hơn để rút ngắn thời gian mỗi trận đấu".

**2. Thu thập / Khám phá yêu cầu (Elicitation)**
- **Lý thuyết:** Lấy thông tin từ các bên liên quan để tìm ra các yêu cầu chi tiết. Việc thu thập thường gặp khó khăn do vấn đề về phạm vi, vấn đề hiểu biết và vấn đề thay đổi. Trong quá trình khám phá yêu cầu, có 3 kỹ thuật chính thường được sử dụng:
  - *Phỏng vấn (Interviews):* Hỏi đáp trực tiếp (phỏng vấn đóng hoặc mở) với khách hàng/người dùng.
  - *Kịch bản / Ca sử dụng (Scenarios / Use Cases):* Mô tả chi tiết luồng công việc thực tế qua các tình huống sử dụng cụ thể.
  - *Nghiên cứu nhân học (Ethnography):* Quan sát thực tế người dùng làm việc hằng ngày để phát hiện các yêu cầu ẩn mà họ thường làm theo thói quen.
- **Ví dụ (Game MOBA):**
  - *Phỏng vấn:* Hỏi Game Designer: "Tướng khi ở trong bụi cỏ bao lâu thì kích hoạt tàng hình?".
  - *Kịch bản:* Xây dựng tình huống: "Người chơi mua trang bị -> Kiểm tra ô đồ -> Trừ vàng nếu hợp lệ -> Trả về lỗi nếu ô đồ đầy".
  - *Nghiên cứu nhân học:* Quan sát game thủ thấy họ hay đập mạnh phím khi combat -> Đưa ra yêu cầu tối ưu bộ đệm nhận phím bấm (key buffer) để không sót phím.

**3. Làm mịn / Phân tích (Elaboration)**
- **Lý thuyết:** Mở rộng và làm mịn các yêu cầu đã thu thập được thành các mô hình chi tiết (mô hình dữ liệu, mô hình chức năng, mô hình hành vi). Mục đích là để làm rõ cấu trúc và chức năng bên trong của hệ thống.
- **Ví dụ (Game MOBA):** Dựa trên yêu cầu nhặt cục máu ở bản đồ 3v3, đội ngũ kỹ thuật phân tích và thiết kế mô hình hành vi chi tiết: "Cục máu sẽ sinh ra mỗi 60 giây tại giữa bản đồ, hồi phục 20% máu tối đa cộng thêm 100 máu cố định, người chơi chỉ cần chạy lướt qua cục máu để kích hoạt".

**4. Thương lượng (Negotiation)**
- **Lý thuyết:** Các bên liên quan thường có những yêu cầu xung đột hoặc vượt quá khả năng về ngân sách/thời gian. Thương lượng là việc tìm ra tiếng nói chung, đánh đổi và gán độ ưu tiên cho các yêu cầu để có thể thực hiện được dự án một cách thực tế.
- **Ví dụ (Game MOBA):** Đội ngũ Marketing muốn "Thiết kế 10 loại cục máu với hiệu ứng hình ảnh 3D cực kỳ phức tạp khác nhau", nhưng đội Dev báo cáo "Việc này tốn 2 tháng, trong khi dự án chỉ còn 2 tuần". Hai bên thương lượng và chốt lại: "Chỉ làm 1 loại cục máu dùng chung để kịp ngày ra mắt".

**5. Đặc tả (Specification)**
- **Lý thuyết:** Chuyển dịch kết quả của quá trình thu thập và phân tích thành một tài liệu chính thức (như tài liệu SRS) hoặc các mô hình toán học/đồ họa có cấu trúc. Tài liệu này sẽ là bản hợp đồng kỹ thuật cho quá trình phát triển (lập trình, kiểm thử).
- **Ví dụ (Game MOBA):** Lập bảng đặc tả Use Case chi tiết cho việc nhặt cục máu: Tác nhân (Tướng), Điều kiện (Bản đồ 3v3, có cục máu xuất hiện), Luồng sự kiện (Tướng di chuyển vào bán kính 50 unit của cục máu -> Cục máu biến mất -> Hiệu ứng hồi máu kích hoạt -> Bắt đầu đếm ngược 60 giây sinh cục máu mới).

**6. Thẩm định (Validation)**
- **Lý thuyết:** Kiểm tra tài liệu đặc tả để đảm bảo các yêu cầu không bị lỗi, không mâu thuẫn, khả thi và phản ánh đúng những gì khách hàng mong đợi. Các kỹ thuật thẩm định chính gồm:
  - *Kiểm định yêu cầu (Requirements reviews):* Kiểm tra và phân tích thủ công.
  - *Làm bản mẫu (Prototyping):* Xây dựng mô hình thực thi được để kiểm tra tính khả thi và logic yêu cầu.
  - *Sinh ca kiểm thử (Test-case generation):* Tạo ca kiểm thử từ đặc tả để chứng minh yêu cầu có thể kiểm thử được.
- **Ví dụ (Game MOBA):**
  - *Kiểm định:* Đọc và rà soát lại tài liệu thiết kế bản đồ 3v3 xem có mâu thuẫn vị trí sinh lính không.
  - *Làm bản mẫu:* Làm một bản 2D Prototype của bụi cỏ ẩn thân để cho Game Designer test thử cơ chế che khuất tầm nhìn trước khi code 3D.
  - *Sinh ca kiểm thử:* Viết sẵn ca kiểm thử "Cho tướng đi vào bụi cỏ, kiểm tra xem biến tàng hình có chuyển thành True hay không".

**7. Quản lý yêu cầu (Requirements Management)**
- **Lý thuyết:** Tập hợp các hoạt động giúp nhóm dự án nhận diện, kiểm soát và theo dõi các thay đổi của yêu cầu trong suốt quá trình phát triển dự án phần mềm. Quản lý giúp phân tích tầm ảnh hưởng (Impact Analysis) và chi phí của mỗi sự thay đổi trước khi quyết định phê duyệt.
- **Ví dụ (Game MOBA):** Sau khi ra mắt bản thử nghiệm, người chơi cho rằng thời gian sinh cục máu 60 giây là quá lâu. Yêu cầu đổi thành 40 giây được tạo trên hệ thống Jira. Team quản lý kiểm tra xem đổi thời gian này có phá hỏng nhịp độ trận đấu hay các module khác không, sau đó mới phê duyệt thay đổi.
