# Tài liệu ôn thi: Thiết kế Kiến trúc Phần mềm

---

## 1. Định nghĩa và Sự quan trọng của Kiến trúc Phần mềm

**1. Khái niệm Kiến trúc Phần mềm (Software Architecture)**
- **Lý thuyết:** Kiến trúc phần mềm là bản thiết kế mức cao của hệ thống. Theo Len Bass, nó là "tập hợp các cấu trúc dùng để suy luận về hệ thống, bao gồm các thành phần phần mềm (elements), các mối quan hệ (relations) giữa chúng, và thuộc tính của cả hai".
- **Ví dụ (Game MOBA):** Kiến trúc của game không quy định chi tiết code chiêu thức. Nó quy định game gồm 3 khối (elements) chính: Game Client (trên điện thoại), Matchmaking Server (ghép trận), và Database Server (lưu trữ). Mối quan hệ giữa Client và Server là truyền tải qua giao thức UDP (relations).

**2. Tại sao Kiến trúc Phần mềm lại quan trọng?**
- **Lý thuyết:** Kiến trúc quan trọng vì 4 lý do:
  - *Hỗ trợ giao tiếp giữa các bên liên quan (stakeholders):* Cung cấp bản thiết kế tổng thể để mọi người (Dev, Tester, PM, Khách hàng) cùng nhìn vào một bức tranh chung.
  - *Xác định các ràng buộc cho việc hiện thực hóa:* Kiến trúc là bản thiết kế mức cao, các thiết kế chi tiết sau này sẽ phải dựa trên các ràng buộc đã định trong kiến trúc.
  - *Dự đoán các thuộc tính chất lượng:* Cho phép đánh giá trước về hiệu năng, an ninh, tính sẵn sàng của hệ thống.
  - *Nâng cao độ chính xác của việc dự đoán chi phí và thời gian:* Giúp ước lượng nguồn lực cần thiết trước khi bắt tay vào code.
- **Ví dụ (Game MOBA):** Nhìn vào bản vẽ kiến trúc (có 3 cụm Server đặt ở 3 châu lục), Chủ đầu tư lập tức dự đoán được chi phí thuê máy chủ hàng tháng sẽ rất cao (dự đoán chi phí), nhưng bù lại đảm bảo được hiệu năng không bị lag cho game thủ ở mọi khu vực (dự đoán thuộc tính chất lượng).

---

## 2. Ba loại Cấu trúc Thiết kế

**Khái niệm:** Cấu trúc thiết kế = elements + mối quan hệ giữa các elements. Một hệ thống phần mềm được thể hiện từ nhiều cấu trúc thiết kế khác nhau, mỗi loại thể hiện một khía cạnh khác nhau. Khi một cấu trúc được sử dụng phổ biến để giải quyết một vấn đề cụ thể, ta gọi đó là **mẫu kiến trúc (architecture pattern)**.

**1. Cấu trúc Mô đun (Module structures)**
- **Lý thuyết:** Thể hiện hệ thống là tập các phần mã nguồn (classes, layers, ...). Trả lời các câu hỏi:
  - Các chức năng chính của từng mô đun là gì?
  - Mối quan hệ phụ thuộc giữa các mô đun như thế nào?
  
  Ý nghĩa: lý giải được **khả năng chỉnh sửa** (modifiability) của hệ thống.
- **Ví dụ (Game MOBA):** Cấu trúc mã nguồn được chia thành gói `Network` (xử lý kết nối mạng, gửi/nhận gói tin) và gói `Graphics` (xử lý hình ảnh 3D, hiệu ứng chiêu thức). Gói `Graphics` phụ thuộc vào gói `GameLogic` (để biết vị trí tướng mà vẽ), nhưng không phụ thuộc vào `Network`. Nhờ vậy, khi cần nâng cấp đồ họa, Dev chỉ cần sửa gói `Graphics` mà không đụng tới mạng.

