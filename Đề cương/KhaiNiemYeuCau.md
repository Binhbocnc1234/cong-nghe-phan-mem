# Tài liệu ôn thi: Thu thập và Phân tích Yêu cầu

---

## 1. Khái niệm cơ bản về Yêu cầu Phần mềm

**1. Định nghĩa Yêu cầu Phần mềm**
- **Lý thuyết:** Yêu cầu phần mềm (Requirement) là các mô tả (từ mức chung chung đến chi tiết) về các dịch vụ/chức năng mà hệ thống phải cung cấp cùng với các ràng buộc đi kèm đối với sự phát triển và vận hành của hệ thống đó.
- **Ví dụ (Game MOBA):** Một yêu cầu cơ bản trong game là: "Hệ thống phải cho phép người chơi chọn vị tướng của mình trong phòng chờ (dịch vụ), và quá trình chọn tướng phải kết thúc trong vòng 60 giây (ràng buộc)".

**2. Phân loại Yêu cầu**
Yêu cầu phần mềm được phân chia thành 3 loại chính:

- **Yêu cầu chức năng (Functional Requirements):**
  - **Lý thuyết:** Mô tả các dịch vụ hay tính năng cụ thể mà hệ thống phải thực hiện, cách hệ thống phản ứng với các đầu vào xác định, và trong một số trường hợp là cả những gì hệ thống không được làm.
  - **Ví dụ (Game MOBA):** Hệ thống phải cung cấp chức năng "Tìm trận" (Matchmaking) để tự động ghép 10 người chơi có cùng bậc xếp hạng (Rank) vào một trận đấu 5v5.
- **Yêu cầu miền (Domain Requirements):**
  - **Lý thuyết:** Các ràng buộc đối với hệ thống xuất phát từ chính lĩnh vực ứng dụng (miền hoạt động) đặc thù của phần mềm, chứ không phải từ yêu cầu trực tiếp của người dùng. Nếu không thỏa mãn yêu cầu miền, hệ thống có thể không hoạt động được.
  - **Ví dụ (Game MOBA):** Trong miền game MOBA, hệ thống tính điểm kinh nghiệm (XP) phải tuân thủ quy tắc: "Khi một lính hoặc tướng địch bị tiêu diệt, lượng XP thu được sẽ được chia đều cho tất cả các tướng đồng minh đứng trong phạm vi bán kính 800 đơn vị khoảng cách".
- **Yêu cầu phi chức năng (Non-functional Requirements):**
  - **Lý thuyết:** Các ràng buộc về dịch vụ hoặc chức năng do hệ thống cung cấp (như thời gian phản hồi, bảo mật, độ tin cậy, quy trình phát triển, các tiêu chuẩn). Yêu cầu phi chức năng thường áp dụng cho toàn bộ hệ thống chứ không riêng lẻ từng tính năng. Nếu các yêu cầu này không được thỏa mãn, toàn bộ hệ thống có thể trở thành vô dụng.
  - **Ví dụ (Game MOBA):** Để đảm bảo tính công bằng và trải nghiệm thi đấu eSports, độ trễ kết nối (ping) giữa thiết bị của người chơi và máy chủ game phải duy trì ổn định dưới 50ms trong suốt trận đấu.

**3. Cây phân loại Yêu cầu phi chức năng (Trích xuất từ Slide 05 - Trang 13)**
Yêu cầu phi chức năng được phân cấp chi tiết thành 3 nhóm lớn: **Yêu cầu sản phẩm**, **Yêu cầu tổ chức**, và **Yêu cầu bên ngoài**.

