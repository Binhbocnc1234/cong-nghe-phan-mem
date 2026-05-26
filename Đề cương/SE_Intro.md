# Tài liệu ôn thi: Các khái niệm cơ bản về Công nghệ Phần mềm

---

## 1. Sản phẩm phần mềm và Hệ thống thông tin

**1. Khái niệm Sản phẩm Phần mềm (Software)**
- **Lý thuyết:** Phần mềm không chỉ là những dòng code. Một sản phẩm phần mềm hoàn chỉnh bao gồm 3 yếu tố: Chương trình máy tính (mã nguồn, mã máy), Cấu trúc dữ liệu (giúp chương trình thao tác với thông tin), và Tài liệu (tài liệu kỹ thuật cho lập trình viên, tài liệu hướng dẫn cho người dùng).
- **Ví dụ (Game MOBA):** Sản phẩm game hoàn chỉnh bao gồm: Mã nguồn viết bằng C# (Chương trình), Database lưu thông tin cấp độ của người chơi (Cấu trúc dữ liệu), và Wiki/Hướng dẫn chơi game (Tài liệu).

**2. Hệ thống thông tin (Information System)**
- **Lý thuyết:** Phần mềm chỉ là một thành phần trong một Hệ thống thông tin lớn hơn. Một hệ thống thông tin bao gồm sự kết hợp của: Phần cứng, Phần mềm, Dữ liệu, Con người và Thủ tục (các quy tắc hoạt động).
- **Ví dụ (Game MOBA):** Hệ thống game bao gồm Server máy chủ (Phần cứng), Game Client (Phần mềm), Dữ liệu lịch sử đấu, Gamer và Admin (Con người), và các luật lệ xử phạt AFK (Thủ tục).

---

## 2. Đặc trưng và bản chất của Phần mềm

**1. Phần mềm không mòn cũ mà chỉ thoái hóa**
- **Lý thuyết:** Khác với phần cứng bị hỏng hóc vật lý theo thời gian, phần mềm không bao giờ bị "mòn". Tuy nhiên, nó sẽ bị "thoái hóa" do môi trường hệ điều hành thay đổi, nhu cầu người dùng đổi mới, và việc liên tục bảo trì/sửa mã nguồn sinh ra các lỗi mới (side effects).
- **Ví dụ (Game MOBA):** Game không bị xước xát vật lý, nhưng sau 5 năm nếu không nâng cấp đồ họa sẽ bị tụt hậu (thoái hóa) so với các game mới. Khi Dev thêm một vị tướng mới, code vô tình làm hỏng kỹ năng của các tướng cũ.

**2. Phần mềm được phát triển theo đơn đặt hàng, ít lắp ráp từ mẫu**
- **Lý thuyết:** Hầu hết phần mềm được xây dựng để đáp ứng yêu cầu riêng biệt của từng khách hàng hoặc tổ chức, do đó nó rất phức tạp, vô hình và mang tính chất cá nhân hóa cao.
- **Ví dụ (Game MOBA):** Dù trên thị trường có nhiều game, nhưng công ty vẫn phải tự thiết kế bộ kỹ năng, bản đồ và cân bằng tướng riêng biệt để tạo bản sắc, không thể cứ lấy râu ông này cắm cằm bà kia.

---

## 3. Tiêu chí của một phần mềm tốt (Theo chuẩn ISO 9126)

**1. Đứng từ góc độ Người dùng và Chủ đầu tư**
- **Lý thuyết:** Chủ đầu tư quan tâm đến việc phần mềm hoàn thành đúng thời gian, đúng kinh phí và dễ nâng cấp. Người dùng quan tâm đến tính khả dụng (dễ học, dễ dùng), tính chính xác và an toàn (bảo mật dữ liệu).
- **Ví dụ (Game MOBA):** Nhà phát hành (Chủ đầu tư) cần game ra mắt đúng hạn để bắt kịp xu hướng. Người chơi (Người dùng) cần game có giao diện dễ làm quen, chạy mượt mà không bị giật lag và không bị hack/cheat.

**2. Đứng từ góc độ Nhà phát triển (Mô hình chất lượng)**
- **Lý thuyết:** Theo ISO 9126, phần mềm tốt phải đảm bảo các tính chất: Tính năng, Tính tin cậy (chịu lỗi, phục hồi), Tính khả dụng, Tính hiệu quả (thời gian phản hồi, tốn ít tài nguyên), Khả năng bảo trì (dễ phân tích, dễ sửa), Tính khả chuyển (chạy được trên nhiều môi trường).
- **Ví dụ (Game MOBA):** Lập trình viên thiết kế kiến trúc game sao cho khi 1 server bị sập, hệ thống tự chuyển người chơi sang server khác mà không bị văng game (Tính chịu lỗi/Tin cậy), đồng thời viết code sạch để sau này dễ thêm tính năng mua trang phục (Dễ bảo trì).

---

## 4. Định nghĩa Kỹ nghệ phần mềm (Software Engineering - SE)

**1. Khái niệm SE**
- **Lý thuyết:** Kỹ nghệ phần mềm (SE) là việc thiết lập và sử dụng các nguyên lý công nghệ đúng đắn để tạo ra phần mềm một cách kinh tế (tiết kiệm), vừa tin cậy vừa hoạt động hiệu quả trên máy thực. Bốn lớp (layer) của SE bao gồm: Quality (chất lượng làm nền tảng), Process (quy trình), Method (phương pháp thực hiện quy trình), và Tool (công cụ hỗ trợ tự động hóa).
- **Ví dụ (Game MOBA):** Để đảm bảo game không có bug (Quality), team áp dụng quy trình Scrum (Process), dùng phương pháp lập trình hướng đối tượng (Method), và sử dụng công cụ Unity IDE kết hợp Github (Tool).

---

## 5. Khó khăn và Thách thức trong Phát triển Phần mềm

**1. Vấn đề về Yêu cầu và Sự thay đổi**
- **Lý thuyết:** Khách hàng thường "mù mờ" về chính sản phẩm họ muốn, dẫn đến yêu cầu liên tục thay đổi. Việc mô tả yêu cầu không đúng chuẩn sẽ sinh ra lỗi khi bàn giao.
- **Ví dụ (Game MOBA):** Nhà đầu tư lúc đầu yêu cầu làm game sinh tồn bắn súng, nhưng sau 6 tháng lại đổi ý muốn kết hợp cả yếu tố MOBA phá nhà. Sự thay đổi đột ngột này khiến team Dev phải đập đi làm lại phần lớn logic game.

**2. Thách thức về Chi phí bảo trì**
- **Lý thuyết:** Công việc bảo trì (sửa lỗi, nâng cấp sau khi đã phát hành) thường kéo dài và tiêu tốn chi phí gấp nhiều lần so với chi phí phát triển ban đầu (phát triển chỉ là phần nổi của tảng băng chìm).
- **Ví dụ (Game MOBA):** Việc code ra bản game đầu tiên tốn 10 tỷ VNĐ. Nhưng việc vận hành, cân bằng tướng hàng tháng, chống hack và ra mắt sự kiện trong 10 năm tiếp theo tiêu tốn tới 100 tỷ VNĐ.
