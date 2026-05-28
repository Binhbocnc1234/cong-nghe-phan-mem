# Tài liệu ôn thi: Một số Kỹ thuật Kiểm thử

---

## 1. Kiểm thử dựa trên Phân tích Giá trị Biên (BVA - Boundary Value Analysis)

**1. Khái niệm BVA**
- **Lý thuyết:** BVA là kỹ thuật kiểm thử **hộp đen** (black-box testing). Xuất phát từ nhận xét thực tế: **các sai sót/lỗi trong phần mềm thường tập trung ở biên (boundary) của miền dữ liệu đầu vào**, chứ không phải ở giữa miền. Do đó, thay vì kiểm thử ngẫu nhiên, ta tập trung chọn các giá trị nằm ngay tại biên và lân cận biên để kiểm thử. [Không có trong sách — nội dung chủ yếu từ slide và tài liệu Jorgensen]
- **Ví dụ (Game MOBA):** Một tướng có chỉ số Công (ATK) hợp lệ trong khoảng [0, 999]. Lỗi thường xảy ra khi ATK = 0 (biên dưới) hoặc ATK = 999 (biên trên), ví dụ game crash khi ATK = 0 do chia cho 0 trong công thức tính sát thương. Do đó ta ưu tiên kiểm thử ở biên thay vì chỉ thử ATK = 500.

**2. Năm giá trị biên cơ bản**
- **Lý thuyết:** Với mỗi biến đầu vào `x` có miền giá trị `[min, max]`, BVA chọn **5 giá trị** đặc trưng để kiểm thử:
  - `min` — giá trị nhỏ nhất hợp lệ
  - `min + 1` — giá trị ngay trên biên dưới
  - `norm` — giá trị bình thường (thường ở giữa miền)
  - `max - 1` — giá trị ngay dưới biên trên
  - `max` — giá trị lớn nhất hợp lệ
- **Ví dụ (Game MOBA):** Biến "Cấp độ tướng" có miền [1, 15]. Năm giá trị biên: `min = 1`, `min+1 = 2`, `norm = 8`, `max-1 = 14`, `max = 15`. Ta sẽ kiểm thử hàm `levelUp()` với 5 giá trị này.

**3. Công thức tính số ca kiểm thử BVA cơ bản**
- **Lý thuyết:** Với `n` biến đầu vào, số ca kiểm thử BVA cơ bản là **4n + 1**. Cách tạo ca kiểm thử: giữ tất cả các biến ở giá trị `norm`, rồi lần lượt cho **từng biến** thay đổi qua 4 giá trị biên (`min`, `min+1`, `max-1`, `max`), cộng thêm 1 ca tất cả biến đều ở `norm`. Các biến được thay đổi **độc lập** — mỗi lần chỉ 1 biến thay đổi, các biến còn lại giữ nguyên `norm`.
- **Ví dụ (Game MOBA):** Hàm `createMatch(numPlayers, mapSize)` có 2 biến (n = 2). `numPlayers ∈ [2, 10]`, `mapSize ∈ [1, 5]`. Số ca = 4×2 + 1 = **9 ca**:
  - Ca 1: (norm, norm) = (6, 3)
  - Ca 2-5: Cố định mapSize = 3, numPlayers lần lượt = 2, 3, 9, 10
  - Ca 6-9: Cố định numPlayers = 6, mapSize lần lượt = 1, 2, 4, 5

---

### Loại 1 — BVA cơ bản (Normal BVA)

**4. BVA cơ bản — Phương pháp**
- **Lý thuyết:** Đây là loại BVA đơn giản nhất. Mỗi biến nhận 5 giá trị: {min, min+1, norm, max-1, max}. Mỗi lần chỉ **1 biến** được thay đổi, các biến còn lại giữ ở `norm`. Số ca kiểm thử = **4n + 1**. Phù hợp khi các biến đầu vào **độc lập** với nhau (không có ràng buộc lẫn nhau).
- **Ví dụ (Game MOBA):** Hàm `setVolume(musicVol, sfxVol)` với `musicVol ∈ [0, 100]`, `sfxVol ∈ [0, 100]`. Hai biến độc lập (âm lượng nhạc nền không ảnh hưởng đến âm lượng hiệu ứng). Số ca = 4×2 + 1 = 9. Ví dụ: (50, 0), (50, 1), (50, 99), (50, 100), (0, 50), (1, 50), (99, 50), (100, 50), (50, 50).

