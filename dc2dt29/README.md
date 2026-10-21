# DC2DT29 — 44 đề, 88 lời giải độc lập

Bản gốc: [DC2DT29 de cuong.docx](DC2DT29%20de%20cuong.docx). [Nội dung từng câu](DE_CUONG.md) và [dữ liệu đối chiếu](problems.json) giữ thứ tự xuất hiện trong tài liệu: 44 đề, mỗi đề có câu 1 (4 điểm) và câu 2 (6 điểm). Tài liệu không đánh số đề; tên `de_01` … `de_44` là số thứ tự được gán để tra cứu. Những câu lặp lại vẫn có file riêng, kể cả các biến thể về Timer, ngắt, giới hạn và giữ nút.

Nguồn tải: https://docs.google.com/document/d/1mh2D75xNiBHrTItzRjf3hnnpLvd3hsYg/edit. File Word được tải qua đường tải gốc của Google Drive, không dựng lại từ văn bản. SHA-256: `673aff4b3101a33497ceb0d9b3e2767c96aeefadf97daf6826eb9ef13a813a13`. Đã đối chiếu toàn bộ nội dung 88 câu với bản Word; không có hình nhúng.

## Tạo project

Dùng **CodeVisionAVR, ATmega16, clock 8 MHz**. Mỗi project chỉ thêm **một** file `cau_1.c` hoặc `cau_2.c`. Mỗi file đã có đầy đủ khởi tạo, hàm, chương trình chính và ngắt cần dùng; không cần thêm file C nào khác. Đây là mã CodeVisionAVR (`mega16.h`, `delay.h`, `interrupt`, `#asm`), không biên dịch trực tiếp bằng avr-gcc hoặc Arduino IDE.

LED đơn và các đoạn LED anode chung sáng mức 0. Chọn digit sáng mức 1 qua mạch driver phù hợp; không nối trực tiếp dòng tổng của nhiều đoạn qua chân MCU. Nối điện trở hạn dòng cho từng đoạn/LED. Nút nhấn kéo xuống GND; pull-up nội đã bật cho đầu vào số.

**Tắt JTAG bằng fuse trong cấu hình ATmega16/Proteus để PC2–PC5 làm GPIO.** Mã không ghi thanh ghi JTAG và không thay đổi fuse. Nếu chưa cấu hình thì các đoạn tại những chân này có thể không hoạt động.

## Đấu chân

| Nhóm | Đấu nối |
|---|---|
| Câu 1 — dãy 8 LED | LED 1 bên trái = PD7, LED 8 bên phải = PD0; toàn bộ PORTD là đầu ra |
| Câu 1 — LED chạy tự động | Nút tăng tốc PC0, giảm tốc PC1, đúng đề |
| Câu 1 — dịch từng bước | Nút dịch phải PA1, dịch trái PA2; ban đầu LED thứ 2 = PD6 |
| Câu 1 — nhấp nháy xen kẽ | Nút tăng tần số PB6, giảm tần số PB7, đúng đề |
| Câu 1 — đảo 8 LED | Nút PA0–PA7 lần lượt điều khiển PD0–PD7, đúng quan hệ theo bit |
| Câu 1 — LED 7 đoạn đơn | a–g, dp = PC0–PC7; hai nút tăng/giảm hoặc START/STOP = PA0/PA1 nếu đề không chỉ định |
| Câu 1 — 10 nút số | Số 0–7 = PA0–PA7; số 8 = PB0; số 9 = PB1 |
| Câu 1 — 9 nút số | Số 1–8 = PA0–PA7; số 9 = PB0; không nhấn hiện 0 |
| Toàn bộ câu 2 | a–g, dp = PC0–PC7; chọn digit từ trái sang phải PA4–PA7 (bài 3 digit chỉ dùng PA4–PA6) |
| Câu 2 — nút điều khiển | Theo chân ghi trong từng đề: PB0/PB1/PB2, PA0/PA1 hoặc PD6/PD7; bài Timer bắt đầu 8000 không chỉ định chân thì dùng PB0/PB1 |
| Câu 2 — ngắt ngoài | INT0 = PD2, INT1 = PD3; Falling hoặc Rising đúng từng đề |
| Câu 2 — ADC | ADC0 = PA0, ADC1 = PA1, ADC2 = PA2; bài LM35 dùng PA0 đo áp, PA1 đo LM35 |
| Câu 2 — ADC có nút | PD0 đổi độ chính xác hoặc kênh; bài áp/LM35 dùng PD0 đổi chế độ, PD1 đổi độ chính xác |
| Câu 2 — LED 7 đoạn phụ | a–g, dp = PB0–PB7; luôn hiển thị số chế độ/kênh |
| Câu 2 — áp/LM35, 4 LED báo chế độ | PB0 = điện áp, PB1 = nhiệt độ, PB2 = 0.1 V, PB3 = 0.01 V; các LED này sáng mức **1**, dùng mạch phù hợp |

