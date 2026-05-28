# Đề thi ôn tập: Bài 1, Bài 3, Bài 4 và Bài 5

Đề thi này bao gồm các câu hỏi dạng lý thuyết phân tích ("Vì sao") và câu hỏi thực hành ("Thực hành") được biên soạn dựa trên giáo trình chuẩn của Pressman, tuân thủ đúng định hướng tại tài liệu hướng dẫn `how-to-create-exam.md`.

---

### Câu 1: Tại sao việc áp dụng quy trình phần mềm (Software Process) chuẩn mực lại cần thiết, thay vì để các lập trình viên lập trình tự do theo mô hình Code-and-Fix?

**Luận điểm 1: Quy trình phần mềm giúp kiểm soát, dự báo và đảm bảo các mốc chất lượng của dự án.**
* *Giải thích:* Lập trình tự do (Code-and-Fix) là cách tiếp cận mà lập trình viên nhảy ngay vào viết code khi chưa phân tích kỹ lưỡng, gặp lỗi đến đâu sửa đến đó. Cách này thiếu khả năng dự báo và không có các cột mốc kiểm soát rủi ro. Quy trình phần mềm chuẩn mực cung cấp một khung công việc rõ ràng với các hoạt động bảo vệ (umbrella activities) như quản lý cấu hình, đảm bảo chất lượng phần mềm (SQA), giúp phát hiện và ngăn chặn rủi ro từ rất sớm.
* *Ví dụ cụ thể:* Khi phát triển một Game MOBA mới, nếu nhóm phát triển code tự do không theo quy trình, họ sẽ viết code tướng, code bản đồ một cách ngẫu hứng. Không có mốc kiểm thử chất lượng, đến khi tích hợp 10 vị tướng vào bản đồ chung, các xung đột mã nguồn xảy ra hàng loạt (crash game, mất đồng bộ mạng). Cả đội phải tốn hàng tháng trời chỉ để dò lỗi thủ công mà không thể xác định ngày phát hành game.

**Luận điểm 2: Quy trình phần mềm đảm bảo tính kế thừa, dễ bảo trì và hạn chế rủi ro khi có sự thay đổi nhân sự.**
* *Giải thích:* Một quy trình chuẩn mực yêu cầu sản sinh tài liệu (tài liệu thiết kế, đặc tả yêu cầu) và quy chuẩn viết mã (coding standards). Điều này giúp tri thức của dự án được lưu trữ lại một cách khách quan trên hệ thống, thay vì nằm hoàn toàn trong đầu của một vài cá nhân đơn lẻ. Khi có nhân sự nghỉ việc, người mới có thể dựa vào quy trình và tài liệu để tiếp quản công việc nhanh chóng.
* *Phản ví dụ:* Nếu áp dụng Code-and-Fix, mã nguồn là sản phẩm mang tính cá nhân cao và không có tài liệu đi kèm. Khi lập trình viên cốt lõi đảm nhận thuật toán "Ghép trận" (Matchmaking) nghỉ việc đột ngột, toàn bộ logic thuật toán nằm trong đầu anh ta. Người mới vào không thể hiểu nổi mớ code hỗn độn, buộc công ty phải đập đi viết lại toàn bộ hệ thống ghép trận từ đầu, gây lãng phí hàng trăm ngàn USD và làm chậm trễ tiến độ ra mắt sản phẩm.

---

### Câu 2: Tại sao mô hình làm bản mẫu (Prototyping) lại là lựa chọn phù hợp nhất khi khách hàng chưa rõ ràng về yêu cầu hệ thống ở giai đoạn đầu?