---

### Loại 2 — Kiểm thử biên mạnh (Robustness Testing)

**5. BVA mạnh — Mở rộng giá trị ngoài biên**
- **Lý thuyết:** Mở rộng BVA cơ bản bằng cách bổ sung **hai giá trị ngoài biên**: `min - 1` (ngay dưới biên dưới) và `max + 1` (ngay trên biên trên). Mục đích: kiểm tra xem chương trình có **kiểm tra tính hợp lệ** (validation) của dữ liệu đầu vào hay không — tức là có báo lỗi đúng cách khi nhận giá trị ngoài miền. Mỗi biến có 7 giá trị: {min-1, min, min+1, norm, max-1, max, max+1}. Số ca kiểm thử = **6n + 1**.
- **Ví dụ (Game MOBA):** Biến "Số lượng tướng được chọn trong đội" ∈ [1, 5]. Robustness testing thêm giá trị `min-1 = 0` (không chọn tướng nào) và `max+1 = 6` (chọn 6 tướng). Ca kiểm thử với giá trị 0 kiểm tra xem hệ thống có hiển thị lỗi "Bạn phải chọn ít nhất 1 tướng" không; ca với giá trị 6 kiểm tra xem hệ thống có chặn và báo "Tối đa 5 tướng" không.

---

### Loại 3 — Kiểm thử trường hợp xấu nhất (Worst-case Testing)

**6. Worst-case BVA — Khi các biến có tương tác**
- **Lý thuyết:** Khi các biến đầu vào **có tương tác** (ảnh hưởng lẫn nhau), BVA cơ bản không đủ vì nó chỉ thay đổi 1 biến mỗi lần. Worst-case testing khắc phục bằng cách cho **tất cả các biến đồng thời** nhận các giá trị biên. Mỗi biến nhận 5 giá trị: {min, min+1, norm, max-1, max}, sau đó lấy **tích Đề-các** (Cartesian product) của tất cả các biến. Số ca kiểm thử = **5^n**. Áp dụng khi: (1) các biến ảnh hưởng lớn đến nhau, hoặc (2) hàm sai sẽ gây hậu quả nghiêm trọng (ví dụ: hệ thống y tế, tài chính).
- **Ví dụ (Game MOBA):** Hàm `calculateDamage(atk, armor)` với `atk ∈ [0, 999]`, `armor ∈ [0, 500]`. Hai biến **tương tác** mạnh (sát thương = atk - armor). Số ca = 5² = **25 ca**. Ví dụ một số ca: (0, 0), (0, 1), (0, 250), (0, 499), (0, 500), (1, 0), (1, 1), ..., (999, 500). Ca (0, 500) phát hiện lỗi sát thương âm mà BVA cơ bản không tìm được.

---

### Loại 4 — Kiểm thử trường hợp xấu nhất mạnh (Robust Worst-case Testing)

**7. Robust Worst-case BVA — Kết hợp tất cả**
- **Lý thuyết:** Kết hợp ý tưởng của Robustness Testing (thêm giá trị ngoài biên) và Worst-case Testing (tích Đề-các). Mỗi biến nhận **7 giá trị**: {min-1, min, min+1, norm, max-1, max, max+1}, sau đó lấy tích Đề-các. Số ca kiểm thử = **7^n**. Đây là loại BVA toàn diện nhất nhưng tốn chi phí nhất.
- **Ví dụ (Game MOBA):** Hàm `calculateDamage(atk, armor)` với 2 biến. Số ca = 7² = **49 ca**. Bao gồm cả các ca ngoài biên như atk = -1 kết hợp armor = 501 — kiểm tra hệ thống xử lý đồng thời cả hai đầu vào không hợp lệ.

