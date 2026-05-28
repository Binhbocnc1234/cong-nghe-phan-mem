# Đề thi ôn tập: Bài 1, Bài 3, Bài 4 và Bài 5 (Bộ câu hỏi số 2)

Đề thi này bao gồm các câu hỏi tự luận lý thuyết ("Vì sao") và thực hành ("Thực hành") được biên soạn dựa trên giáo trình chuẩn của Pressman, tuân thủ nghiêm ngặt nguyên tắc: **Không đưa Ví dụ/Phản ví dụ vào các luận điểm có giải thích đã quá rõ ràng và tường minh về mặt khái niệm**.

---

### Câu 1: Tại sao phần mềm không bị "hao mòn vật lý" (wear out) như phần cứng, nhưng thực tế chất lượng của nó vẫn bị suy giảm theo thời gian?

**Trả lời:**

* **Luận điểm 1: Bản chất phi vật lý của phần mềm ngăn cản sự hao mòn do môi trường cơ học.**
  * *Giải thích:* Phần mềm là một thực thể logic chứ không phải thực thể vật lý. Nó không chịu tác động của các yếu tố vật lý hay môi trường như ma sát, nhiệt độ, độ ẩm hoặc sự mỏi của vật liệu. Do đó, nếu môi trường vận hành không thay đổi, phần mềm hoạt động đúng ở lần đầu tiên sẽ luôn luôn hoạt động đúng như vậy ở các lần sau mà không chịu bất kỳ sự hao mòn cơ học nào.
  *(Luận điểm này đã giải thích rõ ràng về mặt khái niệm nên không cần ví dụ).*

* **Luận điểm 2: Chất lượng phần mềm suy giảm theo thời gian do hiện tượng "lão hóa phần mềm" (Software Aging) dưới tác động của các thay đổi liên tục.**
  * *Giải thích:* Khi phần mềm được đưa vào sử dụng, nó liên tục phải nhận các yêu cầu sửa đổi để vá lỗi, cập nhật tính năng mới hoặc thích ứng với môi trường hệ điều hành/phần cứng mới. Những sửa đổi vội vã này thường làm xáo trộn cấu trúc thiết kế ban đầu, tăng tính phức tạp của mã nguồn và tạo ra các phản ứng phụ ngoài ý muốn, dần dần làm giảm tính ổn định và chất lượng của hệ thống.
  * *Ví dụ cụ thể:* Trong một Game MOBA, hệ thống ban đầu được thiết kế để hiển thị bảng điểm (Scoreboard) đơn giản ở cuối trận. Khi có yêu cầu thêm tính năng hiển thị chi tiết chỉ số sát thương, vàng và số mạng hạ gục của từng thành viên, lập trình viên đã viết code chèn trực tiếp các hàm tính toán vào lớp giao diện hiển thị. Việc vá víu này khiến mã nguồn giao diện bị phình to, đan xen logic nghiệp vụ, dẫn tới việc sau này mỗi khi cập nhật đồ họa bảng điểm thì game lại bị tụt khung hình (FPS drop) nghiêm trọng hoặc hiển thị sai chỉ số của người chơi.

---

### Câu 2: Tại sao mô hình phát triển phần mềm lặp và tăng dần (Iterative and Incremental) lại vượt trội hơn mô hình Thác nước (Waterfall) truyền thống trong việc kiểm soát các thay đổi bất ngờ?

**Trả lời:**

* **Luận điểm 1: Chia nhỏ dự án thành các chu kỳ ngắn giúp thu hẹp phạm vi ảnh hưởng của thay đổi.**
  * *Giải thích:* Thay vì lên kế hoạch chi tiết cho toàn bộ vòng đời kéo dài nhiều năm như Thác nước, mô hình lặp chia nhỏ dự án thành các vòng lặp ngắn (vài tuần đến vài tháng). Bất kỳ yêu cầu thay đổi nào xuất hiện cũng chỉ ảnh hưởng đến kế hoạch của vòng lặp hiện tại hoặc được xếp vào vòng lặp kế tiếp, giúp nhóm phát triển dễ dàng thích ứng mà không làm đổ vỡ toàn bộ kế hoạch tổng thể.
  *(Luận điểm này đã giải thích rõ ràng nên không cần ví dụ).*

