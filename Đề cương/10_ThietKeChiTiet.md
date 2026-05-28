# Tài liệu ôn thi: Thiết kế Chi tiết (Component-Level Design)

*Tham khảo: Pressman - Software Engineering: A Practitioner's Approach, Chương 11 (Mục 11.1 – 11.5)*

---

## 1. Bức tranh lớn về giai đoạn Thiết kế

**1. Các hoạt động thiết kế trong giai đoạn thiết kế**
- **Lý thuyết:** Trong giai đoạn thiết kế, nhà phát triển chia công việc thành các hoạt động thiết kế tách biệt:
  - *Thiết kế kiến trúc mức cao (High-level / Architecture Design):* Xác định các thành phần chính của hệ thống và mối quan hệ giữa chúng (đã học ở bài trước).
  - *Thiết kế giao diện (Interface Design):* Thiết kế cách người dùng tương tác với hệ thống (đã học ở bài trước).
  - *Thiết kế thành phần (Component Design):* Đi sâu vào chi tiết bên trong từng thành phần — thiết kế các lớp, thuộc tính, phương thức, thuật toán cụ thể (bài học này).
  - *Thiết kế CSDL (Database Design):* Thiết kế cấu trúc lưu trữ dữ liệu (bài học này).
- **Ví dụ (Game MOBA):** Ở bước thiết kế kiến trúc, ta đã xác định game gồm 3 thành phần lớn: Game Client, Game Server, Database Server. Bây giờ ở bước thiết kế chi tiết, ta đi sâu vào bên trong Game Server để thiết kế cụ thể các lớp như `MatchManager`, `HeroController`, `DamageCalculator` — mỗi lớp có những thuộc tính và phương thức gì, tương tác với nhau ra sao.

**2. Ôn lại: Thiết kế kiến trúc mức cao (High-level Design)**
- **Lý thuyết:** Thiết kế kiến trúc giúp xác định các thành phần chương trình (program components) chính để xây dựng phần mềm, cấu trúc dữ liệu, và mối quan hệ giữa các thành phần. Công việc này được thực hiện bởi chuyên gia (architect). Theo định nghĩa của OMG, một thành phần là *"a modular, deployable, and replaceable part of a system that encapsulates implementation and exposes a set of interfaces"* — tức là một phần của hệ thống có tính mô đun, có thể triển khai và thay thế được, đóng gói phần hiện thực bên trong và chỉ để lộ các giao diện ra bên ngoài.
- **Ví dụ (Game MOBA):** Thành phần `MatchmakingService` là một component — nó đóng gói toàn bộ thuật toán ghép trận bên trong, chỉ để lộ giao diện `findMatch(playerId)` cho bên ngoài gọi. Khi cần nâng cấp thuật toán ghép trận, ta thay thế component này mà không ảnh hưởng các component khác (deployable & replaceable).

---

## 2. Thiết kế mức Thành phần (Component-Level Design)

**3. Vấn đề và mục tiêu của thiết kế mức thành phần**
- **Lý thuyết:** Thiết kế tổng quan (kiến trúc) vẫn ở mức chung chung, chưa đi sâu vào chi tiết bên trong từng thành phần. Trong khi đó, lập trình viên cần một bản thiết kế chi tiết hơn để có thể bắt tay vào code. Do đó cần thực hiện **thiết kế mức thành phần** — chuyển từ mô tả trừu tượng sang mô tả cụ thể với các lớp, thuộc tính, phương thức, và thuật toán. Người thực hiện thiết kế mức thành phần là **Developer** (không nhất thiết phải là chuyên gia kiến trúc).
- **Ví dụ (Game MOBA):** Ở bước thiết kế kiến trúc, ta chỉ biết có một khối "Game Server" xử lý logic trận đấu. Nhưng Developer không thể code chỉ dựa vào thông tin đó. Thiết kế mức thành phần sẽ chỉ ra rằng bên trong Game Server có lớp `DamageCalculator` với phương thức `calculate(attacker, target): int`, lớp `CollisionDetector` với phương thức `checkCollision(skillshot, targets): List<Hero>`, v.v.

### 2.1. Các góc nhìn về Thành phần (Component Views)

