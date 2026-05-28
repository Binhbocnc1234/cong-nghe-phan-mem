# Tài liệu ôn thi: Tổng quan về Kiểm thử và Đảm bảo Chất lượng Phần mềm

---

## 1. Kiểm chứng và Thẩm định (V&V)

**1. Bối cảnh: Tại sao phần mềm thất bại?**
- **Lý thuyết:** Phần mềm được phát triển để phục vụ yêu cầu khách hàng (KH). Yêu cầu KH được biểu diễn bằng **đặc tả yêu cầu** (requirements specification). PM thất bại khi nó không đáp ứng đúng như đặc tả. Nguyên nhân thất bại có thể đến từ 3 nguồn: (1) Đặc tả sai (phân tích sai yêu cầu), (2) Thiết kế sai (thiết kế không khớp đặc tả), (3) Cài đặt sai (code không khớp thiết kế).
- **Ví dụ (Game MOBA):** Game bị lỗi "tướng Yasuo dùng chiêu cuối không gây sát thương". Nguyên nhân có thể là: (1) Đặc tả sai — tài liệu game design quên ghi chiêu cuối phải gây 300 sát thương, (2) Thiết kế sai — bản thiết kế ghi chiêu cuối chỉ gây hiệu ứng knockup mà thiếu module tính sát thương, (3) Cài đặt sai — thiết kế đúng nhưng Dev quên gọi hàm `applyDamage()` trong code.

**2. Kiểm chứng (Verification)**
- **Lý thuyết:** Kiểm tra xem sản phẩm **có được cài đặt đúng theo thiết kế** không. Mục đích là phát hiện **lỗi lập trình** — sự sai lệch giữa mã nguồn và bản thiết kế. Câu hỏi cốt lõi: *"Are we building the product right?"* (Chúng ta có xây dựng sản phẩm đúng cách không?).
- **Ví dụ (Game MOBA):** Bản thiết kế ghi: "Chiêu Q của tướng Lux có tầm bắn 1000 unit". Dev kiểm chứng bằng cách kiểm tra code xem giá trị `Q_RANGE` có đúng bằng 1000 không. Nếu code ghi `Q_RANGE = 800`, đó là lỗi lập trình (verification fail).

**3. Thẩm định (Validation)**
- **Lý thuyết:** Kiểm tra xem sản phẩm **có đáp ứng yêu cầu khách hàng** không, bao gồm cả yêu cầu **chức năng** (functional) và **phi chức năng** (non-functional). Mục đích là phát hiện **lỗi phân tích và thiết kế** — sự sai lệch giữa sản phẩm và nhu cầu thực sự của người dùng. Câu hỏi cốt lõi: *"Are we building the right product?"* (Chúng ta có xây dựng đúng sản phẩm không?).
- **Ví dụ (Game MOBA):** Khách hàng yêu cầu: "Game phải chạy mượt trên điện thoại tầm trung, ping < 100ms". Dev đã code đúng thiết kế, nhưng khi chạy thực tế, game lag 200ms trên điện thoại tầm trung. Đây là lỗi thẩm định — sản phẩm không đáp ứng yêu cầu phi chức năng (hiệu năng) của KH.

**4. Quy trình V&V: Verification trước → Validation sau**
- **Lý thuyết:** Trong quy trình đảm bảo chất lượng, Verification được thực hiện trước (kiểm tra code đúng thiết kế), sau đó mới Validation (kiểm tra sản phẩm đúng yêu cầu KH). Gộp lại gọi là **V&V**.
- **Ví dụ (Game MOBA):** Đầu tiên, Dev kiểm chứng (Verification) rằng hệ thống mua trang phục đã code đúng thiết kế: nhấn mua → trừ vàng → thêm skin vào kho. Sau đó, QA thẩm định (Validation) rằng toàn bộ luồng mua trang phục đáp ứng yêu cầu KH: mua nhanh, không lag, có xác nhận trước khi trừ tiền.

