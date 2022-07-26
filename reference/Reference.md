一、为何要进行数据预处理？
1.任何收集而来的庞大数据往往是不可能一拿到就可以立马用得上的，比如一些数值大的数据，计算量复杂度高，不容易收敛，很难进行统计处理。

2.数据不符合正态分布，无法做一些符合正态分布的数学分析。

所以为了对数据进行更好的利用，我们需要使数据标准化。

二、数据标准化
数据无量纲化处理主要解决数据的可比性。数据标准化的方法有很多种，常用的有“最小—最大标准化”、“Z-score标准化”和“按小数定标标准化”等。经过上述标准化处理，原始数据均转换为无量纲化指标测评值，即各指标值都处于同一个数量级别上，可以进行综合测评分析。这里我们重点讨论最常用的数据归一化处理，即将数据统一映射到[0,1]区间上。

1.归一化的目标
1.把数据转换为（0,1）区间的小数，  主要是为了数据处理方便提出来的，把数据映射到0～1范围之内处理，更加便捷快速。

2.把有量纲表达式变为无量纲表达式，解决数据的可比性。



[油猴复制当前浏览器页面网址/标题markdown链接](https://cway.top/post/1004.html)

[模糊数学笔记：五、模糊聚类 - 知乎](https://zhuanlan.zhihu.com/p/188712311)

[LBP 简介](https://blog.csdn.net/Lu597203933/article/details/17184503?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165871221616781685385017%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&request_id=165871221616781685385017&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-17184503-null-null.185^v2^control&utm_term=LBP&spm=1018.2226.3001.4450)

[LBP 特征原理及代码实现](https://blog.csdn.net/guo1988kui/article/details/79976202)

[图像特征提取三大法宝：HOG特征，LBP特征，Haar特征](https://www.cnblogs.com/ranjiewen/p/5873514.html)

[LBP特征提取原理和python库代码](https://blog.csdn.net/qq_44386182/article/details/124031615?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~aggregatepage~first_rank_ecpm_v1~rank_v31_ecpm-2-124031615-null-null.pc_agg_new_rank&utm_term=LBP%E6%8F%90%E5%8F%96%E7%89%B9%E5%BE%81%E5%90%91%E9%87%8F%E7%9A%84%E6%AD%A5%E9%AA%A4&spm=1000.2123.3001.4430)

[基于MATLAB和模糊聚类分析的图像分类](https://blog.csdn.net/weixin_43851420/article/details/106533185)

[模糊动态聚类之python实现](https://blog.csdn.net/m0_37804518/article/details/78806138)

[LBP特征](https://blog.csdn.net/lk3030/article/details/84034963)

[LBPH——图像的LBP特征向量](https://blog.csdn.net/zqx951102/article/details/100742463/)

[ python中reshape的用法_粟寒的博客-CSDN博客_python reshape](https://blog.csdn.net/sweat_mango/article/details/88664365)

[关于LBP算法的skimage.feature.local_binary_pattern（）函数解析_WHUAndGXUJavaBoy的博客-CSDN博客_local_binary_pattern函数](https://blog.csdn.net/m0_38027013/article/details/90487243)

[基于MATLAB和模糊聚类分析的图像分类_谁谓河广 一苇杭之的博客-CSDN博客](https://blog.csdn.net/weixin_43851420/article/details/106533185)

[LBP特征提取原理和python库代码_靠你几哇的博客-CSDN博客_lbp特征python](https://blog.csdn.net/qq_44386182/article/details/124031615)

[模糊聚类分析方法_wamg潇潇的博客-CSDN博客_模糊聚类](https://blog.csdn.net/qq_29831163/article/details/89893908)