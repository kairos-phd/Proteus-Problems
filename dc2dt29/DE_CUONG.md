# DC2DT29 — nội dung đề cương

Nguồn: https://docs.google.com/document/d/1mh2D75xNiBHrTItzRjf3hnnpLvd3hsYg/edit

Bản chép nội dung văn bản từ trình xem Google Docs; số đề được gán theo thứ tự xuất hiện. Không thay thế bản Word gốc.

## Đề 01

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển 8 LED đơn nối vào PORTD và nhận lệnh điều khiển từ 2 nút bấm nối vào PC0 và PC1.
Lập trình chương trình hoạt động như sau:
- LED sẽ chạy từ trái sang phải, sau khi hết hàng LED sẽ vòng lại LED đầu tiên.
- Ấn nút thứ nhất thì sẽ tăng tốc độ chạy LED, nhưng không nhanh quá 100Hz.
- Ấn nút thứ hai thì sẽ giảm tốc độ chạy LED, nhưng không chậm dưới 4Hz.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 2 nút bấm.
Thiết lập Timer 0 hoạt động ở chế độ Normal với tần số 125kHz, kích hoạt ngắt tràn.
Thiết lập ngắt ngoài 0 và 1 hoạt động ở chế độ Falling Edge.
Lập trình chương trình hoạt động như sau:
- Tính toán để tạo khoảng thời gian chính xác 0.5(s) bằng timer, ghi chú vào chương trình phục vụ ngắt.
- Ban đầu số hiển thị là 8000
- Ngắt ngoài 0 được kích hoạt thì số hiển thị sẽ tăng 1 đơn vị, nhưng không tăng quá 8888.
- Ngắt ngoài 1 được kích hoạt thì số hiển thị sẽ giảm 1 đơn vị, nhưng không giảm dưới 8000.
- Ấn nút thứ 1 thì số hiển thị sẽ tự động tăng sau mỗi 0.5(s), nếu tăng quá 9000 thì vòng lại 1000, ấn nút thứ 2 thì số hiển thị sẽ dừng lại.

## Đề 02

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 10 nút bấm.
Lập trình chương trình hoạt động như sau:
- Khi ấn một nút bất kỳ thì LED 7 thanh sẽ hiển thị số tương ứng với nút đó.
- Nhả nút ra thì số hiển thị giữ nguyên.
- Khi ấn đồng thời nhiều nút thì LED 7 thanh sẽ hiển thị số lớn hơn.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 3 nút bấm nối vào PB0, PB1, PB2.
Thiết lập Timer 0 hoạt động ở chế độ Normal với tần số 125kHz, kích hoạt ngắt tràn.
Thiết lập Timer 2 hoạt động ở chế độ Normal, kích hoạt ngắt tràn.
Lập trình chương trình hoạt động như sau:
- Tính toán để tạo khoảng thời gian chính xác 0.5(s) bằng timer 0, ghi chú vào chương trình phục vụ ngắt.
- Sử dụng ngắt tràn Timer 2 để quét LED 7 thanh.
- Ban đầu số hiển thị là 1234.
- Ấn nút thứ 1 thì số hiển thị tăng lên 1 đơn vị, nhưng không tăng quá 9999.
- Ấn nút thứ 2 thì số hiển thị giảm 1 đơn vị, nhưng không giảm dưới 0.
- Ấn nút thứ 3 thì số hiển thị sẽ tự động tăng sau mỗi 0.5(s), tăng đến 9999 thì dừng.

## Đề 03

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 2 nút bấm.
Lập trình chương trình hoạt động như sau:
- Trạng thái ban đầu LED hiển thị số 5
- Ấn nút thứ nhất thì số hiển thị tăng 1 đơn vị, nếu tăng quá 9 thì vòng lại 0.
- Ấn nút thứ hai thì số hiển thị giảm 1 đơn vị, nếu giảm dưới 0 thì vòng lên 9.
- Yêu cầu chờ nhả nút ra để thực hiện lệnh tăng/giảm lượt tiếp theo.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 3 nút bấm nối vào PB0, PB1, PB2.
Thiết lập Timer 0 hoạt động ở chế độ Normal với tần số 31250Hz, kích hoạt ngắt tràn
Thiết lập ngắt ngoài 0 hoạt động ở chế độ Falling Edge.
Lập trình chương trình hoạt động như sau:
- Tính toán để tạo khoảng thời gian chính xác 0.5(s) bằng timer, ghi chú vào chương trình phục vụ ngắt.
- Ban đầu số hiển thị là 1111.
- Ấn nút thứ nhất thì số hiển thị sẽ tăng 1 đơn vị, nhưng không tăng quá 9000.
- Ấn nút thứ hai thì số hiển thị sẽ giảm 1 đơn vị, nhưng không giảm dưới 1000.
- Ấn nút thứ 3 thì số hiển thị sẽ tự động tăng sau mỗi 0.5(s), nếu tăng quá 9000 thì vòng lại 1000.
- Ngắt ngoài 0 được kích hoạt thì số hiển thị dừng lại.

## Đề 04

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển 8 LED nối vào PORTD và nhận lệnh điều khiển từ 2 nút bấm nối vào PC0 và PC1.
Lập trình chương trình hoạt động như sau:
- LED sẽ chạy từ phải sang trái, sau khi hết hàng LED sẽ vòng lại LED đầu tiên
- Ấn nút thứ nhất thì sẽ tăng tốc độ chạy LED, nhưng không nhanh quá 25Hz.
- Ấn nút thứ hai thì sẽ giảm tốc độ chạy LED, nhưng không chậm dưới 5Hz.
- Ấn và giữ nút thì tốc độ thay đổi liên tục.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 2 nút bấm nối vào PD6 và PD7. Thiết lập ngắt ngoài 0 hoạt động ở chế độ Falling Edge
Lập trình chương trình hoạt động như sau:
- Ban đầu số hiển thị là 1000.
- Ấn nút thứ nhất thì số hiển thị tăng lên 1 đơn vị, nhưng không tăng quá 9999.
- Ấn nút thứ hai thì số hiển thị giảm 1 đơn vị, nhưng không giảm dưới 0.
- Yêu cầu chờ nhả nút ra để thực hiện lệnh tăng/giảm lượt tiếp theo.
- Ngắt ngoài 0 được kích hoạt thì reset số hiển thị về 1000.

## Đề 05

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 2 nút bấm.
Lập trình chương trình hoạt động như sau:
	- Trạng thái ban đầu LED hiển thị số 6
	- Ấn nút thứ nhất thì số hiển thị tăng 1 đơn vị, tăng tối đa đến 9 thì dừng lại.
	- Ấn nút thứ hai thì số hiển thị giảm 1 đơn vị, giảm tối thiểu đến 0 thì dừng lại.
	- Yêu cầu chờ nhả nút ra để thực hiện lệnh tăng/giảm lượt tiếp theo.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 2 nút bấm nối vào PB0, PB1. Thiết lập ngắt ngoài 1 hoạt động ở chế độ Rising Edge.
Lập trình chương trình hoạt động như sau:
- Ban đầu số hiển thị là 6000.
- Ấn nút thứ nhất thì số hiển thị sẽ tự động giảm với chu kì 1(s), sau khi giảm đến 0 sẽ dừng lại.
- Ấn nút thứ hai thì số hiển thị sẽ dừng lại.
- Ngắt ngoài 1 được kích hoạt thì reset số hiển thị về 6000.

