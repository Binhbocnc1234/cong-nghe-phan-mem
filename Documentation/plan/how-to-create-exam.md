# Plan: Khung tạo câu hỏi ôn tập

**TL;DR**  
Tạo một khung sinh câu hỏi/đáp án tiếng Việt chỉ cho các câu hỏi dạng **“vì sao”** và **“giải thích”**. Câu hỏi phải bám nội dung sách Pressman, trả lời đủ ý, có ví dụ, và tránh trùng ý giữa các câu.

**Steps**
1. **Giới hạn phạm vi câu hỏi**
   - Chỉ nhận câu hỏi dạng **vì sao** và **thực hành**.
   - Loại câu hỏi định nghĩa thuần túy như “Agile là gì”, “Waterfall model là gì”.
   - Mỗi câu phải xoay quanh một ý học thuật rõ ràng của chương.

2. **Chuẩn hóa khung đáp án**
   - Với câu **vì sao**:
     - nêu định nghĩa/khái niệm liên quan,
     - giải thích bám theo định nghĩa,
     - nêu nguyên nhân → hệ quả,
     - thêm ví dụ cụ thể, ưu tiên bám vào **game cụ thể, mình thích game MOBA** thay vì ví dụ quá chung chung. Phản ví dụ nếu có thể, tức là nếu câu hỏi dạng "tại sao lại phải làm như thế này", thì phản ví dụ để minh họa cho việc nếu không làm như câu hỏi thì hậu quả sẽ như thế nào?
   - Với câu hỏi **thực hành**. Mình lấy một số ví dụ: viết user story, vẽ biểu đồ, lấy ví dụ về một quy trình phát triển tuân theo mô hình thác nước
3. **Thiết lập tiêu chí không trùng ý**
   - Không tạo 2 câu cùng một đáp án.
   - Nếu cùng chủ đề lớn, phải khác góc nhìn: nguyên nhân, cơ chế, lợi ích, hệ quả, ứng dụng.
   - Ưu tiên câu hỏi có ý nghĩa học thuật riêng, không chỉ khác câu chữ.

4. **Bám nguồn tham khảo**: đề cương tương ứng với câu hỏi

5. **Định dạng đầu ra cho AI agent**
   - Input: chương/chủ đề.
   - Output:
     - danh sách câu hỏi hợp lệ,
     - đáp án ngắn gọn nhưng đủ ý,
     - mỗi đáp án có ví dụ,
     - không trùng ý.
   - Có thể gắn nhãn: `why` / `explain`.


**Relevant files**
- `C:\Users\binhb\Documents\_Tài liệu học tập\Công nghệ phần mềm\Software Engineering_ A Practitioner's Approach (9th Ed) - R. Pressman, B. Maxim.pdf` — tài liệu tham chiếu chính.
- `answer-04.md` 

**Verification**
1. Sinh thử 5–10 câu cho 1 chương.
2. Kiểm tra:
   - chỉ có câu **vì sao** / **giải thích**,
   - không trùng ý,
   - mỗi đáp án có: định nghĩa + giải thích + ví dụ cụ thể (ưu tiên phần mềm/game).
3. Đọc lại để đảm bảo tiếng Việt tự nhiên và bám sách.

**Decisions / exclusions**
- Chỉ làm câu hỏi vì sao/giải thích.
- Loại câu hỏi định nghĩa thuần túy.
- Đáp án chỉ cần **đủ ý**, không cần quá dài.
- Ngôn ngữ: **tiếng Việt**.
- Ví dụ minh họa nên là **nội dung cụ thể**, ưu tiên **phần mềm/game** nếu phù hợp.

**Risks / open questions**
- Mức “không trùng ý” cần hiểu chặt hay rộng.
- Độ dài tối đa mỗi đáp án chưa cố định.
