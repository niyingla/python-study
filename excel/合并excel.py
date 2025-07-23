import pandas as pd


def split_excel_data(first_excel_path, second_excel_path, output_excel_older, output_excel_younger):
    """
    读取两个Excel文件，根据客户名称匹配数据，并根据年龄筛选条件将数据写入两个新文件

    Args:
        first_excel_path: 第一个Excel文件路径
        second_excel_path: 第二个Excel文件路径
        output_excel_older: 输出Excel文件路径（年龄大于30）
        output_excel_younger: 输出Excel文件路径（年龄小于等于30）
    """

    # 读取第一个Excel文件
    df1 = pd.read_excel(first_excel_path)

    # 读取第二个Excel文件，指定第二行为列名
    df2 = pd.read_excel(second_excel_path, header=1)

    # 找到第一个Excel中"客户名字"列和"工资"列
    name_col_1 = "客户名字"
    salary_col = "工资"

    # 找到第二个Excel中"客户昵称"列和"年龄"列
    nickname_col = "客户昵称"
    age_col = "年龄"

    # 检查必要的列是否存在
    if name_col_1 not in df1.columns:
        raise ValueError(f"第一个Excel中未找到'{name_col_1}'列")

    if salary_col not in df1.columns:
        raise ValueError(f"第一个Excel中未找到'{salary_col}'列")

    if nickname_col not in df2.columns:
        raise ValueError(f"第二个Excel中未找到'{nickname_col}'列")

    if age_col not in df2.columns:
        raise ValueError(f"第二个Excel中未找到'{age_col}'列")

    # 提取需要的列数据
    data1 = df1[[name_col_1, salary_col]].copy()
    data2 = df2[[nickname_col, age_col]].copy()

    # 重命名列以便合并
    data1.rename(columns={name_col_1: '客户名称'}, inplace=True)
    data2.rename(columns={nickname_col: '客户名称', age_col: '年龄'}, inplace=True)

    # 数据合并：基于客户名称进行匹配
    merged_data = pd.merge(data1, data2, on='客户名称', how='inner')

    # 根据年龄条件拆分数据
    older_data = merged_data[merged_data['年龄'] > 30]
    younger_data = merged_data[merged_data['年龄'] <= 30]

    # 重新排列列顺序
    result_columns = ['客户名称', salary_col, '年龄']
    older_result = older_data[result_columns]
    younger_result = younger_data[result_columns]

    # 写入新的Excel文件
    older_result.to_excel(output_excel_older, index=False)
    younger_result.to_excel(output_excel_younger, index=False)

    print(f"30岁以上数据已成功写入: {output_excel_older}")
    print(f"30岁以下数据已成功写入: {output_excel_younger}")


# 使用示例
if __name__ == "__main__":
    # 替换为实际的文件路径
    first_excel = "第一个.xlsx"
    second_excel = "第二个.xlsx"
    output_older = "30岁以上结果.xlsx"
    output_younger = "30岁以下结果.xlsx"

    try:
        split_excel_data(first_excel, second_excel, output_older, output_younger)
    except Exception as e:
        print(f"处理过程中出现错误: {e}")
