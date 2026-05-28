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

**2. Không được lắp ráp từ mẫu có sẵn**
- **Lý thuyết:** Phần mềm không có danh mục chi tiết cho trước như linh kiện phần cứng. Mỗi sản phẩm là một sản phẩm đặt hàng theo yêu cầu riêng, được xây dựng từ đầu hoặc tùy biến sâu để đáp ứng nhu cầu cụ thể của khách hàng/tổ chức.
- **Ví dụ (Game MOBA):** Không tồn tại "danh mục chi tiết tướng tiêu chuẩn" mà mọi công ty game đều dùng chung. Mỗi game MOBA (Liên Quân, DOTA 2, LoL) phải tự thiết kế bộ kỹ năng, bản đồ và hệ thống cân bằng riêng biệt hoàn toàn từ đầu.

**3. Phức tạp, khó hiểu và vô hình**
- **Lý thuyết:** Phần mềm không có hình dạng vật lý, không thể cầm nắm hay nhìn thấy trực tiếp được. Sự phức tạp bên trong (hàng triệu dòng code, hàng nghìn module phụ thuộc lẫn nhau) khiến không một cá nhân nào có thể hiểu toàn bộ hệ thống. Điều này gây khó khăn rất lớn cho việc giao tiếp giữa khách hàng và nhà phát triển.
- **Ví dụ (Game MOBA):** Nhà đầu tư không thể "nhìn" vào hệ thống matchmaking để biết nó hoạt động đúng hay sai — họ chỉ thấy kết quả (ghép trận nhanh hay chậm). Bên trong, hệ thống matchmaking có hàng chục thuật toán phức tạp mà ngay cả Dev cũng phải mất nhiều tuần để hiểu hết.

**4. Luôn luôn thay đổi (Thay đổi là bản chất của PM)**
- [Ở dưới]

**5. Được phát triển theo nhóm**
- **Lý thuyết:** Phần mềm hiện đại quá phức tạp để một người tự làm. Việc phát triển đòi hỏi nhiều kỹ năng khác nhau (phân tích, thiết kế, lập trình, kiểm thử, quản lý dự án) và có nhu cầu bàn giao nhanh, nên bắt buộc phải làm việc theo nhóm.
- **Ví dụ (Game MOBA):** Để phát triển game cần nhiều vai trò: Game Designer (thiết kế luật chơi), Programmer (viết code), Artist (vẽ đồ họa, tướng), Tester (kiểm thử), DevOps (vận hành server). Một mình không thể đảm nhận hết được, và nếu không phân công rõ ràng theo nhóm thì không thể bàn giao game kịp ngày ra mắt.

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
- **Lý thuyết:** Kỹ nghệ phần mềm (SE) là việc thiết lập và sử dụng các nguyên lý công nghệ đúng đắn để tạo ra phần mềm một cách kinh tế (tiết kiệm), vừa tin cậy vừa hoạt động hiệu quả trên máy thực.
- **Ví dụ (Game MOBA):** Việc phát triển game không chỉ đơn thuần là ngồi viết code theo bản năng, mà là việc áp dụng các nguyên lý thiết kế hệ thống, quản lý tài nguyên mạng và tổ chức nhân sự khoa học để game ra mắt đúng tiến độ, không bị đội chi phí và chạy mượt mà trên thiết bị của người chơi.

**2. Bốn lớp cơ bản của Kỹ nghệ phần mềm (Four Layers of SE)**
Kỹ nghệ phần mềm là một công nghệ phân tầng (layered technology). Bất kỳ phương pháp tiếp cận kỹ thuật nào cũng phải dựa trên một cam kết về chất lượng của tổ chức. Bốn lớp này xếp chồng lên nhau từ dưới lên trên, tạo thành nền tảng cho việc phát triển phần mềm:

- **1. Lớp Tập trung vào Chất lượng (A "Quality" Focus):**
  - **Lý thuyết:** Đây là **lớp nền móng (bedrock)** của công nghệ phần mềm. Mọi kỹ thuật, công cụ và quy trình được xây dựng đều phải tựa vào lớp nền tảng này. Nó bao gồm sự cam kết với toàn bộ các hoạt động quản lý chất lượng toàn diện (Total Quality Management - TQM, Six Sigma, v.v.). Trọng tâm của lớp này là việc thúc đẩy **văn hóa cải tiến quy trình liên tục** (continuous process improvement), tạo nên những cách thức phát triển phần mềm hiệu quả và ít lỗi hơn theo thời gian.
  - **Ví dụ (Game MOBA):** Ban giám đốc đưa ra cam kết chất lượng (QA) cao nhất: "Game không được phép giật lag, ping phải < 50ms, và không được có lỗi nghiêm trọng làm hỏng trải nghiệm đấu giải (eSports)". Nếu một bản cập nhật code mới chạy nhanh hơn nhưng lại phát sinh lỗi văng game, bản cập nhật đó sẽ bị loại bỏ vì vi phạm cam kết về chất lượng nền tảng này.

