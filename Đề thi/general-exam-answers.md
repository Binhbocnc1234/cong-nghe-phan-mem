# Trả lời Đề thi (General Exam)

Dưới đây là phần trả lời chi tiết cho các câu hỏi trong đề thi `general-exam.md`, đã được giải lại theo khung hướng dẫn tại `how-to-create-exam.md`, sử dụng các ví dụ thực tế cụ thể và sinh động (như Game MOBA) và lược bỏ Câu 6 theo yêu cầu.

---

### Câu 1: Lầm tưởng của lập trình viên và chi phí trong vòng đời phát triển phần mềm

**Luận điểm 1: Lập trình viên nhầm lẫn giữa "sản phẩm chạy được trên môi trường thử nghiệm" và "hệ thống sẵn sàng vận hành thực tế".**
* *Giải thích:* Trong giai đoạn học tập hoặc làm các bài tập nhỏ, lập trình viên thường chỉ cần mã nguồn biên dịch thành công và vượt qua một số ca kiểm thử (test cases) cố định là đã hoàn thành công việc. Điều này tạo nên thói quen bỏ qua các khía cạnh cực kỳ quan trọng khác của một sản phẩm phần mềm như: hiệu năng tải cao, tính bảo mật, giao diện người dùng tối ưu, tài liệu kỹ thuật và khả năng mở rộng code.
* *Ví dụ cụ thể:* Một lập trình viên viết xong chức năng "Ghép trận" (Matchmaking) cho một Game MOBA mới. Chạy thử nghiệm giả lập cục bộ với 10 người chơi thấy kết nối mượt mà và chuyển hướng vào phòng chờ bình thường. Lập trình viên cho rằng công việc đã xong. Thế nhưng khi phát hành thực tế, dưới áp lực của 100.000 người chơi truy cập cùng lúc, thuật toán ghép trận bị tắc nghẽn, máy chủ quá tải và treo hệ thống liên tục. Do mã nguồn không được viết tài liệu hướng dẫn và cấu trúc rối rắm, các lập trình viên khác trong đội cũng không thể hỗ trợ tối ưu hóa nhanh, gây thiệt hại nghiêm trọng cho nhà phát hành.

**Luận điểm 2: Sự thay đổi liên tục của môi trường vận hành phần mềm theo thời gian.**
* *Giải thích:* Khác với các công trình vật lý tĩnh như cầu đường hay tòa nhà, phần mềm là một thực thể động luôn chịu tác động từ sự thay đổi công nghệ bên ngoài. Hệ điều hành được cập nhật, phần cứng thay đổi, các thư viện liên kết cập nhật phiên bản mới, và các lỗ hổng bảo mật mới liên tục phát lộ buộc phần mềm phải thay đổi để tồn tại. Code chạy đúng ở thời điểm bàn giao không đảm bảo sẽ hoạt động tốt sau vài tháng.
* *Ví dụ cụ thể:* Game MOBA Liên Quân Mobile hoạt động hoàn hảo trên hệ điều hành iOS 14. Tuy nhiên, khi Apple phát hành iOS 15 với cơ chế quản lý bộ nhớ và cấp quyền truy cập mạng nghiêm ngặt hơn, game bắt đầu gặp hiện tượng giật lag và tự động đóng ứng dụng đột ngột (crash) khi đang tải trận. Nhóm phát triển không thể từ chối trách nhiệm với lý do "năm ngoái game đã chạy được", họ phải ngay lập tức phân tích xung đột hệ điều hành để phát hành bản vá tương thích mới.