---

### Hạn chế của BVA

**8. Hạn chế của phương pháp BVA**
- **Lý thuyết:** BVA (đặc biệt loại cơ bản) chỉ hiệu quả khi **các biến đầu vào độc lập** với nhau. BVA **không quan tâm đến ràng buộc** (constraint) giữa các biến. Khi các biến có ràng buộc phức tạp (ví dụ: "nếu x > 5 thì y phải < 10"), BVA cơ bản có thể bỏ sót lỗi. Ngoài ra, BVA chủ yếu áp dụng cho **kiểu dữ liệu số**; với các kiểu khác như xâu ký tự, mảng, con trỏ, kiểu cấu trúc, cần cách tiếp cận khác hoặc phải định nghĩa lại khái niệm "biên".
- **Ví dụ (Game MOBA):** Hàm `createTeam(numWarriors, numMages)` có ràng buộc `numWarriors + numMages = 5`. BVA cơ bản tạo ca (1, 3) — norm cho cả hai — nhưng lại bỏ sót ca (3, 3) tổng bằng 6 (vi phạm ràng buộc). BVA không tự phát hiện được ràng buộc "tổng phải bằng 5".

---

### Tổng hợp 4 loại BVA

| Loại | Giá trị mỗi biến | Số ca kiểm thử | Đặc điểm |
|------|-------------------|-----------------|-----------|
| 1. BVA cơ bản | 5: {min, min+1, norm, max-1, max} | 4n + 1 | Chỉ thay đổi 1 biến/lần |
| 2. Robustness | 7: thêm min-1, max+1 | 6n + 1 | Kiểm tra validation ngoài biên |
| 3. Worst-case | 5 (tích Đề-các) | 5^n | Xét tương tác giữa các biến |
| 4. Robust Worst-case | 7 (tích Đề-các) | 7^n | Toàn diện nhất, chi phí cao nhất |

---

## 2. Kiểm thử Giá trị Đặc biệt (Special Value Testing)

**9. Khái niệm Kiểm thử Giá trị Đặc biệt**
- **Lý thuyết:** Đây là phương pháp kiểm thử **được thực hiện nhiều nhất trên thực tế**. Người kiểm thử sử dụng **kỹ nghệ (engineering judgment)** và **kiến thức về miền ứng dụng (domain knowledge)** để phán đoán các giá trị đặc biệt nào dễ gây lỗi, rồi chọn chúng làm đầu vào kiểm thử. Phương pháp này mang tính **chủ quan** cao (phụ thuộc vào kinh nghiệm và trực giác của người kiểm thử), nhưng thực tế cho thấy **vẫn rất hiệu quả** vì người có kinh nghiệm thường biết chỗ nào hay lỗi. [Không có trong sách]
- **Ví dụ (Game MOBA):** Một tester dày dặn kinh nghiệm biết rằng game hay crash khi tướng đứng **đúng vị trí gốc tọa độ (0, 0)** hoặc khi **2 tướng trùng tọa độ** (cùng đứng một chỗ). Dù BVA không tạo ra ca này, tester vẫn chủ động thử vì kinh nghiệm cho biết đây là giá trị đặc biệt dễ gây bug va chạm.

---

## 3. Kiểm thử Giá trị Ngẫu nhiên (Fuzzy Testing / Random Testing)

