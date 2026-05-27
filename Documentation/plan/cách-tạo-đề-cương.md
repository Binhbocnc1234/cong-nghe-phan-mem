# Hướng dẫn tạo đề cương môn học

Để đảm bảo các tài liệu đề cương ôn thi đạt chất lượng tốt nhất, dễ hiểu và dễ học, quá trình tạo/sửa đề cương cần tuân thủ nghiêm ngặt các nguyên tắc sau:

## 1. Về phạm vi kiến thức (Scope)
- **Bám sát Slide bài giảng:** Đề cương phải phủ toàn bộ các ý chính, các đề mục và phạm vi kiến thức được giảng viên đề cập trong các slide bài giảng. Không bỏ sót các keyword quan trọng có trên slide.

## 2. Về nội dung chi tiết (Content)
- **Ưu tiên dùng sách/giáo trình:** Vì slide thường mang tính chất tóm tắt và có thể bị thiếu sót hoặc chưa đủ rõ ràng, nội dung chi tiết để diễn giải cho các đề mục trên slide phải được tham khảo và trích xuất từ sách giáo trình (Ví dụ: *Software Engineering A Practitioner's Approach - Pressman*).

## 3. Về cấu trúc (Format)
- **Format 1:1 (Lý thuyết đi kèm Ví dụ):** Mỗi một luận điểm lý thuyết phải có một ví dụ minh họa đi kèm ngay bên dưới để làm rõ. 
- **Cấu trúc trình bày:**
  - **1. [Tên luận điểm / Công việc]**
    - **Lý thuyết:** Diễn giải chi tiết lý thuyết (lấy từ sách).
    - **Ví dụ ([Tên bài toán]):** Ví dụ thực tế ánh xạ chính xác 1:1 vào lý thuyết vừa nêu.
- **Tính liên kết:** Các ví dụ tuyệt đối không được viết chung chung, mà phải trực tiếp làm rõ được lý thuyết vừa nhắc đến.
- **Số lượng ví dụ:** Thông thường, mỗi luận điểm lý thuyết chỉ cần **1 ví dụ** duy nhất để minh họa cho ngắn gọn.
- **Quy tắc ưu tiên Ví dụ:** Nếu chỉ dùng 1 ví dụ, ưu tiên dùng bài toán **Game MOBA** làm chuẩn. (Các tài liệu cũ như UP.md có 2 ví dụ là ngoại lệ nhằm mục đích ôn tập kỹ hơn).

## 4. Mục tiêu cuối cùng
- Tài liệu phải rõ ràng, phân cấp ý tốt (dùng bold, bullet points) để sinh viên dễ dàng hiểu, ôn tập.
- Tài liệu phải chi tiết, tránh trường hợp bỏ sót ý
- Khi làm tài liệu cho slide n thì bạn có thể giả định rằng người đọc đã có kiến thức từ các slide trước(n-1, n-2, ..., 1)
- Destination: một file `<chapter_name>.md` mới/đã được chỉnh sửa trong folder `Đề cương`. Mỗi một file .pdf trong `Slides` sẽ có một đề cương markdown tương ứng, tránh gộp file

## 5. Ví dụ cụ thể cho hướng dẫn trên

- Người dùng muốn Agent tạo một file markdown chứa đề cương cho slide số 5: Khái niệm yêu cầu
- Agent cần xác định đúng chương(chapter) trong book, tham khảo file `Title-to-chapter.md`
- Khi quét slide, bạn nhận thấy slide ghi rằng:

Quy trình kỹ nghệ yêu cầu
• Gồm bốn hoạt động cơ bản sau
• Thu thập, phân tích yêu cầu (khám phá, lý luận ..)
• Đặc tả yêu cầu (viết …)
• Thẩm định yêu cầu (kiểm tra …)
• Quản lý yêu cầu

- Agent tra cứu trong sách xem chúng được sách định nghĩa chúng như thế nào
- Agent nhận thấy sách viết có tận 7 hoạt động, như vậy thì agent nên ưu tiên theo định nghĩa của sách
- Agent lấy ví dụ tương ứng với 7 hoạt động trên

- Khi quét slide, bạn nhận thấy slide có ghi chú về quy trình xoắn ốc, nhưng trong sách không có, bạn ghi vào file markdown rằng: Quy trình xoắn ốc: [Không có trong sách]

