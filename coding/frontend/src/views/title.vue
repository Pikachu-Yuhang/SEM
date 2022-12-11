<template>
  <div class="body">
    渔我所欲<br>
    <div class="top1"><br>
      渔业产业地图信息可视化平台
    </div>
    <button class="btn">用户</button>
    <button class="btn">管理员</button>
  </div>
</template>

<script>

import {style_data} from "@/views/stye_data";

export default {
  name: "title",
  data() {
    return {
      style_data
    }
  }
}
</script>

<style scoped>

.top1 {
  color: #1d1e26;
  font-family: -apple-system,
  BlinkMacSystemFont,
  "Segoe UI",
  Roboto,
  Oxygen,
  Ubuntu,
  Cantarell,
  "Open Sans",
  "Helvetica Neue",
  sans-serif;
  font-size: 1.5rem;
  height: 35px;
  border-bottom:none;
  padding-left: 0px;
  padding-top: 15px;
}

.btn {
  background-image: linear-gradient(90deg, rgb(148, 191, 240) 0%, v-bind(style_data.lightblue) 74%);
  border-radius: 20px;
  border: 1px solid lightgrey;
  color: rgb(52, 68, 110);
  cursor: pointer;
  margin-left: 40px;
  font-size: 1rem;
  letter-spacing: 0.1rem;
  padding: 0.9rem 4rem;
  text-transform: uppercase;
  transition: transform 80ms ease-in;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
  Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}

</style>