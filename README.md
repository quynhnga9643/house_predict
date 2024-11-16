# Dự án Dự đoán Giá Nhà bằng Hồi Quy Tuyến Tính

## Giới thiệu
Dự án này sử dụng mô hình hồi quy tuyến tính đơn biến để dự đoán giá nhà dựa trên diện tích nhà ở (sqft_living). Mục tiêu chính của dự án là tìm hiểu mối quan hệ giữa diện tích nhà và giá nhà, đồng thời đánh giá hiệu quả của mô hình qua các chỉ số đánh giá (MAE, MSE, RMSE, R²).

---

## Cấu trúc dự án
- **`code/`**: Chứa mã nguồn Python và các biểu đồ minh họa.
  - `main.py`: File chính để chạy dự án.
  - `plots/`: Thư mục chứa các biểu đồ `*.png` hoặc `*.pdf`.
  - `model_trained.sav`: File mô hình đã được huấn luyện và lưu lại bằng `pickle`.
- **`templates/`**: Chứa giao diện HTML nếu sử dụng web app (Flask).
- **`README.md`**: Tài liệu hướng dẫn sử dụng dự án.

---

## Hướng dẫn cài đặt

### **Yêu cầu hệ thống**
- Python 3.8 hoặc cao hơn.
- Các thư viện Python:
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `matplotlib`
  - `seaborn`
  - `pickle`

### **Cài đặt thư viện**
Sử dụng lệnh sau để cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt


## Cách chạy dự án

1. **Tải dữ liệu**:
   - Đảm bảo file dữ liệu `house_data.csv` nằm trong cùng thư mục với file `main.py`.

2. **Chạy chương trình**:
   - Mở terminal/command prompt, điều hướng đến thư mục chứa file `main.py`, và chạy lệnh:

   ```bash
   python main.py