**2. Cấu trúc Thành phần - Kết nối (Component-and-connector structures)**
- **Lý thuyết:** Thể hiện các thành phần của hệ thống và sự tương tác giữa chúng trong **thời gian thực thi (runtime)**. Trả lời các câu hỏi:
  - Thành phần nào là thành phần chính và tương tác với các thành phần khác như thế nào?
  - Phần nào của hệ thống sẽ được nhân bản (duplicated)?
  - Dữ liệu được xử lý trong hệ thống như thế nào?
  - Những phần nào có thể chạy song song?
  
  Ý nghĩa: lý giải về **hiệu năng** (performance), **tính bảo mật** (security) và **tính hợp lệ** (availability).
- **Ví dụ (Game MOBA):** Khi một trận đấu 5v5 đang diễn ra (runtime), cấu trúc C&C cho thấy:
  - *Thành phần chính:* **Game Logic Process** (xử lý toàn bộ logic trận đấu) là thành phần trung tâm, tương tác với **Input Handler** (nhận lệnh di chuyển/tung chiêu từ 10 người chơi) và **Rendering Engine** (gửi trạng thái game để hiển thị).
  - *Nhân bản:* Thành phần **Player Connection Handler** được nhân bản thành 10 bản (mỗi bản phục vụ 1 người chơi), tất cả đều gửi dữ liệu về 1 **Game Logic Process** duy nhất.
  - *Luồng dữ liệu:* Lệnh di chuyển từ Client → Input Handler → Game Logic (tính toán vị trí mới, va chạm) → State Broadcaster (phát trạng thái game mới) → Client hiển thị.
  - *Chạy song song:* **Damage Calculator** (tính sát thương) và **Collision Detector** (phát hiện va chạm) chạy song song trên 2 thread riêng biệt, cả hai chỉ tồn tại trong suốt thời gian trận đấu (từ khi bắt đầu đến khi kết thúc trận).

**3. Cấu trúc Phân phối (Allocation structures)**
- **Lý thuyết:** Thể hiện mối quan hệ giữa hệ thống phần mềm và các yếu tố bên ngoài (CPU, file systems, networks, ...). Trả lời các câu hỏi:
  - Thành phần nào sẽ chạy trên bộ xử lý nào?
  - Các mô đun sẽ được lưu trữ trên thư mục, file nào?
  - Các mô đun được phân công cho đội phát triển như thế nào?
- **Ví dụ (Game MOBA):** Database Server được cấu hình chạy trên hệ thống máy chủ Cloud của Amazon (AWS ap-southeast-1, Singapore). Game Client được tải xuống và chạy trên chip CPU điện thoại người dùng. Mô đun `Matchmaking` do Team Backend (5 người) phát triển, mô đun `Graphics` do Team Client (3 người) phát triển.

---

## 3. Năm Bước Thiết kế Kiến trúc

Thiết kế kiến trúc là một quá trình lặp. Đầu vào: yêu cầu chức năng, phi chức năng (các ràng buộc). Đầu ra: bản thiết kế kiến trúc.

**1. Xác định mục tiêu (Identify Architecture Goals)**
- **Lý thuyết:** Trả lời 3 câu hỏi: Thiết kế kiến trúc để làm gì? Cho ai? Các ràng buộc (phạm vi, thời gian) là gì?
- **Ví dụ (Game MOBA):** Mục tiêu: "Thiết kế kiến trúc cho hệ thống game MOBA mobile, phục vụ 5 triệu người chơi đồng thời ở khu vực Đông Nam Á, hoàn thành thiết kế trong 2 tháng".

**2. Xác định các hoạt cảnh sử dụng chính (Key Scenarios)**
- **Lý thuyết:** Một hoạt cảnh (scenario) là sự tổng quát của nhiều ca sử dụng (use case) tương tự. Hoạt cảnh chính là hoạt cảnh có ảnh hưởng lớn, được sử dụng nhiều, và thể hiện sự "đánh đổi" (trade-off) giữa các thuộc tính chất lượng.
- **Ví dụ (Game MOBA):** Hoạt cảnh chính: "10 người chơi tham gia trận đấu thời gian thực". Hoạt cảnh này có ảnh hưởng lớn nhất và đòi hỏi sự đánh đổi giữa hiệu năng (cần phản hồi < 50ms) và an ninh (cần xác thực mọi hành động để chống hack).

