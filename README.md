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

---bash
pip install -r requirements.txt


### Cách chạy dự án

1. **Tải dữ liệu**:
   - Đảm bảo file dữ liệu `house_data.csv` nằm trong cùng thư mục với file `main.py`.

2. **Chạy chương trình**:
   - Mở terminal/command prompt, điều hướng đến thư mục chứa file `main.py`, và chạy lệnh:

   ```bash
   python main.py


## Các chức năng chính

1. Phân tích dữ liệu
Hiển thị thống kê cơ bản về dữ liệu qua hàm describe() và info().
Trực quan hóa dữ liệu bằng các biểu đồ:
Scatter plot giữa diện tích nhà (sqft_living) và giá nhà (price).
Scatter plot giữa số phòng ngủ (bedrooms) và giá nhà (price).
Heatmap thể hiện mối tương quan giữa các biến.

2. Xây dựng và huấn luyện mô hình
Sử dụng hồi quy tuyến tính (LinearRegression) để dự đoán giá nhà dựa trên diện tích nhà.
Chia dữ liệu thành tập huấn luyện (70%) và tập kiểm tra (30%) bằng train_test_split.
Lưu mô hình đã huấn luyện vào file model_trained.sav để tái sử dụng.

3. Đánh giá mô hình
- Các chỉ số đánh giá được sử dụng:
MAE (Mean Absolute Error): Sai số trung bình tuyệt đối.
MSE (Mean Squared Error): Sai số bình phương trung bình.
RMSE (Root Mean Squared Error): Căn bậc hai của MSE.
R²: Hệ số xác định (R-Squared).

- Hiển thị biểu đồ dự đoán:
Biểu đồ trên tập dữ liệu huấn luyện.
Biểu đồ trên tập dữ liệu kiểm tra.

4. Dự đoán giá nhà
Sử dụng mô hình đã lưu để dự đoán giá nhà dựa trên diện tích nhập vào.

---

## Hướng dẫn sử dụng GUI
- Chạy giao diện (GUI)
Chạy file Python chứa giao diện:

-```bash
python gui.py

- Giao diện cho phép:
Nhập diện tích nhà (sqft_living).
Dự đoán giá nhà bằng cách bấm nút "Dự đoán".
Hiển thị kết quả giá nhà dự đoán trên màn hình.

---

## Kết luận

- Mô hình hồi quy tuyến tính đơn biến phù hợp cho các bài toán cơ bản nhưng không đạt độ chính xác cao cho dự đoán giá nhà.

- Đề xuất cải tiến:
Sử dụng hồi quy đa biến (Multiple Regression) để đưa thêm các yếu tố như số phòng ngủ, vị trí, số tầng.

- Tích hợp thêm thuật toán khác như Decision Tree, Random Forest để tăng độ chính xác