**5. V&V tĩnh (Static V&V)**
- **Lý thuyết:** Là phương pháp V&V **không thực thi chương trình**. Thực hiện bằng cách **xét duyệt** (review) yêu cầu, thiết kế, và mã nguồn. Có thể tiến hành ở **mọi giai đoạn** phát triển PM (không cần đợi có sản phẩm chạy được). Nhược điểm: **khó đánh giá tính hiệu quả** (không biết chương trình chạy thực tế ra sao).
- **Ví dụ (Game MOBA):** Trước khi code, team Lead ngồi review bản thiết kế hệ thống matchmaking trên giấy. Lead phát hiện: thiết kế thiếu xử lý trường hợp người chơi thoát khỏi hàng đợi giữa chừng. Đây là V&V tĩnh — tìm lỗi thiết kế mà không cần chạy code.

**6. V&V động (Dynamic V&V) — Kiểm thử phần mềm**
- **Lý thuyết:** Là phương pháp V&V **thực thi chương trình** (chạy phần mềm với dữ liệu kiểm thử). Là **cách duy nhất** để kiểm tra các **yêu cầu phi chức năng** như hiệu năng, thời gian phản hồi, tải hệ thống.
- **Ví dụ (Game MOBA):** QA chạy thử trận đấu 5v5 trên server thật với 10 người chơi thật (thực thi chương trình). Đo được ping trung bình = 45ms, FPS = 60. Đây là V&V động — chỉ bằng cách chạy thực tế mới đo được các chỉ số phi chức năng này.

---

## 2. Chất lượng Phần mềm và Kiểm thử Phần mềm

**1. Khái niệm Chất lượng Phần mềm**
- **Lý thuyết:** Chất lượng phần mềm là **sự thỏa mãn của sản phẩm so với đặc tả**. Chất lượng PM bao gồm nhiều yếu tố: (1) **Tính đúng đắn** (correctness), (2) **Tính hiệu quả** (efficiency), (3) **Độ tin cậy** (reliability), (4) **Khả kiểm thử** (testability), (5) **Dễ học/sử dụng** (usability), (6) **Dễ bảo trì** (maintainability). Trong đó, **độ tin cậy** chỉ là một trong nhiều yếu tố đánh giá chất lượng, nhưng là **độ đo quan trọng nhất**.
- **Ví dụ (Game MOBA):** Đặc tả ghi game phải chạy mượt 60 FPS, matchmaking < 30 giây, không crash. Đánh giá chất lượng: Tính đúng đắn (tướng gây đúng sát thương), Hiệu quả (server xử lý 10 triệu người), Độ tin cậy (game không crash 99.9% thời gian), Khả kiểm thử (có API endpoint riêng để test matchmaking), Dễ sử dụng (giao diện trực quan), Dễ bảo trì (code sạch, dễ thêm tướng mới).

**2. Kiểm thử Phần mềm là gì?**
- **Lý thuyết:** Kiểm thử PM là **hoạt động chủ chốt** nhằm đánh giá chất lượng. Nguyên tắc quan trọng: Kiểm thử **có thể chỉ ra rằng phần mềm CÓ lỗi**, nhưng **không thể khẳng định phần mềm KHÔNG còn lỗi**. Về lý thuyết, có thể khẳng định hết lỗi bằng **kiểm thử vét cạn** (exhaustive testing — thử tất cả đầu vào), nhưng điều này **không khả thi** trong thực tế. Một **kiểm thử thành công** là kiểm thử **phát hiện ra lỗi** (chứ không phải kiểm thử mà phần mềm chạy đúng).
- **Ví dụ (Game MOBA):** QA tìm thấy lỗi: "Khi 2 tướng cùng dùng chiêu cuối vào nhau đúng lúc, cả 2 đều không chết". Đây là một **kiểm thử thành công** (vì phát hiện lỗi). Còn nếu QA thử 100 trận mà không thấy lỗi, vẫn không thể kết luận "game không có lỗi" — vì có hàng tỷ tổ hợp tương tác giữa 100+ tướng mà không thể thử hết (kiểm thử vét cạn không khả thi).

---

## 3. Quy trình và Ca kiểm thử