**10. Khái niệm Fuzzy Testing**
- **Lý thuyết:** Phương pháp kiểm thử bằng cách **sinh giá trị đầu vào ngẫu nhiên** và đưa vào chương trình chạy liên tục trong thời gian dài (nhiều giờ, nhiều ngày, thậm chí nhiều tuần). Mục đích: phát hiện lỗi bất ngờ mà các phương pháp có hệ thống có thể bỏ sót (đặc biệt là lỗi crash, memory leak, buffer overflow). Kết quả thực tế nổi tiếng: khi áp dụng fuzzy testing lên các hệ điều hành, tỉ lệ crash ghi nhận được: Windows NT ~21%, macOS X ~7%, Linux ~12%, FreeBSD ~19%. [Không có trong sách]
- **Ví dụ (Game MOBA):** Team QA viết script tự động sinh ngẫu nhiên hàng triệu lệnh: di chuyển đến tọa độ ngẫu nhiên, sử dụng chiêu thức ngẫu nhiên, mua trang bị ngẫu nhiên, rồi cho bot chạy liên tục 72 giờ. Kết quả phát hiện: game crash khi tướng di chuyển đến tọa độ âm (-500, -300) ngoài bản đồ — một lỗi mà không ai nghĩ tới khi viết ca kiểm thử thủ công.

---

## 4. Kiểm thử Lớp Tương đương (ECT - Equivalence Class Testing)

**11. Khái niệm và Ý tưởng ECT**
- **Lý thuyết:** ECT là kỹ thuật kiểm thử hộp đen dựa trên ý tưởng **phân hoạch (partition)** miền dữ liệu đầu vào thành các **lớp tương đương (equivalence classes)**. Hai nguyên tắc:
  - **Hợp** tất cả các lớp = toàn bộ miền đầu vào (đầy đủ, không sót).
  - **Hai lớp bất kỳ không giao nhau** (không trùng lặp).
  
  Ý tưởng cốt lõi: trong cùng một lớp tương đương, tất cả các giá trị được coi là **"giống nhau"** về mặt hành vi — nếu một giá trị phát hiện lỗi thì các giá trị khác trong cùng lớp cũng sẽ phát hiện lỗi đó, và ngược lại. Do đó, ta chỉ cần chọn **1 phần tử đại diện** từ mỗi lớp để kiểm thử, giúp vừa **có cảm giác kiểm thử đầy đủ** vừa **tránh dư thừa** (không thử lại các giá trị cho kết quả giống nhau).
- **Ví dụ (Game MOBA):** Biến "Cấp độ tướng" ∈ [1, 15]. Phân hoạch thành 3 lớp: Lớp "Giai đoạn đầu" [1-5], Lớp "Giữa game" [6-10], Lớp "Late game" [11-15]. Trong lớp [1-5], kiểm thử cấp 3 hay cấp 4 cho kết quả tương tự (hệ số sát thương giống nhau). Vậy ta chỉ cần chọn 1 đại diện mỗi lớp: cấp 3, cấp 8, cấp 13 → 3 ca kiểm thử thay vì 15.

**12. Cách chọn phân hoạch**
- **Lý thuyết:** Việc chọn phân hoạch (xác định các lớp tương đương) được thực hiện bằng cách:
  - **Thủ công (craft):** Dựa trên kinh nghiệm và trực giác.
  - **Dựa trên đặc tả (specification-based):** Đọc đặc tả yêu cầu để xác định các nhóm giá trị có hành vi khác nhau.
  - **Cần hiểu biết miền (domain knowledge):** Am hiểu nghiệp vụ để phân nhóm chính xác.
  
  Ngoài ra cần phân biệt: **lớp hợp lệ** (valid class) — giá trị hệ thống chấp nhận, và **lớp không hợp lệ** (invalid class) — giá trị hệ thống cần từ chối.
- **Ví dụ (Game MOBA):** Đặc tả nói: "Tên tướng phải từ 2-20 ký tự, chỉ chứa chữ cái". Phân hoạch cho biến "Tên tướng":
  - Lớp hợp lệ: chuỗi 2-20 ký tự, toàn chữ cái (VD: "Yasuo")
  - Lớp không hợp lệ 1: chuỗi rỗng hoặc 1 ký tự (VD: "Y")
  - Lớp không hợp lệ 2: chuỗi > 20 ký tự (VD: "AbcDefGhiJklMnoPqrStuVw")
  - Lớp không hợp lệ 3: chuỗi chứa ký tự đặc biệt (VD: "Ya$uo")

---

### Loại 1 — ECT truyền thống (Traditional ECT)