Các lựa chọn chân không nêu trong đề là quy ước của lời giải. Bố trí mới dùng PORTC làm dữ liệu và PA4–PA7 chọn digit để tránh xung đột với các nút PB0–PB2, PD6–PD7 và các ngõ ADC. Không dùng lại cách nối chân trong bộ bài thực hành ở thư mục gốc.

Với ADC: cấp VCC và AVCC = 5 V, nối chung GND, dùng **AVCC làm tham chiếu** (`REFS0=1`), nối tụ lọc AREF xuống GND theo datasheet. Không áp dụng hướng dẫn AREF ngoài của bộ bài thực hành cũ cho các lời giải này. Biến trở nối giữa 5 V và GND, cần gạt vào chân ADC. LM35 nối đầu ra vào PA1; 250 mV tương ứng khoảng 25 °C.

Ngắt Falling kích hoạt khi nhấn nút kéo lên; Rising kích hoạt khi nhả nút. Nếu cần Rising khi nhấn thì dùng mạch kéo xuống và nút lên VCC cho chân ngắt tương ứng. Ngắt ngoài không có chống dội phần mềm: dùng nút không dội trong Proteus hoặc chống dội ngoài.

## Quy tắc và giả định

- Nút đọc bằng chương trình được lọc 20 mẫu liên tiếp, mỗi vòng danh nghĩa 1 ms. Khi yêu cầu chờ nhả, giữ nút chỉ tạo một sự kiện. Khi yêu cầu giữ liên tục, chu kỳ lặp là 200 ms nếu đề chưa quy định; các câu ghi 200/300 ms giữ đúng giá trị đó. Nhấn đồng thời hai nút đối nghịch thì không tăng/giảm; START/STOP đồng thời ưu tiên STOP. Nhấn nhiều nút số thì ưu tiên số lớn nhất. Với bài 9 nút đề không quy định ưu tiên, chọn cùng quy tắc này.
- Câu 1 LED chạy: tần số được hiểu là tần số chuyển sang LED kế tiếp. Ban đầu mỗi bước 100 ms, thay đổi 10 ms/lần. Trái → phải giới hạn 10–250 ms (100–4 Hz), phải → trái 40–200 ms (25–5 Hz). Đề 01 không yêu cầu giữ nút để thay đổi liên tục nên dùng một lần mỗi nhấn; đề 15 và 29 có lặp khi giữ.
- Nhấp nháy xen kẽ: chu kỳ đầy đủ ban đầu 100 ms, mỗi nửa chu kỳ 50 ms. Vì đề không cho giới hạn/bước chỉnh, chọn nửa chu kỳ 5–1000 ms, chỉnh 5 ms/lần (chu kỳ đầy đủ 10–2000 ms).
- Các khoảng thời gian `t` không cho ban đầu dùng 1000 ms, bước chỉnh 100 ms, giới hạn theo từng câu. START/STOP và reset khởi động lại bộ đếm thời gian. Đổi `t` giữ pha thời gian đã trôi qua để giữ nút chỉnh tốc độ không làm dừng chuyển động; nút START của bài Timer không tự lặp khi giữ. Bài 5555 không quy định tràn nên chọn 9999 → 0000. Bài reset 6000 chỉ reset số và thời gian; giữ trạng thái đang chạy/dừng.
- Bài bắt đầu 8000 có hai dải khác nhau trong chính đề: ngắt chỉnh tay trong 8000–8888, tự động chạy đến 9000 rồi vòng về 1000. Chọn **kẹp kết quả chỉnh tay về 8000–8888**, kể cả khi số tự động đang nằm ngoài dải đó. Ví dụ số 1000 rồi INT0 sẽ về 8000. Đây là cách giải quyết phần giao nhau mà đề chưa mô tả.
- Bài áp/LM35: nhiệt độ làm tròn đến độ C nguyên, không dấu thập phân; độ chính xác điện áp được nhớ khi chuyển chế độ. Khi đo nhiệt độ, chỉ LED nhiệt độ sáng; LED báo độ chính xác điện áp tắt. Điện áp chuẩn hóa theo ADC 10 bit, tính `ADC × 5/1023`, làm tròn gần nhất. Ở 5 V hiển thị `05.0`/`5.00` với 3 digit, `005.0`/`05.00` với 4 digit. LED phụ dùng 1/2 để báo 0.1/0.01 V, hoặc 0/1/2 để báo ADC0/ADC1/ADC2.
- Những chỗ đề 31/40/44 bỏ câu mở đầu ở câu 2 được hiểu theo phần yêu cầu và bài tương đương đề 19: 4 digit, nút PA0/PA1, INT0 Falling. Không sửa văn bản đề gốc.