**Luận điểm 1: Bản mẫu trực quan hóa các yêu cầu mơ hồ thành giao diện tương tác thực tế.**
* *Giải thích:* Khách hàng thường gặp khó khăn trong việc mô tả chi tiết những gì họ muốn thông qua văn bản đặc tả khô khan. Làm bản mẫu (Prototyping) cung cấp một phiên bản thô sơ nhưng trực quan của hệ thống để khách hàng tương tác trực tiếp. Nhờ đó, khách hàng có thể kiểm chứng xem ý tưởng của họ khi chạy thực tế sẽ như thế nào, từ đó làm rõ những điểm họ thực sự mong muốn.
* *Ví dụ cụ thể:* Khách hàng muốn tích hợp hệ thống "Cửa hàng trang bị thông minh" tự động gợi ý trang bị cho người chơi trong game MOBA dựa trên tướng đối thủ. Do ý tưởng mới mẻ, họ không biết giao diện và luồng hoạt động nên thế nào. Đội phát triển đã xây dựng một bản mẫu giao diện bằng mô hình giấy tương tác (hoặc wireframe động) hiển thị nút gợi ý khi đối thủ lên đồ chí mạng. Khách hàng bấm thử và nhận ra ngay vị trí nút gợi ý quá nhỏ, khó thao tác khi đang chiến đấu, từ đó yêu cầu phóng to nút và đặt ở góc phải màn hình.

**Luận điểm 2: Giảm thiểu rủi ro xây dựng sai sản phẩm và tiết kiệm chi phí sửa đổi ở các giai đoạn sau.**
* *Giải thích:* Phát hiện sai sót về mặt yêu cầu trong quá trình xây dựng bản mẫu tốn rất ít chi phí vì đây chỉ là bản nháp, chưa được lập trình sâu bên dưới (backend). Nếu đợi đến khi toàn bộ hệ thống được code hoàn thiện mới phát hiện ra yêu cầu bị sai lệch, chi phí sửa chữa sẽ tăng lên gấp hàng chục đến hàng trăm lần do phải sửa đổi cả cấu trúc dữ liệu lẫn kiến trúc hệ thống.
* *Phản ví dụ:* Nếu không làm bản mẫu mà trực tiếp code hệ thống Cửa hàng trang bị thông minh dựa trên mô tả mơ hồ ban đầu. Sau 6 tháng phát triển hệ thống AI phân tích dữ liệu đối thủ phức tạp, khi bàn giao sản phẩm hoàn chỉnh, khách hàng thốt lên: "Giao diện này quá rối mắt và tính năng này làm mất đi tính chiến thuật tự tay lên đồ của game MOBA!". Toàn bộ dự án phải đập bỏ và thiết kế lại từ đầu, gây lãng phí cực kỳ lớn cho nhà phát triển.

---

### Câu 3: Trong quy trình Scrum, tại sao một người không nên kiêm nhiệm đồng thời vai trò Product Owner (PO) và Scrum Master (SM)?

**Luận điểm 1: Xung đột lợi ích cốt lõi giữa mục tiêu kinh doanh của PO và sự bảo vệ quy trình/con người của SM.**
* *Giải thích:* Product Owner (PO) đại diện cho giá trị sản phẩm và khách hàng, luôn muốn đội ngũ làm được nhiều tính năng nhất có thể trong thời gian ngắn nhất (tập trung vào *Cái gì* và *Khi nào*). Trong khi đó, Scrum Master (SM) có nhiệm vụ bảo vệ quy trình, hỗ trợ nhóm phát triển, đảm bảo nhóm làm việc với tốc độ bền vững, không bị quá tải và duy trì chất lượng code (tập trung vào *Như thế nào*). Sự kiêm nhiệm sẽ triệt tiêu cơ chế phản biện lành mạnh này, khiến người kiêm nhiệm dễ có xu hướng ép nhóm phát triển làm việc quá sức để đạt mục tiêu kinh doanh.
* *Ví dụ cụ thể:* Trong một Sprint phát triển tính năng "Đấu giải đấu hàng tuần" cho game MOBA. Gần đến ngày bàn giao, đối tác yêu cầu thêm gấp tính năng "Bảng xếp hạng bang hội" vào Sprint hiện tại. Với tư cách PO, người kiêm nhiệm muốn đưa ngay tính năng này vào Sprint để làm hài lòng đối tác. Với tư cách SM, lẽ ra họ phải bảo vệ Dev Team khỏi việc quá tải, nhưng vì xung đột vai trò, họ quyết định ép Dev Team tăng ca. Kết quả là game ra mắt đúng hạn nhưng phát sinh hàng loạt lỗi nghiêm trọng (bugs) trong trận đấu khiến máy chủ sập liên tục.

