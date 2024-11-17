# import 1 số thư viện cần thiết để để xử lý, phân tích trực quan dữ liệu cũng như là để train/test model
import time
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# load data có đuôi là csv
df = pd.read_csv('house_data.csv')

# Thống kê dữ liệu bằng describe()
print(df.describe())
# Hàm describe() giúp trả về dataframe với số hàng được hiển thị ra các
# thông số như số hàng, giá trị trung bình , min, max, ti lệ phần trăm của các cột.

# Tổng quát dữ liệu
print(df.info())
# Thông qua hàm info()
# ta có thể thấy rằng dataset này có khoảng hơn 6k dòng dữ liệu và ta có thể biết được các kiểu dữ liệu của các cột,...

# Tương quan về toàn bộ dữ liệu
pair_plot=sns.pairplot(df)
pair_plot.fig.set_size_inches(15,10)

# Một vài biểu đồ thể hiện sự tương quan với giá nhà:
# Biểu đồ thể hiện sự tương quan giữa giá nhà và diện tích nhà
plt.scatter(df.sqft_living, df.price, color='navy')
plt.xlabel("Diện tích nhà")
plt.ylabel("Giá nhà")
plt.show()

# Biểu đồ tương quan giữa số phòng ngủ và giá nhà
plt.scatter(df.bedrooms, df.price, color='navy')
plt.xlabel("Số phòng ngủ")
plt.ylabel("Giá nhà")
plt.show()

# Sử dụng biểu đồ heat map để xem tương quan giữa các cột
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='Blues')
plt.show()

# Thông qua biểu đồ ta dễ dàng nhận thấy diện tích nhà(sqft_living) ảnh hưởng lớn nhất đến giá nhà,
# nên ta sẽ sử dụng cột sqft_living để làm tham số chính cho mô hình dự đoán linear regression

# Tách dữ liệu thành 2 biến x(chứa các biến input để train) và y(output (biến mục tiêu) là kết quả dự đoán)
x = df[['sqft_living']]
y = df['price']

# Tách dữ liệu thành train/test
# Ta sẽ chia dữ liệu thành 70% train (x_train, y_train) và 30% test (x_test, y_test)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=68)

# Tạo model để training và test Linear Regression
model = LinearRegression()

# Train dữ liệu bằng phương thức fit() và tạo 1 biến start_time để đo lường thời gian khi train xong
start_time = time.time()
model.fit(x_train, y_train)
print(f"\n-----Training time: {time.time()-start_time}s")

# Lưu lại file model sau khi train xong để sau này có thể tái sử dụng để dự đoán/test
file = 'model_trained.sav'
pickle.dump(model, open(file, 'wb'))

# Dự đoán dữ liệu từ x_test, ta sẽ dùng phương thức predict() để dự đoán
prediction = model.predict(x_test)

# load model và thử dự đoán kết quả (price) khi sqft_living = 1710
loaded_model = pickle.load(open(file, 'rb'))
pred_test = loaded_model.predict(pd.DataFrame([
    {"sqft_living": 1710}
]))

print(f'Kết quả dự đoán: {pred_test[0]}USD')

# Dự đoán và đánh giá mô hình
plt.scatter(x_train, y_train, color='navy')
plt.plot(x_train, model.predict(x_train), color="orange")
plt.title ("Biểu đồ cho tập dữ liệu train")
plt.xlabel("Diện tích nhà")
plt.ylabel("Giá nhà")
plt.show()

plt.scatter(x_test, y_test, color='navy')
plt.plot(x_test, model.predict(x_test), color="orange")
plt.title ("Biểu đồ cho tập dữ liệu test")
plt.xlabel("Diện tích nhà")
plt.ylabel("Giá nhà")
plt.show()

print("score_train:", model.score(x_train, y_train))
print("coef:", model.coef_)

# Một vài chỉ số hồi quy để đánh giá
print('MAE:', mean_absolute_error(y_test, prediction))
print('MSE:', mean_squared_error(y_test, prediction))
print('RMSE', np.sqrt(mean_squared_error(y_test, prediction)))
print('r_squared: ', r2_score(y_test, prediction))

# Kết luận:
# - Với chỉ số RMSE cho thấy giá trị chênh lệch trung bình của giá dự đoán từ mô hình và giá trị thực tế xấp xỉ 262.060 USD
# trong khoảng giá mà dữ liệu cung cấp từ 0 USD -> 5.000.000 USD.
# - Từ các chỉ số: score_train, r_squared. Ta thấy mô hình dự đoán chính xác khoảng cỡ ~50%
# => Đây là 1 chỉ số dự đoán không cao vì:
#   + Giới hạn bài báo cáo chỉ dừng ở mức nghiên cứu & thực hành Linear Regression nên chỉ dùng 1 biến là sqft_living để dự đoán => chính xác không cao

# Giải pháp: Ở tương lai ta có thể dùng thêm phương pháp Multiple Regression (Hồi quy đa biến) để có thể kết hợp nhiều biến lại với nhau để dự đoán