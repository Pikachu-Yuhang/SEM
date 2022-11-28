<template>
  <div id="total1">
    <div class="top">
      渔我所欲
    </div>
    <div class="nav clearfloat">
      <ul>
        <li><router-link to="/data1">淡水养殖产量</router-link></li>
        <li><router-link to="/data2">海水捕捞产量</router-link></li>
        <li><router-link to="/data3">海水养殖产量</router-link></li>
        <li><router-link to="/data4">渔业贸易数据分析</router-link></li>
        <li class="current"><router-link to="/data5">水产种质资源保护区</router-link></li>
      </ul>
    </div>
    <div class="main">
      <div>
        <select id="s" class="sel">
          <option selected>保护区名称</option>
          <option>所在行政区</option>
          <option>批准编号</option>
        </select>
        <input id="seach" class="inp" type="text" placeholder="请输入搜索值(可以空格隔开)" />
        <button id="qstnMark" onclick="seach()">Q</button>
        <input id="addTmplFile" type="button" value="新增数据" onclick="addTmplFile()" />
      </div>
      <div>
        <table id="table1" cellspacing="0px">
          <tr class="tableTitle" align="center">
            <td class="col1">保护区名称</td>
            <td class="col2">批准编号</td>
            <td class="col3">所在行政区</td>
            <td class="col4">管理机构名称</td>
            <td class="col5">保护区总面积(公顷)</td>
            <td class="col6">核心区面积(公顷)</td>
            <td class="col7">试验区面积(公顷)</td>
            <td class="col9">地理坐标范围</td>
            <td class="col10">重点保护对象</td>
            <td class="col8">操作</td>
          </tr>
        </table>
        <div id="lowerLbl" align="center">
          <p>共</p>
          <p id="rowsNum">0</p>
          <p>条</p>
          <select id="sel" onclick="pagination()">
            <option id="opt0" value="10">10条/页</option>
            <option id="opt1" value="20">20条/页</option>
            <option id="opt2" value="50">50条/页</option>
          </select>
          &nbsp;
          <button onclick="last()"></button>
          <button id="pno" style="background-color: #5899ce; color: white">1</button>
          <button onclick="next()"></button>
          &nbsp;
          <p>前往</p>
          <input type="text" id="gopg" onclick="gopage()" />
          <p>页</p>
        </div>
      </div>
    </div>

  </div>

  <div id="total2">
    <div class="top1">
      渔业数据管理列表
      <p style="display: inline; color: #999999"> > 渔业数据管理 </p>
    </div>
    <div class="main" align="center">
      <table id="table2" cellspacing="18px">
        <tr class="table2Tr">
          <td class="table2Td1" align="right">保护区名称</td>
          <td class="table2Td2"><input id="country" type="text" placeholder="保护区名称" /></td>
        </tr>
        <tr class="table2Tr">
          <td class="table2Td1" align="right">批准编号</td>
          <td class="table2Td2"><input id="wu" type="text" placeholder="批准编号" /></td>
        </tr>
        <tr class="table2Tr">
          <td class="table2Td1" align="right">所在行政区</td>
          <td class="table2Td2"><input id="chan" type="text" placeholder="所在行政区" /></td>
        </tr>
        <tr class="table2Tr">
          <td class="table2Td1" align="right">管理机构名称</td>
          <td class="table2Td2"><input id="lai" type="text" placeholder="管理机构名称" /></td>
        </tr>
        <tr class="table2Tr">
          <td class="table2Td1" align="right">保护区总面积(公顷)</td>
          <td class="table2Td2"><input id="lei" type="text" placeholder="保护区总面积(公顷)" /></td>
        </tr>
        <tr class="table2Tr">
          <td class="table2Td1" align="right">核心区面积(公顷)</td>
          <td class="table2Td2"><input id="zhi" type="text" placeholder="核心区面积(公顷)" /></td>
        </tr>
        <tr class="table2Tr">
          <td class="table2Td1" align="right">试验区面积(公顷)</td>
          <td class="table2Td2"><input id="nian" type="text" placeholder="试验区面积(公顷)" /></td>
        </tr>
        <tr class="table2Tr">
          <td class="table2Td1" align="right">地理坐标范围</td>
          <td class="table2Td2"><input id="q1" type="text" placeholder="地理坐标范围" /></td>
        </tr>
        <tr class="table2Tr">
          <td class="table2Td1" align="right">重点保护对象</td>
          <td class="table2Td2"><input id="q2" type="text" placeholder="重点保护对象" /></td>
        </tr>
        <tr>
          <td></td>
          <td><input id="submit1" style="height: 35px; width: 80px;" type="button" value="提交"
                     onclick="submit1()" /></td>
          <td><input id="submit2" style="height: 35px; width: 80px; display: none" type="button" value="提交"
                     onclick="submit2()" /></td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: "dataView5"
}
</script>

<style scoped>

@import "@/views/dataView/data_view_style.css";

</style>