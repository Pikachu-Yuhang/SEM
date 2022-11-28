<template>
  <div id="total1">
    <div class="top">
      渔我所欲
    </div>
    <div class="nav clearfloat">
      <ul>
        <li v-for="(item, i) in links" :class="{'current': i === current}">
          <router-link :to="item.data_link" v-text="item.name"></router-link>
        </li>
      </ul>
    </div>

  </div>
</template>

<script>
export default {
  name: "navigate",
  props: {
    current: {
      required: true
    }
  },
  data() {
    return {
      links: [
        {
          data_link: '/data/1',
          name: '淡水养殖产量'
        },
        {
          data_link: '/data/2',
          name: '海水捕捞产量'
        },
        {
          data_link: '/data/3',
          name: '海水养殖产量'
        },
        {
          data_link: '/data/4',
          name: '渔业贸易数据分析'
        }
      ]
    }
  }
}
</script>

<style scoped>

@import "@/views/dataView/data_view_style.css";

</style>