**3. Tổng quan về ứng dụng (Application Overview)**
- **Lý thuyết:** Xác định kiểu ứng dụng (web, mobile, desktop), xác định các ràng buộc triển khai, các kiểu kiến trúc có thể sử dụng, và các công nghệ liên quan. Từ đó phác thảo kiến trúc tổng quan.
- **Ví dụ (Game MOBA):** Xác định: Kiểu ứng dụng = Mobile app (iOS + Android). Ràng buộc triển khai = Server đặt tại Singapore. Kiến trúc = Client/Server + Microservices. Công nghệ = Unity (Client), Go (Server), Redis (Cache).

**4. Xác định các vấn đề chính (Key Issues)**
- **Lý thuyết:** Đánh giá các thuộc tính chất lượng cần quan tâm: Tính hợp lệ (availability), Tính linh hoạt (modifiability), Tính khả chuyển (portability), Tính sử dụng lại (reusability), Tính hiệu năng (performance), Tính an ninh (security).
- **Ví dụ (Game MOBA):** Vấn đề chính được xác định: Hiệu năng (làm sao phản hồi < 50ms cho 10 triệu người?), An ninh (làm sao ngăn chặn hack map, hack sát thương?), Hợp lệ (nếu 1 server sập, người chơi có bị ảnh hưởng không?).

**5. Xác định các giải pháp chính (Candidate Solutions)**
- **Lý thuyết:** Đề xuất các giải pháp kiến trúc cụ thể để giải quyết từng vấn đề đã xác định ở bước 4.
- **Ví dụ (Game MOBA):** Giải pháp cho Hiệu năng: Dùng giao thức UDP thay vì TCP, đặt server gần người chơi. Giải pháp cho An ninh: Toàn bộ logic tính sát thương chạy phía Server (authoritative server), Client chỉ hiển thị kết quả. Giải pháp cho Hợp lệ: Thiết kế cơ chế failover — khi server A sập, tự động chuyển sang server B.

---

## 4. Các Nguyên lý Thiết kế (Design Principles)

**1. Phân tách các khía cạnh (Separation of concerns) & Trách nhiệm đơn (Single responsibility)**
- **Lý thuyết:** Chia ứng dụng thành các phần càng ít sự chồng chéo về chức năng càng tốt, đồng thời hạn chế tối đa sự tương tác giữa các thành phần (giảm sự phụ thuộc — coupling, tăng sự kết dính — cohesion). Mỗi thành phần chỉ thực hiện đúng một chức năng hoặc một tập chức năng gắn kết chặt chẽ.
- **Ví dụ (Game MOBA):** Module "Tính toán sát thương" chỉ làm đúng việc nhận đầu vào (Công vật lý, Giáp đối phương) và trả ra kết quả (Máu bị trừ). Việc hiển thị dòng chữ "−500 HP" bay lên màn hình do module "UI Graphics" đảm nhận. Nếu sau này muốn đổi font chữ hiệu ứng, logic tính sát thương không bị ảnh hưởng.

**2. Hiểu biết tối thiểu (Least knowledge)**
- **Lý thuyết:** Các thành phần không cần biết chi tiết bên trong của các thành phần khác (tính đóng gói / encapsulation). Một thành phần chỉ giao tiếp với thành phần khác thông qua giao diện công khai (interface).
- **Ví dụ (Game MOBA):** Module `Matchmaking` (ghép trận) chỉ biết rằng `PlayerService` có hàm `getPlayerRank(playerId)` trả về hạng của người chơi. Nó không biết (và không cần biết) rằng bên trong `PlayerService` đang dùng Redis cache hay truy xuất trực tiếp từ PostgreSQL.

