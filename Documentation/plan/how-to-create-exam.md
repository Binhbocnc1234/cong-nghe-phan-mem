# Plan: Khung tạo câu hỏi ôn tập

**TL;DR**  
Tạo một khung sinh câu hỏi/đáp án tiếng Việt chỉ cho các câu hỏi dạng **vì sao** và **thực hành**. Trong đó câu hỏi vì sao chiếm lượng lớn. Câu hỏi phải bám nội dung sách Pressman, trả lời đủ ý, có ví dụ, và tránh trùng ý giữa các câu.

# Giới hạn phạm vi câu hỏi
   - Chỉ nhận câu hỏi dạng **vì sao** và **thực hành**.
   - Loại câu hỏi định nghĩa thuần túy như “Agile là gì”, “Waterfall model là gì”.
   - Mỗi câu phải xoay quanh một ý học thuật rõ ràng của chương.

# Chuẩn hóa khung đáp án
   - Với câu **vì sao**:
     - Giải thích bám theo định nghĩa. Với một hoặc nhiều luận điểm
     - Nếu luận điểm khó hiểu, trừu tượng thì ví dụ đưa ra là cần thiết. Phản ví dụ nếu có thể, tức là nếu câu hỏi dạng "tại sao lại phải làm như thế này", thì phản ví dụ để minh họa cho việc nếu không làm như câu hỏi thì hậu quả sẽ như thế nào?
     - Ví dụ minh họa nên là **nội dung cụ thể**, không được quá chung chung, ưu tiên **Game MOBA** nếu phù hợp, còn không thì chuyển sang phần mềm khác tiêu biểu hơn. Ví dụ với câu hỏi "lấy một phần mềm phát triển dựa trên Waterfall", ta không thể cố chấp lấy Game MOBA để làm ví dụ, vì rõ ràng nhu cầu người dùng thay đổi liên tục
   - Với câu hỏi **thực hành**. Mình lấy một số ví dụ: viết user story, vẽ biểu đồ, lấy ví dụ về một quy trình phát triển tuân theo mô hình thác nước
   - Dung lượng, giải thích đầy đủ, chi tiết

# Bám nguồn tham khảo: đề cương tương ứng với câu hỏi

# Định dạng đầu ra cho AI agent
   - Input: chương/chủ đề.
   - Output:
     - danh sách câu hỏi hợp lệ, nằm trong phạm vi chương/chủ đề ở Input
     - Theo sau mỗi câu hỏi là một đáp án

# Ví dụ

Câu hỏi 1: "Tại sao Waterfall không còn phù hợp cho đa số các phần mềm hiện nay?"
1. Thời gian ra thị trường (Time-to-Market) quá chậmVới Waterfall, khách hàng chỉ nhìn thấy sản phẩm ở giai đoạn cuối cùng của dự án.
Vấn đề: Một dự án Waterfall có thể mất 1–2 năm để đi từ bước khảo sát đến khi ra mắt.Hậu quả: Trong 2 năm đó, thị trường đã thay đổi hoàn toàn, đối thủ đã ra mắt tính năng tương tự từ lâu, và công nghệ bạn dùng từ 2 năm trước đã trở nên lạc hậu. Bạn bàn giao một phần mềm "hoàn hảo theo đúng kế hoạch năm 2024", nhưng hoàn toàn vô dụng vào năm 2026.
2. Chi phí sửa sai tăng theo cấp số nhân
Đây là điểm yếu chết người của kỹ nghệ dạng tuyến tính. 
Nếu một sai lầm trong việc hiểu sai yêu cầu xảy ra ở tháng thứ 1, nhưng phải đến tháng thứ 12 (khi kiểm thử) mới phát hiện ra, cái giá phải trả để sửa chữa là cực kỳ khủng khiếp.
Mối quan hệ này có thể được hình dung qua biểu đồ chi phí sửa lỗi trong kỹ nghệ phần mềm: lúc ban đầu chỉ mất vài giờ chỉnh sửa tài liệu, nhưng ở giai đoạn cuối sẽ kéo theo việc đập đi xây lại toàn bộ cấu trúc hệ thống và cơ sở dữ liệu.
3. Người dùng không thể "hình dung" phần mềm qua văn bản
Waterfall dựa dẫm hoàn toàn vào Tài liệu tả yêu cầu (BRD/SRS) dài cả trăm trang.Thực tế: Khách hàng (và cả người dùng cuối) không thể hiểu hết hệ thống sẽ vận hành ra sao chỉ bằng việc đọc chữ trên giấy.Kết quả: Họ ký xác nhận vào tài liệu vì tưởng rằng mình đã hiểu.
 Nhưng khi nhận sản phẩm thật sau nhiều tháng chờ đợi, họ lập tức thốt lên: "Nó chạy đúng như mô tả, nhưng đây không phải là cái tôi thực sự cần!"