**Luận điểm 3: Giai đoạn có chi phí lớn nhất trong vòng đời phần mềm là Bảo trì (Maintenance Phase).**
* *Giải thích:* Theo thống kê thực tế trong Kỹ nghệ phần mềm (sách Pressman), chi phí cho giai đoạn bảo trì chiếm khoảng 60% đến 80% tổng chi phí của cả vòng đời phát triển phần mềm. Sự chênh lệch này xuất phát từ việc các giai đoạn phân tích, thiết kế, lập trình chỉ diễn ra trong vài tháng đến vài năm đầu, trong khi giai đoạn bảo trì (bao gồm: sửa lỗi phát sinh, nâng cấp thích ứng môi trường mới, cải tiến chức năng theo yêu cầu thị trường) kéo dài suốt hàng chục năm vận hành sản phẩm.
* *Phản ví dụ:* Nếu một nhà phát triển game MOBA cắt bỏ toàn bộ chi phí bảo trì ngay sau khi game ra mắt thành công phiên bản 1.0 (cho rằng game chạy được là xong). Chỉ sau 3-6 tháng, game sẽ tràn ngập các công cụ hack/cheat (như hack map, sửa file cài đặt để tăng sát thương), phát sinh hàng loạt lỗi hiển thị với các dòng điện thoại mới, và mất hoàn toàn tính cạnh tranh do không có tướng hay chế độ chơi mới. Dự án nhanh chóng bị người chơi quay lưng và sụp đổ hoàn toàn.

---

### Câu 2: Sự phù hợp của Mô hình Tăng dần (Incremental) so với Thác nước (Waterfall) khi cần bản dùng thử sớm

**Luận điểm 1: Mô hình Tăng dần bàn giao sản phẩm chạy được rất sớm thông qua việc chia nhỏ hệ thống thành các phân đoạn (Increments).**
* *Giải thích:* Mô hình Tăng dần chia hệ thống thành các phần tăng trưởng độc lập, trong đó phân đoạn đầu tiên (Increment 1) luôn tập trung hoàn thiện các tính năng cốt lõi (Core Product). Khách hàng có thể cài đặt và sử dụng thực tế ngay phân đoạn này để phản hồi. Ngược lại, mô hình Thác nước (Waterfall) đi theo luồng tuyến tính chặt chẽ từ trên xuống dưới; khách hàng phải đợi đến pha cuối cùng của toàn bộ dự án mới được nhìn thấy sản phẩm thật, dù các yêu cầu có rõ ràng ngay từ đầu đi chăng nữa.
* *Ví dụ cụ thể:* Khi phát triển một Game MOBA mới:
  * *Theo mô hình Tăng dần:* Tại Increment 1 (sau 3 tháng phát triển), đội ngũ bàn giao bản chạy thử nghiệm nội bộ gồm 3 vị tướng cơ bản, bản đồ 5v5 tối giản và cơ chế di chuyển/đánh thường. Khách hàng lập tức có thể đăng nhập chơi thử để cảm nhận độ nhạy của nút điều khiển.
  * *Theo mô hình Thác nước:* Khách hàng phải đợi tới tháng thứ 18 để được chơi thử, vì dự án bắt buộc phải hoàn thành việc thiết kế chi tiết tất cả 50 vị tướng, vẽ xong tất cả hiệu ứng đồ họa 3D phức tạp, và lập trình tất cả tính năng rồi mới bắt đầu đóng gói sản phẩm.

**Luận điểm 2: Bản dùng thử sớm giúp phát hiện sớm các "điểm mù" về trải nghiệm thực tế mà văn bản đặc tả không thể mô tả hết.**
* *Giải thích:* Dù các yêu cầu ban đầu được ghi chép rõ ràng đến đâu, con người luôn bị giới hạn trong việc hình dung hoạt động của phần mềm chỉ qua việc đọc tài liệu giấy. Việc cho phép khách hàng tương tác với một prototype/increment hoạt động thực tế giúp họ nhanh chóng phát hiện ra các bất hợp lý trong thiết kế và đưa ra các thay đổi kịp thời khi chi phí sửa sai còn thấp.
* *Ví dụ cụ thể:* Tài liệu yêu cầu ghi rất rõ: "Camera tự động di chuyển bám sát nhân vật". Tuy nhiên, khi khách hàng chơi thử bản Increment 1 của game MOBA, họ nhận thấy camera bám quá sát và xoay nhanh mỗi khi tướng lướt đi, gây cảm giác chóng mặt cho người chơi (UX tệ). Nhờ phát hiện sớm khi game mới ở giai đoạn core, lập trình viên chỉ mất 2 ngày để sửa lại thuật toán làm mượt camera.
* *Phản ví dụ (Thác nước):* Nếu sử dụng Thác nước, khách hàng chỉ phát hiện ra vấn đề camera gây chóng mặt này ở tháng thứ 18 khi nhận bàn giao. Lúc này, toàn bộ mã nguồn của các chiêu thức lướt, hiệu ứng bay nhảy của 50 tướng đã được lập trình cứng dựa trên hệ thống camera cũ. Việc sửa đổi camera lúc này sẽ kéo theo sửa đổi cấu trúc đồ họa diện rộng, tốn hàng tháng trời và tăng chi phí lên gấp nhiều lần.