## Đề 06

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 2 nút bấm nối vào PA0 và PA1.
Lập trình chương trình hoạt động như sau:
	- Trạng thái ban đầu LED hiển thị số 0.
	- Ấn nút thứ nhất thì số hiển thị sẽ tự động tăng với chu kì 100 (ms).
	- Ấn nút thứ hai thì số hiển thị sẽ dừng lại.
	- Nếu số tăng quá 9 thì sẽ vòng lại 0.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 2 nút bấm nối vào PA0, PA1. Thiết lập ngắt ngoài 1 hoạt động ở chế độ Falling Edge.
Lập trình chương trình hoạt động như sau:
- Ban đầu số hiển thị là 0.
- Ngắt ngoài được kích hoạt thì số hiển thị sẽ tự động tăng sau một khoảng thời gian t, tăng quá 9000 thì vòng về 0.
- Ấn nút thứ nhất thì sẽ tăng thời gian tăng số này, nhưng không tăng quá 2 (s).
- Ấn nút thứ hai thì sẽ giảm thời gian tăng số này, nhưng không giảm dưới 100 (ms).

## Đề 07

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 2 nút bấm nối vào PA0 và PA1.
Lập trình chương trình hoạt động như sau:
	- Số hiển thị sẽ tự động tăng từ 0 đến 9 sau một khoảng thời gian t.
	- Nếu số tăng quá 9 thì sẽ vòng lại 0.
	- Ấn nút thứ nhất thì sẽ làm tăng thời gian tăng số, nhưng không tăng quá 2 (s).
	- Ấn nút thứ hai thì sẽ làm giảm thời gian tăng số, nhưng không giảm dưới 200 (ms).

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 2 nút bấm nối vào PB0, PB1. Thiết lập 2 ngắt ngoài 0 và 1 hoạt động ở chế độ Falling Edge
Lập trình chương trình hoạt động như sau:
- Ban đầu số hiển thị là 0.
- Ngắt ngoài 0 được kích hoạt thì số hiển thị sẽ tự động giảm sau một khoảng thời gian t, giảm dưới 0 thì vòng lên 9999.
- Ngắt ngoài 1 được kích hoạt thì số hiển thị sẽ dừng lại.
- Ấn nút thứ nhất thì sẽ tăng thời gian tăng số này, nhưng không tăng quá 2(s).
- Ấn nút thứ hai thì sẽ giảm thời gian tăng số này, nhưng không giảm dưới 100 (ms).

## Đề 08

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 2 nút bấm nối vào PA0 và PA1.
Lập trình chương trình hoạt động như sau:
	- Trạng thái ban đầu LED hiển thị số 9.
- Ấn nút thứ nhất thì số hiển thị sẽ tự động giảm với chu kì 300 (ms).
	- Ấn nút thứ hai thì số hiển thị sẽ dừng lại.
	- Nếu số giảm dưới 0 thì sẽ vòng lại 9.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 1 nút bấm nối vào PA0. Lập trình chương trình hoạt động như sau:
- Thiết lập 2 ngắt ngoài 0 và 1 hoạt động ở chế độ Falling Edge.
- Ban đầu số hiển thị là 5555.
- Ấn nút lần thứ nhất thì số hiển thị sẽ tự động tăng sau mỗi khoảng thời gian t, ấn nút lần thứ 2 thì số hiển thị sẽ dừng lại.
- Nếu ngắt ngoài 0 được kích hoạt thì sẽ tăng khoảng thời gian t, nhưng không tăng quá 3 (s).
- Nếu ngắt ngoài 1 được kích hoạt thì sẽ giảm khoảng thời gian t, nhưng không giảm dưới 500 (ms).

## Đề 09

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển 8 LED đơn nối vào PORTD và nhận lệnh điều khiển từ 8 nút bấm nối vào PORTA.
Lập trình chương trình hoạt động như sau:
- Khi ấn một nút bất kỳ thì LED tương ứng sẽ đảo trạng thái (LED đang sáng sẽ tắt và ngược lại).
- Nếu ấn và giữ nút thì LED đảo trạng thái liên tục với chu kì 300 (ms).

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để đo điện áp từ 0-5V và đo nhiệt độ bằng cảm biến nhiệt LM35, hiển thị giá trị lên 3 LED 7 thanh, sử dụng 2 nút bấm để điều khiển, sử dụng 4 LED đơn để hiển thị chế độ.
Lập trình chương trình hoạt động như sau:
- Đo điện áp bằng chân ADC0, đo nhiệt độ bằng chân ADC1.
- Ban đầu LED hiển thị giá trị điện áp với độ chính xác 0.1V.
- Khi ấn nút thứ nhất thì sẽ chuyển đổi giữa đo điện áp và đo nhiệt độ, sử dụng LED 1 và LED 2 để cho biết đang ở chế độ đo nào.
- Khi ấn nút thứ hai thì sẽ chuyển đổi độ chính xác khi đo điện áp giữa 0.1V và 0.01V, sử dụng LED 3 và LED 4 để cho biết đang ở độ chính xác nào.

## Đề 10

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 2 nút bấm.
Lập trình chương trình hoạt động như sau:
	- Trạng thái ban đầu LED hiển thị số 5.
	- Ấn nút thứ nhất thì số hiển thị tăng 1 đơn vị, nếu tăng quá 9 thì vòng lại 0.
	- Ấn nút thứ hai thì số hiển thị giảm 1 đơn vị, nếu giảm dưới 0 thì vòng lên 9.
	- Nếu ấn và giữ nút thì số thay đổi liên tục sau mỗi 300 (ms).

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để đo điện áp từ 0 - 5V nhận lệnh điều khiển từ 1 nút bấm nối vào PD0, hiển thị giá trị lên LED 7 thanh 4 số, sử dụng thêm một con LED 7 thanh hiển thị số.
Lập trình chương trình hoạt động như sau:
- Ban đầu đo điện áp, hiển thị điện áp với độ chính xác 0.1V.
- Ấn nút lần thứ nhất thì chuyển đổi sang độ chính xác 0.01V, ấn lần tiếp theo thì chuyển sang độ chính xác 0.1V,...
- Giá trị trên con LED 7 thanh đơn hiển thị 1 nếu đang đo độ chính xác là 0.1V, hiển thị 2 nếu đang đo độ chính xác là 0.01V.

## Đề 11

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển 8 LED đơn nối vào PORTD và nhận lệnh điều khiển từ 8 nút bấm nối vào PORTA.
Lập trình chương trình hoạt động như sau:
- Khi ấn một nút bất kỳ thì LED tương ứng sẽ đảo trạng thái (LED đang sáng sẽ tắt và ngược lại).
- Chờ nhả nút ra mới thực hiện đảo trạng thái lần tiếp theo.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 2 nút bấm nối vào PD6 và PD7. Thiết lập ngắt ngoài 0 hoạt động ở chế độ Falling Edge
Lập trình chương trình hoạt động như sau:
- Ban đầu số hiển thị là 1000.
- Ấn nút thứ nhất thì số hiển thị tăng lên 1 đơn vị, nhưng không tăng quá 9999.
- Ấn nút thứ hai thì số hiển thị giảm 1 đơn vị, nhưng không giảm dưới 0.
	- Yêu cầu chờ nhả nút ra để thực hiện lệnh tăng/giảm lượt tiếp theo.
	- Ngắt ngoài 0 được kích hoạt thì reset số hiển thị về 1000.

