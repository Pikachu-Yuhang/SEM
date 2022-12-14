## 8 项目风险管理

### 8.1 实施周期延期的风险

​	    1、小组内部建立统一的生产制造管理制度的完成日期不确定。

​	    解决方法：建立周密的计划，确保按实施计划完成管理制度。项目经理及时跟进项目，确保项目的顺利进行。

​		2、因任务过重导致的时间拖延。

​		解决方法：小组成员统一协调，向老师说明原因，请求延长实现系统的时间。

​		3、个人因事缺课的风险。

​		解决方法：小组成员向缺课成员说明课堂内容，缺课成员及时进行弥补。

### 8.2 实施范围的风险

​		1、在某一实施分步内的实施主体范围过多，可能会导致项目延期。

​		解决方法：按照实施计划分步实施。

​		2、过分关注细节，导致项目耗费在无尽的开会。

​		解决方法：以实施目标为重点，先上线，后改进。

​		3、在某一实施分步内的实施模块过多，也可能导致项目延期。

​		解决方法：按照实施计划建立各个步骤的实施目标值。

### 8.3 人员的风险

​		1、消极应对项目实施，缺乏激情，怠工等。

​		解决方法：建立有效的奖惩措施，对其造成的影响予以公布和警告，项目组成员互相鼓励和交流，项目组长对消极怠工的成员进行一对一交流。

​		2、项目组人员经验、知识水平不足。

​		解决方法：积极学习，在开发过程中不断完善。

## 9 项目变更管理

### 9.1 微小改正时的变更控制

		1. 在评审或测试后发现的问题由评审组组长或项目经理形成《软件问题报告单》或《源代码修改记录单》，并通知配置管理员。
  		2. 由配置管理员将需要修改的软件的备份从项目配置数据库中检出，开发人员执行修改。
  		3. 修改完毕后进行修改测试，编程错误累计到了一定的量或者测试时间已满一个月（从上一次入配置库后算起），凭《源代码修改记录单》及修改后的源代码，通知配置管理员，配置管理员确定测试报告的完备性，并在核对软件修改内容和修改人员填写的《软件修改报告单》或《源代码修改记录单》中的修改描述一致后，将文件登入项目配置数据库中，生成新版本。
  		4. 配置管理员通过修改《软件配置状态表》和《软件变更记录表》，以使其他相关开发人员及时了解软件变化情况。

### 9.2 较大变动时的变更控制

1. 开发人员或用户提出影响较大的修改要求（这是指要增加或删除某些功能或者是发现错误的阶段在造成错误的阶段后面等）。
2. 配置管理员在收到这类修改要求时，必须组织有项目经理以及开发人员参加的修改评审会，讨论修改的影响范围，修改的必要性、可行性以及修改方法、步骤和实施计划。
3. 在修改方案通过并经项目经理审核后，要由产品开发部经理签字批准。涉及重大技术方案的修改时，修改方案必须由总工程师或技术总监签字批准。以决断修改工作中各项活动的先后顺序及各自的完成日期，以保证整个开发工作按原定计划日期完成。
4. 配置管理员在接到修改批准——由项目经理或产品开发部经理或总工程师或技术总监签字同意的《软件问题报告单》后才可将需修改的软件的备份从项目数据库中检出，开发人员执行修改。
5. 修改完毕后，交客户服务部进行测试和评审，测试和评审都通过后，交配置管理员处理。
6. 配置管理员检查测试报告和评审报告是否完备，核对《软件修改报告单》中的修改描述和修改后的软件是否相符。核查结果符合要求，配置管理员将修改后的软件登入项目数据库中，生成新版本。
7. 配置管理员通过修改《软件配置状态表》和《软件变更记录表》，以使其他相关开发人员及时了解软件变化情况。