**Luận điểm 3: Duy trì sự gắn kết và lòng tin của khách hàng đối với dự án.**
* *Giải thích:* Khách hàng sẽ cảm thấy yên tâm và hài lòng hơn rất nhiều khi thấy dự án liên tục có tiến triển thực tế qua từng tháng, các ý kiến đóng góp của họ được cập nhật trực tiếp vào các Increment tiếp theo. Thác nước giống như một "hộp đen" kéo dài nhiều tháng, khách hàng hoàn toàn không biết đội phát triển đang làm gì, dễ dẫn đến tâm lý lo âu và thiếu tin tưởng. 
*(Lưu ý: Luận điểm này rõ ràng nên không cần ví dụ minh họa).*

---

### Câu 3: Sự khác biệt về tính bắt buộc/tùy chọn giữa mối quan hệ `<<include>>` và `<<extend>>` trong Biểu đồ ca sử dụng (Use Case Diagram)

**Luận điểm 1: Mối quan hệ `<<include>>` thể hiện tính bắt buộc tuyệt đối.**
* *Giải thích:* Trong biểu đồ ca sử dụng, `<<include>>` (Bao gồm) chỉ ra rằng hành vi của ca sử dụng bị bao gồm (included use case) là một phần không thể thiếu để hoàn thành mục tiêu của ca sử dụng cơ sở (base use case). Mỗi khi ca sử dụng cơ sở được thực thi, ca sử dụng bị bao gồm **bắt buộc** phải chạy.
* *Ví dụ cụ thể:* Trong Game MOBA Liên Quân Mobile, khi người chơi thực hiện ca sử dụng "Đấu Xếp Hạng", hệ thống bắt buộc phải thực hiện ca sử dụng "Tìm trận" (Matchmaking). Người chơi không có cách nào tham gia đấu rank mà không đi qua bước tìm trận của hệ thống.

**Luận điểm 2: Mối quan hệ `<<extend>>` thể hiện tính tùy chọn hoặc phụ thuộc điều kiện.**
* *Giải thích:* Mối quan hệ `<<extend>>` (Mở rộng) chỉ ra rằng ca sử dụng mở rộng (extending use case) chỉ được chèn vào luồng hoạt động của ca sử dụng cơ sở dưới những điều kiện cụ thể (Extension Points). Khi điều kiện này không thỏa mãn, ca sử dụng cơ sở vẫn hoạt động bình thường mà không cần gọi đến ca sử dụng mở rộng.
* *Ví dụ cụ thể:* Trong ca sử dụng "Chọn Tướng" trước trận đấu, người chơi có thể thực hiện ca sử dụng mở rộng "Áp dụng Trang phục (Skin)". Hành động này là tùy chọn: nếu người chơi có trang phục và muốn sử dụng thì họ chọn, còn nếu không có trang phục, họ vẫn hoàn thành việc chọn tướng để vào trận đấu bình thường.

**Luận điểm 3: Thiết kế sai mối quan hệ gây phá vỡ logic nghiệp vụ của hệ thống.**
* *Giải thích:* Việc nhầm lẫn giữa hai mối quan hệ này trên sơ đồ thiết kế sẽ dẫn tới việc lập trình viên cài đặt sai quy trình nghiệp vụ của phần mềm, biến những tính năng tùy chọn thành rào cản bắt buộc hoặc ngược lại.
* *Phản ví dụ:* Nếu nhà thiết kế biểu đồ đặt mối quan hệ giữa "Chọn Tướng" và "Áp dụng Trang phục" là `<<include>>` thay vì `<<extend>>`. Lập trình viên sẽ viết code bắt buộc tài khoản phải chọn skin mới cho khóa tướng. Kết quả là những người chơi mới (chưa sở hữu skin nào) sẽ bị kẹt vĩnh viễn ở màn hình chọn tướng và không thể vào chơi game.

---