- **A. Yêu cầu sản phẩm (Product Requirements):** Đặt ra các ràng buộc về hành vi vận hành hoặc các thuộc tính chất lượng của sản phẩm phần mềm.
  - **Yêu cầu về tính khả dụng / dễ dùng (Usability Requirements):**
    - **Lý thuyết:** Ràng buộc liên quan đến độ dễ học, dễ thao tác của giao diện người dùng để người dùng cuối có thể sử dụng hệ thống hiệu quả.
    - **Ví dụ (Game MOBA):** Giao diện điều khiển (nút di chuyển joystick và các nút tung chiêu) phải được bố trí trực quan để người chơi mới có thể nắm bắt và thực hiện thành thạo các thao tác di chuyển, tấn công trong vòng dưới 5 phút ở phần chơi hướng dẫn tân thủ (Tutorial).
  - **Yêu cầu về tính hiệu quả (Efficiency Requirements) - gồm Hiệu năng và Bộ nhớ:**
    - **Yêu cầu hiệu năng (Performance Requirements):**
      - **Lý thuyết:** Đo lường tốc độ phản hồi, thời gian xử lý và năng lực chịu tải của hệ thống.
      - **Ví dụ (Game MOBA):** Hệ thống máy chủ đăng nhập phải xử lý được ít nhất 10,000 yêu cầu đăng nhập của người chơi trong mỗi giây vào khung giờ cao điểm mà không xảy ra tình trạng tắc nghẽn.
    - **Yêu cầu không gian bộ nhớ/lưu trữ (Space Requirements):**
      - **Lý thuyết:** Giới hạn dung lượng bộ nhớ (RAM, ROM, ổ cứng) mà phần mềm được phép chiếm dụng khi cài đặt hoặc vận hành.
      - **Ví dụ (Game MOBA):** Ứng dụng game client khi chạy trên điện thoại di động không được tiêu tốn vượt quá 1.5 GB dung lượng bộ nhớ RAM ở mức thiết lập đồ họa mặc định.
  - **Yêu cầu về độ tin cậy (Dependability Requirements):**
    - **Lý thuyết:** Ràng buộc về độ ổn định, khả năng sẵn sàng phục vụ và tỷ lệ xảy ra lỗi của hệ thống.
    - **Ví dụ (Game MOBA):** Tỷ lệ crash game (ứng dụng tự thoát đột ngột) trong trận đấu phải nhỏ hơn 0.1% trên tổng số trận đấu diễn ra hàng ngày.
  - **Yêu cầu về tính bảo mật (Security Requirements):**
    - **Lý thuyết:** Khả năng bảo vệ dữ liệu, chống lại các truy cập trái phép và ngăn chặn các hành vi gian lận phá hoại hệ thống.
    - **Ví dụ (Game MOBA):** Hệ thống phải tích hợp phần mềm chống gian lận (Anti-cheat) chạy nền để tự động phát hiện và ngăn chặn các công cụ can thiệp vào bộ nhớ game (như hack map, hack hồi chiêu) trong vòng 5 giây từ khi chúng kích hoạt.

- **B. Yêu cầu tổ chức (Organizational Requirements):** Xuất phát từ chính sách, tiêu chuẩn hoặc quy trình làm việc nội bộ của tổ chức khách hàng hoặc tổ chức phát triển.
  - **Yêu cầu về môi trường (Environmental Requirements):**
    - **Lý thuyết:** Ràng buộc về sự tương thích với cơ sở hạ tầng phần cứng, phần mềm hoặc hệ thống mạng sẵn có của tổ chức.
    - **Ví dụ (Game MOBA):** Cơ sở dữ liệu lưu trữ lịch sử đấu của game phải được triển khai trên hạ tầng điện toán đám mây Amazon Web Services (AWS) để đồng bộ với hệ thống hạ tầng sẵn có của công ty phát hành.
  - **Yêu cầu về vận hành (Operational Requirements):**
    - **Lý thuyết:** Các ràng buộc liên quan đến quy trình vận hành, bảo trì, giám sát và phân phối phần mềm khi đưa vào hoạt động thực tế.
    - **Ví dụ (Game MOBA):** Hệ thống máy chủ game phải hỗ trợ việc cập nhật các bản vá lỗi nóng (hot-fix) hoặc cập nhật cân bằng tướng mà không cần phải đóng máy chủ dừng game (zero-downtime deployment).
  - **Yêu cầu về phát triển (Development Requirements):**
    - **Lý thuyết:** Ràng buộc về công cụ phát triển, ngôn ngữ lập trình, tiêu chuẩn viết mã nguồn hoặc mô hình quy trình phần mềm được áp dụng.
    - **Ví dụ (Game MOBA):** Toàn bộ mã nguồn của game Client phải được phát triển trên Game Engine Unity bằng ngôn ngữ C# để đảm bảo đội ngũ kỹ sư hiện tại của công ty có thể tiếp nhận và bảo trì dễ dàng.