## Đề 12

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển 8 LED đơn nối vào PORTD và nhận lệnh điều khiển từ 2 nút bấm nối vào PA1 và PA2.
Lập trình chương trình hoạt động như sau:
- Trạng thái ban đầu chỉ có LED thứ 2 sáng.
- Ấn nút thứ nhất thì LED sáng sẽ di chuyển sang phải.
- Ấn nút thứ hai thì LED sáng sẽ di chuyển sang trái.
- Nếu LED di chuyển đến cuối cùng thì sẽ vòng lại.
- Nếu ấn và giữ nút thì LED sẽ di chuyển với chu kì là 200 (ms).

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 2 nút bấm nối vào PB0, PB1. Thiết lập ngắt ngoài 1 hoạt động ở chế độ Rising Edge.
Lập trình chương trình hoạt động như sau:
- Ban đầu số hiển thị là 6000.
- Ấn nút thứ nhất thì số hiển thị sẽ tự động giảm với chu kì 1(s), sau khi giảm đến 0 sẽ dừng lại.
- Ấn nút thứ hai thì số hiển thị sẽ dừng lại.
- Ngắt ngoài 1 được kích hoạt thì reset số hiển thị về 6000.

## Đề 13

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển 8 LED đơn nối vào PORTD và nhận lệnh điều khiển từ 2 nút bấm nối vào PB6 và PB7.
Lập trình chương trình hoạt động như sau:
- Trạng thái ban đầu 8 LED nhấp nháy xen kẽ với chu kì 100 (ms).
- Ấn nút thứ nhất thì tăng tần số nhấp nháy.
- Ấn nút thứ hai thì giảm tần số nhấp nháy.
- Nếu ấn và giữ nút thì tần số sẽ tiếp tục thay đổi mà không phải chờ nhả nút ra.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 2 nút bấm nối vào PA0, PA1. Thiết lập ngắt ngoài 1 hoạt động ở chế độ Falling Edge.
Lập trình chương trình hoạt động như sau:
- Ban đầu số hiển thị là 0.
- Ngắt ngoài được kích hoạt thì số hiển thị sẽ tự động tăng sau một khoảng thời gian t, tăng quá 9000 thì vòng về 0.
- Ấn nút thứ nhất thì sẽ tăng thời gian tăng số này, nhưng không tăng quá 2(s).
- Ấn nút thứ hai thì sẽ giảm thời gian tăng số này, nhưng không giảm dưới 100(ms).

## Đề 14

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 9 nút bấm.
Lập trình chương trình hoạt động như sau:
	- Khi ấn 1 nút thì LED sẽ hiển thị số tương ứng từ 1-9.
	- Khi không ấn nút nào thì LED hiển thị số 0.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 2 nút bấm nối vào PB0, PB1. Thiết lập 2 ngắt ngoài 0 và 1 hoạt động ở chế độ Falling Edge.
Lập trình chương trình hoạt động như sau:
- Ban đầu số hiển thị là 0
- Ngắt ngoài 0 được kích hoạt thì số hiển thị sẽ tự động giảm sau một khoảng thời gian t, giảm dưới 0 thì vòng lên 9999.
- Ngắt ngoài 1 được kích hoạt thì số hiển thị sẽ dừng lại.
- Ấn nút thứ nhất thì sẽ tăng thời gian tăng số này, nhưng không tăng quá 2(s).
- Ấn nút thứ hai thì sẽ giảm thời gian tăng số này, nhưng không giảm dưới 100(ms).

## Đề 15

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển 8 LED đơn nối vào PORTD và nhận lệnh điều khiển từ 2 nút bấm nối vào PC0 và PC1.
Lập trình chương trình hoạt động như sau:
	- LED sẽ chạy từ trái sang phải, sau khi hết hàng LED sẽ vòng lại LED đầu tiên.
	- Ấn nút thứ nhất thì sẽ tăng tốc độ chạy LED, nhưng không nhanh quá 100Hz.
	- Ấn nút thứ hai thì sẽ giảm tốc độ chạy LED, nhưng không chậm dưới 4Hz.
	- Ấn và giữ nút thì tốc độ thay đổi liên tục.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 1 nút bấm nối vào PA0. Lập trình chương trình hoạt động như sau:
- Thiết lập 2 ngắt ngoài 0 và 1 hoạt động ở chế độ Falling Edge.
- Ban đầu số hiển thị là 5555.
- Ấn nút lần thứ nhất thì số hiển thị sẽ tự động tăng sau mỗi khoảng thời gian t, ấn nút lần thứ 2 thì số hiển thị sẽ dừng lại.
- Nếu ngắt ngoài 0 được kích hoạt thì sẽ tăng khoảng thời gian t, nhưng không tăng quá 3 (s).
- Nếu ngắt ngoài 1 được kích hoạt thì sẽ giảm khoảng thời gian t, nhưng không giảm dưới 500 (ms).

## Đề 16

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 10 nút bấm.
Lập trình chương trình hoạt động như sau:
	- Khi ấn một nút bất kỳ thì LED 7 thanh sẽ hiển thị số tương ứng với nút đó.
	- Nhả nút ra thì số hiển thị giữ nguyên.
	- Khi ấn đồng thời nhiều nút thì LED 7 thanh sẽ hiển thị số lớn hơn.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để đo điện áp từ 0-5V và đo nhiệt độ bằng cảm biến nhiệt LM35, hiển thị giá trị lên 3 LED 7 thanh, sử dụng 2 nút bấm để điều khiển, sử dụng 4 LED đơn để hiển thị chế độ.
Lập trình chương trình hoạt động như sau:
- Đo điện áp bằng chân ADC0, đo nhiệt độ bằng chân ADC1.
- Ban đầu LED hiển thị giá trị điện áp với độ chính xác 0.1 V.
- Khi ấn nút thứ nhất thì sẽ chuyển đổi giữa đo điện áp và đo nhiệt độ, sử dụng LED 1 và LED 2 để cho biết đang ở chế độ đo nào.
- Khi ấn nút thứ hai thì sẽ chuyển đổi độ chính xác khi đo điện áp giữa 0.1V và 0.01V, sử dụng LED 3 và LED 4 để cho biết đang ở độ chính xác nào.

## Đề 17

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 2 nút bấm.
Lập trình chương trình hoạt động như sau:
	- Trạng thái ban đầu LED hiển thị số 5
	- Ấn nút thứ nhất thì số hiển thị tăng 1 đơn vị, nếu tăng quá 9 thì vòng lại 0.
	- Ấn nút thứ hai thì số hiển thị giảm 1 đơn vị, nếu giảm dưới 0 thì vòng lên 9.
	- Yêu cầu chờ nhả nút ra để thực hiện lệnh tăng/giảm lượt tiếp theo.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để đo điện áp từ 0-5V nhận lệnh điều khiển từ 1 nút bấm nối vào PD0, hiển thị giá trị lên LED 7 thanh 4 số, sử dụng thêm một con LED 7 thanh hiển thị số.
Lập trình chương trình hoạt động như sau:
- Ban đầu đo điện áp, hiển thị điện áp với độ chính xác 0.1V.
- Ấn nút lần thứ nhất thì chuyển đổi sang độ chính xác 0.01V, ấn lần tiếp theo thì chuyển sang độ chính xác 0.1V,...
- Giá trị trên con LED 7 thanh đơn hiển thị 1 nếu đang đo độ chính xác là 0.1V, hiển thị 2 nếu đang đo độ chính xác là 0.01V.

