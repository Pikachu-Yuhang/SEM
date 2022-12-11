<template>
  <div class="main">
    <div class="filter">
      <span class="choice">筛选时间</span>
      <select id="time" class="select" v-bind="currentYear" @change="changeCurrentYear">
        <option v-for="(year, index) in yearList" :value="index">{{year}}</option>
      </select>

      <span class="choice">筛选种类</span>
      <select id="kind" class="select" v-model="currentKind" @change="changeCurrentKind">
        <option v-for="(kind, index) in kindList" :value="index">{{kind}}</option>
      </select>

      <button id="filter" @click="filterData">筛选</button>

      <select id="s" class="sel">
        <option selected>国家</option>
        <option>物种</option>
        <option>产区</option>
      </select>
      <input id="seach" class="inp" type="text" placeholder="请输入搜索值(可以空格隔开)" />
      <button id="qstnMark" onclick="seach()">Q</button>

<!--      <button class="newTableButton" v-show="mode === 'admin' && !adding"><router-link v-if="mode === 'admin'" to="/addTable" class="newButton" tag="p">新增数据表</router-link></button>-->
      <button class="newButton"  v-show="mode === 'admin' && !adding">新增数据表</button>
      <button class="newButton" v-show="mode === 'admin' && !adding" @click="startAdd">新增数据</button>

      <input v-if="mode === 'user'" class="newButton" type="button" style="margin-left:15px;" :value="ifShowMap?'隐藏地图':'显示地图'" @click="showMap"/>
      <input v-if="mode === 'user'" class="newButton" type="button" value="导出表格" onclick="load()" />
    </div>

    <div>
      <table id="table1" :class="{thinTable:ifShowMap}" cellspacing="0px">
          <tr class="tableTitle">
            <th v-for="item in tableAttributes" v-text="item"></th>
          </tr>

        <tr v-for="(row, index) in tableRows.slice((currentPage - 1) * 20, currentPage * 20)">
          <td v-for="item in row">
            <p v-show="!modifyList[index]">{{item}}</p>
            <input v-if="modifyList[index]">
          </td>
          <td v-if="mode === 'admin'">
            <button class="modifyButton" @click="startModify" :value="index">修改</button>
            <button class="deleteButton" @click="deleteRow">删除</button>
          </td>
        </tr>

        <tr v-if="mode === 'admin' && adding">
          <td v-for="(value, key) in newRow">
            <input v-model="newRow[key]">
          </td>
          <td>
            <button class="submitButton" @click="submitAdd">完成</button>
            <button class="cancelButton" @click="cancelAdd">取消</button>
          </td>
        </tr>
      </table>

      <data-map v-show="ifShowMap" ref="map"></data-map>

      <div id="lowerLbl" align="center">
        <p>共</p>
        <p id="rowsNum">{{tableRows.length}}</p>
        <p>条</p>
        &nbsp;
        <button @click="lastPage">&lt</button>
        <button id="pno" style="background-color: #5899ce; color: white">{{currentPage}}</button>
        <button @click="nextPage">&gt</button>
        &nbsp;
        <p>前往</p>
        <input type="text" id="gopg" @change="goPage" />
        <p>页</p>
      </div>
    </div>
  </div>
</template>

<script>

import DataMap from "@/components/map.vue";

