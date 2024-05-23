# # data preprocessing
# from sklearn.preprocessing import StandardScaler
# from ydata_profiling import ProfileReport
# # loading dataset
# import pandas as pd
# import argparse
# import pickle
# import os


# # 创建解析器并添加参数
# parser = argparse.ArgumentParser()
# parser.add_argument('--data_path', required=True, help='Path to the data file')
# parser.add_argument('--model_path', required=True, help='Path to the model file')
# args = parser.parse_args()

# # 加载需要预测的数据
# data = pd.read_csv(args.data_path)
# print(data.head())

# # 创建数据分析报告
# report = ProfileReport(data)

# # 保存报告为 HTML 文件
# report_dir = "report"
# if not os.path.exists(report_dir):
#     os.makedirs(report_dir)

# report.to_file(os.path.join(report_dir, "data_analysis_report.html"))
# print("Data analysis report saved as data_analysis_report.html")


# # y = data["target"]
# # X = data.drop('target',axis=1)
# # 划分X，Y,预测不需要划分
# # 划分X和Y
# # X = df.iloc[:, :-1]  # 所有行，除了最后一列之外的所有列作为X
# # Y = df.iloc[:, -1]   # 所有行，最后一列作为Y

# scaler = StandardScaler()
# data_test = scaler.fit_transform(data)

# # 使用 pickle 加载模型
# # 假设模型已存在于mid_model中

# # 使用 pickle 加载模型
# with open(args.model_path, 'rb') as f:
#     model = pickle.load(f)

# # 预测
# predictions = model.predict(data_test)

# X = data
# Y = predictions
# # Y[1] = 'target'

# # 将 X 和 Y 合并为一个 DataFrame
# # X_df = pd.DataFrame(data_test, columns=X.columns)  # 假设 X 是一个 DataFrame，列名为 X.columns
# # Y_df = pd.DataFrame(predictions, columns=['Y'])  # 假设 Y 是一个数组，列名为 'Y'
# # merged_df = pd.concat([X_df, Y_df], axis=1)
# X_test_df = pd.DataFrame(X,columns=X.columns)
# Y_test_df = pd.DataFrame(Y,columns=['target'])
# merged_df = pd.concat([X_test_df, Y_test_df], axis=1)

# # 生成 CSV 文件
# result_dir = "predict_result"
# if not os.path.exists(result_dir):
#     os.makedirs(result_dir)

# merged_df.to_csv(os.path.join(result_dir, 'result.csv'), index=False)
# data preprocessing
from sklearn.preprocessing import StandardScaler
from ydata_profiling import ProfileReport
# loading dataset
import pandas as pd
import argparse
import pickle
import os


# 创建解析器并添加参数
parser = argparse.ArgumentParser()
parser.add_argument('--data_path', required=True, help='Path to the data file')
parser.add_argument('--model_path', required=True, help='Path to the model file')
args = parser.parse_args()

# 加载需要预测的数据
data = pd.read_csv(args.data_path)
print(data.head())

scaler = StandardScaler()
data_test = scaler.fit_transform(data)

# 使用 pickle 加载模型
with open(args.model_path, 'rb') as f:
    model = pickle.load(f)

# 预测
predictions = model.predict(data_test)

X = data
Y = predictions

# 将 X 和 Y 合并为一个 DataFrame
X_test_df = pd.DataFrame(X,columns=X.columns)
Y_test_df = pd.DataFrame(Y,columns=['target'])
merged_df = pd.concat([X_test_df, Y_test_df], axis=1)

# 生成 CSV 文件
result_dir = "predict_result"
if not os.path.exists(result_dir):
    os.makedirs(result_dir)

merged_df.to_csv(os.path.join(result_dir, 'result.csv'), index=False)

# 加载预测结果数据
result_data = pd.read_csv(os.path.join(result_dir, 'result.csv'))

# 创建数据分析报告
report = ProfileReport(result_data)

# 保存报告为 HTML 文件
report_dir = "report"
if not os.path.exists(report_dir):
    os.makedirs(report_dir)

report.to_file(os.path.join(report_dir, "data_analysis_report.html"))
print("Data analysis report saved as data_analysis_report.html")