**1. Các hoạt động trong quy trình kiểm thử**
- **Lý thuyết:** Quy trình kiểm thử gồm 5 hoạt động chính:
  - **(1) Xác định** (What): Xác định điều kiện kiểm thử — "Cái gì cần kiểm tra?"
  - **(2) Thiết kế** (How): Thiết kế phương pháp kiểm tra — "Làm thế nào để kiểm tra?"
  - **(3) Xây dựng** (Build): Xây dựng ca kiểm thử — viết mã kiểm thử, chuẩn bị dữ liệu.
  - **(4) Chạy** (Run): Chạy hệ thống với các ca kiểm thử.
  - **(5) So sánh** (Compare): So sánh kết quả thu được (actual) với kết quả mong đợi (expected).
- **Ví dụ (Game MOBA):** Kiểm thử hệ thống matchmaking: (1) Xác định: "Cần kiểm tra xem 10 người cùng rank có được ghép chung trận không". (2) Thiết kế: "Tạo 10 tài khoản rank Vàng, cho vào hàng đợi cùng lúc". (3) Xây dựng: Viết script tự động tạo 10 tài khoản giả, set rank Vàng, gửi request vào hàng đợi. (4) Chạy: Thực thi script trên server test. (5) So sánh: Kết quả mong đợi = 10 người vào chung 1 trận → Kết quả thực tế = 10 người vào chung 1 trận → **PASSED**.

**2. Ca kiểm thử (Test Case)**
- **Lý thuyết:** Một ca kiểm thử (test case) gồm 4 thành phần: **(1) TC_id** — mã định danh duy nhất, **(2) Inputs** — dữ liệu đầu vào, **(3) EO (Expected Output)** — kết quả mong đợi, **(4) Note** — ghi chú thêm. Khi chạy xong, báo cáo kiểm thử (test report) bổ sung thêm cột **Result** với giá trị **Passed** hoặc **Failed**.
- **Ví dụ (Game MOBA):**

| TC_id | Inputs | EO (Expected Output) | Note | Result |
|-------|--------|----------------------|------|--------|
| TC_001 | Tướng Jinx bắn tướng có 100 HP, sát thương = 120 | Tướng đối phương chết, HP = 0 | Không có giáp | Passed |
| TC_002 | Tướng Jinx bắn tướng có 200 HP, sát thương = 120 | Tướng đối phương còn 80 HP | Không có giáp | Passed |
| TC_003 | Người chơi AFK > 3 phút | Hệ thống hiện cảnh báo + báo AFK | | Failed |

**3. Bộ kiểm thử tốt**
- **Lý thuyết:** Một bộ kiểm thử (test suite) tốt phải **bao phủ** ba khía cạnh: (1) **Yêu cầu** (mọi yêu cầu đều được kiểm tra), (2) **Chức năng** (mọi chức năng đều được thử), (3) **Cấu trúc** (mọi đường đi trong code đều được thử). **Tiêu chuẩn bao phủ** (coverage criteria) sẽ định hướng cho việc thiết kế ca kiểm thử. Bộ kiểm thử tốt = đạt **100% tiêu chuẩn bao phủ**.
- **Ví dụ (Game MOBA):** Bộ kiểm thử cho tướng Lux cần bao phủ: (1) Yêu cầu — "chiêu Q phải trói được 2 mục tiêu" → có test case kiểm tra, (2) Chức năng — "mua trang bị, dùng chiêu, hồi máu" → mỗi chức năng có ít nhất 1 test case, (3) Cấu trúc — mọi nhánh if-else trong hàm `castQ()` đều được chạy qua (trúng 0, 1, 2 mục tiêu). Nếu đạt 100% cả 3, bộ kiểm thử là tốt.

---

## 4. Biểu đồ Venn — Bài toán Kiểm thử

**1. Mô hình biểu đồ Venn cho kiểm thử**
- **Lý thuyết:** Bài toán kiểm thử được mô tả bằng biểu đồ Venn với 2 tập hợp:
  - **S (Specified behavior):** Tập hành vi được đặc tả (những gì tài liệu yêu cầu PM phải làm).
  - **P (Programmed behavior):** Tập hành vi được lập trình (những gì PM thực sự làm).
  - **S ∩ P (Giao của S và P):** Phần hành vi **đúng đắn** — vừa được đặc tả, vừa được lập trình đúng.
