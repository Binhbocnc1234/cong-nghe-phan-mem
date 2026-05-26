# Tài liệu ôn thi: Các Mô hình Phát triển Phần mềm

---

## 1. Luồng tiến trình (Process Flow)

**1. Khái niệm Luồng tiến trình**
- **Lý thuyết:** 5 hoạt động chính của kỹ nghệ phần mềm (Communication, Planning, Modeling, Construction, Deployment) có thể được sắp xếp và kết hợp theo 4 loại luồng tiến trình chính: Tuyến tính (Linear), Lặp lại (Iterative), Tiến hóa (Evolutionary), và Song song (Parallel).
- **Ví dụ (Game MOBA):** Nếu team làm game theo luồng Tuyến tính, họ sẽ thiết kế toàn bộ 100 vị tướng trên giấy (Modeling) rồi mới bắt tay vào code (Construction). Nếu theo luồng Lặp lại, họ code 1 tướng, test xong, rồi lặp lại quy trình với tướng thứ 2.

---

## 2. Mô hình Thác nước (Waterfall) và Chữ V (V-Model)

**1. Mô hình Thác nước**
- **Lý thuyết:** Là mô hình phát triển theo luồng tuyến tính. Các giai đoạn nối tiếp nhau tuần tự như thác nước chảy từ trên xuống. Chỉ thích hợp khi yêu cầu của khách hàng cực kỳ rõ ràng, không thay đổi và khách hàng có thể kiên nhẫn chờ đến cuối dự án mới thấy sản phẩm.
- **Ví dụ (Game MOBA):** Rất hiếm công ty làm game dùng mô hình Thác nước. Nếu dùng, nhà phát hành phải chốt chặt danh sách 50 tướng, cốt truyện, bản đồ từ ngày đầu. Team dev sẽ làm việc liên tục 3 năm, không thay đổi 1 dòng yêu cầu nào, và tung ra game hoàn chỉnh đúng ngày định trước.

**2. Mô hình chữ V (V-Model)**
- **Lý thuyết:** Là biến thể của mô hình Thác nước, nhưng tập trung cực mạnh vào việc Kiểm thử (Testing). Mỗi một bước thiết kế ở nửa bên trái chữ V sẽ tương ứng với một bước kiểm thử ở nửa bên phải chữ V. Giúp phát hiện lỗi từ sớm nhưng vẫn mang tính chất tuyến tính, khó đối phó với sự thay đổi.
- **Ví dụ (Game MOBA):** Khi thiết kế bộ kỹ năng tướng (nửa trái), team Tester ngay lập tức phải lên kịch bản test (Test cases) cho bộ kỹ năng đó (nửa phải). Phải xong xuôi khâu test trên giấy mới được chuyển sang code.

---

## 3. Mô hình Phát triển tăng dần (Incremental Model)

**1. Khái niệm và cách hoạt động**
- **Lý thuyết:** Phần mềm được chia nhỏ thành nhiều nhóm tính năng (increment). Mỗi nhóm tính năng sẽ được phát triển qua 5 hoạt động chuẩn và bàn giao sớm cho khách hàng. Bản demo đầu tiên chứa các tính năng cốt lõi (Core features), các bản sau bổ sung tính năng nâng cao.
- **Ví dụ (Game MOBA):** 
  - *Increment 1:* Hoàn thành tính năng đăng nhập và hệ thống di chuyển cơ bản -> Ra mắt bản Demo để người chơi test cảm giác di chuyển.
  - *Increment 2:* Thêm hệ thống sát thương và 5 vị tướng đầu tiên.
  - *Increment 3:* Thêm hệ thống cửa hàng mua vật phẩm trong trận.

---

## 4. Mô hình Phát triển tiến hóa (Evolutionary Model)

Mô hình tiến hóa thích hợp khi yêu cầu của khách hàng chưa rõ ràng và có nhiều thay đổi liên tục. Gồm 2 loại chính: Bản mẫu và Xoắn ốc.

**1. Mô hình Bản mẫu (Prototyping)**
- **Lý thuyết:** Khi khách hàng chỉ có ý tưởng chung chung, team sẽ làm thật nhanh một bản nháp (Prototype - có thể thiết kế rất "xấu" hoặc "stupid") để khách hàng chơi thử và hiểu rõ hơn về yêu cầu của chính họ. Sau đó mới đập đi để xây dựng hệ thống thật hoặc tiếp tục phát triển trên bản nháp đó.
- **Ví dụ (Game MOBA):** Khách hàng chưa hình dung được game MOBA chơi trên điện thoại vuốt chiêu sẽ như thế nào. Team Dev lấy các khối vuông (cube) đơn giản làm 1 bản game chạy được trong 1 tuần, cho khách hàng vuốt thử màn hình để chốt cơ chế điều khiển trước khi vẽ đồ họa thật.

**2. Mô hình Xoắn ốc (Spiral Model)**
- **Lý thuyết:** Dành cho các hệ thống phần mềm quy mô rất lớn, nơi rủi ro thất bại là cực kỳ cao. Quá trình phát triển là các vòng xoắn ốc lặp đi lặp lại. Điểm khác biệt lớn nhất là mỗi vòng lặp đều đòi hỏi phải có sự phân tích rủi ro cực kỳ kỹ lưỡng từ chuyên gia trước khi đi tiếp.
- **Ví dụ (Game MOBA):** Phát triển một dự án siêu phẩm AAA vốn 50 triệu USD. Vòng xoắn ốc 1 chỉ làm tài liệu. Vòng 2 làm demo. Ở mỗi vòng, team đều phải thuê chuyên gia phân tích rủi ro thị trường xem người chơi có còn thích MOBA không, đánh giá rủi ro công nghệ đồ họa mới có khả thi không rồi mới rót tiền làm tiếp.

---

## 5. Mô hình Phát triển dựa trên thành phần (Component-based Model)

**1. Khái niệm và lợi ích**
- **Lý thuyết:** Thay vì code mọi thứ từ đầu, mô hình này tận dụng việc tái sử dụng (Software reuse) các thành phần phần mềm (Component) đã được xây dựng sẵn. Mỗi thành phần là một khối có chức năng rõ ràng, giao diện giao tiếp chuẩn, giúp rút ngắn cực lớn thời gian phát triển.
- **Ví dụ (Game MOBA):** Để xây dựng tính năng trò chuyện bằng giọng nói (Voice Chat) trong game, team không tự code lại hệ thống truyền âm thanh từ đầu. Họ mua một Component Voice Chat có sẵn của bên thứ 3 (như Vivox) và cắm thẳng vào kiến trúc game hiện tại.