## Đề 18

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển 8 LED nối vào PORTD và nhận lệnh điều khiển từ 2 nút bấm nối vào PC0 và PC1.
Lập trình chương trình hoạt động như sau:
	- LED sẽ chạy từ phải sang trái, sau khi hết hàng LED sẽ vòng lại LED đầu tiên
	- Ấn nút thứ nhất thì sẽ tăng tốc độ chạy LED, nhưng không nhanh quá 25Hz.
	- Ấn nút thứ hai thì sẽ giảm tốc độ chạy LED, nhưng không chậm dưới 5Hz.
	- Ấn và giữ nút thì tốc độ thay đổi liên tục.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để đo 3 tín hiệu điện áp từ 0-5V đưa vào 3 chân ADC0, ADC1, ADC2 nhận lệnh điều khiển từ 1 nút bấm nối vào PD0, hiển thị giá trị lên LED 7 thanh 4 số, sử dụng thêm một con LED 7 thanh hiển thị số. Lập trình chương trình hoạt động như sau:
- Ban đầu đo điện áp tại đầu vào chân ADC0, hiển thị với độ chính xác 0.1V
- Ấn nút thì chuyển sang đo điện áp tại chân ADC tiếp theo (0 –> 1 –> 2 –> 0)
- Giá trị trên con LED 7 thanh đơn hiển thị 0 nếu đang đo điện áp tại chân ADC0, hiển thị 1 nếu đang đo điện áp tại chân ADC1,hiển thị 2 nếu đang đo điện áp tại chân ADC2.
- Yêu cầu chờ nhả nút ra mới chuyển đổi lần tiếp theo.

## Đề 19

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 2 nút bấm.
Lập trình chương trình hoạt động như sau:
	- Trạng thái ban đầu LED hiển thị số 6
	- Ấn nút thứ nhất thì số hiển thị tăng 1 đơn vị, tăng tối đa đến 9 thì dừng lại.
	- Ấn nút thứ hai thì số hiển thị giảm 1 đơn vị, giảm tối thiểu đến 0 thì dừng lại.
	- Yêu cầu chờ nhả nút ra để thực hiện lệnh tăng/giảm lượt tiếp theo.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 2 nút bấm nối vào PA0 và PA1. Lập trình chương trình hoạt động như sau:
- Thiết lập ngắt ngoài 0 hoạt động ở chế độ Falling Edge.
- Ban đầu số hiển thị là 10.
- Ấn nút thứ nhất thì số hiển thị tăng 1 đơn vị, nhưng không tăng quá 9999.
- Ấn nút thứ 2 thì số hiển thị giảm 1 đơn vị, nhưng không giảm dưới 1.
- Ấn và giữ nút thì số thay đổi liên tục.
- Nếu ngắt ngoài 0 được kích hoạt thì số hiển thị tự động giảm dần sau mỗi 1(s).
- Nếu số hiển thị giảm đến 0 thì reset về 10 và dừng lại.

## Đề 20

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 2 nút bấm nối vào PA0 và PA1.
Lập trình chương trình hoạt động như sau:
	- Trạng thái ban đầu LED hiển thị số 0.
	- Ấn nút thứ nhất thì số hiển thị sẽ tự động tăng với chu kì 100 (ms).
	- Ấn nút thứ hai thì số hiển thị sẽ dừng lại.
	- Nếu số tăng quá 9 thì sẽ vòng lại 0.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để đo 3 tín hiệu điện áp từ 0 - 5V đưa vào 3 chân ADC0, ADC1, ADC2, hiển thị giá trị lên LED 7 thanh 4 số, sử dụng thêm một con LED 7 thanh hiển thị số.
Lập trình chương trình hoạt động như sau:
- Thiết lập ngắt ngoài 1 hoạt động ở chế độ Rising Edge.
- Ban đầu đo điện áp tại đầu vào chân ADC0, hiển thị với độ chính xác 0.1V.
- Ngắt ngoài được kích hoạt thì chuyển sang đo điện áp tại chân ADC tiếp theo (0 –> 1 –> 2 –> 0).
- Giá trị trên con LED 7 thanh đơn hiển thị 0 nếu đang đo điện áp tại chân ADC0, hiển thị 1 nếu đang đo điện áp tại chân ADC1,hiển thị 2 nếu đang đo điện áp tại chân ADC2.

## Đề 21

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 2 nút bấm nối vào PA0 và PA1.
Lập trình chương trình hoạt động như sau:
- Số hiển thị sẽ tự động tăng từ 0 đến 9 sau một khoảng thời gian t.
- Nếu số tăng quá 9 thì sẽ vòng lại 0.
- Ấn nút thứ nhất thì sẽ làm tăng thời gian tăng số, nhưng không tăng quá 2(s).
- Ấn nút thứ hai thì sẽ làm giảm thời gian tăng số, nhưng không giảm dưới 200 (ms)

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 3 nút bấm nối vào PB0, PB1, PB2.Thiết lập Timer 0 hoạt động ở chế độ Normal với tần số 31250Hz, kích hoạt ngắt tràn. Thiết lập Timer 2 hoạt động ở chế độ Normal, kích hoạt ngắt tràn.
Lập trình chương trình hoạt động như sau:
- Tính toán để tạo khoảng thời gian chính xác 0.5(s) bằng timer 0, ghi chú vào chương trình phục vụ ngắt.Sử dụng ngắt tràn Timer 2 để quét LED 7 thanh
- Ban đầu số hiển thị là 1234.
- Ấn nút thứ 1 thì số hiển thị tăng lên 1 đơn vị, nhưng không tăng quá 9999.
- Ấn nút thứ 2 thì số hiển thị giảm 1 đơn vị, nhưng không giảm dưới 0.
- Ấn nút thứ 3 thì số hiển thị sẽ tự động giảm sau mỗi 0.5(s), giảm đến 0 thì dừng.

## Đề 22

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 2 nút bấm nối vào PA0 và PA1.
Lập trình chương trình hoạt động như sau:
	- Trạng thái ban đầu LED hiển thị số 9.
- Ấn nút thứ nhất thì số hiển thị sẽ tự động giảm với chu kì 300 (ms).
	- Ấn nút thứ hai thì số hiển thị sẽ dừng lại.
	- Nếu số giảm dưới 0 thì sẽ vòng lại 9.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 2 nút bấm.
Thiết lập Timer 0 hoạt động ở chế độ Normal với tần số 125kHz, kích hoạt ngắt tràn. Thiết lập ngắt ngoài 0 và 1 hoạt động ở chế độ Falling Edge.
Lập trình chương trình hoạt động như sau:
- Tính toán để tạo khoảng thời gian chính xác 0.5(s) bằng timer.
- Ban đầu số hiển thị là 8000
- Ngắt ngoài 0 được kích hoạt thì số hiển thị sẽ tăng 1, không  quá 8888.
- Ngắt ngoài 1 được kích hoạt thì số hiển thị sẽ giảm 1 đơn vị, nhưng không giảm dưới 8000.
- Ấn nút thứ 1 thì số hiển thị sẽ tự động tăng sau mỗi 0.5(s), nếu tăng quá 9000 thì vòng lại 1000.
- Ấn nút thứ 2 thì số hiển thị sẽ dừng lại.