* **Luận điểm 2: Tích hợp và kiểm thử liên tục trong từng chu kỳ giúp phát hiện sớm các xung đột hệ thống.**
  * *Giải thích:* Trong mô hình lặp, mã nguồn được tích hợp và kiểm thử liên tục sau mỗi chu kỳ ngắn. Điều này giúp phát hiện ra các lỗi tương thích hoặc xung đột kiến trúc ngay lập tức, thay vì để tích tụ đến cuối dự án mới phát hiện như trong mô hình Thác nước.
  * *Ví dụ cụ thể:* Khi phát triển một tính năng mới là "Hệ thống bang hội" trong game MOBA. Nếu dùng mô hình lặp, ngay khi code xong tính năng trò chuyện trong bang hội ở tuần thứ 2, nhóm phát triển sẽ tích hợp và chạy thử nghiệm trên máy chủ. Họ phát hiện ngay lỗi nghẽn mạng do định dạng gói tin trò chuyện quá lớn $\rightarrow$ sửa lỗi ngay lập tức. Nếu dùng Thác nước, tính năng trò chuyện này sẽ đợi đến tháng thứ 12 mới được ghép nối với hệ thống mạng chung. Khi đó, nếu xảy ra nghẽn mạng, việc tìm ra nguyên nhân giữa hàng ngàn tính năng khác đã được lập trình là vô cùng khó khăn và tốn kém chi phí.

---

### Câu 3: Trong quy trình Scrum, tại sao việc ước lượng khối lượng công việc bằng điểm câu chuyện (Story Points) lại được khuyến khích hơn việc ước lượng bằng thời gian thực tế (Giờ hoặc Ngày làm việc)?

**Trả lời:**

* **Luận điểm 1: Story Points phản ánh độ phức tạp và rủi ro một cách khách quan, độc lập với năng lực cá nhân.**
  * *Giải thích:* Thời gian thực tế để hoàn thành một nhiệm vụ phụ thuộc rất lớn vào trình độ của lập trình viên (một Senior có thể chỉ mất 2 giờ để viết xong một API, trong khi một Junior có thể mất tới 2 ngày). Story Points đo lường kích thước tương đối, độ phức tạp và các yếu tố rủi ro của công việc. Do đó, điểm số này là thống nhất cho cả đội ngũ và không bị thay đổi bất kể ai là người thực hiện.
  *(Luận điểm này đã giải thích rõ ràng về mặt khái niệm nên không cần ví dụ).*

* **Luận điểm 2: Giảm bớt áp lực tâm lý và tăng độ chính xác trong lập kế hoạch dài hạn nhờ khái niệm Vận tốc (Velocity).**
  * *Giải thích:* Ước lượng bằng thời gian thường tạo ra áp lực đè nặng lên lập trình viên, dẫn đến xu hướng "đệm" thêm thời gian (buffer) để đề phòng rủi ro, làm sai lệch kế hoạch thực tế. Khi dùng Story Points, Scrum Master có thể tính toán được Vận tốc trung bình của nhóm (số Story Points trung bình nhóm hoàn thành được trong một Sprint). Từ đó, việc lập kế hoạch cho các Sprint sau sẽ dựa trên dữ liệu thực tế này, giúp dự báo tiến độ bàn giao sản phẩm chính xác hơn.
  *(Luận điểm này đã giải thích rõ ràng nên không cần ví dụ).*

---

### Câu 4: Tại sao việc khảo sát yêu cầu phần mềm không thể chỉ dựa vào phương pháp phỏng vấn (Interview) trực tiếp khách hàng, mà cần kết hợp với các kỹ thuật khác như quan sát (Observation) hoặc phân tích tài liệu (Document Analysis)?

**Trả lời:**

* **Luận điểm 1: Khách hàng thường gặp khó khăn trong việc nhớ và diễn tả đầy đủ quy trình làm việc thực tế hàng ngày của họ.**
  * *Giải thích:* Nhiều quy trình nghiệp vụ đã trở thành thói quen vô thức (tacit knowledge) của người dùng. Khi được hỏi trong phòng phỏng vấn, họ thường chỉ trả lời các luồng nghiệp vụ chính (happy path) và vô tình bỏ qua các bước nhỏ, các trường hợp ngoại lệ hoặc các quy tắc ngầm định, dẫn đến việc đặc tả yêu cầu bị thiếu sót nghiêm trọng.
  * *Ví dụ cụ thể:* Khi phỏng vấn người quản lý vận hành giải đấu game MOBA để xây dựng phần mềm "Quản lý Giải đấu", họ mô tả quy trình rất đơn giản: Đội đăng ký $\rightarrow$ Hệ thống xếp lịch $\rightarrow$ Đội thi đấu và nhập kết quả. Tuy nhiên, khi kỹ sư yêu cầu trực tiếp đến quan sát họ làm việc thực tế, họ mới thấy người quản lý phải xử lý các tình huống như: một đội đến muộn 15 phút thì phải xử thua như thế nào, hoặc hai đội trùng màu áo đấu thì trọng tài phải yêu cầu đổi màu ra sao. Đây là những yêu cầu nghiệp vụ cực kỳ quan trọng nhưng đã bị bỏ quên trong buổi phỏng vấn.