**13. ECT truyền thống — Phương pháp**
- **Lý thuyết:** Phân biệt rõ lớp hợp lệ và lớp không hợp lệ, sau đó tạo ca kiểm thử:
  - **Tc0 (ca chuẩn):** Tất cả các biến đều nhận giá trị từ lớp **hợp lệ** → kiểm tra hoạt động bình thường.
  - **Tc1, Tc2, ... (các ca lỗi):** Cố định `n-1` biến ở giá trị hợp lệ, **đổi 1 biến còn lại** sang giá trị từ lớp **không hợp lệ** → kiểm tra từng trường hợp lỗi riêng lẻ.
  
  Mục đích: đảm bảo hệ thống xử lý đúng cả trường hợp bình thường lẫn từng trường hợp lỗi riêng biệt.
- **Ví dụ (Game MOBA):** Hàm `register(username, password)`. Username hợp lệ: 3-15 ký tự chữ; Password hợp lệ: 8-20 ký tự.
  - Tc0: username = "Player01" (hợp lệ), password = "Abc12345" (hợp lệ) → đăng ký thành công.
  - Tc1: username = "" (không hợp lệ — rỗng), password = "Abc12345" (hợp lệ) → báo lỗi "Username không hợp lệ".
  - Tc2: username = "Player01" (hợp lệ), password = "123" (không hợp lệ — quá ngắn) → báo lỗi "Password quá ngắn".

---

### Loại 2 — ECT yếu (Weak ECT)

**14. ECT yếu — Lấy đại diện ít nhất 1 lần**
- **Lý thuyết:** Đảm bảo mỗi phần tử đại diện của mỗi lớp tương đương xuất hiện **ít nhất 1 lần** trong tập ca kiểm thử. Số ca kiểm thử tối thiểu = **số lớp của phân hoạch có nhiều tập con nhất** (max across all variables). ECT yếu giả định rằng các biến **không tương tác** với nhau.
- **Ví dụ (Game MOBA):** Hàm `matchmaking(rank, region)`. Biến `rank` có 3 lớp: {Đồng, Vàng, Kim Cương}. Biến `region` có 2 lớp: {VN, SEA}. Số ca tối thiểu = max(3, 2) = **3 ca**:
  - Ca 1: (Đồng, VN)
  - Ca 2: (Vàng, SEA)
  - Ca 3: (Kim Cương, VN)
  
  → Mỗi lớp của `rank` và `region` đều xuất hiện ít nhất 1 lần.

---

### Loại 3 — ECT mạnh (Strong ECT)

**15. ECT mạnh — Tích Đề-các**
- **Lý thuyết:** Dựa trên **tích Đề-các (Cartesian product)** của tất cả các lớp tương đương của tất cả các biến. Mỗi tổ hợp giá trị đại diện từ các lớp đều được tạo thành 1 ca kiểm thử. Số ca = tích số lớp của tất cả các biến. ECT mạnh xét **tất cả tương tác** giữa các giá trị đại diện, đảm bảo kiểm thử toàn diện hơn nhưng tốn chi phí hơn.
- **Ví dụ (Game MOBA):** Hàm `matchmaking(rank, region, mode)`. `rank` có 3 lớp: {Đồng, Vàng, Kim Cương}. `region` có 4 lớp: {VN, SEA, EU, NA}. `mode` có 2 lớp: {Xếp hạng, Thường}. Số ca = 3 × 4 × 2 = **24 ca**. Ví dụ: (Đồng, VN, Xếp hạng), (Đồng, VN, Thường), (Đồng, SEA, Xếp hạng), ..., (Kim Cương, NA, Thường).

---

### Tổng hợp 3 loại ECT

| Loại | Số ca kiểm thử | Đặc điểm |
|------|-----------------|-----------|
| 1. ECT truyền thống | 1 (tất cả hợp lệ) + k (mỗi ca đổi 1 biến không hợp lệ) | Phân biệt hợp lệ/không hợp lệ |
| 2. ECT yếu | max(số lớp của từng biến) | Mỗi lớp xuất hiện ≥ 1 lần, không xét tương tác |
| 3. ECT mạnh | Tích số lớp tất cả các biến | Tích Đề-các, xét mọi tương tác |