## Đề 23

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển 8 LED đơn nối vào PORTD và nhận lệnh điều khiển từ 8 nút bấm nối vào PORTA.
Lập trình chương trình hoạt động như sau:
- Khi ấn một nút bất kỳ thì LED tương ứng sẽ đảo trạng thái (LED đang sáng sẽ tắt và ngược lại).
- Nếu ấn và giữ nút thì LED đảo trạng thái liên tục với chu kì 300 (ms).

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 3 nút bấm nối vào PB0, PB1, PB2.
Thiết lập Timer 0 hoạt động ở chế độ Normal với tần số 125kHz, kích hoạt ngắt tràn.
Thiết lập Timer 2 hoạt động ở chế độ Normal, kích hoạt ngắt tràn.
Lập trình chương trình hoạt động như sau:
- Tính toán để tạo khoảng thời gian chính xác 0.5(s) bằng timer 0, ghi chú vào chương trình phục vụ ngắt.
- Sử dụng ngắt tràn Timer 2 để quét LED 7 thanh.
- Ban đầu số hiển thị là 1234.
- Ấn nút thứ 1 thì số hiển thị tăng lên 1 đơn vị, nhưng không tăng quá 9999.
- Ấn nút thứ 2 thì số hiển thị giảm 1 đơn vị, nhưng không giảm dưới 0.
- Ấn nút thứ 3 thì số hiển thị sẽ tự động tăng sau mỗi 0.5(s), tăng đến 9999 thì dừng.

## Đề 24

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 2 nút bấm.
Lập trình chương trình hoạt động như sau:
- Trạng thái ban đầu LED hiển thị số 5.
- Ấn nút thứ nhất thì số hiển thị tăng 1 đơn vị, nếu tăng quá 9 thì vòng lại 0.
- Ấn nút thứ hai thì số hiển thị giảm 1 đơn vị, nếu giảm dưới 0 thì vòng lên 9.
- Nếu ấn và giữ nút thì số thay đổi liên tục sau mỗi 300(ms).

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 3 nút bấm nối vào PB0, PB1, PB2.
Thiết lập Timer 0 hoạt động ở chế độ Normal với tần số 31250Hz, kích hoạt ngắt tràn. Thiết lập ngắt ngoài 0 hoạt động ở chế độ Falling Edge.
Lập trình chương trình hoạt động như sau:
- Tính toán để tạo khoảng thời gian chính xác 0.5(s) bằng timer.
- Ban đầu số hiển thị là 1111.
- Ấn nút thứ nhất thì số hiển thị sẽ tăng 1 đơn vị, nhưng không tăng quá 9000.
- Ấn nút thứ hai thì số hiển thị sẽ giảm 1 đơn vị, nhưng không giảm dưới 1000.
- Nếu ấn và giữ nút thì số hiển thị tăng liên tục.
- Ấn nút thứ 3 thì số hiển thị sẽ tự động tăng sau mỗi 0.5(s), nếu tăng quá 9000 thì vòng lại 1000.
- Ngắt ngoài 0 được kích hoạt thì số hiển thị dừng lại.

## Đề 25

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển 8 LED đơn nối vào PORTD và nhận lệnh điều khiển từ 8 nút bấm nối vào PORTA.
Lập trình chương trình hoạt động như sau:
- Khi ấn một nút bất kỳ thì LED tương ứng sẽ đảo trạng thái (LED đang sáng sẽ tắt và ngược lại).
- Chờ nhả nút ra mới thực hiện đảo trạng thái lần tiếp theo.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 2 nút bấm nối vào PA0, PA1. Thiết lập ngắt ngoài 1 hoạt động ở chế độ Falling Edge.
Lập trình chương trình hoạt động như sau:
- Ban đầu số hiển thị là 0.
- Ngắt ngoài được kích hoạt thì số hiển thị sẽ tự động tăng sau một khoảng thời gian t, tăng quá 9000 thì vòng về 0.
- Ấn nút thứ nhất thì sẽ tăng thời gian tăng số này, nhưng không tăng quá 2 (s).
- Ấn nút thứ hai thì sẽ giảm thời gian tăng số này, nhưng không giảm dưới 100 (ms).

## Đề 26

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển 8 LED đơn nối vào PORTD và nhận lệnh điều khiển từ 2 nút bấm nối vào PA1 và PA2.
Lập trình chương trình hoạt động như sau:
- Trạng thái ban đầu chỉ có LED thứ 2 sáng.
- Ấn nút thứ nhất thì LED sáng sẽ di chuyển sang phải.
- Ấn nút thứ hai thì LED sáng sẽ di chuyển sang trái.
- Nếu LED di chuyển đến cuối cùng thì sẽ vòng lại.
- Nếu ấn và giữ nút thì LED sẽ di chuyển với chu kì là 200 (ms).

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 2 nút bấm nối vào PB0, PB1. Thiết lập 2 ngắt ngoài 0 và 1 hoạt động ở chế độ Falling Edge
Lập trình chương trình hoạt động như sau:
- Ban đầu số hiển thị là 0.
- Ngắt ngoài 0 được kích hoạt thì số hiển thị sẽ tự động giảm sau một khoảng thời gian t, giảm dưới 0 thì vòng lên 9999.
- Ngắt ngoài 1 được kích hoạt thì số hiển thị sẽ dừng lại.
- Ấn nút thứ nhất thì sẽ tăng thời gian tăng số này, nhưng không tăng quá 2(s).
- Ấn nút thứ hai thì sẽ giảm thời gian tăng số này, nhưng không giảm dưới 100 (ms).

## Đề 27

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển 8 LED đơn nối vào PORTD và nhận lệnh điều khiển từ 2 nút bấm nối vào PB6 và PB7.
Lập trình chương trình hoạt động như sau:
- Trạng thái ban đầu 8 LED nhấp nháy xen kẽ với chu kì 100 (ms).
- Ấn nút thứ nhất thì tăng tần số nhấp nháy.
- Ấn nút thứ hai thì giảm tần số nhấp nháy.
- Nếu ấn và giữ nút thì tần số sẽ tiếp tục thay đổi mà không phải chờ nhả nút ra.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 1 nút bấm nối vào PA0. Lập trình chương trình hoạt động như sau:
- Thiết lập 2 ngắt ngoài 0 và 1 hoạt động ở chế độ Falling Edge.
- Ban đầu số hiển thị là 5555.
- Ấn nút lần thứ nhất thì số hiển thị sẽ tự động tăng sau mỗi khoảng thời gian t, ấn nút lần thứ 2 thì số hiển thị sẽ dừng lại.
- Nếu ngắt ngoài 0 được kích hoạt thì sẽ tăng khoảng thời gian t, nhưng không tăng quá 3 (s).
- Nếu ngắt ngoài 1 được kích hoạt thì sẽ giảm khoảng thời gian t, nhưng không giảm dưới 500 (ms).

## Đề 28

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 9 nút bấm.
Lập trình chương trình hoạt động như sau:
	- Khi ấn 1 nút thì LED sẽ hiển thị số tương ứng từ 1- 9.
	- Khi không ấn nút nào thì LED hiển thị số 0.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để đo điện áp từ 0-5V và đo nhiệt độ bằng cảm biến nhiệt LM35, hiển thị giá trị lên 3 LED 7 thanh, sử dụng 2 nút bấm để điều khiển, sử dụng 4 LED đơn để hiển thị chế độ.
Lập trình chương trình hoạt động như sau:
- Đo điện áp bằng chân ADC0, đo nhiệt độ bằng chân ADC1.
- Ban đầu LED hiển thị giá trị điện áp với độ chính xác 0.1V.
- Khi ấn nút thứ nhất thì sẽ chuyển đổi giữa đo điện áp và đo nhiệt độ, sử dụng LED 1 và LED 2 để cho biết đang ở chế độ đo nào.
- Khi ấn nút thứ hai thì sẽ chuyển đổi độ chính xác khi đo điện áp giữa 0.1V và 0.01V, sử dụng LED 3 và LED 4 để cho biết đang ở độ chính xác nào.