export default {
  name: "DataTable",
  components: {DataMap},
  props: {
    mode: {
      default: 'admin'
    }
  },
  data() {
    return {
      /*state of operation*/
      ifShowMap: false,
      adding: false,

      /*information about the metadata of all tables*/
      table_list: [],

      /*information about the current table*/
      current: 0,
      tableName: '远洋渔业',
      tableAttributes: [
          '省份',
          '时间',
          '种类',
          '数值'
      ],
      currentYear: 0,
      yearList: [
          '全部',
          '2013',
          '2014',
          '2015',
          '2016'
      ],
      currentKind: 0,
      kindList: [
          '全部',
          '鲫鱼',
          '草鱼'
      ],
      tableRows: [],
      currentPage: 1,
      modifyList: [],

      /*reserved for the new row*/
      newRow: {
        city: '',
        time: '',
        kind: '',
        num: ''
      }
    }
  },
  created() {
    if (this.mode === 'admin')
      this.tableAttributes.push('操作');
    this.$http.post("/tables/getall", {
      'tablename': '远洋渔业',
    }).then((res) => {
      this.tableRows = res.data;
      for (let i in this.tableRows.length)
        this.modifyList[i] = false;
    })
  },
  methods: {
    changeCurrentYear(event) {
      this.currentYear = event.target.value;
    },
    changeCurrentKind(event) {
      this.currentKind = event.target.value;
    },
    filterData() {
      this.$http.post('/tables/data', {
        'tablename': this.tableName,
        'kind': this.kindList[this.currentKind],
        'year': this.yearList[this.currentYear]
      }).then((res) => {
        console.log(res);
      })
    },
    changeCurrentTable(new_current) {
      this.current = new_current;
    },
    startAdd() {
      this.adding = true;
    },
    submitAdd() {
      var newRowToAdd = Object.assign({}, this.newRow);
      this.tableRows.push(newRowToAdd);
      for (let item in this.newRow)
        this.newRow[item] = '';
      this.adding = false;
      this.$http.post('/edit/insert', {
        'tablename': '远洋渔业',
        'city': newRowToAdd.city,
        'year': '2022',
        'kind': '都可以',
        'num': newRowToAdd.num
      }).then((res) => {
        console.log(res);
      });
    },
    cancelAdd() {
      this.adding = false;
    },
    startModify(event) {
      this.modifyList[event.target.value] = true;
    },
    submitModify() {
      this.$http.post('/edit/update', {
        "tablename": '',
        "del_city": __,
        "del_year": __,
        "del_kind": __,
        "del_num":  __,
        "neo_city": __,
        "neo_year": __,
        "neo_kind": __,
        "neo_num":  __
      }).then((res) => {
        console.log(res);
      });
    },
    deleteRow() {
      this.$http.post('/edit/delete', {
        "tablename": '',
        "del_city": __,
        "del_year": __,
        "del_kind": __,
        "del_num":  __,
        "neo_city": __,
        "neo_year": __,
        "neo_kind": __,
        "neo_num":  __
      }).then((res) => {
        console.log(res)
      });
    },
    lastPage() {
      if (this.currentPage !== 1) {
        this.currentPage -= 1;
      }
    },
    nextPage() {
      console.log(parseInt((this.tableRows.length - 1) / 20) + 1);
      if (this.currentPage !== parseInt((this.tableRows.length - 1) / 20) + 1)
        this.currentPage += 1;
    },
    goPage(event) {
      let page = parseInt(event.target.value)
      if (page <= 0)
        this.currentPage = 1;
      else if (page > parseInt((this.tableRows.length - 1) / 20) + 1)
        this.currentPage = parseInt((this.tableRows.length - 1) / 20) + 1;
      else
        this.currentPage = page;
    },
    showMap() {
      this.ifShowMap = !this.ifShowMap;
    },
  }
}
</script>

<style scoped>

@import "@/views/dataView/data_view_style.css";

.select {
  width: 100px;
  height: 30px;
  margin: 0 40px 0 20px;
  border: rgb(211, 211, 211) solid 1px;
  border-radius: 6px;
  background-color: rgb(240, 240, 240);
  font-weight: 600;
  padding-left: 10px;
}

.select option {
  background-color: white;
}

#filter {
  width: 100px;
  border: none;
  cursor: pointer;
  font-weight: 700;
  padding: 10px 15px;
  font-size: 18px;
  border-radius: 8px;
  margin-right: 40px;
  background-color: rgb(116, 194, 233);
  color: white;
}

#table1 {
  margin: 15px auto 0;
  border: none;
  width: 95%;
  box-shadow: 0px 4px 25px rgba(0, 0, 0, 0.1);
  border-radius: 20px;
  transition: all 0.3s;
}

.thinTable {
  margin: 15px 0 0 0 !important;
  width: 50% !important;
}

/*表头*/
.tableTitle {
  background: linear-gradient(90.64deg, rgb(77, 179, 241) 1.1%, rgb(103, 189, 236) 98.61%);
  font-weight: bold;
  border-radius: 10px;
}

/*第一张表中的单元格格式*/
#table1 th {
  color: white;
  height: 50px;
  width: 20%;
  border-left: rgb(240, 240, 240) 1px solid;
}

#table1 th:first-child {
  border-top-left-radius: 20px;
}

#table1 th:last-child {
  border-top-right-radius: 20px;
}

#table1 td {
  height: 40px;
  border: none;
  border-bottom: 1px solid rgb(220, 220, 220);
}

#table1 tr:last-child td {
  border-bottom: none;
}

.modifyButton, .submitButton, .deleteButton, .cancelButton {
  width: 45px;
  height: 25px;
  border-radius: 5px;
  border: none;
  font-weight: 700;
  cursor: pointer;
}

.modifyButton {
  background-color: rgb(193, 226, 243);
  color: rgb(40, 127, 175);
  margin-right: 10px;
}

.submitButton {
  background-color: rgb(227, 243, 223);
  color: rgb(6, 115, 0);
  margin-right: 10px;
}

.deleteButton {
  background-color: rgb(243, 223, 223);
  color: rgb(240, 30, 30);
  margin-left: 10px;
}

.cancelButton {
  background-color: rgb(255, 245, 223);
  color: rgb(229, 135, 0);
  margin-left: 10px;
}

.newButton {
  float: right;
  border: none;
  cursor: pointer;
  font-weight: 700;
  padding: 10px 15px;
  font-size: 18px;
  border-radius: 8px;
  margin-left: 15px;
}

.choice {
  font-weight: 700;
}

.filter {
  position: relative;
  width: 97%;
}

</style>