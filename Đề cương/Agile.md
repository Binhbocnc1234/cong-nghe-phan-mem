# Tài liệu ôn thi: Agile, XP và Scrum

---

## 1. Tổng quan về Agile

**1. Vấn đề của các mô hình truyền thống và sự ra đời của Agile**
- **Lý thuyết:** Trong thực tế, yêu cầu của khách hàng liên tục thay đổi và rất khó xác định chính xác ngay từ đầu. Các mô hình PTPM truyền thống (Thác nước, chữ V) có chi phí đối phó với sự thay đổi (cost of change) cực kỳ cao ở các giai đoạn sau. Agile ra đời nhằm giữ chi phí thay đổi ở mức thấp, bằng cách thiết kế quy trình có khả năng chấp nhận và thích ứng với sự thay đổi yêu cầu kể cả khi dự án đã đi vào sâu.
- **Ví dụ (Game MOBA):** Ban đầu dự án định làm game 3v3, nhưng khi đang code được 3 tháng, thị trường lại chuộng 5v5. Nếu dùng mô hình Thác nước, việc đập đi làm lại kiến trúc mạng sẽ tốn cực kỳ nhiều tiền. Agile cho phép team linh hoạt điều chỉnh sang 5v5 nhanh chóng nhờ các vòng lặp ngắn và chưa tốn quá nhiều công thiết kế thừa thãi.

**2. Tuyên ngôn Agile (Agile Manifesto)**
- **Lý thuyết:** Agile dựa trên 4 giá trị cốt lõi:
  - (1) **Ưu tiên cá nhân và tương tác** *hơn là* quy trình và công cụ. (Giao tiếp trực tiếp hiệu quả hơn làm việc qua tool/quy trình cứng nhắc).
  - (2) **Ưu tiên phần mềm chạy tốt** *hơn là* tài liệu đầy đủ. (Sản phẩm cuối cùng quan trọng hơn đống tài liệu mô tả nó).
  - (3) **Ưu tiên cộng tác với khách hàng** *hơn là* đàm phán hợp đồng. (Khách hàng cùng tham gia làm việc liên tục thay vì chỉ ký hợp đồng rồi bỏ mặc).
  - (4) **Ưu tiên phản hồi sự thay đổi** *hơn là* bám sát kế hoạch. (Kế hoạch có thể thay đổi bất cứ lúc nào miễn là mang lại giá trị tốt nhất cho sản phẩm).
- **Ví dụ (Game MOBA):** Ánh xạ 4 giá trị trên vào thực tế:
  - *(1) Cá nhân & tương tác:* Khi gặp lỗi sát thương, Dev và Tester kéo ghế ngồi cạnh nhau kiểm tra trực tiếp trên màn hình, thay vì tạo hàng tá ticket/email qua lại rườm rà.
  - *(2) Phần mềm > Tài liệu:* Thay vì viết tài liệu 100 trang mô tả chi tiết chiêu thức, team code thẳng 1 bản demo kỹ năng chạy được trên màn hình để kiểm chứng ngay lập tức.
  - *(3) Cộng tác KH:* Phía nhà phát hành (Khách hàng) chơi thử bản demo mỗi cuối tuần để góp ý cân bằng tướng, thay vì đợi 2 năm xong game mới đánh giá dựa trên hợp đồng ban đầu.
  - *(4) Phản hồi thay đổi:* Đang định làm bản đồ mùa hè nhưng thấy thị hiếu cộng đồng đang sốt mùa đông, team lập tức đổi hướng ưu tiên làm bản đồ tuyết rơi mà không ngại việc phải thay đổi kế hoạch cũ.

**3. Khó khăn và hạn chế khi áp dụng Agile**
- **Lý thuyết:** Khó khăn lớn nhất là đòi hỏi khách hàng phải có mặt toàn thời gian để phản hồi, và các thành viên trong đội phải giao tiếp rất tốt, làm việc gắn kết. Agile thường không phù hợp với các hệ thống quá lớn, siêu phức tạp hoặc có yêu cầu an toàn/an ninh sinh mạng khắt khe (do ít tài liệu và cấu trúc thay đổi liên tục).
- **Ví dụ (Game MOBA):** Nếu dự án game có tới 1000 nhân sự rải rác ở 5 múi giờ khác nhau, việc bắt tất cả họp mặt trao đổi trực tiếp hàng ngày và linh hoạt thay đổi yêu cầu mà không có tài liệu chặt chẽ là điều gần như bất khả thi.

---

## 2. Quy trình Extreme Programming (XP)

XP là một quy trình Agile nổi bật, tập trung vào kỹ thuật lập trình và nâng cao chất lượng mã nguồn.

**1. Hoạt động Lập kế hoạch (Planning) và User Story**
- **Lý thuyết:** Khách hàng sẽ viết các yêu cầu dưới dạng "User Story" theo template: `"As a <role>, I want <goal/desire> so that <benefit>"`. Khách hàng gán độ ưu tiên, sau đó đội ngũ Phát triển đánh giá và ước lượng chi phí (số tuần) để hoàn thành. Nếu 1 story lớn hơn 3 tuần, cần phải chia nhỏ ra nữa.
- **Ví dụ (Game MOBA):** Yêu cầu được viết là: "Với vai trò là *Người chơi*, tôi muốn *có nút Tìm trận* để *nhanh chóng được ghép nối với 9 người khác*". Team Dev phân tích và đánh giá Story này tốn 2 tuần để hoàn thành.