## Đề 29

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển 8 LED đơn nối vào PORTD và nhận lệnh điều khiển từ 2 nút bấm nối vào PC0 và PC1.
Lập trình chương trình hoạt động như sau:
	- LED sẽ chạy từ trái sang phải, sau khi hết hàng LED sẽ vòng lại LED đầu tiên.
	- Ấn nút thứ nhất thì sẽ tăng tốc độ chạy LED, nhưng không nhanh quá 100Hz.
	- Ấn nút thứ hai thì sẽ giảm tốc độ chạy LED, nhưng không chậm dưới 4Hz.
	- Ấn và giữ nút thì tốc độ thay đổi liên tục.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để đo điện áp từ 0 - 5V nhận lệnh điều khiển từ 1 nút bấm nối vào PD0, hiển thị giá trị lên LED 7 thanh 4 số, sử dụng thêm một con LED 7 thanh hiển thị số.
Lập trình chương trình hoạt động như sau:
- Ban đầu đo điện áp, hiển thị điện áp với độ chính xác 0.1V.
- Ấn nút lần thứ nhất thì chuyển đổi sang độ chính xác 0.01V, ấn lần tiếp theo thì chuyển sang độ chính xác 0.1V,...
- Giá trị trên con LED 7 thanh đơn hiển thị 1 nếu đang đo độ chính xác là 0.1V, hiển thị 2 nếu đang đo độ chính xác là 0.01V.

## Đề 30

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 10 nút bấm.
Lập trình chương trình hoạt động như sau:
	- Khi ấn một nút bất kỳ thì LED 7 thanh sẽ hiển thị số tương ứng với nút đó.
	- Nhả nút ra thì số hiển thị giữ nguyên.
	- Khi ấn đồng thời nhiều nút thì LED 7 thanh sẽ hiển thị số lớn hơn.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để đo 3 tín hiệu điện áp từ 0-5V đưa vào 3 chân ADC0, ADC1, ADC2 nhận lệnh điều khiển từ 1 nút bấm nối vào PD0, hiển thị giá trị lên LED 7 thanh 4 số, sử dụng thêm một con LED 7 thanh hiển thị số.
Lập trình chương trình hoạt động như sau:
- Ban đầu đo điện áp tại đầu vào chân ADC0, hiển thị với độ chính xác 0.1V.
- Ấn nút thì chuyển sang đo điện áp tại chân ADC tiếp theo (0 –> 1 –> 2 –> 0).
- Giá trị trên con LED 7 thanh đơn hiển thị 0 nếu đang đo điện áp tại chân ADC0, hiển thị 1 nếu đang đo điện áp tại chân ADC1,hiển thị 2 nếu đang đo điện áp tại chân ADC2.
- Yêu cầu chờ nhả nút ra mới chuyển đổi lần tiếp theo.

## Đề 31

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 2 nút bấm.
Lập trình chương trình hoạt động như sau:
	- Trạng thái ban đầu LED hiển thị số 5
	- Ấn nút thứ nhất thì số hiển thị tăng 1 đơn vị, nếu tăng quá 9 thì vòng lại 0.
	- Ấn nút thứ hai thì số hiển thị giảm 1 đơn vị, nếu giảm dưới 0 thì vòng lên 9.
	- Yêu cầu chờ nhả nút ra để thực hiện lệnh tăng/giảm lượt tiếp theo.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 2 nút bấm nối vào PA0 và PA1. Lập trình chương trình hoạt động như sau:
- Thiết lập ngắt ngoài 0 hoạt động ở chế độ Falling Edge.
- Ban đầu số hiển thị là 10.
- Ấn nút thứ nhất thì số hiển thị tăng 1 đơn vị, nhưng không tăng quá 9999.
- Ấn nút thứ 2 thì số hiển thị giảm 1 đơn vị, nhưng không giảm dưới 1.
- Ấn và giữ nút thì số thay đổi liên tục.
- Nếu ngắt ngoài 0 được kích hoạt thì số hiển thị tự động giảm dần sau mỗi 1 (s).
- Nếu số hiển thị giảm đến 0 thì reset về 10 và dừng lại.

## Đề 32

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển 8 LED nối vào PORTD và nhận lệnh điều khiển từ 2 nút bấm nối vào PC0 và PC1.
Lập trình chương trình hoạt động như sau:
- LED sẽ chạy từ phải sang trái, sau khi hết hàng LED sẽ vòng lại LED đầu tiên
- Ấn nút thứ nhất thì sẽ tăng tốc độ chạy LED, nhưng không nhanh quá 25Hz.
- Ấn nút thứ hai thì sẽ giảm tốc độ chạy LED, nhưng không chậm dưới 5Hz.
- Ấn và giữ nút thì tốc độ thay đổi liên tục.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để đo 3 tín hiệu điện áp từ 0 - 5V đưa vào 3 chân ADC0, ADC1, ADC2, hiển thị giá trị lên LED 7 thanh 4 số, sử dụng thêm một con LED 7 thanh hiển thị số.
Lập trình chương trình hoạt động như sau:
- Thiết lập ngắt ngoài 1 hoạt động ở chế độ Rising Edge.
- Ban đầu đo điện áp tại đầu vào chân ADC0, hiển thị với độ chính xác 0.1V.
- Ngắt ngoài được kích hoạt thì chuyển sang đo điện áp tại chân ADC tiếp theo (0 –> 1 –> 2 –> 0).
- Giá trị trên con LED 7 thanh đơn hiển thị 0 nếu đang đo điện áp tại chân ADC0, hiển thị 1 nếu đang đo điện áp tại chân ADC1,hiển thị 2 nếu đang đo điện áp tại chân ADC2.

## Đề 33

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 2 nút bấm.
Lập trình chương trình hoạt động như sau:
- Trạng thái ban đầu LED hiển thị số 6
- Ấn nút thứ nhất thì số hiển thị tăng 1 đơn vị, tăng tối đa đến 9 thì dừng lại.
- Ấn nút thứ hai thì số hiển thị giảm 1 đơn vị, giảm tối thiểu đến 0 thì dừng lại.
- Yêu cầu chờ nhả nút ra để thực hiện lệnh tăng/giảm lượt tiếp theo.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 3 nút bấm nối vào PB0, PB1, PB2.
Thiết lập Timer 0 hoạt động ở chế độ Normal với tần số 31250Hz, kích hoạt ngắt tràn.
Thiết lập Timer 2 hoạt động ở chế độ Normal, kích hoạt ngắt tràn.
Lập trình chương trình hoạt động như sau:
- Tính toán để tạo khoảng thời gian chính xác 0.5(s) bằng timer 0, ghi chú vào chương trình phục vụ ngắt.
- Sử dụng ngắt tràn Timer 2 để quét LED 7 thanh.
- Ban đầu số hiển thị là 1234.
- Ấn nút thứ 1 thì số hiển thị tăng lên 1 đơn vị, nhưng không tăng quá 9999.
- Ấn nút thứ 2 thì số hiển thị giảm 1 đơn vị, nhưng không giảm dưới 0.
- Ấn nút thứ 3 thì số hiển thị sẽ tự động giảm sau mỗi 0.5(s), giảm đến 0 thì dừng.

## Đề 34

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 2 nút bấm nối vào PA0 và PA1.
Lập trình chương trình hoạt động như sau:
	- Trạng thái ban đầu LED hiển thị số 0.
	- Ấn nút thứ nhất thì số hiển thị sẽ tự động tăng với chu kì 100 (ms).
	- Ấn nút thứ hai thì số hiển thị sẽ dừng lại.
	- Nếu số tăng quá 9 thì sẽ vòng lại 0.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 2 nút bấm.
