<template>
  <div id="background"></div>
    <div id="body">
      <div class="title">渔我所欲</div>
      <div class="top1"><br>
        渔业产业地图信息可视化平台
      </div>
      <router-link to="/userData"><button class="btn">用户</button></router-link>
      <router-link to="/login"><button class="btn">管理员</button></router-link>
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

#background {
  width: 100%;
  height: 100vh;
  position: absolute;
  top: 0;
  background-image: url("@/assets/loginBackground.jpg");
  background-size: cover;
}

#body {
  margin: 0 auto;
  width: 40vw;
  height: 45vh;
  background-color: rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(20px);
  border-radius: 20px;
  box-shadow: 0 0 15px 3px rgba(0, 0, 0, 0.05);
}

.title {
  font-size: 90px;
  margin-top: 20vh;
  padding-top: 48px;
  color: white;
}

.top1 {
  margin-top: 1vh;
  color: white;
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
}

.btn {
  margin-top: 10vh;
  background-image: linear-gradient(90deg, rgb(127, 197, 231) 0%, rgb(177, 216, 222) 74%);
  border-radius: 20px;
  border: none;
  color: white;
  font-weight: 600;
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