**4. Tổng quan về các góc nhìn**
- **Lý thuyết:** Để hiểu đầy đủ về một thành phần, ta cần nhìn nó từ nhiều góc nhìn (view) khác nhau:
  - *Góc nhìn hướng đối tượng (Object-Oriented View):* Thành phần gồm nhiều lớp (class) hợp tác với nhau (trọng tâm bài học này).
  - *Góc nhìn truyền thống (Traditional View):* Thành phần là một module xử lý với đầu vào, đầu ra, và luồng xử lý [Đọc thêm].
  - *Góc nhìn quy trình (Process-Related View):* Thành phần được xem xét trong bối cảnh quy trình phát triển phần mềm [Đọc thêm].
- **Ví dụ (Game MOBA):** Với thành phần "Hệ thống chiến đấu" (Combat System), góc nhìn OO sẽ mô tả các lớp `Hero`, `Skill`, `DamageCalculator` và cách chúng tương tác. Góc nhìn truyền thống sẽ mô tả nó là một module nhận đầu vào (hành động tấn công) và trả đầu ra (kết quả sát thương). Góc nhìn quy trình sẽ xem xét thành phần này được phát triển ở sprint nào.

**5. Góc nhìn hướng đối tượng (Object-Oriented View)**
- **Lý thuyết:** Trong góc nhìn OO, một thành phần bao gồm **nhiều lớp (class) có liên quan và tương tác với nhau**. Khi biểu diễn từng lớp, các **thuộc tính (attributes)** và **phương thức (operations/methods) cốt lõi** sẽ được thể hiện. Quá trình thiết kế đi từ lớp phân tích (Analysis Class) → lớp thiết kế (Design Class) → lớp thiết kế chi tiết (Elaborated Design Class), trong đó mỗi bước bổ sung thêm chi tiết cụ thể hơn.
- **Ví dụ (Game MOBA):** Ban đầu ở giai đoạn phân tích, ta chỉ có lớp phân tích `Hero` với ý tưởng chung. Sang giai đoạn thiết kế, ta bổ sung thuộc tính: `name: String`, `hp: int`, `attackDamage: int`, và phương thức: `attack(target: Hero)`, `useSkill(skill: Skill)`. Sang thiết kế chi tiết, ta bổ sung thêm: kiểu trả về, xử lý ngoại lệ, quan hệ kế thừa (ví dụ `Mage extends Hero`), và giao diện mà component cung cấp (ví dụ interface `ICombatable`).