### Câu 4: Sự khác biệt cốt lõi giữa Kiểm thử Hộp đen (Black-box) và Kiểm thử Hộp trắng (White-box) & Lý do không dùng Hộp trắng ở mức Hệ thống (System testing)

**Luận điểm 1: Khác biệt cốt lõi nằm ở đối tượng tham chiếu và phương pháp tiếp cận.**
* *Giải thích:* 
  * Kiểm thử hộp đen (Black-box testing) coi phần mềm như một hộp kín, chỉ quan tâm đến chức năng bên ngoài dựa trên tài liệu đặc tả yêu cầu (đầu vào và đầu ra mong đợi), hoàn toàn không cần biết mã nguồn bên trong viết như thế nào.
  * Kiểm thử hộp trắng (White-box testing) đi sâu vào cấu trúc logic bên trong của mã nguồn, kiểm tra các câu lệnh, nhánh rẽ (branches), các đường dẫn (paths) và vòng lặp để đảm bảo tính đúng đắn của thuật toán.
* *Ví dụ cụ thể:*
  * *Kiểm thử hộp trắng:* Developer mở file code C++ chứa hàm tính lượng sát thương chí mạng của tướng xạ thủ để viết test case phủ hết các nhánh logic `if (isCritical == true)` và `else`.
  * *Kiểm thử hộp đen:* Tester đăng nhập game, chọn tướng xạ thủ bắn thử vào quái rừng và quan sát xem con số sát thương hiển thị trên màn hình có đúng bằng 200% sát thương cơ bản như trong mô tả kỹ năng hay không mà không cần đọc dòng code nào.

**Luận điểm 2: Sự phức tạp và quy mô quá lớn của hệ thống khiến kiểm thử hộp trắng không khả thi ở mức Hệ thống (System Testing).**
* *Giải thích:* Kiểm thử hệ thống là giai đoạn kiểm thử toàn bộ phần mềm sau khi đã tích hợp mọi module. Ở giai đoạn này, quy mô mã nguồn có thể lên đến hàng triệu dòng lệnh với hàng tỷ nhánh rẽ và luồng tương tác đan xen. Việc phân tích cấu trúc code để thiết kế các ca kiểm thử hộp trắng phủ hết mọi đường dẫn logic lúc này là bất khả thi về mặt thời gian, nhân lực và chi phí.
* *Phản ví dụ:* Nếu cố tình áp dụng kiểm thử hộp trắng ở mức hệ thống cho game MOBA, đội ngũ tester sẽ phải phân tích từng dòng code của công cụ vẽ đồ họa 3D, hệ thống kết nối mạng, âm thanh, cơ chế tương tác vật lý của hàng trăm vị tướng... Dự án sẽ bị trễ hạn nhiều năm mà vẫn không thể hoàn thành việc phủ hết các nhánh logic trong mã nguồn khổng lồ đó.

**Luận điểm 3: Mục tiêu của Kiểm thử hệ thống hướng tới trải nghiệm người dùng và đặc tả yêu cầu tổng thể.**
* *Giải thích:* System testing nhằm xác minh xem toàn bộ hệ thống có hoạt động đúng theo các yêu cầu nghiệp vụ và kỹ thuật đã thỏa thuận với khách hàng hay không. Khách hàng chỉ quan tâm đến hành vi bên ngoài của phần mềm (hộp đen), chứ không quan tâm mã nguồn chạy nhánh rẽ nào. Do đó, kiểm thử hộp đen là lựa chọn tự nhiên và tối ưu nhất.

---

### Câu 5: Nguyên lý "Phân tách các khía cạnh quan tâm" (Separation of concerns - SoC) trong thiết kế kiến trúc phần mềm