---

## 5. Kiểm thử dựa trên Bảng Quyết định (Decision Table Testing)

**16. Khái niệm Bảng Quyết định**
- **Lý thuyết:** Bảng quyết định (Decision Table - DT) là công cụ mô tả **logic nghiệp vụ phức tạp** bằng cách gắn kết các **điều kiện (conditions)** với các **hành động (actions)**. Nó tương đương với cấu trúc `if-then-else` hoặc `switch-case` trong lập trình nhưng được trình bày dưới dạng bảng rõ ràng, dễ đọc. Phù hợp khi đặc tả có nhiều điều kiện kết hợp tạo ra các hành vi khác nhau.
- **Ví dụ (Game MOBA):** Hệ thống xét thưởng cuối trận phụ thuộc vào 3 điều kiện: "Thắng trận? (Y/N)", "MVP? (Y/N)", "Có lượt chơi đầu tiên trong ngày? (Y/N)". Mỗi tổ hợp Y/N khác nhau dẫn đến hành động thưởng khác nhau → phù hợp để dùng bảng quyết định.

**17. Cấu trúc Bảng Quyết định**
- **Lý thuyết:** Bảng quyết định gồm **4 phần**:
  1. **Danh sách điều kiện (Conditions):** Các yếu tố đầu vào cần xem xét (cột trái, hàng trên).
  2. **Giá trị điều kiện (Condition values):** Giá trị của từng điều kiện (Y/N hoặc giá trị cụ thể) (phần trên bên phải).
  3. **Danh sách hành động (Actions):** Các thao tác có thể xảy ra (cột trái, hàng dưới).
  4. **Xảy ra hay không (Action entries):** Đánh dấu hành động nào được thực hiện ứng với mỗi tổ hợp điều kiện (X hoặc để trống) (phần dưới bên phải).
  
  Mỗi **cột** trong bảng (phần giá trị) gọi là một **luật (rule)**, tương ứng với 1 tổ hợp điều kiện cụ thể và các hành động kèm theo.
- **Ví dụ (Game MOBA):**

  | | Luật 1 | Luật 2 | Luật 3 | Luật 4 |
  |---|---|---|---|---|
  | **Điều kiện** | | | | |
  | Thắng trận? | Y | Y | N | N |
  | MVP? | Y | N | Y | N |
  | **Hành động** | | | | |
  | +100 Vàng | X | X | | |
  | +50 Vàng | | | X | X |
  | +Huy hiệu MVP | X | | X | |

**18. Phương pháp xây dựng Bảng Quyết định**
- **Lý thuyết:** Quy trình 7 bước:
  1. **Xác định các điều kiện** từ đặc tả yêu cầu.
  2. **Xác định số luật tối đa:** Nếu có `n` điều kiện boolean (Y/N), số luật tối đa = **2^n**.
  3. **Xác định các hành động** có thể xảy ra.
  4. **Điền giá trị điều kiện** cho từng luật (đánh số luật).
  5. **Điền hành động** tương ứng cho từng luật (đánh số hành động).
  6. **Kiểm tra chính sách (policy verification):** Đảm bảo bảng phản ánh đúng nghiệp vụ.
  7. **Đơn giản hóa (simplification):** Gộp các luật có cùng hành động mà chỉ khác nhau ở 1 điều kiện không ảnh hưởng.
- **Ví dụ (Game MOBA):** Bước 1: Xác định 3 điều kiện — Thắng trận (Y/N), MVP (Y/N), Trận đầu tiên trong ngày (Y/N). Bước 2: Số luật tối đa = 2³ = 8 luật. Bước 3: Hành động — +100 Vàng, +50 Vàng, +Huy hiệu MVP, +Bonus trận đầu. Bước 4-5: Điền giá trị. Bước 6: Kiểm tra với Product Owner. Bước 7: Phát hiện rằng "Trận đầu tiên = Y hay N" không ảnh hưởng đến việc trao Huy hiệu MVP → gộp 2 luật thành 1.