4. Phần mềm hiện nay có độ phức tạp cao (Complex Systems)
Phần mềm ngày nay không còn là những ứng dụng độc lập, tính toán đơn giản. Chúng kết nối với hàng tá API bên ngoài, chạy trên đa nền tảng, tích hợp AI, Cloud, và xử lý dữ liệu lớn (Big Data). Trong môi trường này, có vô số "biến số không thể biết trước" (Unknown Unknowns) mà bạn không bao giờ dự đoán hết được ở giai đoạn phân tích đầu dự án. Bạn buộc phải vừa làm, vừa thử nghiệm, vừa sửa sai — điều mà Waterfall cấm ngặt.

Câu hỏi 2: "Why do requirements change so much? After all, don’t people know what they want?"

Luận điểm 1: Do kĩ nghệ phần mềm không tốt

Sự thiếu hụt trong mô hình hóa (Modeling)
Khi không có các sơ đồ luồng dữ liệu hoặc sơ đồ nghiệp vụ rõ ràng, các bên liên quan dễ hiểu lầm ý nhau.

Ví dụ: Trong hệ thống thanh toán, lập trình viên mặc định là chỉ có VNPay, nhưng khách hàng lại mặc định là phải có cả thẻ tín dụng quốc tế. Đến khi tích hợp mới phát hiện ra cấu trúc dữ liệu không khớp.

Luật điểm 2: Khả năng tưởng tượng của con người khá yếu, mọi rủi ro chỉ thực sự lộ rõ khi đã có prototype

Ví dụ: ở trong kế hoạch có ghi là "Các tướng đều có 4 skill". Nhưng đến lúc tester chơi thử prototype đầu tiên thì họ nhận ra 4 skill là quá phức tạp, khó chơi, tức UX tệ. Do đó plan được điều chỉnh thành 3 skil

Luận điểm 3: Nhu cầu của con người ngày càng tăng

Ví dụ: Người chơi muốn game đồ họa càng ngày càng đẹp và game càng ngày càng có nhiều tính năng đa dạng

Luận điểm 4: Thị trường thay đổi

Ví dụ: Khi khách hàng từ việc chơi game trên máy tính chuyển sang chơi game trên điện thoại thì yêu cầu phần mềm cũng phải thích nghi với API của điện thoại. 

Ví dụ: Đối thủ ra mắt phần mềm có tính năng vượt trội và thu hút hết khách hàng của mình. 

Luận điểm 5: Luật pháp thay đổi 

Ví dụ: Luật pháp thay đổi yêu cầu các giao dịch trong game cần phải được liên kết với mã số thuế của nhà nước

# Ví dụ về một luận điểm mà phần giải thích đã quá rõ ràng và không cần thêm ví dụ

**Luận điểm 2: Quy trình phần mềm đảm bảo tính kế thừa, dễ bảo trì và hạn chế rủi ro khi có sự thay đổi nhân sự.**
* *Giải thích:* Một quy trình chuẩn mực yêu cầu sản sinh tài liệu (tài liệu thiết kế, đặc tả yêu cầu) và quy chuẩn viết mã (coding standards). Điều này giúp tri thức của dự án được lưu trữ lại một cách khách quan trên hệ thống, thay vì nằm hoàn toàn trong đầu của một vài cá nhân đơn lẻ. Khi có nhân sự nghỉ việc, người mới có thể dựa vào quy trình và tài liệu để tiếp quản công việc nhanh chóng.