**3. Không lặp lại (DRY - Don't Repeat Yourself)**
- **Lý thuyết:** Mỗi một chức năng chỉ được hiện thực hóa bởi đúng một thành phần duy nhất. Tránh copy-paste code.
- **Ví dụ (Game MOBA):** Thuật toán "Tính sát thương" được viết thành 1 hàm `calculateDamage()` duy nhất dùng chung. Khi trụ bắn, lính đánh, hay tướng xả chiêu đều gọi hàm này thay vì mỗi nơi viết một hàm tính riêng.

**4. Hạn chế thiết kế trước (YAGNI - You Ain't Gonna Need It)**
- **Lý thuyết:** Chỉ thiết kế khi cần và khi có đủ thông tin. Không nên thiết kế dự phòng cho các tính năng chưa chắc sẽ cần trong tương lai.
- **Ví dụ (Game MOBA):** Team Dev không thiết kế sẵn module "Hệ thống VR" trong kiến trúc game mobile hiện tại chỉ vì "biết đâu sau này cần". Khi nào có yêu cầu VR rõ ràng, mới bắt đầu thiết kế.

---

## 5. Một số Kiểu Kiến trúc (Architecture Patterns)

**1. Kiến trúc Khách/Chủ (Client/Server)**
- **Lý thuyết:** Thuộc cấu trúc thành phần – kết nối (C&C). Hệ thống tách làm hai phần: Client (gửi yêu cầu) và Server (xử lý và trả kết quả). Hỗ trợ cấu hình 1-1 (1 client kết nối 1 server), 1-n (1 client kết nối nhiều server), n-1 (nhiều client kết nối 1 server). Client có thể là ứng dụng desktop, web browser, hoặc ứng dụng di động. Có 2 biến thể quan trọng:
  - *Client-Queue-Client:* Các client giao tiếp với nhau thông qua hàng đợi (queue). Server chỉ đóng vai trò là hàng đợi bị động để chứa dữ liệu (passive queue).
  - *Peer-to-Peer (P2P):* Client và Server có thể đổi vai trò cho nhau.
- **Ví dụ (Game MOBA):** 
  - *Cấu hình n-1:* 10 điện thoại người chơi (n Clients) cùng kết nối vào 1 Game Server trong trận đấu. Client gửi lệnh "Di chuyển lên trên", Server tính toán và trả về vị trí mới.
  - *Client-Queue-Client:* Hệ thống chat trong game: Khi người chơi A gửi tin nhắn "Rush Baron!", tin nhắn được đẩy vào hàng đợi (message queue) trên server, và tất cả đồng đội sẽ lấy tin nhắn từ hàng đợi đó.

**2. Kiến trúc Monolithic (Nguyên khối)**
- **Lý thuyết:** Giao diện người dùng và mã nguồn logic được kết hợp thành 1 chương trình duy nhất từ một nền tảng duy nhất (ví dụ: đóng gói thành 1 file WAR chạy trên Tomcat).
  - *Ưu điểm:*
    - Dễ phát triển: nhiều IDE hỗ trợ.
    - Dễ triển khai: chỉ cần tạo file WAR đưa lên server.
    - Dễ mở rộng ban đầu: có thể tạo nhiều bản sao (copies) của file WAR.
  - *Nhược điểm (khi mã nguồn đủ lớn):*
    - Không có sự phân tách rõ ràng giữa các thành phần nên khó hiểu.
    - Web container tốn nhiều thời gian để khởi chạy file WAR.
    - Tạo nhiều bản sao tốn RAM và gặp vấn đề I/O.
    - Không phù hợp khi có nhiều đội phát triển (cập nhật 1 module nhỏ phải build lại toàn bộ WAR).
    - Khó áp dụng công nghệ mới.
- **Ví dụ (Game MOBA):** Ngày xưa, toàn bộ logic từ Đăng nhập, Cửa hàng skin, đến Chơi game đều nhồi chung 1 server (1 file WAR). Cứ mỗi lần update thêm 1 trang phục mới, phải build lại toàn bộ file WAR và khởi động lại server → game phải bảo trì sập toàn bộ hệ thống trong 5 tiếng.

**3. Kiến trúc Microservices (Vi dịch vụ)**
- **Lý thuyết:** Giải quyết các vấn đề của Monolithic. Kiến trúc gồm một tập các service, mỗi service có một vai trò riêng, có thể được phát triển và triển khai độc lập. Các service giao tiếp với nhau qua HTTP/REST. Các công ty lớn đang dùng: Netflix, Amazon, eBay, Uber, SoundCloud.
- **Ví dụ (Game MOBA):** Game được tách thành các dịch vụ độc lập: "Dịch vụ Đăng nhập", "Dịch vụ Cửa hàng", "Dịch vụ Ingame". Nếu ngày Giáng sinh, số lượng người mua trang phục quá tải làm sập "Dịch vụ Cửa hàng", thì những người đang trong trận đấu (Dịch vụ Ingame) vẫn không bị giật lag hay văng game. Team Cửa hàng chỉ cần restart lại service của mình mà không ảnh hưởng ai.

**4. Kiến trúc Phân lớp (Layered)**
- **Lý thuyết:** Nhóm các chức năng có liên quan chặt chẽ vào chung một lớp. Các lớp được sắp xếp chồng lên nhau, chỉ lớp trên mới sử dụng chức năng của lớp dưới (gọi xuống, không gọi ngược lên).
- **Ví dụ (Game MOBA):** Trong màn hình lịch sử đấu: Tầng UI (hiển thị bảng KDA) → gọi xuống Tầng Logic (tính toán tỉ lệ thắng, trung bình kills) → gọi xuống Tầng Database (truy vấn bảng `match_history` trong PostgreSQL). Tầng Database không bao giờ gọi ngược lên Tầng UI.

**5. Kiến trúc Ống dẫn và Bộ lọc (Pipe and Filter)**
- **Lý thuyết:** Dữ liệu chảy qua một chuỗi các bước xử lý. Mỗi bước gọi là một **bộ lọc (filter)** — nơi xử lý/biến đổi dữ liệu. Giữa các bộ lọc là các **ống dẫn (pipe)** — đường truyền dữ liệu. Các bộ lọc hoạt động độc lập với nhau, chỉ biết dữ liệu đầu vào và đầu ra.
- **Ví dụ (Game MOBA):** Hệ thống phát hiện hành vi gian lận (anti-cheat pipeline): Dữ liệu hành vi người chơi → **Filter 1: Phát hiện tốc độ di chuyển bất thường** (tốc độ > 500 unit/s → gắn cờ) → **Filter 2: Phát hiện sát thương bất thường** (dame > 9999 → gắn cờ) → **Filter 3: Quyết định** (nếu có ≥ 2 cờ → ban tài khoản). Mỗi filter hoạt động độc lập, có thể thêm/bớt filter mới mà không ảnh hưởng các filter còn lại.

**6. Kiến trúc Hướng dữ liệu (Data-centered)**
- **Lý thuyết:** Trung tâm của kiến trúc là một **kho dữ liệu chung (data store)**. Các **phần mềm khách (client software)** truy cập vào kho dữ liệu này để thêm/xóa/sửa/đọc dữ liệu. Các client không giao tiếp trực tiếp với nhau mà thông qua data store.
- **Ví dụ (Game MOBA):** Kho dữ liệu chung là Database chứa thông tin tất cả tướng (chỉ số, kỹ năng). Các client gồm: "Module Cân bằng tướng" (đọc/sửa chỉ số tướng), "Module Cửa hàng" (đọc danh sách tướng để hiển thị giá), "Module Ingame" (đọc chỉ số tướng khi vào trận). Tất cả đều truy cập cùng một database, không giao tiếp trực tiếp với nhau.

---

## 6. Thuộc tính Chất lượng Phần mềm (Quality Attributes)

**Khái niệm:** Thuộc tính chất lượng là một **độ đo hệ thống có thể đánh giá được và định lượng được**, từ đó làm rõ mức độ mà hệ thống thỏa mãn yêu cầu của các bên liên quan.

**1. Tính hợp lệ / Sẵn sàng (Availability)**
- **Lý thuyết:** Đo mức độ sẵn sàng của hệ thống để thực hiện tác vụ khi cần. Sử dụng công thức: Availability = MTBF / (MTBF + MTTR). Trong đó MTBF = thời gian trung bình giữa các lần lỗi, MTTR = thời gian trung bình để sửa lỗi.
- **Ví dụ (Game MOBA):** Server game hoạt động 720 giờ/tháng, sập 2 lần, mỗi lần mất 1 giờ để phục hồi. MTBF = 720/2 = 360 giờ, MTTR = 1 giờ. Availability = 360/(360+1) ≈ 99.7%.

**2. Tính linh hoạt (Modifiability)**
- **Lý thuyết:** Đánh giá khả năng thay đổi một thành phần X mà không ảnh hưởng đến phần còn lại. Trả lời câu hỏi: "Chúng ta có thể thay đổi thành phần X không?"
- **Ví dụ (Game MOBA):** Khi muốn đổi thuật toán ghép trận từ "theo rank" sang "theo MMR ẩn", team chỉ cần sửa module `Matchmaking` mà không cần đụng vào module `Ingame` hay `Database`. Kiến trúc có tính linh hoạt cao.

**3. Tính khả chuyển (Portability)**
- **Lý thuyết:** Đánh giá khả năng triển khai hệ thống trên một máy/môi trường khác. Trả lời câu hỏi: "Chúng ta có thể triển khai trên một máy khác không?"
- **Ví dụ (Game MOBA):** Game ban đầu chỉ chạy trên Android. Nhờ kiến trúc tách biệt (Game Logic viết bằng C# trên Unity, không phụ thuộc vào API riêng của Android), team Dev có thể port sang iOS chỉ trong 2 tháng.

**4. Tính sử dụng lại (Reusability)**
- **Lý thuyết:** Đánh giá khả năng sử dụng lại một phần hoặc toàn bộ hệ thống cho ứng dụng khác. Trả lời câu hỏi: "Chúng ta có thể sử dụng lại cho ứng dụng khác không?"
- **Ví dụ (Game MOBA):** Module `Network` (xử lý kết nối UDP, đồng bộ trạng thái real-time) được thiết kế đủ tổng quát để có thể tái sử dụng cho dự án game Battle Royale tiếp theo của công ty mà không cần viết lại từ đầu.

**5. Tính hiệu năng (Performance)**
- **Lý thuyết:** Đo thời gian hệ thống phản hồi tương tác của người dùng. Cải thiện bằng cách: phân rã thành các tiến trình chạy song song, quản lý lượng/tần suất dữ liệu truyền nhận, xác định "nút cổ chai" (bottleneck) của hệ thống.
- **Ví dụ (Game MOBA):** Khi có 10 triệu người chơi đồng thời, team Dev không để 1 server xử lý mọi thứ (nút cổ chai). Họ tạo ra 1000 cụm máy chủ và phân tải đều (load balancing) để mỗi cụm chỉ phục vụ 10,000 người, đảm bảo ping < 50ms.

**6. Tính an ninh (Security)**
- **Lý thuyết:** Đo khả năng hệ thống bảo vệ dữ liệu và thông tin từ các truy cập bất hợp pháp, trong khi vẫn cho phép người dùng/hệ thống hợp lệ được truy cập. Cải thiện bằng cách: phân chia chức năng cần/không cần login, cấu trúc phần mềm thành nhiều tầng bảo mật.
- **Ví dụ (Game MOBA):** Mọi dữ liệu tính toán sát thương đều chạy ở phía Server (authoritative server), Client chỉ hiển thị kết quả chứ không có quyền sửa đổi → ngăn chặn phần mềm hack map, hack sát thương. Ngoài ra, API mua trang phục yêu cầu login + xác thực token, còn API xem bảng xếp hạng thì không cần login.
