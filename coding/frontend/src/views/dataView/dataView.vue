<template>
  <navigate @changeCurrent="changeCurrent" :current="current"></navigate>
  <data-table ref="data_table" mode="admin"></data-table>
</template>

<script>

import Navigate from "@/components/navigate.vue";
import DataTable from "@/components/table.vue";

export default {
  name: "dataView",
  components: {DataTable, Navigate},
  data() {
    return {
      current: 0
    }
  },
  methods: {
    changeCurrent(new_current, new_name) {
      this.current = new_current;
      this.$refs.data_table.changeCurrentTable(new_current, new_name);
    }
  }
}
</script>

<style scoped>

@import "@/views/dataView/data_view_style.css";

</style>