**Luận điểm 2: Làm mất đi vai trò trung gian giải quyết xung đột khách quan trong đội ngũ.**
* *Giải thích:* Scrum Master đóng vai trò như một trọng tài khách quan để giải quyết các bất đồng giữa Product Owner (người yêu cầu) và Dev Team (người thực hiện kỹ thuật). Nếu SM cũng chính là PO, tiếng nói chuyên môn và những khó khăn kỹ thuật của Dev Team sẽ không có ai đứng ra bảo vệ một cách công tâm, khiến quy trình Scrum bị biến tướng thành mô hình quản lý mệnh lệnh áp đặt từ trên xuống.

---

### Câu 4: Tại sao trong đặc tả yêu cầu, ta cần phân biệt rõ ràng Yêu cầu chức năng (Functional Requirements) và Yêu cầu phi chức năng (Non-functional Requirements)? Hệ quả nếu vi phạm yêu cầu phi chức năng cốt lõi là gì?

**Luận điểm 1: Hai nhóm yêu cầu định hình hai khía cạnh hoàn toàn khác nhau của hệ thống (Hành vi vs. Chất lượng vận hành).**
* *Giải thích:* Yêu cầu chức năng (FR) mô tả các dịch vụ, chức năng cụ thể mà hệ thống bắt buộc phải thực hiện để đáp ứng tác vụ của người dùng (trả lời câu hỏi: *"Hệ thống làm được gì?"*). Yêu cầu phi chức năng (NFR) mô tả các ràng buộc về mặt chất lượng, hiệu năng, bảo mật, độ trễ hoặc khả năng mở rộng của hệ thống (trả lời câu hỏi: *"Hệ thống thực hiện chức năng đó tốt đến mức nào?"*).
* *Ví dụ cụ thể:* Trong game MOBA:
  * Yêu cầu chức năng (FR): *"Người chơi có thể thực hiện ca sử dụng 'Tấn công thường' để gây sát thương vật lý lên tướng đối thủ"*.
  * Yêu cầu phi chức năng (NFR): *"Thời gian phản hồi từ lúc người chơi chạm nút đánh thường trên màn hình điện thoại đến khi hoạt ảnh nhân vật hiển thị hoạt động không được vượt quá 50 miligiây (ms)"* (NFR về hiệu năng/độ trễ).

**Luận điểm 2: Vi phạm yêu cầu phi chức năng cốt lõi sẽ khiến phần mềm hoàn toàn vô dụng dù chức năng có chạy đúng.**
* *Giải thích:* Người dùng cuối thường chỉ tập trung vào yêu cầu chức năng mà bỏ quên yêu cầu phi chức năng. Tuy nhiên, nếu hệ thống không đáp ứng được các ràng buộc phi chức năng (như bảo mật thông tin, độ trễ, khả năng chịu tải), người dùng sẽ không thể sử dụng được các chức năng đó một cách bình thường, dẫn tới sự thất bại hoàn toàn của sản phẩm.
* *Phản ví dụ:* Nhóm phát triển game MOBA xây dựng xong chức năng "Đấu Xếp Hạng" chạy rất đúng logic (FR chạy tốt). Tuy nhiên, họ bỏ qua yêu cầu phi chức năng về khả năng chịu tải của máy chủ. Khi game ra mắt, chỉ cần 5.000 người đăng nhập đồng thời là ping của tất cả người chơi tăng vọt lên 999ms, gây mất kết nối liên tục. Dù chức năng đấu rank có hoàn hảo đến đâu, người chơi cũng không thể chơi nổi một trận đấu trọn vẹn và sẽ ngay lập tức xóa game.

---

### Câu 5: (Thực hành) Hãy viết 3 User Stories hoàn chỉnh cho một chức năng cụ thể của Game MOBA (ví dụ: Hệ thống Chọn tướng) đảm bảo tuân thủ tiêu chuẩn INVEST.

* **Chức năng lựa chọn:** Hệ thống chọn tướng trước trận đấu trong game MOBA.