**6. Mức độ truy xuất (Access Modifiers)**
- **Lý thuyết:** Mỗi thuộc tính và phương thức trong một lớp đều có **mức độ truy xuất** quy định ai được phép truy cập:
  - `private` (-): Chỉ truy cập được **trong chính lớp đó**. Dùng để bảo vệ dữ liệu nội bộ.
  - `package` (~): Truy cập được bởi các lớp **trong cùng gói (package)**. Mức mặc định trong Java.
  - `protected` (#): Truy cập được bởi **lớp con (subclass) và các lớp cùng gói**.
  - `public` (+): Truy cập được từ **mọi nơi** trong chương trình.
- **Ví dụ (Game MOBA):** Lớp `Hero` có:
  - `private hp: int` → Chỉ lớp `Hero` mới được trực tiếp thay đổi máu, tránh bị hack từ bên ngoài.
  - `protected attackDamage: int` → Lớp con `Mage` kế thừa từ `Hero` có thể truy cập để tính sát thương phép.
  - `public getName(): String` → Bất kỳ nơi nào cũng có thể lấy tên tướng để hiển thị trên bảng điểm.
  - `~calculateInternalCooldown(): float` → Chỉ các lớp trong cùng package `combat` mới dùng được hàm tính thời gian hồi chiêu nội bộ.

**7. Từ lớp phân tích đến lớp thiết kế chi tiết (Analysis → Design → Elaborated Design Class)**
- **Lý thuyết:** Thiết kế mức thành phần hướng đối tượng trải qua quá trình tinh chỉnh dần:
  - *Lớp phân tích (Analysis Class):* Mô tả khái niệm từ nghiệp vụ, chưa có chi tiết kỹ thuật.
  - *Lớp thiết kế (Design Class):* Bổ sung kiểu dữ liệu, phương thức cụ thể, mối quan hệ giữa các lớp.
  - *Lớp thiết kế chi tiết (Elaborated Design Class):* Bổ sung thuật toán, xử lý ngoại lệ, giao diện mà component cung cấp cho bên ngoài, và cách component tương tác với các component khác.

  Một component thường cung cấp **giao diện (interface)** để các component khác sử dụng. Ví dụ trong slide: component PrintJob cung cấp hai giao diện `computeJob` và `initiateJob`.
- **Ví dụ (Game MOBA):** Component `CombatSystem` cung cấp hai giao diện:
  - `IAttackable` (giao diện cho hệ thống tấn công): có phương thức `dealDamage(source, target, amount)`.
  - `IBuffable` (giao diện cho hệ thống buff/debuff): có phương thức `applyBuff(target, buff)`.

  Các component khác như `SkillSystem` hay `TowerAI` chỉ tương tác với `CombatSystem` thông qua các giao diện này, không cần biết chi tiết bên trong.

---

### 2.2. Nguyên lý Thiết kế Hướng Đối tượng — SOLID

**8. SRP — The Single Responsibility Principle (Nguyên lý Trách nhiệm Đơn)**
- **Lý thuyết:** Một lớp đối tượng chỉ nên có **một và chỉ một lý do để thay đổi** — tức là chỉ đảm nhận **một nhiệm vụ duy nhất**. Nếu một lớp phải thay đổi vì 2 lý do khác nhau, thì nó đang vi phạm SRP và cần được tách ra. Nguyên lý này giúp giảm coupling và tăng cohesion. (Pressman, Mục 11.3)
- **Ví dụ (Game MOBA):** Lớp `Hero` chỉ chịu trách nhiệm quản lý trạng thái của tướng (máu, mana, vị trí). Việc tính sát thương được tách sang lớp `DamageCalculator`, việc hiển thị thanh máu tách sang lớp `HealthBarUI`. Nếu gộp cả 3 việc vào `Hero`, khi thay đổi cách hiển thị thanh máu, ta phải sửa lớp `Hero` — vi phạm SRP.

**9. OCP — The Open-Closed Principle (Nguyên lý Mở-Đóng)**
- **Lý thuyết:** Lớp đối tượng phải **mở cho việc mở rộng** (open for extension) nhưng **đóng cho việc chỉnh sửa** (closed for modification). Nghĩa là khi cần thêm chức năng mới, ta mở rộng bằng cách tạo lớp con hoặc implement interface, **không sửa mã nguồn hiện có**. Điều này đảm bảo code đã hoạt động ổn định không bị phá vỡ khi thêm tính năng. (Pressman, Mục 11.3)
- **Ví dụ (Game MOBA):** Lớp trừu tượng `Skill` có phương thức `execute()`. Khi thêm tướng mới với chiêu thức mới, ta chỉ cần tạo lớp con `FireballSkill extends Skill` và override phương thức `execute()`, mà **không cần sửa** bất kỳ dòng code nào trong lớp `Skill` gốc hay trong `Hero`. Nếu phải sửa lớp `Skill` mỗi khi thêm chiêu mới (ví dụ thêm `if-else`), ta đang vi phạm OCP.

**10. LSP — The Liskov Substitution Principle (Nguyên lý Thay thế Liskov)**
- **Lý thuyết:** Các **lớp con phải thay thế được cho lớp cha** mà không làm sai lệch hành vi của chương trình. Nghĩa là ở bất kỳ đâu trong code sử dụng đối tượng kiểu lớp cha, ta có thể thay bằng đối tượng kiểu lớp con mà chương trình vẫn hoạt động đúng. (Pressman, Mục 11.3)
- **Ví dụ (Game MOBA):** Lớp `Hero` có phương thức `attack(target)` trả về lượng sát thương > 0. Lớp con `Mage extends Hero` override phương thức `attack()` để tính sát thương phép. Hàm `processCombat(hero: Hero)` nhận tham số kiểu `Hero`, khi truyền vào đối tượng `Mage`, nó vẫn hoạt động đúng vì `Mage.attack()` vẫn trả về sát thương > 0 đúng như kỳ vọng. Nếu `Mage.attack()` trả về giá trị âm hoặc ném exception không mong muốn, ta vi phạm LSP.

**11. ISP — The Interface Segregation Principle (Nguyên lý Phân tách Giao diện)**
- **Lý thuyết:** **Phân tách các giao diện** sao cho client (lớp sử dụng) **không phải phụ thuộc vào các giao diện mà nó không sử dụng**. Thay vì tạo một giao diện lớn chứa nhiều phương thức, nên tách thành nhiều giao diện nhỏ, mỗi giao diện phục vụ một mục đích cụ thể. (Pressman, Mục 11.3)
- **Ví dụ (Game MOBA):** Thay vì tạo một giao diện `IGameEntity` chứa cả `attack()`, `move()`, `heal()`, `build()`, ta tách thành: `IAttackable` (có `attack()`), `IMovable` (có `move()`), `IHealable` (có `heal()`). Lớp `Tower` (trụ phòng thủ) chỉ implement `IAttackable` vì trụ chỉ cần tấn công, không cần di chuyển hay hồi máu. Nếu dùng `IGameEntity` lớn, `Tower` buộc phải implement `move()` — một phương thức vô nghĩa với trụ.

**12. DIP — The Dependency Inversion Principle (Nguyên lý Đảo ngược Phụ thuộc)**
- **Lý thuyết:** **Phụ thuộc vào lớp trừu tượng** (abstract class / interface) **thay vì lớp cụ thể** (concrete class). Các module cấp cao không nên phụ thuộc vào module cấp thấp; cả hai nên phụ thuộc vào abstraction. Điều này giúp giảm sự phụ thuộc cứng giữa các lớp, dễ dàng thay đổi implementation mà không ảnh hưởng đến code sử dụng. (Pressman, Mục 11.3)
- **Ví dụ (Game MOBA):** Lớp `MatchmakingService` cần lưu trữ dữ liệu. Thay vì phụ thuộc trực tiếp vào `MySQLDatabase` (lớp cụ thể), nó phụ thuộc vào interface `IDatabase` (lớp trừu tượng) có phương thức `save()`, `find()`. Lớp `MySQLDatabase` và `RedisCache` đều implement `IDatabase`. Khi muốn chuyển từ MySQL sang MongoDB, ta chỉ cần tạo lớp `MongoDatabase implements IDatabase` mà không cần sửa bất kỳ dòng code nào trong `MatchmakingService`.

---

## 3. Thiết kế Dữ liệu (Database Design)

### 3.1. Mô hình Thực thể – Quan hệ (Entity-Relationship Model - ERM)

**13. Khái niệm mô hình Thực thể – Quan hệ (ERM)**
- **Lý thuyết:** Mô hình thực thể – quan hệ (ERM) là **dạng tiền sơ khai** (precursor) để tạo ra một cơ sở dữ liệu hoàn chỉnh. ERM giúp mô hình hóa dữ liệu ở mức khái niệm trước khi chuyển sang thiết kế vật lý (bảng trong CSDL). Các thành phần chính của ERM:
  - **Thực thể (Entity):** Đại diện cho một đối tượng/khái niệm trong thế giới thực cần lưu trữ thông tin.
  - **Thuộc tính (Attribute):** Đặc điểm mô tả thực thể.
  - **Quan hệ (Relationship):** Mối liên kết giữa các thực thể.
  - **Thuộc tính của quan hệ:** Một số quan hệ có thể mang theo thuộc tính riêng.
- **Ví dụ (Game MOBA):** Trong hệ thống game, có thực thể `Hero` (thuộc tính: tên, vai trò, chỉ số cơ bản) và thực thể `Player` (thuộc tính: username, rank, level). Quan hệ giữa chúng là `Sở hữu` (Player sở hữu Hero). Thuộc tính của quan hệ `Sở hữu` có thể là `ngayMua` (ngày người chơi mua tướng) và `skinEquipped` (skin đang trang bị).

**14. Các bước xây dựng ERM**
- **Lý thuyết:** Quy trình xây dựng ERM gồm 4 bước:
  - **B1: Xác định các thực thể và thuộc tính** — Liệt kê tất cả các đối tượng cần lưu trữ và các đặc điểm của chúng.
  - **B2: Xác định các mối quan hệ và thuộc tính của quan hệ** — Xác định thực thể nào liên quan đến thực thể nào, và loại quan hệ (1-1, 1-n, n-n).
  - **B3: Vẽ biểu đồ ERM** — Biểu diễn trực quan các thực thể, thuộc tính, và quan hệ. Lưu ý: ERM ban đầu có thể **chưa tối ưu**.
  - **B4: Chuẩn hóa ERM (Normalization)** — Áp dụng các dạng chuẩn (1NF, 2NF, 3NF, ...) để loại bỏ dư thừa dữ liệu và bất thường khi thêm/sửa/xóa.
- **Ví dụ (Game MOBA):**
  - *B1:* Xác định thực thể: `Player` (username, rank), `Hero` (name, role, baseHP), `Match` (matchId, duration, result).
  - *B2:* Quan hệ: `Player` — Tham gia — `Match` (quan hệ n-n, thuộc tính quan hệ: `kills`, `deaths`, `assists`). `Player` — Sở hữu — `Hero` (quan hệ n-n, thuộc tính: `purchaseDate`).
  - *B3:* Vẽ sơ đồ ERM với 3 thực thể hình chữ nhật, 2 quan hệ hình thoi, các thuộc tính hình oval.
  - *B4:* Chuẩn hóa: tách bảng `Player_Hero` (chứa cặp playerId + heroId + purchaseDate) thay vì lưu danh sách hero dưới dạng chuỗi trong bảng `Player`.

### 3.2. Ánh xạ lớp Đối tượng vào CSDL (Object-to-Database Mapping)

**15. Nguyên tắc ánh xạ cơ bản**
- **Lý thuyết:** Khi chuyển từ thiết kế hướng đối tượng sang cơ sở dữ liệu quan hệ, cần tuân theo các nguyên tắc ánh xạ:
  - **Lớp đối tượng → Bảng (Table):** Mỗi lớp ánh xạ thành một bảng, thường cùng tên.
  - **Thuộc tính đơn giản → Cột (Column):** Mỗi thuộc tính của lớp trở thành một cột trong bảng.
- **Ví dụ (Game MOBA):** Lớp `Hero` có thuộc tính `name: String`, `role: String`, `baseHP: int` → Ánh xạ thành bảng `Hero` với 3 cột: `name VARCHAR(50)`, `role VARCHAR(20)`, `baseHP INT`.

**16. Ánh xạ quan hệ One-to-One (1-1)**
- **Lý thuyết:** Với quan hệ 1-1 giữa hai lớp, ta **thêm khóa ngoại (foreign key)** của bảng này vào bảng kia (chọn một trong hai bảng).
- **Ví dụ (Game MOBA):** Mỗi `Player` có đúng một `PlayerProfile` (hồ sơ chi tiết). Ta thêm cột `profileId` (khóa ngoại) vào bảng `Player` trỏ đến bảng `PlayerProfile`, hoặc ngược lại.

**17. Ánh xạ quan hệ One-to-Many (1-n)**
- **Lý thuyết:** Với quan hệ 1-n, ta **thêm khóa ngoại (foreign key) của bảng phía "One" vào bảng phía "Many"**. Bảng phía "Many" sẽ chứa cột tham chiếu đến bảng phía "One".
- **Ví dụ (Game MOBA):** Một `Team` có nhiều `Player` (1-n). Ta thêm cột `teamId` (khóa ngoại) vào bảng `Player` trỏ đến bảng `Team`. Mỗi dòng trong bảng `Player` sẽ có `teamId` cho biết player đó thuộc team nào.

**18. Ánh xạ quan hệ Many-to-Many (n-n)**
- **Lý thuyết:** Với quan hệ n-n, ta **tạo một bảng trung gian mới** chứa khóa chính của cả hai bảng (composite key). Bảng trung gian này cũng có thể chứa thêm các thuộc tính riêng của mối quan hệ.
- **Ví dụ (Game MOBA):** Quan hệ `Player` — Sở hữu — `Hero` là n-n (một người chơi sở hữu nhiều tướng, một tướng được nhiều người chơi sở hữu). Ta tạo bảng trung gian `Player_Hero` với các cột: `playerId` (FK → Player), `heroId` (FK → Hero), `purchaseDate DATE`, `skinEquipped VARCHAR(50)`. Khóa chính là cặp (`playerId`, `heroId`).
