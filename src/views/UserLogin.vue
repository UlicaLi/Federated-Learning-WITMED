<!-- <template>标签用来定义组件的HTML模板。这是该组件的视图部分，即用户所看到的内容。 -->
<template>
  <div class="background">
    <div class="login-wrapper">
      <div class="header">Login</div>
      <div class="form-wrapper">
        <input type="text" v-model="username" placeholder="请输入用户名" class="input-item username">
        <input type="password" v-model="password" placeholder="请输入密码" class="input-item password">
        <!-- <h1>{{ username }}</h1> -->
        <div class="btn" @click="login">Login</div>
      </div>
      <div class="msg">
        Don't have account?
        <router-link to="/signup">Sign up</router-link>
      </div>
    </div>
  </div>
</template>

<style scoped src='../css/user-login.css'></style>

<script >
import axios from 'axios'
export default {
  name: 'UserLogin',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login() {
      axios({
        url: 'http://10.29.75.164:8000/login/',
        method: 'POST',
        data: {
          username: this.username,
          password: this.password
        }
      }).then(result => {
        this.$router.push('/admin')
      }).catch(error => {
        alert('用户不存在', error)
      })
    }
  }
}

</script>
