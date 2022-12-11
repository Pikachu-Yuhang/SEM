<template>
  <navigate :current="current"></navigate>
  <data-table mode="user"></data-table>
</template>

<script>

import Navigate from "@/components/navigate.vue";
import DataTable from "@/components/table.vue";
import DataMap from "@/components/map.vue";
import EchartsMap from "@/components/mapView.vue";

export default {
  name: "userDataView",
  components: {EchartsMap, DataMap, DataTable, Navigate},
  data() {
    return {
      current: 0,
      ifShowMap: false
    }
  },
  methods: {
    showMap() {
      this.ifShowMap = true;
    },
    hideMap() {
      this.ifShowMap = false;
    }
  }
}
</script>

<style scoped>

@import "@/views/userDataView/user_data_view_style.css";

</style>