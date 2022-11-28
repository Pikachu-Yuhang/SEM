<template>
  <div id="total1">
    <div class="top">
      渔我所欲
    </div>
    <div class="nav clearfloat">
      <ul>
        <li><router-link to="/userData1">淡水养殖产量</router-link></li>
        <li><router-link to="/userData2">海水捕捞产量</router-link></li>
        <li><router-link to="/userData3">海水养殖产量</router-link></li>
        <li class="current"><router-link to="/userData4">渔业贸易数据分析</router-link></li>
        <li><router-link to="/userData5">水产种质资源保护区</router-link></li>
      </ul>
    </div>
    <div class="main">
      <div>
        <select id="s" class="sel">
          <option selected>年份</option>
          <option>地区</option>
          <option>品种</option>
        </select>
        <input id="seach" class="inp" type="text" placeholder="请输入搜索值(可以空格隔开)" />
        <button id="qstnMark" onclick="seach()">Q</button>
        <input id="addTmplFile" type="button" style="margin-left:10px;" value="显示地图" onclick="map()" />
        <input id="addTmplFile" type="button" value="导出表格" onclick="load()" />
      </div>
      <div>
        <table id="table1" cellspacing="0px">
          <tr class="tableTitle" align="center">
            <td class="col1">年份</td>
            <td class="col2">地区</td>
            <td class="col3">品种</td>
            <td class="col4">进口
              <select id="s" class="sel1">
                <option selected>></option>
                <option>=</option>
                <option></option>
              </select>
              <input id="seach" class="inp1" type="text" placeholder=" " />
              <button id="qstnMark1" onclick="seach()">Q</button>
            </td>
            <td class="col5">出口
              <select id="s" class="sel1">
                <option selected>></option>
                <option>=</option>
                <option></option>
              </select>
              <input id="seach" class="inp1" type="text" placeholder=" " />
              <button id="qstnMark1" onclick="seach()">Q</button>
            </td>
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
    <div class="top">
      渔我所欲
    </div>
    <div class="nav clearfloat">
      <ul>
        <li><a href="userdsyz.html">淡水养殖产量</a></li>
        <li><a href="userhsbl.html">海水捕捞产量</a></li>
        <li><a href="userhsyz.html">海水养殖产量</a></li>
        <li class="current"><a href="usermaoyi.html">渔业贸易数据分析</a></li>
        <li><a href="userqv.html">水产种质资源保护区</a></li>
      </ul>
    </div>
    <div class="main">
      <div>
        <select id="s" class="sel">
          <option selected>年份</option>
          <option>地区</option>
          <option>品种</option>
        </select>
        <input id="seach" class="inp" type="text" placeholder="请输入搜索值(可以空格隔开)" />
        <button id="qstnMark" onclick="seach()">Q</button>
        <input id="addTmplFile" type="button" style="margin-left:10px;" value="显示表格" onclick="table()" />
        <input id="addTmplFile" type="button" value="导出图片" onclick="load()" />
        <div>
          <div class="box"><br>
            <input id="addTmplFile1" type="button" value="添加图层" onclick="inimage()" /><br><br>
            <input id="addTmplFile1" type="button" value="删除图层" onclick="delimage()" />
          </div>
          <p>
            <img src="map.png" />
          </p>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "userDataView4"
}
</script>

<style scoped>

@import "@/views/userDataView/user_data_view_style.css";

</style>