Thiết lập Timer 0 hoạt động ở chế độ Normal với tần số 125kHz, kích hoạt ngắt tràn.
Thiết lập ngắt ngoài 0 và 1 hoạt động ở chế độ Falling Edge.
Tính toán để tạo khoảng thời gian chính xác 0.5(s) bằng timer, ghi chú vào chương trình phục vụ ngắt.
- Ban đầu số hiển thị là 8000
- Ngắt ngoài 0 được kích hoạt thì số hiển thị sẽ tăng 1 đơn vị, nhưng không tăng quá 8888.
- Ngắt ngoài 1 được kích hoạt thì số hiển thị sẽ giảm 1 đơn vị, nhưng không giảm dưới 8000.
- Ấn nút thứ 1 thì số hiển thị sẽ tự động tăng sau mỗi 0.5(s), nếu tăng quá 9000 thì vòng lại 1000. Ấn nút thứ 2 thì số hiển thị sẽ dừng lại.

## Đề 35

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 2 nút bấm nối vào PA0 và PA1.
Lập trình chương trình hoạt động như sau:
- Số hiển thị sẽ tự động tăng từ 0 đến 9 sau một khoảng thời gian t.
- Nếu số tăng quá 9 thì sẽ vòng lại 0.
- Ấn nút thứ nhất thì sẽ làm tăng thời gian tăng số, nhưng không tăng quá 2 (s).
- Ấn nút thứ hai thì sẽ làm giảm thời gian tăng số, nhưng không giảm dưới 200 (ms).

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 3 nút bấm nối vào PB0, PB1, PB2.
Thiết lập Timer 0 hoạt động ở chế độ Normal với tần số 125kHz, kích hoạt ngắt tràn.
Thiết lập Timer 2 hoạt động ở chế độ Normal, kích hoạt ngắt tràn.
Lập trình chương trình hoạt động như sau:
- Tính toán để tạo khoảng thời gian chính xác 0.5(s) bằng timer 0, ghi chú vào chương trình phục vụ ngắt.
- Sử dụng ngắt tràn Timer 2 để quét LED 7 thanh.
- Ban đầu số hiển thị là 1234.
- Ấn nút thứ 1 thì số hiển thị tăng lên 1 đơn vị, nhưng không tăng quá 9999.
- Ấn nút thứ 2 thì số hiển thị giảm 1 đơn vị, nhưng không giảm dưới 0.
- Ấn nút thứ 3 thì số hiển thị sẽ tự động tăng sau mỗi 0.5(s), tăng đến 9999 dừng

## Đề 36

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 2 nút bấm nối vào PA0 và PA1.
Lập trình chương trình hoạt động như sau:
- Trạng thái ban đầu LED hiển thị số 9.
- Ấn nút thứ nhất thì số hiển thị sẽ tự động giảm với chu kì 300 (ms).
- Ấn nút thứ hai thì số hiển thị sẽ dừng lại.
- Nếu số giảm dưới 0 thì sẽ vòng lại 9.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 3 nút bấm nối vào PB0, PB1, PB2.
Thiết lập Timer 0 hoạt động ở chế độ Normal với tần số 31250Hz, kích hoạt ngắt tràn
Thiết lập ngắt ngoài 0 hoạt động ở chế độ Falling Edge.
Lập trình chương trình hoạt động như sau:
- Tính toán để tạo khoảng thời gian chính xác 0.5(s) bằng timer, ghi chú vào chương trình phục vụ ngắt.
- Ban đầu số hiển thị là 1111.
- Ấn nút thứ nhất thì số hiển thị sẽ tăng 1 đơn vị, nhưng không tăng quá 9000.
- Ấn nút thứ hai thì số hiển thị sẽ giảm 1 đơn vị, nhưng không giảm dưới 1000.
- Nếu ấn và giữ nút thì số hiển thị tăng liên tục.
- Ấn nút thứ 3 thì số hiển thị sẽ tự động tăng sau mỗi 0.5(s), nếu tăng quá 9000 thì vòng lại 1000.
- Ngắt ngoài 0 được kích hoạt thì số hiển thị dừng lại.

## Đề 37

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển 8 LED đơn nối vào PORTD và nhận lệnh điều khiển từ 8 nút bấm nối vào PORTA.
Lập trình chương trình hoạt động như sau:
- Khi ấn một nút bất kỳ thì LED tương ứng sẽ đảo trạng thái (LED đang sáng sẽ tắt và ngược lại).
- Nếu ấn và giữ nút thì LED đảo trạng thái liên tục với chu kì 300 (ms).

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 2 nút bấm nối vào PD6 và PD7. Thiết lập ngắt ngoài 0 hoạt động ở chế độ Falling Edge
Lập trình chương trình hoạt động như sau:
- Ban đầu số hiển thị là 1000.
- Ấn nút thứ nhất thì số hiển thị tăng lên 1 đơn vị, nhưng không tăng quá 9999.
- Ấn nút thứ hai thì số hiển thị giảm 1 đơn vị, nhưng không giảm dưới 0.
- Yêu cầu chờ nhả nút ra để thực hiện lệnh tăng/giảm lượt tiếp theo.
- Ngắt ngoài 0 được kích hoạt thì reset số hiển thị về 1000.

## Đề 38

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 2 nút bấm.
Lập trình chương trình hoạt động như sau:
	- Trạng thái ban đầu LED hiển thị số 5.
	- Ấn nút thứ nhất thì số hiển thị tăng 1 đơn vị, nếu tăng quá 9 thì vòng lại 0.
	- Ấn nút thứ hai thì số hiển thị giảm 1 đơn vị, nếu giảm dưới 0 thì vòng lên 9.
	- Nếu ấn và giữ nút thì số thay đổi liên tục sau mỗi 300 (ms).

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 2 nút bấm nối vào PB0, PB1. Thiết lập ngắt ngoài 1 hoạt động ở chế độ Rising Edge.
Lập trình chương trình hoạt động như sau:
- Ban đầu số hiển thị là 6000.
- Ấn nút thứ nhất thì số hiển thị sẽ tự động giảm với chu kì 1(s), sau khi giảm đến 0 sẽ dừng lại.
- Ấn nút thứ hai thì số hiển thị sẽ dừng lại.
- Ngắt ngoài 1 được kích hoạt thì reset số hiển thị về 6000.

## Đề 39

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển 8 LED đơn nối vào PORTD và nhận lệnh điều khiển từ 8 nút bấm nối vào PORTA.
Lập trình chương trình hoạt động như sau:
- Khi ấn một nút bất kỳ thì LED tương ứng sẽ đảo trạng thái (LED đang sáng sẽ tắt và ngược lại).
- Chờ nhả nút ra mới thực hiện đảo trạng thái lần tiếp theo.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để đo 3 tín hiệu điện áp từ 0-5V đưa vào 3 chân ADC0, ADC1, ADC2 nhận lệnh điều khiển từ 1 nút bấm nối vào PD0, hiển thị giá trị lên LED 7 thanh 4 số, sử dụng thêm một con LED 7 thanh hiển thị số.
Lập trình chương trình hoạt động như sau:
- Ban đầu đo điện áp tại đầu vào chân ADC0, hiển thị với độ chính xác 0.1V.
- Ấn nút thì chuyển sang đo điện áp tại chân ADC tiếp theo (0 –> 1 –> 2 –> 0).
- Giá trị trên con LED 7 thanh đơn hiển thị 0 nếu đang đo điện áp tại chân ADC0, hiển thị 1 nếu đang đo điện áp tại chân ADC1,hiển thị 2 nếu đang đo điện áp tại chân ADC2.
- Yêu cầu chờ nhả nút ra mới chuyển đổi lần tiếp theo.