**Luận điểm 1: SoC yêu cầu chia nhỏ hệ thống thành các module độc lập đảm nhận các trách nhiệm riêng biệt.**
* *Giải thích:* Nguyên lý SoC đòi hỏi các kỹ sư phải phân rã một hệ thống phức tạp thành các thành phần (modules/components) độc lập, sao cho mỗi thành phần chỉ tập trung giải quyết một khía cạnh hoặc chức năng nghiệp vụ cụ thể. Các thành phần này tương tác với nhau qua các giao diện rõ ràng (interfaces) nhằm đạt được trạng thái: Kết tụ cao (High Cohesion) và Phụ thuộc thấp (Low Coupling).
* *Ví dụ cụ thể:* Kiến trúc của một Game MOBA được phân tách rõ ràng theo SoC:
  * Module hiển thị hình ảnh (Rendering Engine) chỉ lo việc vẽ đồ họa 3D lên màn hình.
  * Module mạng (Network Engine) chỉ lo việc truyền nhận gói tin đồng bộ vị trí giữa client và server.
  * Module logic game (Logic Engine) chỉ phụ trách tính toán lượng máu, sát thương.
  Khi thiết kế như vậy, lập trình viên đồ họa có thể nâng cấp hiệu ứng hình ảnh của bản đồ mà không cần chỉnh sửa bất kỳ dòng code nào liên quan đến giao thức mạng.

**Luận điểm 2: SoC mang lại lợi ích cốt lõi cho bảo trì bằng cách hạn chế tác động lan truyền khi sửa đổi hệ thống.**
* *Giải thích:* Khi phần mềm cần sửa lỗi hoặc nâng cấp một tính năng cụ thể, nhà phát triển chỉ cần khoanh vùng và chỉnh sửa bên trong module chịu trách nhiệm cho khía cạnh đó. Nhờ tính độc lập cao, sự thay đổi này sẽ không làm ảnh hưởng hoặc làm phát sinh lỗi ngoài ý muốn ở các module khác, giúp giảm thiểu rủi ro bảo trì.
* *Phản ví dụ:* Nếu một kiến trúc sư thiết kế game MOBA không áp dụng SoC, để code xử lý va chạm đồ họa và code tính sát thương vật lý trộn lẫn vào nhau (Spaghetti code). Khi nhà phát triển sửa lại hoạt ảnh di chuyển của vị tướng $\rightarrow$ vô tình làm thay đổi biến sát thương $\rightarrow$ dẫn tới lỗi tướng có khả năng bất tử hoặc gây sát thương vô hạn khi lướt đi. Việc tìm ra và sửa lỗi trong mớ hỗn độn này sẽ cực kỳ tốn thời gian.

---

### Câu 7: Tại sao Daily Meeting trong Agile được ưu tiên hơn việc viết tài liệu đặc tả cồng kềnh

**Luận điểm 1: Phản hồi nhanh và tháo gỡ khó khăn (Blockers) tức thời.**
* *Giải thích:* Quy trình Agile ưu tiên sự tương tác trực tiếp hàng ngày thông qua cuộc họp Daily Stand-up (15 phút). Tại đây, từng thành viên báo cáo ngắn gọn về việc đã làm, việc sẽ làm và những khó khăn đang gặp phải. Sự giao tiếp trực tiếp giúp các thành viên khác trong đội có thể hỗ trợ tháo gỡ vướng mắc ngay lập tức, ngăn ngừa tình trạng một thành viên bị kẹt công việc nhiều ngày liền.
* *Ví dụ cụ thể:* Trong một buổi Daily meeting của dự án game MOBA, một lập trình viên báo cáo: *"Tôi đang bị kẹt ở phần đồng bộ hóa kỹ năng định hướng của tướng mới qua mạng mạng do gặp hiện tượng giật lag"*. Ngay lập tức, kỹ sư mạng đứng cạnh phản hồi: *"Tôi mới tối ưu hóa thuật toán nén gói tin hôm qua, lát nữa tôi sẽ chỉ bạn cách tích hợp vào tướng mới"*. Vướng mắc được giải quyết ngay trong ngày.

**Luận điểm 2: Tránh lãng phí thời gian và giảm thiểu sự lỗi thời của tài liệu đặc tả.**
* *Giải thích:* Trong môi trường thay đổi nhanh chóng, việc viết các tài liệu đặc tả chi tiết dài hàng trăm trang tốn rất nhiều thời gian. Hơn nữa, ngay khi tài liệu vừa viết xong, yêu cầu thực tế đã có thể thay đổi, biến tài liệu thành đống giấy tờ lỗi thời. Daily meeting giúp toàn đội liên tục đồng bộ thông tin thay đổi trực tiếp mà không cần đi qua các thủ tục giấy tờ rườm rà.
* *Phản ví dụ:* Nếu không họp hàng ngày mà trao đổi qua tài liệu/email: Lập trình viên bị kẹt lỗi đồng bộ mạng mạng phải viết một tài liệu mô tả lỗi $\rightarrow$ gửi email lên hệ thống quản lý $\rightarrow$ Scrum Master duyệt $\rightarrow$ chuyển tiếp cho kỹ sư mạng $\rightarrow$ kỹ sư mạng đọc tài liệu thiết kế và phản hồi sau 2 ngày. Quy trình hành chính này làm chậm tiến độ dự án nghiêm trọng.