- **2. Lớp Quy trình (Process):**
  - **Lý thuyết:** Đây là **chất kết dính (glue)** giữ chặt các lớp của kỹ nghệ phần mềm với nhau. Quy trình cung cấp một **khung làm việc (framework)** thiết lập ra các khu vực quy trình quan trọng (Key Process Areas). Các khu vực này thiết lập bối cảnh để áp dụng các phương pháp kỹ thuật (khi nào thì dùng phương pháp gì), tạo ra các sản phẩm bàn giao (work products/deliverables), thiết lập các mốc thời gian (milestones), thiết lập các chốt kiểm soát chất lượng (quality assurance) và kiểm soát sự thay đổi (change management).
  - **Ví dụ (Game MOBA):** Đội ngũ phát triển thiết lập quy trình Scrum. Quy trình này quy định rõ: Dự án chia thành nhiều giai đoạn (Sprint), cứ 2 tuần (milestone) thì phải bàn giao 1 tính năng chơi thử được (work product). Nhờ quy trình này, toàn bộ công việc từ thiết kế, code đến test được tổ chức lại một cách có trật tự, thay vì mọi người làm việc tùy hứng.

- **3. Lớp Phương pháp (Method):**
  - **Lý thuyết:** Phương pháp cung cấp các câu trả lời **"làm thế nào" (how-to)** mang tính kỹ thuật để xây dựng phần mềm (đi vào chi tiết cụ thể hơn lớp Quy trình). Phương pháp bao gồm một mảng rộng các công việc kỹ thuật: giao tiếp (communication), phân tích yêu cầu (requirements analysis), mô hình hóa thiết kế (design modeling), xây dựng chương trình/viết mã nguồn (program construction), kiểm thử (testing) và hỗ trợ (support). Các phương pháp đều dựa trên một tập hợp các nguyên lý căn bản của chuyên ngành.
  - **Ví dụ (Game MOBA):** Khi thực thi các nhiệm vụ trong quy trình, team Dev áp dụng các phương pháp kỹ thuật cụ thể:
    - *Để thiết kế:* Dùng phương pháp Thiết kế hướng đối tượng (Object-Oriented Design) để thiết kế các class Tướng, class Trang bị.
    - *Để tìm lỗi:* Dùng phương pháp kiểm thử Hộp đen (Black-box Testing) kết hợp với kiểm thử hồi quy (Regression Testing) để kiểm tra xem chiêu cuối của tướng mới có hoạt động đúng không và có làm hỏng các tướng cũ không.

- **4. Lớp Công cụ (Tool):**
  - **Lý thuyết:** Công cụ cung cấp **sự hỗ trợ tự động (automated) hoặc bán tự động (semi-automated)** cho lớp Quy trình và Phương pháp. Khi các công cụ được tích hợp lại với nhau sao cho thông tin tạo ra bởi công cụ này có thể được sử dụng bởi công cụ khác, hệ thống đó được thiết lập thành **CASE** (Computer-Aided Software Engineering - Kỹ nghệ phần mềm có sự trợ giúp của máy tính).
  - **Ví dụ (Game MOBA):** Thay vì quản lý code và test thủ công, nhóm sử dụng bộ công cụ tích hợp (CASE): 
    - Lập trình bằng IDE (Unity/Rider).
    - Quản lý mã nguồn bằng Git (hỗ trợ bán tự động việc ghép code).
    - Quản lý tiến độ bằng Jira. Khi lập trình viên đẩy code lên Git và có từ khóa "Fix bug 123", hệ thống Jira tự động chuyển trạng thái công việc sang "Done". Đây là sự tự động hóa giúp giảm sai sót và tăng năng suất.

---

## 5. Tiến hóa Phần mềm và Thách thức