## Đề 40

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển 8 LED đơn nối vào PORTD và nhận lệnh điều khiển từ 2 nút bấm nối vào PA1 và PA2.
Lập trình chương trình hoạt động như sau:
- Trạng thái ban đầu chỉ có LED thứ 2 sáng.
- Ấn nút thứ nhất thì LED sáng sẽ di chuyển sang phải.
- Ấn nút thứ hai thì LED sáng sẽ di chuyển sang trái.
- Nếu LED di chuyển đến cuối cùng thì sẽ vòng lại.
- Nếu ấn và giữ nút thì LED sẽ di chuyển với chu kì là 200 (ms).

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 2 nút bấm nối vào PA0 và PA1. Lập trình chương trình hoạt động như sau:
- Thiết lập ngắt ngoài 0 hoạt động ở chế độ Falling Edge.
- Ban đầu số hiển thị là 10.
- Ấn nút thứ nhất thì số hiển thị tăng 1 đơn vị, nhưng không tăng quá 9999.
- Ấn nút thứ 2 thì số hiển thị giảm 1 đơn vị, nhưng không giảm dưới 1.
- Ấn và giữ nút thì số thay đổi liên tục.
- Nếu ngắt ngoài 0 được kích hoạt thì số hiển thị tự động giảm dần sau mỗi 1 (s).
- Nếu số hiển thị giảm đến 0 thì reset về 10 và dừng lại.

## Đề 41

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển 8 LED đơn nối vào PORTD và nhận lệnh điều khiển từ 2 nút bấm nối vào PB6 và PB7.
Lập trình chương trình hoạt động như sau:
- Trạng thái ban đầu 8 LED nhấp nháy xen kẽ với chu kì 100 (ms).
- Ấn nút thứ nhất thì tăng tần số nhấp nháy.
- Ấn nút thứ hai thì giảm tần số nhấp nháy.
- Nếu ấn và giữ nút thì tần số sẽ tiếp tục thay đổi mà không phải chờ nhả nút ra.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để đo 3 tín hiệu điện áp từ 0 -5V đưa vào 3 chân ADC0, ADC1, ADC2, hiển thị giá trị lên LED 7 thanh 4 số, sử dụng thêm một con LED 7 thanh hiển thị số.
Lập trình chương trình hoạt động như sau:
- Thiết lập ngắt ngoài 1 hoạt động ở chế độ Rising Edge.
- Ban đầu đo điện áp tại đầu vào chân ADC0, hiển thị với độ chính xác 0.1V.
- Ngắt ngoài được kích hoạt thì chuyển sang đo điện áp tại chân ADC tiếp theo (0 –> 1 –> 2 –> 0).
- Giá trị trên con LED 7 thanh đơn hiển thị 0 nếu đang đo điện áp tại chân ADC0, hiển thị 1 nếu đang đo điện áp tại chân ADC1,hiển thị 2 nếu đang đo điện áp tại chân ADC2.

## Đề 42

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị một LED 7 thanh và nhận lệnh điều khiển từ 9 nút bấm.
Lập trình chương trình hoạt động như sau:
	- Khi ấn 1 nút thì LED sẽ hiển thị số tương ứng từ 1- 9.
	- Khi không ấn nút nào thì LED hiển thị số 0.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 3 nút bấm nối vào PB0, PB1, PB2.
Thiết lập Timer 0 hoạt động ở chế độ Normal với tần số 31250Hz, kích hoạt ngắt tràn.
Thiết lập Timer 2 hoạt động ở chế độ Normal, kích hoạt ngắt tràn.
Lập trình chương trình hoạt động như sau:
- Tính toán để tạo khoảng thời gian chính xác 0.5(s) bằng timer 0, ghi chú vào chương trình phục vụ ngắt.
- Sử dụng ngắt tràn Timer 2 để quét LED 7 thanh.
- Ban đầu số hiển thị là 1234.
- Ấn nút thứ 1 thì số hiển thị tăng lên 1 đơn vị, nhưng không tăng quá 9999.
- Ấn nút thứ 2 thì số hiển thị giảm 1 đơn vị, nhưng không giảm dưới 0.
- Ấn nút thứ 3 thì số hiển thị sẽ tự động giảm sau mỗi 0.5(s), giảm đến 0 thì dừng.

## Đề 43

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển 8 LED đơn nối vào PORTD và nhận lệnh điều khiển từ 8 nút bấm nối vào PORTA.
Lập trình chương trình hoạt động như sau:
- Khi ấn một nút bất kỳ thì LED tương ứng sẽ đảo trạng thái (LED đang sáng sẽ tắt và ngược lại)
- Chờ nhả nút ra mới thực hiện đảo trạng thái lần tiếp theo.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để đo 3 tín hiệu điện áp từ 0-5V đưa vào 3 chân ADC0, ADC1, ADC2 nhận lệnh điều khiển từ 1 nút bấm nối vào PD0, hiển thị giá trị lên LED 7 thanh 4 số, sử dụng thêm một con LED 7 thanh hiển thị số.
Lập trình chương trình hoạt động như sau:
- Ban đầu đo điện áp tại đầu vào chân ADC0, hiển thị với độ chính xác 0.1V
- Ấn nút thì chuyển sang đo điện áp tại chân ADC tiếp theo (0 –> 1 –> 2 –> 0)
- Giá trị trên con LED 7 thanh đơn hiển thị 0 nếu đang đo điện áp tại chân ADC0, hiển thị 1 nếu đang đo điện áp tại chân ADC1, hiển thị 2 nếu đang đo điện áp tại chân ADC2.
- Yêu cầu chờ nhả nút ra mới chuyển đổi lần tiếp theo.

## Đề 44

### Câu 1 (4 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển 8 LED đơn nối vào PORTD và nhận lệnh điều khiển từ 2 nút bấm nối vào PA1 và PA2.
Lập trình chương trình hoạt động như sau:
- Trạng thái ban đầu chỉ có LED thứ 2 sáng
- Ấn nút thứ nhất thì LED sáng sẽ di chuyển sang phải
- Ấn nút thứ hai thì LED sáng sẽ di chuyển sang trái
- Nếu LED di chuyển đến cuối cùng thì sẽ vòng lại
- Nếu ấn và giữ nút thì LED sẽ di chuyển với chu kì là 200ms.

### Câu 2 (6 điểm)

Thiết kế mạch sử dụng vi điều khiển Atmega16 để điều khiển hiển thị 4 LED 7 thanh bằng phương pháp quét và nhận lệnh điều khiển từ 2 nút bấm nối vào PA0 và PA1. Lập trình chương trình hoạt động như sau:
- Thiết lập ngắt ngoài 0 hoạt động ở chế độ Falling Edge
- Ban đầu số hiển thị là 10
- Ấn nút thứ nhất thì số hiển thị tăng 1 đơn vị, nhưng không tăng quá 9999
- Ấn nút thứ 2 thì số hiển thị giảm 1 đơn vị, nhưng không giảm dưới 1
- Ấn và giữ nút thì số thay đổi liên tục
- Nếu ngắt ngoài 0 được kích hoạt thì số hiển thị tự động giảm dần sau mỗi 1(s)
- Nếu số hiển thị giảm đến 0 thì reset về 10 và dừng lại