- **Ví dụ (Game MOBA):** S = {Tướng di chuyển, Tướng đánh thường, Tướng dùng chiêu, Tướng hồi máu tại suối}. P = {Tướng di chuyển, Tướng đánh thường, Tướng dùng chiêu, Tướng đi xuyên tường}. S ∩ P = {Tướng di chuyển, Tướng đánh thường, Tướng dùng chiêu} — phần đúng đắn.

**2. Sai lầm về bỏ quên (S \ P)**
- **Lý thuyết:** **S \ P** = hành vi **được đặc tả nhưng KHÔNG được lập trình**. Đây là **sai lầm về bỏ quên** (omission error) — PM thiếu chức năng so với yêu cầu.
- **Ví dụ (Game MOBA):** Đặc tả ghi "Tướng hồi máu khi đứng tại suối" (thuộc S), nhưng Dev quên code chức năng này (không thuộc P). Vậy "Hồi máu tại suối" nằm trong S \ P → đây là lỗi bỏ quên.

**3. Sai lầm về nhiệm vụ (P \ S)**
- **Lý thuyết:** **P \ S** = hành vi **được lập trình mà KHÔNG được đặc tả**. Đây là **sai lầm về nhiệm vụ** (commission error) — PM làm thêm thứ mà không ai yêu cầu, có thể gây hậu quả ngoài ý muốn.
- **Ví dụ (Game MOBA):** Đặc tả không hề ghi "tướng đi xuyên tường" (không thuộc S), nhưng do lỗi code, tướng có thể đi xuyên tường (thuộc P). Vậy "Đi xuyên tường" nằm trong P \ S → đây là lỗi nhiệm vụ (PM làm điều không được yêu cầu).

---

## 5. Kiểm thử Hộp đen và Kiểm thử Hộp trắng

**1. Kiểm thử Hộp đen (Black-box Testing)**
- **Lý thuyết:** Còn gọi là **kiểm thử hàm/chức năng** (functional testing). Tập trung vào **hành vi vào/ra** (input/output) của phần mềm mà **không quan tâm cấu trúc bên trong**. Vấn đề: không thể kiểm thử hết tất cả đầu vào. Giải pháp: **chia không gian đầu vào thành các miền tương đương** (equivalence partitions), chọn **1 ca kiểm thử đại diện từ mỗi miền**.
- **Ví dụ (Game MOBA):** Kiểm thử hàm `calculateDamage(attack, armor)`. Chia miền tương đương: (1) armor = 0 (không giáp), (2) armor > 0 (có giáp), (3) armor < 0 (giá trị không hợp lệ). Chọn đại diện: TC1: (100, 0), TC2: (100, 50), TC3: (100, -10). Chỉ cần 3 test case thay vì thử hàng triệu tổ hợp.

**2. Kiểm thử Hộp trắng (White-box Testing)**
- **Lý thuyết:** Còn gọi là **kiểm thử cấu trúc/logic** (structural testing). Kiểm tra dựa trên **cấu trúc bên trong** của mã nguồn. Có 4 tiêu chuẩn bao phủ (coverage criteria):
  - **(1) Bao phủ dòng lệnh** (Statement coverage): Mọi dòng lệnh đều được thực thi ít nhất 1 lần.
  - **(2) Bao phủ nhánh** (Branch coverage): Mọi biểu thức điều kiện đều được thử cả True và False, mỗi nhánh ít nhất 1 lần.
  - **(3) Bao phủ đường đi** (Path coverage): Tất cả các khả năng đường đi trong chương trình đều được thử.
  - **(4) Bao phủ vòng lặp** (Loop coverage): Mỗi vòng lặp được thử với 0 lần, 1 lần, và > 1 lần lặp.
