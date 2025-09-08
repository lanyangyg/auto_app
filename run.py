import pytest
import os
import shutil

if __name__ == '__main__':
    # 定义 Allure 结果和报告的目录
    allure_result_dir = 'allure_result'
    allure_report_dir = 'allure_report'

    # 1. 执行 pytest 测试，并生成 Allure 结果
    # 我们不再需要在 pytest.ini 中指定 --clean-alluredir，在这里手动清理更灵活
    if os.path.exists(allure_result_dir):
        shutil.rmtree(allure_result_dir)

    pytest.main(['-sv', 'tests/', f'--alluredir={allure_result_dir}'])

    # 2. 使用 Allure 命令从结果生成 HTML 报告
    # 首先清理旧的报告
    if os.path.exists(allure_report_dir):
        shutil.rmtree(allure_report_dir)

    os.system(f'allure generate {allure_result_dir} -o {allure_report_dir} --clean')

    # 3. （可选）自动在浏览器中打开报告
    # 注意：os.system() 的行为可能因操作系统而异
    report_index_file = os.path.join(allure_report_dir, 'index.html')
    print(f"Allure 报告已生成。请在浏览器中打开: file://{os.path.abspath(report_index_file)}")

    # 如果你想自动打开，可以取消下面的注释
    # import webbrowser
    # webbrowser.open(f'file://{os.path.abspath(report_index_file)}')
