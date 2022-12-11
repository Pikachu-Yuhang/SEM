<template>
  <navigate current="0"></navigate>

  <div id="total2">
    <div class="top1">
      渔业数据管理列表
      <p style="display: inline; color: #999999"> > 渔业数据管理 </p>
    </div>
    <div class="main" align="center">
      <table id="table2" cellspacing="18px">
        <tr class="table2Tr">
          <td class="table2Td1" align="right">国家</td>
          <td class="table2Td2"><input id="country" type="text" placeholder="国家" /></td>
        </tr>
        <tr class="table2Tr">
          <td class="table2Td1" align="right">物种</td>
          <td class="table2Td2"><input id="wu" type="text" placeholder="物种" /></td>
        </tr>
        <tr class="table2Tr">
          <td class="table2Td1" align="right">产区</td>
          <td class="table2Td2"><input id="chan" type="text" placeholder="产区" /></td>
        </tr>
        <tr class="table2Tr">
          <td class="table2Td1" align="right">来源</td>
          <td class="table2Td2"><input id="lai" type="text" placeholder="来源" /></td>
        </tr>
        <tr class="table2Tr">
          <td class="table2Td1" align="right">类型（单位）</td>
          <td class="table2Td2"><input id="lei" type="text" placeholder="类型（单位）" /></td>
        </tr>
        <tr class="table2Tr">
          <td class="table2Td1" align="right">值</td>
          <td class="table2Td2"><input id="zhi" type="text" placeholder="值" /></td>
        </tr>
        <tr class="table2Tr">
          <td class="table2Td1" align="right">年限</td>
          <td class="table2Td2"><input id="nian" type="text" placeholder="年限" /></td>
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
import Navigate from "@/components/navigate.vue";

export default {
  name: "AddTableView",
  components: {Navigate},
  data() {
    return {
      tableName: ''
    }
  },
  methods: {
    createTable() {
      this.$http.post('/tables/create', {
        'tablename': this.tableName
      }).then((res) => {
        console.log(res);
      })
    }
  }
}
</script>

<style scoped>

@import "@/views/dataView/data_view_style.css";

</style>