- **Ví dụ (Game MOBA):** Kiểm thử hộp trắng cho hàm:
  ```python
  def calculateDamage(attack, armor):
      if armor > 0:                    # Nhánh 1
          damage = attack - armor
      else:                            # Nhánh 2
          damage = attack
      if damage < 0:                   # Nhánh 3
          damage = 0
      return damage
  ```
  - Bao phủ dòng lệnh: cần ít nhất 2 test (1 cho armor > 0, 1 cho armor ≤ 0) để chạy qua mọi dòng.
  - Bao phủ nhánh: cần test armor > 0 (True), armor ≤ 0 (False), damage < 0 (True), damage ≥ 0 (False) → ít nhất 3 test case.
  - Bao phủ đường đi: Nhánh1→Nhánh3, Nhánh1→không Nhánh3, Nhánh2→Nhánh3, Nhánh2→không Nhánh3 = 4 đường.

**3. So sánh Hộp đen và Hộp trắng**
- **Lý thuyết:**

| Tiêu chí | Hộp trắng (White-box) | Hộp đen (Black-box) |
|----------|----------------------|---------------------|
| Dựa trên | Cấu trúc/logic bên trong code | Hành vi vào/ra (đặc tả) |
| Vấn đề | Số đường đi có thể **vô hạn** | Dễ **bùng nổ tổ hợp** đầu vào |
| Hạn chế | Kiểm tra **cái đã làm**, không phải **cái cần làm** | Không chắc phát hiện được **lỗi cụ thể** trong code |
| Phù hợp | **Không** thích hợp cho kiểm thử hệ thống | Thích hợp cho **tất cả cấp độ** kiểm thử |
| Kết luận | **Cần cả hai** — hai chiến lược **bổ sung cho nhau** |

- **Ví dụ (Game MOBA):** Hộp trắng: Dev kiểm tra mọi nhánh if-else trong hàm `castUltimate()` — nhưng chỉ kiểm tra code đã viết, không biết Dev có quên code tính năng nào không (cái đã làm vs cái cần làm). Hộp đen: QA thử dùng chiêu cuối trong trận — kiểm tra đúng yêu cầu "chiêu cuối gây 500 sát thương", nhưng nếu chỉ thử 1 trường hợp thì có thể bỏ lỡ lỗi khi chiêu cuối dùng lên mục tiêu miễn sát thương. → Cần kết hợp cả hai.

---

## 6. Kiểm thử và Gỡ lỗi

**1. Phân biệt Kiểm thử (Testing) và Gỡ lỗi (Debugging)**
- **Lý thuyết:** Kiểm thử và gỡ lỗi là hai hoạt động khác nhau:
  - **Kiểm thử (Testing):** Mục đích là **khẳng định rằng phần mềm CÓ lỗi**. Kiểm thử trả lời câu hỏi: "Phần mềm có lỗi không?"
  - **Gỡ lỗi (Debugging):** Mục đích là **định vị và sửa lỗi**. Sau khi kiểm thử phát hiện lỗi, gỡ lỗi trả lời câu hỏi: "Lỗi nằm ở đâu và sửa thế nào?"
  - Quy trình gỡ lỗi thường bao gồm: **lập giả thuyết** về nguyên nhân hành vi sai, sau đó **kiểm tra giả thuyết** bằng cách đặt breakpoint, in log, hoặc viết test nhỏ.
- **Ví dụ (Game MOBA):** **Kiểm thử:** QA phát hiện lỗi "Tướng Zed dùng chiêu W (phân thân) nhưng phân thân không xuất hiện". QA ghi bug report → kiểm thử thành công (đã tìm ra lỗi). **Gỡ lỗi:** Dev nhận bug, lập giả thuyết: "Có thể animation phân thân không được load". Dev đặt breakpoint tại hàm `spawnClone()`, chạy debug, phát hiện biến `clonePosition` bị null do thiếu khởi tạo. Dev sửa code, chạy lại test → lỗi đã hết.

---

## 7. Các mức Kiểm thử