---

### Câu 8: Nhược điểm của Ngôn ngữ tự nhiên trong Tài liệu đặc tả (SRS) và các quy tắc khắc phục

**Luận điểm 1: Tính nhập nhằng (Ambiguity) là nhược điểm chí mạng của ngôn ngữ tự nhiên.**
* *Giải thích:* Ngôn ngữ tự nhiên có tính đa nghĩa, phụ thuộc nhiều vào ngữ cảnh và sự diễn giải cá nhân. Khi viết đặc tả yêu cầu hoàn toàn bằng ngôn ngữ tự nhiên tự do, khách hàng, lập trình viên và tester dễ hiểu một câu mô tả theo các cách hoàn toàn khác nhau, dẫn đến sản phẩm làm ra không đúng kỳ vọng.
* *Ví dụ cụ thể:* Tài liệu yêu cầu ghi mơ hồ: *"Hệ thống phải hồi chiêu nhanh khi tướng tiêu diệt được mục tiêu"*.
  * Lập trình viên hiểu: Giảm 50% thời gian hồi chiêu hiện tại.
  * Khách hàng hiểu: Hồi chiêu lập tức (giảm 100%) để tiếp tục combo kỹ năng.
  * Tester không biết làm sao để kiểm thử chữ "nhanh".

**Luận điểm 2: Khắc phục tính nhập nhằng bằng ngôn ngữ cấu trúc và lượng hóa chỉ số.**
* *Giải thích:* Các tài liệu kỹ nghệ phần mềm đưa ra các quy tắc để chuẩn hóa việc viết yêu cầu:
  1. Sử dụng Ngôn ngữ tự nhiên có cấu trúc (Structured Natural Language) với các biểu mẫu định sẵn (ví dụ: cấu trúc *Nếu... Thì...* hoặc *Khi... Hệ thống sẽ...*).
  2. Xây dựng Bảng thuật ngữ (Glossary) để định nghĩa thống nhất các từ chuyên ngành trong toàn dự án.
  3. Lượng hóa cụ thể các tiêu chuẩn: Thay vì dùng các từ mơ hồ như "nhanh", "mạnh", "tối ưu", phải ghi rõ số liệu đo lường được.
* *Ví dụ cụ thể cải tiến:* *"Khi tướng đạt trạng thái hạ gục (Kill) hoặc hỗ trợ hạ gục (Assist) một tướng đối phương, hệ thống phải giảm ngay lập tức 80% thời gian hồi chiêu còn lại của tất cả kỹ năng đang trong thời gian chờ (Cooldown)"*. Yêu cầu này giúp lập trình viên code chính xác và tester có số liệu cụ thể để kiểm tra.
* *Phản ví dụ:* Nếu không khắc phục tính nhập nhằng, khi bàn giao sản phẩm game MOBA, đối tác sẽ từ chối nghiệm thu vì chiêu thức hồi quá lâu so với suy nghĩ của họ, buộc nhà phát triển phải sửa lại code hệ thống kỹ năng từ đầu, gây lãng phí lớn về chi phí và thời gian.

---

### Câu 9: Ý tưởng nền tảng của kỹ thuật "Kiểm thử dựa trên phân hoạch tương đương" (ECT) và sự tránh bùng nổ test case

