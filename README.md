## Đề cương DC2DT29

Đã bổ sung [đề cương gốc và 88 lời giải cho 44 đề](dc2dt29/README.md), mỗi câu có một file CodeVisionAVR độc lập. Xem hướng dẫn đấu chân, các giả định và kiểm thử trong thư mục đó.

## Bộ bài thực hành ban đầu

Bộ này gồm 25 chương trình độc lập: bài 1–16 và 23–31. Bài 17–22 đã được bỏ theo yêu cầu.

Mỗi file dùng định dạng CodeWizardAVR theo mẫu bai 6.c trên Google Drive: phần đầu /****, mega16.h, delay.h, các biến và hàm cần thiết, void main(void), khởi tạo ngoại vi, rồi while (1). Cấu hình chân, ngắt và ADC của từng bài được đặt trực tiếp trong phần khởi tạo trước vòng lặp; không còn khối da_khoitao. Các lệnh ghi thanh ghi điều khiển JTAG đã được bỏ theo yêu cầu; mã C không thiết lập fuse. Một số bài vẫn giữ maden/i của mẫu để dễ đối chiếu, nên có thể có cảnh báo unused variable.

Mỗi lần tạo project, chỉ đưa MỘT file bài vào project. Dùng CodeVisionAVR, chip ATmega16, clock 8 MHz như mẫu. Đây là cú pháp CodeVisionAVR (mega16.h, interrupt, #asm), không phải mã để nạp trực tiếp bằng Arduino IDE hay avr-gcc.

Nguồn đã đọc:
- [BaiTapThucHanh.docx](BaiTapThucHanh.docx)
- [Code proteus: mẫu 6–12, 16, 23](https://drive.google.com/drive/folders/1ywxU_8SP5XalwFGuTg_DzMzSKEK8DARQ)
- [Datasheet ATmega16A của Microchip](https://www.microchip.com/content/dam/mchp/documents/OTH/ProductDocuments/DataSheets/Atmel-8154-8-bit-AVR-ATmega16A_Datasheet.pdf), dùng đối chiếu bảng cạnh ngắt và ADC. Clock ADC được chọn 8 MHz / 64 = 125 kHz; dải khuyến nghị cho độ phân giải 10 bit là 50–200 kHz.

| Nhóm bài | Nối chân |
|---|---|
| 1–3 | 8 nút PD0–PD7 tương ứng 8 LED PC0–PC7. Nút nhấn nối GND; LED sáng mức 0. |
| 4–5, 12 | 8 LED tại PC0–PC7, sáng mức 0. Bài 5 quy ước PC7 ở bên trái, PC0 bên phải. |
| 6–8 | LED 7 đoạn đơn tại PORTC; a–g lần lượt PC0–PC6, dấu chấm PC7. Bài 7: PD0 tăng, PD1 giảm. |
| 9–10 | a–g, dp tại PB0–PB7; chọn 4 digit trái sang phải tại PC4–PC7 đúng đề. Bài 10: PD0 tăng, PD1 giảm. |
| 11, 13–16, 23–30 | a–g, dp tại PB0–PB7; chọn 4 digit trái sang phải tại PC0–PC3, theo nhóm mẫu bài 11/16/23. |
| 11–12, 24–25 | INT0 = PD2, INT1 = PD3. |
| 13–16 | ADC0 = PA0. Bài 13–15 nối chân giữa biến trở vào PA0; bài 16 nối đầu ra LM35 vào PA0. Bài 15 dùng nút PD0. |
| 23 | 8 đầu ra biến trở tại PA0–PA7; nút chọn kênh tại PC5; 8 LED báo kênh tại PD0–PD7, sáng mức 1 theo mẫu bài 23. |
| 24, 26–27, 30 | Nút 1 PD0, nút 2 PD1. Bài 26 thêm INT0 tại PD2. |
| 25, 28–29 | Nút tại PD0. |
| 31 | Nút số 0–7 tại PD0–PD7; nút 8 tại PA0, nút 9 tại PA1; LED 7 đoạn đơn tại PORTC. Đây là cách nối được chọn vì đề chưa chỉ rõ chân. |

LED 7 đoạn là loại anode chung, đoạn sáng mức 0; chọn digit mức 1 qua mạch điều khiển phù hợp với mẫu. Nút thông thường nhấn xuống GND; pull-up đã bật. Mã không tự tắt JTAG. Khi mô phỏng, cần dùng cấu hình ATmega16 cho phép PC2–PC5 hoạt động như GPIO; nếu giao diện JTAG đang chiếm các chân này thì LED hoặc nút trên các chân đó sẽ không hoạt động đúng. Việc chuẩn bị các file C không thay đổi cấu hình chip trong các project Proteus hay phần cứng thật.

Với các bài ADC, cấp VCC và AVCC = 5 V, nối AREF = 5 V, nối chung GND. Hai đầu mỗi biến trở nối 5 V và GND. Giữ đúng nguồn tham chiếu 5 V vì công thức đo dựa trên giá trị đó.

| Bài | Nội dung và kết quả cần kiểm tra |
|---|---|
| [01](bai_01.c) | Nhấn nút nào thì LED đó sáng và giữ sáng khi nhả. Đề 1 chưa nói lúc nhả; chọn cách giữ sáng để phân biệt với bài 2. |
| [02](bai_02.c) | Nhấn sáng, nhả tắt; xử lý độc lập cả 8 nút. |
| [03](bai_03.c) | Mỗi lần nhấn đảo LED tương ứng một lần; giữ nút không đảo liên tục. |
| [04](bai_04.c) | Sáng 500 ms, tắt 500 ms: chu kỳ 1 giây. |
| [05](bai_05.c) | Một LED chạy PC7 → PC0 rồi lặp; chọn 200 ms mỗi bước vì đề chưa quy định. |
| [06](bai_06.c) | 0 → 9 → 0, mỗi số 1 giây. |
| [07](bai_07.c) | PD0 tăng, PD1 giảm; 9 tăng về 0, 0 giảm về 9. |
| [08](bai_08.c) | 0 → 1 → … → 9 → 8 → … → 0, mỗi số 1 giây. |
| [09](bai_09.c) | Bắt đầu 0000, mỗi khoảng 1 giây tăng một; 9999 về 0000. |
| [10](bai_10.c) | Mỗi lần nhấn tăng/giảm một; giữ nút vẫn quét đủ 4 digit. |
| [11](bai_11.c) | INT0 Falling tăng, INT1 Falling giảm; bắt đầu 0000, quay vòng 0–9999. |
| [12](bai_12.c) | 0xAA xen kẽ 0x55. INT0 tăng tần số, INT1 giảm tần số. Chu kỳ ban đầu 1 giây; nửa chu kỳ thay đổi 50 ms, giới hạn 50–1000 ms. Chọn Falling Edge vì đề chưa nêu cạnh. |
| [13](bai_13.c) | Điện áp một số lẻ: ví dụ 005.0 tại 5 V. |
| [14](bai_14.c) | Điện áp hai số lẻ: ví dụ 05.00 tại 5 V. |
| [15](bai_15.c) | Ban đầu hai số lẻ; nhấn lần 1 một số lẻ, lần 2 hai số lẻ, lặp lại. |
| [16](bai_16.c) | LM35: 250 mV hiển thị khoảng 0025, tức 25 °C; làm tròn đến độ nguyên. Không hiển thị ký hiệu °C. |
| [23](bai_23.c) | Mỗi lần nhấn PC5 đổi kênh 0 → 7 → 0; LED PD tương ứng sáng. Hiển thị ba số lẻ như mẫu: 5.000 tại 5 V. |
| [24](bai_24.c) | Bắt đầu 1234 và dừng. PD0 chạy tăng, PD1 dừng; INT0/INT1 Falling tăng/giảm thời gian t. |
| [25](bai_25.c) | Bắt đầu 1234 và dừng. PD0 đảo chạy giảm/dừng; INT0/INT1 Rising tăng/giảm t. Giảm dưới 0000 về 9999. |
| [26](bai_26.c) | Bắt đầu 1234 và dừng. INT0 Rising đảo chạy tăng/dừng; PD0 tăng t tối đa 2 s, PD1 giảm t tối thiểu 200 ms. |
| [27](bai_27.c) | Bắt đầu 1234. PD0 chạy tăng khoảng 1 s/lần, PD1 dừng; 9999 về 0000. |
| [28](bai_28.c) | Bắt đầu 1234. PD0 nhấn lần 1 chạy tăng khoảng 1 s/lần, lần 2 dừng. |
| [29](bai_29.c) | Bắt đầu 1234. Giữ PD0 khoảng 600 ms tăng một; nhả dừng. Nhấn lại đếm lại đủ 600 ms. |
| [30](bai_30.c) | Bắt đầu 1234 và tự tăng sau mỗi t; PD0 tăng t, PD1 giảm t. |
| [31](bai_31.c) | Hiện số lớn nhất trong các nút đang nhấn; không nhấn nút nào thì tắt LED. |

Bài 24–26, 30 chọn t ban đầu 1 s và bước điều chỉnh 100 ms. Bài 24, 25, 30 chọn giới hạn 200 ms–10 s để tránh t về 0 hoặc tràn biến; đề chưa quy định các giá trị này. Bài 26 giữ đúng giới hạn 200 ms–2 s của đề. Các bài START/STOP bắt đầu đếm lại thời gian khi chạy lại.

Các nút đọc bằng chương trình có lọc hai mẫu liên tiếp khoảng 20 ms và phát hiện lần nhấn. Riêng ngắt ngoài phản ứng với mỗi cạnh, đúng yêu cầu đề. Dùng nút Proteus không dội hoặc mạch chống dội ngoài cho PD2/PD3. Với cách nối nút xuống GND đang dùng, Falling xảy ra khi nhấn, Rising khi nhả; muốn Rising khi nhấn thì đổi mạch nút sang kéo xuống và nhấn lên VCC.

Đã chạy kiểm thử trên máy tính cho cả 25 bài bằng mã C trích trực tiếp từ các file, chuyển riêng cú pháp đặc thù và giả lập thanh ghi/delay/ADC. Đã kiểm tra vòng đếm, chống lặp khi giữ nút, giới hạn thời gian, cạnh được cấu hình, toàn bộ 1024 mã ADC và toàn bộ 1024 tổ hợp nút của bài 31. Kiểm thử hiện chạy cả phần khởi tạo thật của mỗi bài trước các bước trong vòng lặp, và kiểm tra mã không ghi thanh ghi điều khiển JTAG.

Chạy lại kiểm thử trên máy có Python 3 và GCC trong PATH:

```powershell
python kiemtra.py
```

Chưa biên dịch bằng CodeVisionAVR và chưa mô phỏng trong Proteus. Kiểm thử máy tính không xác nhận thời gian máy thực, chống dội vật lý, tín hiệu ADC hoặc đấu mạch. Thời gian ở các bài quét LED là xấp xỉ vì cộng thời gian delay, chưa bù thời gian thực thi lệnh. Để kiểm tra tiếp: biên dịch từng bài, nạp HEX vào ATmega16 8 MHz, thử các tình huống trong bảng, rồi đo chu kỳ bằng oscilloscope/logic analyzer trong Proteus.
