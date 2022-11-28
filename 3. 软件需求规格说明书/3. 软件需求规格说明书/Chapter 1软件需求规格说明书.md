## 1 引言

​		引言提出了对软件需求规格说明的纵览，希望能帮助读者理解本文档是如何编写，并如何阅读和解释。



### 1.1 目的

​		在完成针对“渔业产业地图信息可视化平台”的前期调查，同时与多位项目用户代表进行了全面深入地探讨和分析的基础上，提出这份软件需求规格书。

​		此需求规格说明书对“渔业产业地图信息可视化平台”做了全面细致的用户需求分析，明确了本系统应具有的概貌、功能要求、性能分析、运行要求等，并尽可能完整地描述系统预期的外部行为和用户可视化行为，使系统分析人员及软件开发人员能清楚地了解用户需求，并在此基础上进一步提出概要设计说明书和完成后续设计与开发工作。



### 1.2 文档约定

​		本部分描述编写文档时采用的标准或排版约定，包括撰写软件、正文风格、表格格式、提示区和重要符号等。

<h5 style="color:#0487de">采用标准</h5>

​		编写文档采用的标准为IEEE_830-1998版本软件需求规格说明书，部分内容根据项目实际情况进行调整或删减。

<h5 style="color:#0487de">撰写软件</h5>

​		文档由Typora的Markdown统一撰写，并以pdf格式存储。

<h5 style="color:#0487de">排版约定</h5>

| 格式   | 字体      | 字号 | 加粗 | 斜体 | 下划线 |
| ------ | --------- | ---- | ---- | ---- | ------ |
| 标题   | Open Sans | 48   | 否   | 否   | 否     |
| 副标题 | Open Sans | 小二 | 否   | 否   | 否     |
| 标题1  | Open Sans | 28   | 是   | 否   | 否     |
| 标题2  | Open Sans | 20   | 是   | 否   | 否     |
| 标题3  | Open Sans | 18   | 是   | 否   | 否     |
| 标题4  | Open Sans | 16   | 是   | 否   | 否     |
| 正文   | Open Sans | 16   | 否   | 否   | 否     |
| 引用   | Open Sans | 14   | 否   | 否   | 否     |



### 1.3 预期读者和阅读建议

​		此部分列举了该软件需求规格说明书所针对的目标读者群，并且针对不同的读者提出了相应的阅读建议。

<h5 style="color:#0487de">读者范围</h5>

​		此说明书的预期读者群为：客户、业务分析员、需求分析员、用户文档编写人员、测试人员和项目管理人员。

<h5 style="color:#0487de">阅读建议</h5>

|                                   | 管理人员           | 客户               | 用户               | 需求分析员         | 测试人员           | 文档编写人员       |
| --------------------------------- | ------------------ | ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| <center>引言</center>             | <center>√</center> | <center>√</center> | <center>√</center> | <center>√</center> | <center>√</center> | <center>√</center> |
| <center>产品概述</center>         | <center>√</center> | <center>√</center> |                    | <center>√</center> | <center>√</center> | <center>√</center> |
| <center>系统需求分析概述</center> | <center>√</center> | <center>√</center> |                    | <center>√</center> |                    | <center>√</center> |
| <center>功能需求</center>         | <center>√</center> | <center>√</center> | <center>√</center> | <center>√</center> | <center>√</center> | <center>√</center> |
| <center>其他非功能需求</center>   | <center>√</center> | <center>√</center> |                    | <center>√</center> | <center>√</center> | <center>√</center> |
| <center>外部接口需求</center>     | <center>√</center> | <center>√</center> | <center>√</center> | <center>√</center> | <center>√</center> | <center>√</center> |
| <center>其他需求</center>         | <center>√</center> | <center>√</center> | <center>√</center> | <center>√</center> | <center>√</center> | <center>√</center> |
| <center>术语表</center>           |                    | <center>√</center> |                    | <center>√</center> |                    | <center>√</center> |
| <center>待解决问题列表</center>   | <center>√</center> | <center>√</center> | <center>√</center> | <center>√</center> |                    | <center>√</center> |



### 1.4 参考文献

<p style='font-size:14px'>[1] 《软件工程——实践者的研究方法》, Roger S.Pressman, 机械工业出版社<p>

<p style='font-size:14px'>[2] 《软件需求（第三版）》, Karl Wiegers，Joy Beatty, 清华大学出版社<p>

<p style='font-size:14px'>[3] 《软件工程开发国家标准》<p>

<p style='font-size:14px'>[4] “在线教学辅助系统” G04-1-项目章程<p>

<p style='font-size:14px'>[5] “在线教学辅助系统” G04-2-项目计划<p>

<p style='font-size:14px'>[6] “在线教学辅助系统” G04-3-软件需求规格说明书 </p>