**1. Phần mềm bị thay đổi khi nào và như thế nào?**
- **Lý thuyết:** Thay đổi là bản chất của phần mềm. Thay đổi xảy ra cả trong **quá trình phát triển** (development) lẫn trong **quá trình sử dụng/bảo trì** (maintenance). Cụ thể, phần mềm bị thay đổi khi:
  - Một yêu cầu cũ bị sửa hoặc loại bỏ.
  - Một yêu cầu mới phát sinh.
  - Lỗi phát sinh (bug).
  - Môi trường phần mềm thay đổi (hệ điều hành, các hệ thống tương tác).
  - Môi trường phần cứng thay đổi.
- **Ví dụ (Game MOBA):** 
  - *Yêu cầu cũ bị sửa:* Cơ chế "mua đồ chỉ ở Tế đàn" bị sửa thành "mua đồ ở bất kỳ đâu" (trong giai đoạn phát triển, do Game Designer đổi ý).
  - *Yêu cầu mới:* Sau 1 năm vận hành, phát sinh yêu cầu thêm chế độ chơi mới "Đấu trường Aram" (trong giai đoạn bảo trì).
  - *Lỗi phát sinh:* Bug tướng X dùng chiêu cuối xuyên tường.
  - *Môi trường thay đổi:* Apple ra iOS 18, game phải cập nhật SDK mới để không bị crash.

**2. Nguyên nhân sâu xa của sự thay đổi**
- **Lý thuyết:** Có 5 nguyên nhân chính khiến phần mềm phải thay đổi:
  - *Quá trình thu thập, phân tích và đặc tả yêu cầu có vấn đề:* Sức ép thời gian, làm ẩu, khách hàng không biết hợp tác hoặc không diễn đạt rõ yêu cầu.
  - *Đảm bảo chất lượng có vấn đề:* Kiểm thử không đủ kỹ, bỏ sót lỗi.
  - *Nhu cầu con người ngày càng cao và phức tạp:* Người dùng luôn đòi hỏi thêm tính năng mới.
  - *Nghiệp vụ của tổ chức thay đổi/tái cấu trúc:* Doanh nghiệp đổi chiến lược kinh doanh, sáp nhập, mở rộng.
  - *Môi trường phần mềm thường xuyên thay đổi:* Hệ điều hành nâng cấp, thư viện bên thứ 3 ngừng hỗ trợ, phần cứng đổi thế hệ.
- **Ví dụ (Game MOBA):** Nguyên nhân game phải update liên tục: Team QA không đủ thời gian test kỹ trước ngày ra mắt nên còn nhiều bug (chất lượng có vấn đề). Cộng đồng game thủ liên tục đòi thêm chế độ chơi mới, tướng mới (nhu cầu ngày càng cao). Nhà phát hành đổi chiến lược sang thị trường eSports, yêu cầu thêm hệ thống giải đấu (nghiệp vụ thay đổi). Google Play yêu cầu tất cả app phải target Android 14 (môi trường thay đổi).

**3. Thách thức đặt ra từ tiến hóa phần mềm**
- **Lý thuyết:** Sự thay đổi liên tục tạo ra 3 thách thức lớn:
  - *Tăng chi phí phát triển (rework):* Mỗi lần thay đổi yêu cầu giữa chừng, team phải làm lại (rework) những phần đã hoàn thành, tốn thêm thời gian và tiền bạc.
  - *Tăng chi phí bảo trì:* Chi phí bảo trì (sửa lỗi, nâng cấp sau khi phát hành) thường **gấp nhiều lần** chi phí phát triển ban đầu. Phát triển chỉ là phần nổi của tảng băng chìm.
  - *Phát sinh nhiều vấn đề lớn:* Về kỹ thuật (code cũ trở nên khó bảo trì — technical debt), về ứng dụng (tính năng mới xung đột với tính năng cũ).
  
  **Câu hỏi lớn chưa có lời đáp thỏa đáng:** Làm thế nào để phát triển các sản phẩm phần mềm có khả năng bảo trì với chi phí thấp và thời gian ngắn?
- **Ví dụ (Game MOBA):** Việc code ra bản game đầu tiên tốn 10 tỷ VNĐ. Nhưng việc vận hành, cân bằng tướng hàng tháng, chống hack và ra mắt sự kiện trong 10 năm tiếp theo tiêu tốn tới 100 tỷ VNĐ (chi phí bảo trì >> chi phí phát triển). Mỗi bản cập nhật lớn, team phải rework lại phần code matchmaking vì yêu cầu thay đổi liên tục, dẫn đến code ngày càng rối rắm (technical debt tích tụ).
