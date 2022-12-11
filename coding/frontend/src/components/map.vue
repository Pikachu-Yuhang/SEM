<template>
  <div class="main">
    <div class="box"><br>
      <input class="newButton" type="button" value="添加图层" onclick="inimage()" /><br><br>
      <input class="newButton" type="button" value="删除图层" onclick="delimage()" />
    </div>
    <echarts-map ref="map"></echarts-map>
  </div>
</template>

<script>

import EchartsMap from "@/components/mapView.vue";

export default {
  name: "dataMap",
  components: {EchartsMap},
  methods: {
    changeMap(param) {
      this.$refs.map.init(param)
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