* **Luận điểm 2: Phỏng vấn dễ bị ảnh hưởng bởi thiên kiến cá nhân hoặc mong muốn chủ quan của người trả lời.**
  * *Giải thích:* Người được phỏng vấn có thể trả lời theo cách họ muốn quy trình diễn ra lý tưởng, hoặc trả lời dựa trên vị trí quyền lực của họ trong doanh nghiệp, thay vì phản ánh đúng thực tế vận hành hàng ngày của những nhân viên trực tiếp sử dụng phần mềm.
  *(Luận điểm này đã giải thích rõ ràng về mặt khái niệm nên không cần ví dụ).*

---

### Câu 5: (Thực hành) Hãy lấy ví dụ về một quy trình phát triển sản phẩm cụ thể tuân theo mô hình RUP (Rational Unified Process) qua 4 pha: Inception, Elaboration, Construction, Transition.

**Trả lời:**

* **Sản phẩm giả định:** Phát triển chức năng "Hệ thống Cửa hàng Trang phục (Skin Store)" cho một Game MOBA.

* **1. Pha Khởi đầu (Inception):**
  * *Mục tiêu:* Xác định phạm vi dự án, đánh giá tính khả thi và ước lượng chi phí/lợi ích ban đầu.
  * *Hoạt động cụ thể:*
    * Đội ngũ phát triển gặp gỡ Product Owner để làm rõ mục tiêu: Cửa hàng trang phục cần hỗ trợ hiển thị danh sách skin, cho phép mua bằng tiền trong game hoặc thẻ nạp, và có tính năng thử trang phục trước khi mua.
    * Xác định các rủi ro lớn: Rủi ro về bảo mật cổng thanh toán giao dịch và rủi ro về độ trễ khi tải hình ảnh 3D của trang phục.
    * Đầu ra: Tài liệu tầm nhìn sản phẩm (Vision Document) và các ca sử dụng cốt lõi (Core Use Cases).

* **2. Pha Tinh chế (Elaboration):**
  * *Mục tiêu:* Thiết kế kiến trúc nền tảng ổn định, giải quyết các rủi ro lớn nhất và đặc tả chi tiết hầu hết các yêu cầu.
  * *Hoạt động cụ thể:*
    * Kỹ sư thiết kế cấu trúc dữ liệu cho cửa hàng skin và viết mã nguồn chạy thử nghiệm (Architecture Prototype) kết nối thử tới cổng thanh toán ngân hàng/nhà mạng để triệt tiêu rủi ro bảo mật giao dịch.
    * Thiết kế giao diện chi tiết (UI/UX) cho màn hình chọn và thử skin 3D.
    * Đầu ra: Bản thiết kế kiến trúc hệ thống đã được xác minh (Executable Architecture Baseline) và tài liệu đặc tả yêu cầu chi tiết.

* **3. Pha Xây dựng (Construction):**
  * *Mục tiêu:* Phát triển toàn bộ các chức năng còn lại và tiến hành kiểm thử tích hợp.
  * *Hoạt động cụ thể:*
    * Lập trình viên tập trung viết code cho tất cả các chức năng: giỏ hàng, áp dụng mã giảm giá, lọc skin theo tướng, tặng skin cho bạn bè.
    * Đội ngũ QA tiến hành kiểm thử hộp đen, kiểm thử hiệu năng tải hình ảnh khi có nhiều người truy cập cửa hàng cùng lúc.
    * Đầu ra: Phiên bản beta của tính năng Cửa hàng trang phục hoạt động ổn định và sẵn sàng cho việc triển khai.

* **4. Pha Chuyển giao (Transition):**
  * *Mục tiêu:* Đưa sản phẩm đến tay người dùng cuối, đào tạo vận hành và sửa đổi các lỗi phát sinh cuối cùng.
  * *Hoạt động cụ thể:*
    * Phát hành bản cập nhật game MOBA chứa tính năng Cửa hàng trang phục lên các chợ ứng dụng (Google Play, App Store).
    * Hướng dẫn đội ngũ vận hành game cách cấu hình giá bán skin, thiết lập sự kiện giảm giá trên trang quản trị (Admin Dashboard).
    * Theo dõi phản hồi từ cộng đồng người chơi, tiến hành vá các lỗi hiển thị đồ họa phát sinh trên một số dòng máy điện thoại đặc thù.
    * Đầu ra: Tính năng hoạt động ổn định trong thực tế và dự án chính thức khép lại.
