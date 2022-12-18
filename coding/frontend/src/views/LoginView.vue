<template>
  <div class="body">
    <div class="container right-panel-active">
      <!-- Sign Up -->
      <div class="container__form container--signup">
        <form action="#" class="form" id="form1" @submit="submitSignUp">
          <h2 class="form__title">管理员注册</h2>
          <input v-model="sign_up_name" type="user" placeholder="用户名" class="input"/>
          <input v-model="sign_up_email" type="email" placeholder="电子邮箱" class="input" />
          <input v-model="sign_up_pwd" type="password" placeholder="密码" class="input" />
          <router-link to="/data"><button class="btn">注册</button></router-link>
        </form>
      </div>

      <!-- Sign In -->
      <div class="container__form container--signin">
        <form action="#" class="form" id="form2" @submit="submitSignIn">
          <h2 class="form__title">管理员登录</h2>
          <input v-model="sign_in_name" type="user" placeholder="用户名" class="input" />
          <input v-model="sign_in_pwd" type="password" placeholder="密码" class="input" />
          <a href="#" class="link">忘记密码?</a>
          <router-link to="/data"><button class="btn">登录</button></router-link>
        </form>
      </div>

      <!-- Overlay -->
      <div class="container__overlay">
        <div class="overlay">
          <div class="overlay__panel overlay--left">
            <button @click="switchToSignIn" class="btn" id="signIn">管理员登录</button>
          </div>
          <div class="overlay__panel overlay--right">
            <button @click="switchToSignUp" class="btn" id="signUp">管理员注册</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import {style_data} from "@/views/stye_data";

export default {
  name: "LoginView",
  data() {
    return {
      style_data,
      sign_in_name: '',
      sign_in_pwd: '',
      sign_up_name: '',
      sign_up_email: '',
      sign_up_pwd: ''
    }
  },
  methods: {
    switchToSignIn() {
      const container = document.querySelector(".container");
      container.classList.remove("right-panel-active");
    },
    switchToSignUp() {
      const container = document.querySelector(".container");
      container.classList.add("right-panel-active");
    },
    submitSignIn(e) {
      e.preventDefault();
      console.log(this.sign_in_name, this.sign_in_pwd)
      this.$http.post('/accounts/login', {
        'username': this.sign_in_name,
        'password': this.sign_in_pwd
      }).then((res) => {});
    },
    submitSignUp(e) {
      e.preventDefault();
      this.$http.post('/accounts/signup', {
        'username': this.sign_up_name,
        'email': this.sign_up_email,
        'password': this.sign_up_pwd
      }).then((res) => {});
    }
  }
}


</script>

<style scoped>

:root {
  font-size: 16px;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
  Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}

.body {
  align-items: center;
  background: url("@/assets/loginBackground.jpg");
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  display: grid;
  height: 100vh;
  place-items: center;
}

.form__title {
  font-weight: 300;
  margin: 0;
  margin-bottom: 1.25rem;
}

.link {
  color: v-bind(style_data.gray);
  font-size: 0.9rem;
  margin: 1.5rem 0;
  text-decoration: none;
}

.container {
  background-color: white;
  border-radius: v-bind(style_data.button_radius);
  box-shadow: 0 0.9rem 1.7rem rgba(0, 0, 0, 0.25),
  0 0.7rem 0.7rem rgba(0, 0, 0, 0.22);
  height: v-bind(style_data.max_height);
  max-width: v-bind(style_data.max_width);
  overflow: hidden;
  position: relative;
  width: 100%;
}

.container__form {
  height: 100%;
  position: absolute;
  top: 0;
  transition: all 0.6s ease-in-out;
}

.container--signin {
  left: 0;
  width: 50%;
  z-index: 2;
}

.container.right-panel-active .container--signin {
  transform: translateX(100%);
}

.container--signup {
  left: 0;
  opacity: 0;
  width: 50%;
  z-index: 1;
}

.container.right-panel-active .container--signup {
  animation: show 0.6s;
  opacity: 1;
  transform: translateX(100%);
  z-index: 5;
}

.container__overlay {
  height: 100%;
  left: 50%;
  overflow: hidden;
  position: absolute;
  top: 0;
  transition: transform 0.6s ease-in-out;
  width: 50%;
  z-index: 100;
}

.container.right-panel-active .container__overlay {
  transform: translateX(-100%);
}

.overlay {
  background: url("@/assets/loginBackground2.jpg");
  background-color: white;
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  height: 100%;
  left: -100%;
  position: relative;
  transform: translateX(0);
  transition: transform 0.6s ease-in-out;
  width: 200%;
}

.container.right-panel-active .overlay {
  transform: translateX(50%);
}

.overlay__panel {
  align-items: center;
  display: flex;
  flex-direction: column;
  height: 100%;
  justify-content: center;
  position: absolute;
  text-align: center;
  top: 0;
  transform: translateX(0);
  transition: transform 0.6s ease-in-out;
  width: 50%;
}

.overlay--left {
  transform: translateX(-20%);
}

.container.right-panel-active .overlay--left {
  transform: translateX(0);
}

.overlay--right {
  right: 0;
  transform: translateX(0);
}

.container.right-panel-active .overlay--right {
  transform: translateX(20%);
}

.btn {
  background: linear-gradient(94.06deg, #73C1E9 3.33%, #9CD0E2 96.7%);
  border-radius: 20px;
  border: none;
  color: #fff;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: 0.1rem;
  padding: 0.9rem 4rem;
  text-transform: uppercase;
  transition: transform 80ms ease-in;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
  Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}

.form>.btn {
  margin-top: 1.5rem;
}

.btn:active {
  transform: scale(0.95);
}

.btn:focus {
  outline: none;
}

.form {
  background: white;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 3rem;
  height: 100%;
  text-align: center;
}

.input {
  background-color: rgb(245, 245, 245);
  border: none;
  padding: 0.9rem 0.9rem;
  margin: 0.5rem 0;
  width: 100%;
  border-radius: 8px;
}

@keyframes show {

  0%,
  49.99% {
    opacity: 0;
    z-index: 1;
  }

  50%,
  100% {
    opacity: 1;
    z-index: 5;
  }
}

</style>