**Luận điểm 1: Phân chia miền giá trị đầu vào thành các lớp tương đương.**
* *Giải thích:* Ý tưởng cốt lõi của ECT là chia toàn bộ miền giá trị đầu vào của một biến thành các khoảng/lớp giá trị tương đương (bao gồm các lớp hợp lệ và không hợp lệ). Kỹ thuật này dựa trên giả định rằng mọi giá trị trong cùng một lớp tương đương sẽ được phần mềm xử lý theo cùng một cách thức và cho ra hành vi giống nhau (nếu một giá trị chạy đúng thì các giá trị khác trong lớp cũng chạy đúng, và ngược lại).
* *Ví dụ cụ thể:* Trong một Game MOBA, điều kiện để người chơi tham gia phòng "Đấu Xếp Hạng" là tài khoản phải đạt cấp độ từ 10 đến 90. Ta chia làm 3 lớp tương đương:
  * Lớp 1 (Không hợp lệ - quá nhỏ): Cấp độ dưới 10 (từ 1 đến 9).
  * Lớp 2 (Hợp lệ): Cấp độ từ 10 đến 90.
  * Lớp 3 (Không hợp lệ - quá lớn): Cấp độ trên 90 (từ 91 trở lên).

**Luận điểm 2: Lựa chọn phần tử đại diện để bao phủ kiểm thử, tránh bùng nổ số lượng test case.**
* *Giải thích:* Thay vì phải kiểm thử vét cạn mọi giá trị đầu vào khả dĩ (ví dụ test toàn bộ các cấp độ từ 1 đến 100, điều này gây bùng nổ số lượng test case không cần thiết), tester chỉ cần chọn đúng **một giá trị đại diện** từ mỗi lớp tương đương để chạy thử. Kết quả của giá trị đại diện này sẽ đại diện cho cả lớp đó. Nhờ vậy, ta vừa có cảm giác kiểm thử đầy đủ mọi kịch bản đầu vào (vét cạn miền giá trị), vừa giảm thiểu tối đa số lượng ca kiểm thử phải thực hiện.
* *Ví dụ cụ thể ứng dụng:* Tester chỉ cần chọn 3 giá trị đại diện:
  * Cấp độ 5 (đại diện Lớp 1) $\rightarrow$ Hệ thống phải chặn không cho vào phòng rank.
  * Cấp độ 30 (đại diện Lớp 2) $\rightarrow$ Hệ thống cho phép vào phòng rank bình thường.
  * Cấp độ 95 (đại diện Lớp 3) $\rightarrow$ Hệ thống chặn không cho vào phòng rank.
  Chỉ với 3 ca kiểm thử, ta đã bao phủ toàn bộ logic phân quyền cấp độ mà không cần chạy 100 lần test.
* *Phản ví dụ:* Nếu không sử dụng ECT, tester sẽ phải test thủ công từng cấp độ từ 1 đến 100 $\rightarrow$ mất hàng giờ làm việc vô ích chỉ để kiểm thử một điều kiện logic cơ bản, gây lãng phí nghiêm trọng nguồn lực của dự án.

---

### Câu 10: Mô hình phát triển tối ưu cho phần mềm ngân hàng (nhiều rủi ro tiềm ẩn, yêu cầu thay đổi liên tục)

**Luận điểm 1: Yêu cầu quản lý rủi ro chặt chẽ đối với hệ thống ngân hàng.**
* *Giải thích:* Phần mềm ngân hàng là hệ thống tối quan trọng, liên quan trực tiếp đến tài chính và thông tin mật của khách hàng. Bất kỳ lỗi tiềm ẩn nào lọt ra môi trường thật đều có thể gây ra thiệt hại tài chính khổng lồ hoặc hậu quả pháp lý nghiêm trọng. Do đó, quy trình phát triển bắt buộc phải có cơ chế phân tích và kiểm soát rủi ro cực kỳ nghiêm ngặt qua từng bước đi.

**Luận điểm 2: Sự phù hợp của Mô hình Xoắn ốc (Spiral Model) nhờ tích hợp cơ chế Phân tích rủi ro vào quy trình lặp.**
* *Giải thích:* Mô hình Xoắn ốc kết hợp tính chất lặp lại (Iterative) của Prototyping giúp đáp ứng việc thay đổi yêu cầu liên tục từ khách hàng, đồng thời tích hợp tính kiểm soát có hệ thống của mô hình Thác nước. Đặc biệt, điểm độc nhất của mô hình Xoắn ốc là mỗi vòng lặp (xoắn) đều bắt buộc đi qua pha **Phân tích rủi ro (Risk Analysis)** trước khi tiến hành thiết kế và viết code. Điều này giúp phát hiện và tiêu diệt các nguy cơ mất an toàn bảo mật từ rất sớm.
* *Ví dụ thực tế:* Ngân hàng muốn phát triển tính năng "Rút tiền bằng nhận diện khuôn mặt (FaceID)".
  * Vòng xoắn 1: Làm prototype đơn giản để kiểm tra camera. Pha phân tích rủi ro chỉ ra nguy cơ: kẻ gian có thể dùng ảnh chụp 2D của chủ tài khoản để đánh lừa hệ thống.
  * Vòng xoắn 2: Tập trung giải quyết rủi ro này bằng cách thiết kế thêm thuật toán nhận diện thực thể sống (liveness detection - yêu cầu nháy mắt, quay đầu). Rủi ro bảo mật được triệt tiêu trước khi hệ thống được code diện rộng và tích hợp vào Core Banking.