- **C. Yêu cầu bên ngoài (External Requirements):** Ràng buộc do các yếu tố nằm ngoài hệ thống và ngoài tổ chức phát triển áp đặt lên.
  - **Yêu cầu về đạo đức (Ethical Requirements):**
    - **Lý thuyết:** Đảm bảo hệ thống không vi phạm các giá trị đạo đức, văn hóa và chuẩn mực xã hội chung.
    - **Ví dụ (Game MOBA):** Hệ thống lọc chat trong game phải tự động ẩn đi hoặc thay thế bằng ký tự "*" đối với các từ ngữ tục tĩu, lăng mạ, phân biệt chủng tộc để đảm bảo môi trường chơi game lành mạnh.
  - **Yêu cầu về quản lý / quy định (Regulatory Requirements):**
    - **Lý thuyết:** Tuân thủ các thông tư, quyết định hoặc quy chế quản lý chuyên ngành từ các cơ quan quản lý nhà nước.
    - **Ví dụ (Game MOBA):** Theo quy định quản lý game trực tuyến của cơ quan nhà nước, hệ thống phải tích hợp tính năng giới hạn giờ chơi (hiển thị cảnh báo và giảm 100% phần thưởng nhận được sau khi chơi quá 180 phút/ngày đối với tài khoản của người chơi dưới 18 tuổi).
  - **Yêu cầu về luật pháp / pháp lý (Legislative Requirements) - gồm Kế toán và An toàn/bảo mật:**
    - **Yêu cầu về kế toán / giao dịch tài chính (Accounting Requirements):**
      - **Lý thuyết:** Đảm bảo hệ thống xử lý giao dịch tiền tệ tuân thủ đúng các quy định về hóa đơn, thuế và tài chính quốc gia.
      - **Ví dụ (Game MOBA):** Hệ thống cửa hàng bán trang phục (Skins) trong game phải tự động ghi nhận doanh thu và tính thuế giá trị gia tăng (VAT) cho mỗi giao dịch nạp thẻ để phục vụ công tác báo cáo thuế theo luật định.
    - **Yêu cầu về an toàn / bảo mật thông tin (Safety/security Requirements):**
      - **Lý thuyết:** Đảm bảo an toàn tuyệt đối cho thông tin cá nhân và quyền riêng tư của người dùng theo quy định pháp luật.
      - **Ví dụ (Game MOBA):** Hệ thống lưu trữ dữ liệu người chơi phải tuân thủ nghiêm ngặt Luật An ninh mạng và Nghị định bảo vệ dữ liệu cá nhân (GDPR của Châu Âu hoặc Nghị định 13/2023/NĐ-CP của Việt Nam), không được tự ý chia sẻ thông tin đăng ký của game thủ cho bất kỳ bên thứ ba nào.

**4. Bốn thuộc tính cốt lõi cần đạt được của Yêu cầu Phần mềm (Slide 05 - Trang 14, 15, 16)**
Để đảm bảo chất lượng tài liệu và khả năng hiện thực hóa, các yêu cầu phần mềm cần đạt được 4 thuộc tính cốt lõi sau:

- **Tính chính xác (Accuracy / Precision):**
  - **Lý thuyết:** Các yêu cầu phải được mô tả rõ ràng, chính xác, không mơ hồ hay nhập nhằng để tránh việc người phát triển và khách hàng hiểu theo những cách khác nhau, dẫn đến cài đặt sai chức năng.
  - **Ví dụ (Game MOBA):**
    - *Mô tả thiếu chính xác (nhập nhằng):* "Game có tính năng tìm kiếm tướng."
    - *Mô tả chính xác:* "Trong phòng trưng bày tướng, hệ thống phải cho phép người chơi tìm kiếm tướng bằng cách nhập ký tự tên tướng hoặc lọc theo các vai trò bao gồm: Đỡ đòn, Đấu sĩ, Pháp sư, Xạ thủ, Sát thủ, Hỗ trợ."