## Timer và thời gian

Các câu nêu Timer 0 đều dùng **Normal mode và ngắt tràn**:

| Clock Timer 0 | Prescaler ở 8 MHz | Preload | Số đếm mỗi ngắt | Thời gian một ngắt | Số ngắt cho 0.5 s |
|---|---:|---:|---:|---:|---:|
| 125000 Hz | 64 | 6 | 250 | 2 ms | 250 |
| 31250 Hz | 256 | 131 | 125 | 4 ms | 125 |

ISR cộng preload vào `TCNT0` để bù phần độ trễ đã trôi qua theo tick timer; không dùng delay trong ngắt. Các câu yêu cầu Timer 2 dùng Normal mode, prescaler 64, preload 6: mỗi 2 ms chuyển một digit, chu kỳ quét 4 digit là 8 ms (125 Hz). Tắt mọi digit trước khi đổi dữ liệu đoạn để tránh bóng mờ. Bộ đệm digit và số 16 bit được bảo vệ bằng lưu SREG, tắt ngắt, rồi khôi phục SREG khi cập nhật ở vòng chính.

Những câu **không yêu cầu timer** dùng vòng chính `delay_ms(1)` cộng thời gian xử lý; thời gian chống dội, quét LED, tự động đếm và lặp nút ở các câu này là xấp xỉ. Các giá trị timer ở bảng là chính xác theo số tick với clock danh nghĩa 8 MHz; độ chính xác dao động, độ trễ ISR và thời gian thực vẫn cần đo trong Proteus hoặc trên mạch thật.

## Kiểm thử

Từ thư mục gốc repository:

```sh
python dc2dt29/tests/check_solutions.py
python kiemtra.py
```

Bộ kiểm thử mới xác nhận đủ 88 file, thích nghi cú pháp riêng của CodeVision, biên dịch từng chương trình kiểm thử bằng GCC (`-Wall -Wextra -Werror`, UndefinedBehaviorSanitizer), rồi chạy kiểm tra hành vi trên mã C thật: khởi tạo, nút, giới hạn, ngắt, 0.5 s theo tick timer, quét Timer 2, các tổ hợp nút số và toàn bộ 1024 mã ADC. Chỉ thay đổi cú pháp vendor và phần chuyển đổi ADC phần cứng để chạy được trên máy tính. Thư viện tiêu chuẩn Python là đủ; không cần package ngoài. File tạm được tạo ngoài checkout và tự xóa.

Đã chạy **88/88** chương trình mới và **25/25** bài thực hành cũ thành công. **Chưa biên dịch bằng CodeVisionAVR, chưa tạo HEX, chưa mô phỏng Proteus.** Kiểm thử host không xác nhận kích thước kiểu `int` của AVR, mã máy, dòng điện, đấu dây, chống dội vật lý hoặc thời gian trên MCU. Để hoàn tất kiểm chứng phần cứng: biên dịch từng file bằng CodeVisionAVR, nạp HEX vào ATmega16 8 MHz với fuse JTAG phù hợp, rồi thử các yêu cầu tương ứng và đo thời gian.