**2. Hoạt động Thiết kế (Design)**
- **Lý thuyết:** Nguyên tắc KIS (Keep It Simple) - thiết kế càng đơn giản càng tốt. Chỉ thiết kế kiến trúc đủ để giải quyết các User Story hiện tại đang quan tâm. Tuyệt đối không thiết kế trước các tính năng phức tạp dự phòng cho tương lai chưa chắc đã xảy ra.
- **Ví dụ (Game MOBA):** Trong vòng lặp hiện tại chỉ cần làm chế độ "Đấu thường". Team thiết kế Database rất đơn giản, chỉ lưu thông tin trận đấu thường. Không thiết kế sẵn hệ thống điểm Xếp hạng (Rank) phức tạp vì chưa biết tương lai luật trừ điểm Rank sẽ như thế nào.

**3. Hoạt động Lập trình (Coding)**
- **Lý thuyết:** Khuyến khích lập trình cặp (Pair programming): 2 lập trình viên ngồi chung 1 máy tính để code, 1 người gõ và 1 người theo dõi/review trực tiếp. Đặc biệt, phải thiết kế và viết Kiểm thử đơn vị (Unit Test) trước khi viết code logic thật.
- **Ví dụ (Game MOBA):** Hai Dev ngồi cùng nhau để code luồng tính sát thương chiêu cuối. Dev A gõ code trừ HP, Dev B ngồi cạnh phát hiện ngay lỗi quên chưa trừ giáp vật lý. Nhờ vậy code xong là sạch bug ngay.

**4. Hoạt động Kiểm thử (Testing)**
- **Lý thuyết:** Các Unit Test phải được chạy tự động liên tục (Continuous Integration) để phát hiện lỗi ngay khi ghép code. Cuối cùng, thực hiện Kiểm thử chấp nhận (Acceptance Testing) bởi khách hàng để chốt User Story.
- **Ví dụ (Game MOBA):** Mỗi khi Dev đưa đoạn code chiêu thức mới lên máy chủ, hệ thống tự động chạy hàng loạt bài Unit Test sát thương. Nếu qua hết, Game Designer sẽ mở game lên tự chơi thử (Acceptance Test) xem chiêu thức bay có đúng ý đồ không.

---

## 3. Quy trình Scrum

Scrum là quy trình Agile thông dụng nhất, tập trung mạnh vào quản lý và tổ chức tiến độ dự án.

**1. Khái niệm Sprint và Increment**
- **Lý thuyết:** Quá trình phát triển được chia thành các chu kỳ ngắn, cố định thời gian (time-boxed) gọi là Sprint (thường kéo dài khoảng 30 ngày / 2-4 tuần). Kết thúc mỗi Sprint, team phải bàn giao được một "Increment" - một phần của phần mềm đã chạy tốt và mang lại giá trị sử dụng.
- **Ví dụ (Game MOBA):** Dự án chia làm nhiều Sprint, mỗi Sprint kéo dài 30 ngày. Kết thúc Sprint 1, team phải giao được 1 bản game cho phép 2 người chơi có thể đăng nhập, vào chung 1 phòng và di chuyển quanh bản đồ (đây là 1 Increment chạy được).

**2. Product Backlog và Sprint Backlog**
- **Lý thuyết:** 
  - *Product Backlog:* Danh sách toàn bộ mọi yêu cầu, tính năng mà khách hàng mong muốn có trong sản phẩm, được Product Owner sắp xếp theo độ ưu tiên.
  - *Sprint Backlog:* Danh sách một số yêu cầu được team rút ra từ Product Backlog trong buổi họp kế hoạch để cam kết hoàn thành trong 1 Sprint sắp tới.
- **Ví dụ (Game MOBA):** 
  - *Product Backlog:* Bao gồm hàng chục tính năng như Hệ thống bạn bè, Hệ thống nạp thẻ, Mua Skin, Khóa tài khoản AFK. 
  - *Sprint Backlog:* Trong tháng này, team chỉ bốc đúng "Hệ thống bạn bè" ra để làm và cho vào Sprint Backlog.

**3. Họp Scrum hàng ngày (Daily Scrum Meeting)**
- **Lý thuyết:** Toàn bộ đội ngũ phát triển đứng họp nhanh khoảng 15 phút mỗi ngày để đồng bộ tiến độ. Mỗi người phải trả lời 3 câu hỏi: Đã làm gì kể từ buổi họp trước? Có gặp khó khăn/trở ngại gì không? Sẽ làm gì trước buổi họp kế tiếp?
- **Ví dụ (Game MOBA):** Đúng 9h sáng, team đứng họp vòng tròn. Dev A báo cáo: "Hôm qua tôi đã làm xong giao diện Tìm trận. Hôm nay tôi sẽ làm logic xử lý hàng chờ. Tôi đang bị kẹt vì chưa có API lưu dữ liệu từ đội Database."

**4. Đánh giá và Rút kinh nghiệm cuối Sprint (Review & Retrospective)**
- **Lý thuyết:** Khi hết khung thời gian của Sprint, đội cùng ngồi lại với nhau để xem xét phần mềm vừa tạo ra, kiểm tra xem đội đã làm việc tốt chưa và tìm ra các điểm/quy trình cần cải tiến cho Sprint tiếp theo.
- **Ví dụ (Game MOBA):** Cuối tháng, team họp lại và nhận ra khâu thiết kế hiệu ứng 3D bị chậm làm dev phải chờ. Team rút kinh nghiệm: từ Sprint sau, Artist phải gửi ảnh tĩnh (placeholder) cho Dev ráp vào code trước, hiệu ứng đẹp sẽ đắp vào sau.