**19. Thiết kế ca kiểm thử từ Bảng Quyết định**
- **Lý thuyết:** Mỗi **luật (rule)** trong bảng quyết định trở thành (ít nhất) **1 ca kiểm thử**. Cách chuyển đổi:
  - **Điều kiện → Đầu vào** của ca kiểm thử: chuyển các giá trị Y/N thành dữ liệu đầu vào cụ thể.
  - **Hành động → Đầu ra mong đợi** của ca kiểm thử: các hành động được đánh dấu X là kết quả cần kiểm tra.
  
  Nếu bảng có `k` luật và `n` điều kiện boolean: ít nhất `k` ca kiểm thử, nhiều nhất `2^n` ca. Bảng quyết định cần đảm bảo:
  - **Đầy đủ (completeness):** Phủ hết mọi tổ hợp điều kiện.
  - **Nhất quán (consistency):** Mỗi tổ hợp điều kiện chỉ dẫn đến **đúng 1 tập hành động** (không mâu thuẫn).
- **Ví dụ (Game MOBA):** Luật 1: Thắng = Y, MVP = Y, Trận đầu = Y → Ca kiểm thử: Đầu vào: Tạo trận đấu, đội người chơi thắng, người chơi có KDA cao nhất, đây là trận đầu trong ngày. Đầu ra mong đợi: nhận +100 Vàng + Huy hiệu MVP + Bonus trận đầu. Tester kiểm tra xem tất cả 3 phần thưởng có hiển thị đúng trên màn hình kết quả không.

**20. Ví dụ kinh điển — Bảng quyết định máy in**
- **Lý thuyết:** Bài toán máy in là ví dụ kinh điển cho kiểm thử bảng quyết định. Có **3 điều kiện** boolean:
  - C1: Máy in không in? (Y/N)
  - C2: Đèn đỏ nhấp nháy? (Y/N)
  - C3: Không nhận ra máy in? (Y/N)
  
  Số luật tối đa = 2³ = **8 luật** → **8 ca kiểm thử**. Mỗi luật tương ứng một tổ hợp Y/N của 3 điều kiện, dẫn đến các hành động xử lý khác nhau (kiểm tra kết nối cáp, thay mực, khởi động lại máy in, v.v.).
- **Ví dụ (Game MOBA):** Tương tự, hệ thống xử lý lỗi kết nối game có 3 điều kiện: "Mất kết nối server? (Y/N)", "Ping > 200ms? (Y/N)", "Packet loss > 10%? (Y/N)" → 8 luật. Ví dụ: Luật (Y, Y, Y) → Hành động: Ngắt kết nối + Hiển thị "Lỗi mạng nghiêm trọng" + Gợi ý kiểm tra WiFi. Luật (N, Y, N) → Hành động: Hiển thị icon cảnh báo lag. Mỗi luật tạo 1 ca kiểm thử để xác minh hành vi hệ thống.

---

## Tổng hợp các Kỹ thuật Kiểm thử

| Kỹ thuật | Loại | Ưu điểm | Hạn chế |
|----------|------|---------|---------|
| BVA | Hộp đen | Tập trung vào biên — nơi hay lỗi nhất | Chỉ hiệu quả với biến độc lập, kiểu số |
| Giá trị Đặc biệt | Hộp đen | Hiệu quả cao nhờ kinh nghiệm | Chủ quan, phụ thuộc người kiểm thử |
| Fuzzy Testing | Hộp đen | Phát hiện lỗi bất ngờ, tự động hóa | Không có hệ thống, khó tái lập lỗi |
| ECT | Hộp đen | Giảm số ca kiểm thử, có hệ thống | Phụ thuộc chất lượng phân hoạch |
| Bảng Quyết định | Hộp đen | Rõ ràng cho logic phức tạp, đầy đủ | Số luật tăng theo cấp số mũ (2^n) |
