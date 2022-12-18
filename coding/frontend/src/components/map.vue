<template>
  <div class="main">
<!--    <div class="box"><br>-->
<!--      <input class="newButton" type="button" value="添加图层"/><br><br>-->
<!--      <input class="newButton" type="button" value="删除图层"/>-->
<!--    </div>-->
    <echarts-map ref="map"></echarts-map>
  </div>
</template>

<script>

import EchartsMap from "@/components/mapView.vue";

export default {
  name: "dataMap",
  components: {EchartsMap},
  methods: {
    changeMap(mapData, tableName, tableSubName, max) {
      this.$refs.map.init(mapData, tableName, tableSubName, max);
    }
  }
}
</script>

<style scoped>

@import "@/views/userDataView/user_data_view_style.css";

.newButton {
  float: right;
  border: none;
  cursor: pointer;
  font-weight: 700;
  padding: 10px 15px;
  font-size: 18px;
  border-radius: 8px;
  margin-left: 15px;
  margin-bottom: 10px;
}


</style>