**1. Kiểm thử Đơn vị (Unit Testing)**
- **Lý thuyết:** Mục đích: tìm sự **khác biệt giữa đặc tả và cài đặt** của từng đơn vị nhỏ nhất. Đơn vị có thể là: lớp (class), hàm (function), đối tượng (object), gói (package), mô-đun (module). Môi trường kiểm thử đơn vị gồm: **Đơn vị cần test** + **Stub** (mô phỏng các đơn vị mà đơn vị đang test gọi đến) + **Bộ điều khiển** (Driver — gọi đơn vị cần test) + **Ca kiểm thử** → Cho ra **Kết quả**.
- **Ví dụ (Game MOBA):** Kiểm thử đơn vị hàm `calculateDamage(attack, armor)`. **Driver:** đoạn code gọi `calculateDamage(100, 30)`. **Stub:** hàm `getArmorReduction()` giả lập trả về giá trị cố định 0.3 (vì module Armor chưa code xong). **Ca kiểm thử:** Input = (100, 30), Expected = 70. **Kết quả:** Actual = 70 → Passed.

**2. Kiểm thử Tích hợp (Integration Testing)**
- **Lý thuyết:** Phát hiện vấn đề khi **ghép các mô-đun** lại với nhau. Kiểm tra hai nhóm vấn đề:
  - **Bên trong (Internal):** Lời gọi hàm/message giữa các module, tham số (kiểu, số lượng, thứ tự, giá trị), kết quả trả về.
  - **Bên ngoài (External):** Ngắt (interrupt), thời gian vào ra (I/O timing), tương tác với hệ thống bên ngoài.
- **Ví dụ (Game MOBA):** Module `Matchmaking` gọi module `PlayerService.getPlayerRank(playerId)` để lấy rank người chơi. Kiểm thử tích hợp phát hiện: `Matchmaking` truyền `playerId` kiểu `int`, nhưng `PlayerService` nhận kiểu `string` → lỗi kiểu tham số. Hoặc `Matchmaking` mong nhận về "Gold", nhưng `PlayerService` trả về mã số 3 → lỗi giá trị trả về.

**3. Kiểm thử Hệ thống (System Testing)**
- **Lý thuyết:** Kiểm thử toàn bộ hệ thống sau khi đã tích hợp xong, **trước khi phát hành**. Liên quan đến các **yếu tố bên ngoài**. Không chỉ kiểm tra chức năng mà còn: **Khả dụng** (usability — dễ sử dụng), **Hiệu năng** (performance — tốc độ phản hồi), **Tài nguyên sử dụng** (resource usage — RAM, CPU, băng thông).
- **Ví dụ (Game MOBA):** Kiểm thử hệ thống game MOBA trước khi ra mắt: (1) Chức năng: chơi trận 5v5, mua trang bị, chat đều hoạt động. (2) Khả dụng: người chơi mới có thể tự hiểu cách chơi qua tutorial. (3) Hiệu năng: 100,000 người chơi đồng thời, ping < 80ms. (4) Tài nguyên: game tiêu tốn < 2GB RAM trên điện thoại, CPU < 70%.

**4. Kiểm thử Chấp thuận (Acceptance Testing)**
- **Lý thuyết:** Người dùng dùng thử sản phẩm, còn gọi là **kiểm thử alpha**. Có hai loại:
  - **BAT (Business Acceptance Testing):** Do **cơ quan phát triển** (công ty phát triển) thực hiện.
  - **UAT (User Acceptance Testing):** Do **người dùng cuối** thực hiện.
  - **Mục đích:** Kiểm tra sự **hài lòng** của người dùng.
  - **Cơ sở:** Dựa trên **mong muốn của người dùng** (không phải đặc tả kỹ thuật).
  - **Môi trường:** Môi trường **thật** (production-like).
  - **Người thực hiện:** **Bởi và cho** người dùng.
- **Ví dụ (Game MOBA):** **BAT:** Trước khi ra mắt, team QA nội bộ công ty chơi thử 100 trận, đánh giá trải nghiệm tổng thể. **UAT:** Mở Closed Beta cho 10,000 game thủ thật tải game về chơi trên điện thoại thật. Game thủ phản hồi: "Nút mua trang bị quá nhỏ, hay bấm nhầm" → lỗi usability do UAT phát hiện.

---

## 8. Kiểm thử Hồi quy (Regression Testing)