* *Phản ví dụ:* Nếu sử dụng mô hình Thác nước, dự án sẽ bỏ qua bước làm prototype để phân tích rủi ro bảo mật sớm. Đến cuối dự án sau 1 năm phát triển, khi bàn giao hệ thống, ngân hàng mới phát hiện ra lỗ hổng FaceID bị qua mặt bởi ảnh chụp $\rightarrow$ dự án thất bại hoàn toàn, gây tổn thất hàng triệu USD chi phí phát triển và đe dọa an toàn tài sản của khách hàng.

---

### Câu 11: Quyền quyết định khi xuất hiện yêu cầu thay đổi cực kỳ quan trọng giữa Sprint trong Scrum

**Luận điểm 1: Quyền quyết định tối cao thuộc về Product Owner (PO).**
* *Giải thích:* Trong mô hình Scrum, Product Owner là vai trò duy nhất chịu trách nhiệm quản lý Product Backlog, tối ưu hóa giá trị của sản phẩm và sự thành bại của dự án. PO là người sở hữu quyền lực đưa ra quyết định chấp nhận hay từ chối các yêu cầu thay đổi từ phía khách hàng/thị trường, và quyết định khi nào các yêu cầu đó được thực hiện.

**Luận điểm 2: Cơ chế xử lý thay đổi khẩn cấp để bảo vệ sự tập trung của Dev Team.**
* *Giải thích:* Nguyên tắc của Scrum quy định: Một khi Sprint đã bắt đầu, mục tiêu của Sprint (Sprint Goal) không được phép thay đổi để Dev Team tập trung hoàn thành công việc đã cam kết. 
  * Nếu yêu cầu thay đổi xuất hiện và cực kỳ quan trọng (mang tính sống còn cho sản phẩm), PO có quyền đưa ra quyết định **hủy bỏ (Cancel) Sprint hiện tại**. Toàn bộ đội ngũ sẽ dừng lại, thiết lập Sprint Goal mới dựa trên yêu cầu khẩn cấp đó và bắt đầu một Sprint mới.
  * Nếu yêu cầu quan trọng nhưng không đến mức sinh tử ngay lập tức, PO sẽ quản lý bằng cách đưa yêu cầu đó vào Product Backlog, xếp độ ưu tiên cao nhất để thực hiện ở Sprint tiếp theo. Dev Team hay Scrum Master không có quyền tự ý nhét yêu cầu mới vào Sprint đang chạy.
* *Ví dụ cụ thể:* Đội ngũ đang thực hiện Sprint làm tính năng "Hệ thống bang hội mới" cho game MOBA. Giữa Sprint, Apple cập nhật chính sách bắt buộc mọi game phải có nút "Xóa tài khoản trực tuyến" ngay lập tức nếu không sẽ bị gỡ khỏi App Store sau 3 ngày. Đây là thay đổi sinh tử ảnh hưởng trực tiếp đến sự tồn tại của game. Product Owner lập tức quyết định hủy Sprint hiện tại để Dev Team chuyển sang làm tính năng xóa tài khoản khẩn cấp nhằm giữ game trên Store.
* *Phản ví dụ:* Nếu Scrum Master hoặc Dev Team tự ý đưa tính năng "Xóa tài khoản" vào Sprint hiện tại mà không thông qua PO $\rightarrow$ dẫn tới quá tải công việc, phá vỡ cam kết mục tiêu ban đầu, làm nhiễu loạn thứ tự ưu tiên kinh doanh và vi phạm nghiêm trọng nguyên tắc phân chia vai trò của Scrum.