## Mục lục 88 câu

| Đề | Câu 1 | Câu 2 |
|---:|---|---|
| 01 | [LED trái → phải, 4–100 Hz](de_01/cau_1.c) | [Timer 0 125 kHz, 8000, ngắt chỉnh tay](de_01/cau_2.c) |
| 02 | [10 nút số, giữ giá trị](de_02/cau_1.c) | [Timer 0 125 kHz, Timer 2 quét, tự tăng](de_02/cau_2.c) |
| 03 | [Một digit, tăng/giảm vòng, chờ nhả](de_03/cau_1.c) | [Timer 0 31250 Hz, 1111, INT0 STOP](de_03/cau_2.c) |
| 04 | [LED phải → trái, 5–25 Hz](de_04/cau_1.c) | [Tăng/giảm PD6/PD7, INT0 reset 1000](de_04/cau_2.c) |
| 05 | [Một digit, giới hạn 0–9](de_05/cau_1.c) | [Đếm giảm 6000, INT1 Rising reset](de_05/cau_2.c) |
| 06 | [Một digit, START/STOP, tăng 100 ms](de_06/cau_1.c) | [INT1 START, tăng với t chỉnh được](de_06/cau_2.c) |
| 07 | [Một digit, tăng với t chỉnh được](de_07/cau_1.c) | [INT0 START/INT1 STOP, giảm với t chỉnh được](de_07/cau_2.c) |
| 08 | [Một digit, START/STOP, giảm 300 ms](de_08/cau_1.c) | [5555, PA0 START/STOP, ngắt chỉnh t](de_08/cau_2.c) |
| 09 | [8 LED đảo, giữ lặp 300 ms](de_09/cau_1.c) | [ADC0 điện áp/ADC1 LM35, 3 digit](de_09/cau_2.c) |
| 10 | [Một digit, tăng/giảm vòng, giữ lặp 300 ms](de_10/cau_1.c) | [Điện áp, đổi độ chính xác, digit phụ](de_10/cau_2.c) |
| 11 | [8 LED đảo, chờ nhả](de_11/cau_1.c) | [Tăng/giảm PD6/PD7, INT0 reset 1000](de_11/cau_2.c) |
| 12 | [Dịch LED bằng PA1/PA2](de_12/cau_1.c) | [Đếm giảm 6000, INT1 Rising reset](de_12/cau_2.c) |
| 13 | [LED xen kẽ, chỉnh tần số](de_13/cau_1.c) | [INT1 START, tăng với t chỉnh được](de_13/cau_2.c) |
| 14 | [9 nút số, nhả về 0](de_14/cau_1.c) | [INT0 START/INT1 STOP, giảm với t chỉnh được](de_14/cau_2.c) |
| 15 | [LED trái → phải, 4–100 Hz](de_15/cau_1.c) | [5555, PA0 START/STOP, ngắt chỉnh t](de_15/cau_2.c) |
| 16 | [10 nút số, giữ giá trị](de_16/cau_1.c) | [ADC0 điện áp/ADC1 LM35, 3 digit](de_16/cau_2.c) |
| 17 | [Một digit, tăng/giảm vòng, chờ nhả](de_17/cau_1.c) | [Điện áp, đổi độ chính xác, digit phụ](de_17/cau_2.c) |
| 18 | [LED phải → trái, 5–25 Hz](de_18/cau_1.c) | [3 ADC, PD0 đổi kênh, digit phụ](de_18/cau_2.c) |
| 19 | [Một digit, giới hạn 0–9](de_19/cau_1.c) | [Tăng/giảm, INT0 đếm giảm về 10](de_19/cau_2.c) |
| 20 | [Một digit, START/STOP, tăng 100 ms](de_20/cau_1.c) | [3 ADC, INT1 Rising đổi kênh, digit phụ](de_20/cau_2.c) |
| 21 | [Một digit, tăng với t chỉnh được](de_21/cau_1.c) | [Timer 0 31250 Hz, Timer 2 quét, tự giảm](de_21/cau_2.c) |
| 22 | [Một digit, START/STOP, giảm 300 ms](de_22/cau_1.c) | [Timer 0 125 kHz, 8000, ngắt chỉnh tay](de_22/cau_2.c) |
| 23 | [8 LED đảo, giữ lặp 300 ms](de_23/cau_1.c) | [Timer 0 125 kHz, Timer 2 quét, tự tăng](de_23/cau_2.c) |
| 24 | [Một digit, tăng/giảm vòng, giữ lặp 300 ms](de_24/cau_1.c) | [Timer 0 31250 Hz, 1111, INT0 STOP](de_24/cau_2.c) |
| 25 | [8 LED đảo, chờ nhả](de_25/cau_1.c) | [INT1 START, tăng với t chỉnh được](de_25/cau_2.c) |
| 26 | [Dịch LED bằng PA1/PA2](de_26/cau_1.c) | [INT0 START/INT1 STOP, giảm với t chỉnh được](de_26/cau_2.c) |
| 27 | [LED xen kẽ, chỉnh tần số](de_27/cau_1.c) | [5555, PA0 START/STOP, ngắt chỉnh t](de_27/cau_2.c) |
| 28 | [9 nút số, nhả về 0](de_28/cau_1.c) | [ADC0 điện áp/ADC1 LM35, 3 digit](de_28/cau_2.c) |
| 29 | [LED trái → phải, 4–100 Hz](de_29/cau_1.c) | [Điện áp, đổi độ chính xác, digit phụ](de_29/cau_2.c) |
| 30 | [10 nút số, giữ giá trị](de_30/cau_1.c) | [3 ADC, PD0 đổi kênh, digit phụ](de_30/cau_2.c) |
| 31 | [Một digit, tăng/giảm vòng, chờ nhả](de_31/cau_1.c) | [Tăng/giảm, INT0 đếm giảm về 10](de_31/cau_2.c) |
| 32 | [LED phải → trái, 5–25 Hz](de_32/cau_1.c) | [3 ADC, INT1 Rising đổi kênh, digit phụ](de_32/cau_2.c) |
| 33 | [Một digit, giới hạn 0–9](de_33/cau_1.c) | [Timer 0 31250 Hz, Timer 2 quét, tự giảm](de_33/cau_2.c) |
| 34 | [Một digit, START/STOP, tăng 100 ms](de_34/cau_1.c) | [Timer 0 125 kHz, 8000, ngắt chỉnh tay](de_34/cau_2.c) |
| 35 | [Một digit, tăng với t chỉnh được](de_35/cau_1.c) | [Timer 0 125 kHz, Timer 2 quét, tự tăng](de_35/cau_2.c) |
| 36 | [Một digit, START/STOP, giảm 300 ms](de_36/cau_1.c) | [Timer 0 31250 Hz, 1111, INT0 STOP](de_36/cau_2.c) |
| 37 | [8 LED đảo, giữ lặp 300 ms](de_37/cau_1.c) | [Tăng/giảm PD6/PD7, INT0 reset 1000](de_37/cau_2.c) |
| 38 | [Một digit, tăng/giảm vòng, giữ lặp 300 ms](de_38/cau_1.c) | [Đếm giảm 6000, INT1 Rising reset](de_38/cau_2.c) |
| 39 | [8 LED đảo, chờ nhả](de_39/cau_1.c) | [3 ADC, PD0 đổi kênh, digit phụ](de_39/cau_2.c) |
| 40 | [Dịch LED bằng PA1/PA2](de_40/cau_1.c) | [Tăng/giảm, INT0 đếm giảm về 10](de_40/cau_2.c) |
| 41 | [LED xen kẽ, chỉnh tần số](de_41/cau_1.c) | [3 ADC, INT1 Rising đổi kênh, digit phụ](de_41/cau_2.c) |
| 42 | [9 nút số, nhả về 0](de_42/cau_1.c) | [Timer 0 31250 Hz, Timer 2 quét, tự giảm](de_42/cau_2.c) |
| 43 | [8 LED đảo, chờ nhả](de_43/cau_1.c) | [3 ADC, PD0 đổi kênh, digit phụ](de_43/cau_2.c) |
| 44 | [Dịch LED bằng PA1/PA2](de_44/cau_1.c) | [Tăng/giảm, INT0 đếm giảm về 10](de_44/cau_2.c) |