**1. Khái niệm và Mục đích**
- **Lý thuyết:** Khi hệ thống được **chỉnh sửa** (fix bug, thêm tính năng), **toàn bộ bộ kiểm thử** cần được **chạy lại**. Mục đích: đảm bảo các **tính năng đang hoạt động tốt không bị ảnh hưởng** bởi thay đổi mới. Kiểm thử hồi quy nên được **tự động hóa** và chạy **trước khi lưu code vào repo** (repository). Với hệ thống lớn, cần **chiến lược kiểm thử tăng dần** (incremental testing strategy) vì chạy lại toàn bộ quá tốn thời gian.
- **Ví dụ (Game MOBA):** Dev sửa lỗi "tướng Yasuo chiêu Q không gây sát thương" bằng cách sửa hàm `castQ()`. Sau khi sửa, hệ thống CI/CD tự động chạy lại toàn bộ 5,000 test case (regression test). Kết quả: chiêu Q của Yasuo đã gây sát thương đúng (Passed), nhưng phát hiện chiêu Q của tướng Yone bị ảnh hưởng và gây sát thương gấp đôi (Failed) → hồi quy phát hiện lỗi phụ do thay đổi mới gây ra.

---

## 9. Khi nào Dừng Kiểm thử

**1. Các tiêu chí dừng kiểm thử**
- **Lý thuyết:** Có 3 tiêu chí để quyết định dừng kiểm thử:
  - **(1) Hết thời gian hoặc ngân sách:** Đã dùng hết thời gian/tiền được phân bổ cho kiểm thử.
  - **(2) Đạt mức bao phủ mong muốn:** Đạt được tỷ lệ bao phủ (coverage) đã đặt ra (ví dụ: 90% statement coverage).
  - **(3) Đạt tần suất hỏng hóc mong muốn:** Số lỗi tìm được trong một khoảng thời gian giảm xuống dưới ngưỡng chấp nhận (tức là PM đã đủ ổn định).
- **Ví dụ (Game MOBA):** Team QA đặt tiêu chí dừng: "Dừng khi đạt 95% branch coverage VÀ trong 1 tuần test cuối không tìm thấy lỗi nghiêm trọng nào (severity = critical)". Sau 3 tuần test: tuần 1 tìm được 20 lỗi critical, tuần 2 tìm 5 lỗi, tuần 3 tìm 0 lỗi critical + coverage đạt 96%. → Đủ điều kiện dừng, chuyển sang phát hành.

---

## 10. Công cụ Hỗ trợ Kiểm thử

**1. Các loại công cụ kiểm thử** [Không có trong sách]
- **Lý thuyết:** Các công cụ hỗ trợ kiểm thử được phân loại theo mục đích sử dụng:

| Loại công cụ | Công cụ | Mục đích |
|-------------|---------|----------|
| Kiểm thử đơn vị | **JUnit**, **PyUnit** | Viết và chạy test cho từng hàm/class |
| Tự động hóa kiểm thử | **TestComplete** | Tự động hóa toàn bộ quy trình kiểm thử |
| Kiểm thử hiệu năng | **JMeter** | Đo thời gian phản hồi, tải hệ thống |
| Kiểm thử giao diện | **Ranorex** | Kiểm thử tự động giao diện người dùng |
| Kiểm thử tổ hợp | **AETG** | Sinh bộ test tổ hợp các đầu vào |
| Dựa trên mô hình | **Spec Explorer** | Sinh test case từ mô hình hành vi |
| Bao phủ mã nguồn | **Cobertura** | Đo tỷ lệ bao phủ code (coverage) |
| Quản lý lỗi | **Bugzilla** | Theo dõi, quản lý, phân loại lỗi |

- **Ví dụ (Game MOBA):** Trong dự án game MOBA: Dev dùng **JUnit** để viết unit test cho hàm `calculateDamage()`. QA dùng **JMeter** để mô phỏng 100,000 người chơi đồng thời vào server để đo hiệu năng. Khi tìm thấy lỗi, QA tạo ticket trên **Bugzilla** với mô tả: "Bug #1234: Tướng Jinx chiêu W không gây sát thương khi bắn qua tường". Dev dùng **Cobertura** kiểm tra coverage đạt 92% → còn 8% code chưa được test.
