1 项目概述
本工具用于​​量化评估密码学基础操作的计算效率​​，主要对比两类运算：

​​双线性配对操作​​（基于charm.toolbox.pairinggroup库）：包括椭圆曲线点乘、配对计算、群哈希等
​​自定义模运算​​（基于环Zn）：模加/模乘/模幂/模逆运算通过多轮批量测试，输出各操作的耗时统计，为密码协议设计提供性能参考。
2 环境要求

2.1 依赖库

pip install charm-crypto==0.43  # 核心密码学库[1,9](@ref)
pip install numpy               # 数据分析支持（可选）

3 使用说明

3.1 运行测试
# 激活环境后直接执行
python main.py

3.2 关键参数配置

| 参数  | 默认值 |  作用 |
| ------------- | ------------- |  ------------- |
| n  | 100  | 外部测试轮数 |
| bulk  |100  | 每轮模运算执行次数 |
| mod_n  |104729  | 模运算素数模数（可替换更大素数）  |
