<template>
  <div class="main">
    <div>
      <select id="s" class="sel">
        <option selected>国家</option>
        <option>物种</option>
        <option>产区</option>
      </select>
      <input id="seach" class="inp" type="text" placeholder="请输入搜索值(可以空格隔开)" />
      <button id="qstnMark" onclick="seach()">Q</button>
      <input id="addTmplFile" type="button" value="新增数据" @click="addTmplFile" />
    </div>
    <div>
      <table id="table1" cellspacing="0px">
        <tr class="tableTitle" align="center">
          <td class="col1">国家</td>
          <td class="col2">物种</td>
          <td class="col3">产区</td>
          <td class="col4">来源</td>
          <td class="col5">类型（单位）</td>
          <td class="col6">值</td>
          <td class="col7">年限</td>
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
        <button onclick="last()">&lt</button>
        <button id="pno" style="background-color: #5899ce; color: white">1</button>
        <button onclick="next()">&gt</button>
        &nbsp;
        <p>前往</p>
        <input type="text" id="gopg" onclick="gopage()" />
        <p>页</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DataTable",
  data() {
    return {
      tableAttributes: [
          '省份',
          '年份',
          '类别',
          '数值'
      ]
    }
  }
}
</script>

<style scoped>

@import "@/views/dataView/data_view_style.css";

</style>