- **Tính đầy đủ (Completeness):**
  - **Lý thuyết:** Tài liệu yêu cầu phải mô tả đầy đủ mọi chức năng, dịch vụ mà khách hàng mong muốn và các ràng buộc đi kèm mà không bỏ sót bất kỳ chi tiết nghiệp vụ quan trọng nào.
  - **Ví dụ (Game MOBA):** Khi đặc tả tính năng "Treo máy (AFK) trong trận đấu", tài liệu yêu cầu phải mô tả đầy đủ: cách hệ thống nhận diện trạng thái AFK (người chơi không di chuyển/tung chiêu quá 2 phút), hình phạt (trừ điểm uy tín, cấm tìm trận trong 15 phút), và cơ chế cho phép đồng đội bầu chọn hủy trận đấu mà không bị trừ điểm rank.
- **Tính nhất quán (Consistency):**
  - **Lý thuyết:** Các yêu cầu không được mâu thuẫn hay xung đột lẫn nhau. Trong thực tế, đối với các hệ thống lớn, rất khó để đạt được cả tính đầy đủ và tính nhất quán cùng một lúc trong tài liệu yêu cầu.
  - **Ví dụ (Game MOBA):** 
    - *Không nhất quán (Mâu thuẫn):* Yêu cầu 1 ghi "Game phải chạy mượt mà ở mức ổn định 60 FPS trên mọi điện thoại đời cũ RAM 2GB". Yêu cầu 2 lại ghi "Game phải bật hiệu ứng bóng đổ thời gian thực và ánh sáng động độ phân giải cao cho tất cả các tướng". Máy RAM 2GB không thể gánh nổi đồ họa phức tạp này ở mức 60 FPS.
- **Tính đo được / Kiểm chứng được (Measurability / Verifiability):**
  - **Lý thuyết:** Các yêu cầu phi chức năng cần phải được lượng hóa bằng các chỉ số hoặc tiêu chí cụ thể để có thể đo lường và kiểm tra xem hệ thống có thực sự thỏa mãn yêu cầu đó hay không khi nghiệm thu. Tránh dùng các từ mơ hồ như "nhanh", "dễ dùng", "mượt".
  - **Ví dụ (Game MOBA):**
    - *Không đo được:* "Game phải tải màn hình trận đấu thật nhanh."
    - *Đo được:* "Thời gian tải bản đồ trận đấu (Loading screen) từ lúc kết thúc phòng chờ chọn tướng đến khi người chơi vào trận không được vượt quá 15 giây đối với thiết bị có kết nối mạng từ 10 Mbps trở lên."

---

## 2. Tài liệu yêu cầu và Đặc tả

**1. Tài liệu yêu cầu (Requirements Document)**
- **Lý thuyết:** Là phát biểu chính thống về những gì hệ thống cần làm. Thường tập trung trả lời câu hỏi **"Cái gì?" (What)** thay vì "Như thế nào? (How)". Một chuẩn phổ biến là chuẩn tài liệu IEEE SRS (Software Requirements Specification) bao gồm: Giới thiệu, Mô tả chung, Đặc tả chi tiết, Phụ lục.
- **Ví dụ (Game MOBA):** Tài liệu SRS của game sẽ ghi "Hệ thống cần cung cấp tính năng Tố cáo người chơi phá game". Tài liệu này chỉ dừng ở mức yêu cầu, KHÔNG đi sâu vào việc sẽ code tính năng tố cáo đó bằng ngôn ngữ gì hay dùng database nào.

**2. Các hình thức Đặc tả yêu cầu**
- **Lý thuyết:** Có thể dùng ngôn ngữ tự nhiên (dễ hiểu nhưng dễ nhập nhằng), ngôn ngữ tự nhiên có cấu trúc (điền theo form/bảng biểu để bớt nhập nhằng), ngôn ngữ mô tả đồ họa (UML), hoặc mô hình toán học hình thức.
- **Ví dụ (Game MOBA):** Sử dụng ngôn ngữ cấu trúc (bảng biểu) để đặc tả luật trừ điểm rank: 
  - *Điều kiện:* AFK quá 5 phút -> *Hành động:* Trừ 50 điểm uy tín.
  - *Điều kiện:* AFK dưới 2 phút -> *Hành động:* Gửi cảnh báo.