#### User Story 1: Tìm kiếm tướng theo tên
* **Nội dung:** *"Là một người chơi trong phòng chuẩn bị trận đấu, tôi muốn tìm kiếm tướng bằng cách gõ tên vào ô tìm kiếm, để tôi có thể nhanh chóng chọn được vị tướng mình muốn chơi trước khi hết thời gian đếm ngược."*
* **Tiêu chuẩn nghiệm thu (Acceptance Criteria - AC):**
  1. Khi người chơi gõ các chữ cái đầu tiên (ví dụ: "Va"), danh sách tướng lập tức lọc ra các tướng khớp (như Valhein, Vane).
  2. Nếu gõ tên không có trong danh sách tướng sở hữu hoặc tướng miễn phí tuần, hệ thống hiển thị thông báo "Không tìm thấy tướng phù hợp".
  3. Thời gian hiển thị kết quả lọc phải dưới 0.1 giây từ khi người chơi dừng gõ phím.
* **Đánh giá tiêu chuẩn INVEST:**
  * *Independent (Độc lập):* Độc lập với việc khóa tướng hay áp dụng trang phục.
  * *Negotiable (Có thể thương lượng):* Có thể thương lượng về cách lọc (lọc theo tên hoặc lọc theo vị trí).
  * *Valuable (Giá trị):* Giúp người chơi tiết kiệm thời gian chọn tướng trong giới hạn 30 giây của phòng chờ.
  * *Estimatable (Ước lượng được):* Dev ước lượng được độ phức tạp (thuật toán filter chuỗi đơn giản).
  * *Small (Nhỏ):* Nhỏ gọn, hoàn thành được trong 1-2 ngày.
  * *Testable (Kiểm thử được):* Tester có thể test trực tiếp bằng cách gõ ký tự và đếm số tướng hiển thị.

#### User Story 2: Lọc tướng theo vai trò chiến thuật
* **Nội dung:** *"Là một người chơi trong phòng chuẩn bị trận đấu, tôi muốn lọc danh sách tướng theo vai trò chiến thuật (Đỡ đòn, Sát thủ, Pháp sư, Xạ thủ...), để tôi dễ dàng tìm thấy vị tướng phù hợp với đội hình đang thiếu của đồng đội."*
* **Tiêu chuẩn nghiệm thu (Acceptance Criteria - AC):**
  1. Hệ thống cung cấp các nút tab đại diện cho các vai trò tướng ở phía trên danh sách tướng.
  2. Khi người chơi bấm vào tab "Xạ thủ", danh sách chỉ hiển thị các tướng có vai trò chính hoặc phụ là xạ thủ.
  3. Người chơi có thể kết hợp vừa bấm tab vai trò vừa gõ tên tướng ở ô tìm kiếm.
* **Đánh giá tiêu chuẩn INVEST:** Đạt các tiêu chí tương tự (Độc lập, tạo giá trị cao cho việc phối hợp chiến thuật đội hình, dễ ước lượng và kiểm thử).

#### User Story 3: Khóa tướng đã chọn
* **Nội dung:** *"Là một người chơi đã chọn tướng, tôi muốn xác nhận khóa tướng đó lại, để hệ thống ghi nhận lựa chọn của tôi và cho phép các đồng đội khác biết tôi chắc chắn sẽ chơi vị tướng này."*
* **Tiêu chuẩn nghiệm thu (Acceptance Criteria - AC):**
  1. Nút "Khóa" chỉ sáng lên và cho phép bấm sau khi người chơi đã bấm chọn một vị tướng cụ thể trong danh sách.
  2. Sau khi bấm nút "Khóa", vị tướng đó sẽ bị khóa cứng (không thể đổi sang tướng khác) và avatar tướng của người chơi hiển thị trạng thái "Đã khóa" cho đồng đội nhìn thấy.
  3. Nếu hết thời gian đếm ngược (30 giây) mà người chơi chưa bấm nút "Khóa" nhưng đã chọn một tướng, hệ thống sẽ tự động khóa vị tướng đó. Nếu người chơi chưa chọn tướng nào, hệ thống tự động khóa một vị tướng ngẫu nhiên phù hợp với vị trí còn thiếu trong đội hình.
* **Đánh giá tiêu chuẩn INVEST:** Độc lập với bước tìm kiếm/lọc, có giá trị nghiệp vụ cốt lõi, nhỏ gọn và hoàn toàn kiểm thử được hành vi đếm ngược thời gian để tự động khóa.
