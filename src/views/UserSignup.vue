<template>
  <div class="background">
    <div class="login-wrapper">
      <div class="header">Sign up</div>
      <div class="form-wrapper">
        <input type="text" v-model="username" placeholder="请输入用户名" class="input-item username">
        <input type="password" v-model="password" placeholder="请输入密码" class="input-item password">
        <input type="ensure" v-model="ensure" placeholder="确认密码" class="input-item ensure">
        <div class="btn" @click="signup">Sign up</div>
      </div>
    </div>
  </div>
</template>
<style scoped src='../css/user-login.css'></style>
<script>
import axios from 'axios'
export default {
  name: 'UserSignup', // 决定组件名字
  data() {
    return {
      username: '',
      password: '',
      ensure: ''
    }
  },
  methods: {
    signup() {
      // 注册
      if (this.username === '' || this.password === '' || this.ensure === '') {
        alert('请输入完整信息')
        return
      }
      if (this.password !== this.ensure) {
        alert('两次密码输入不一致')
        return
      }
      if (this.password.length < 6) {
        alert('密码长度至少6位')
        return
      }
      axios({
        url: 'http://10.29.75.164:8000/signup/',
        method: 'POST',
        data: {
          username: this.username,
          password: this.password
        }
      }).then(result => {
        this.$router.push({ name: 'home' })
      }).catch(error => {
        alert('error:', error)
      })
    }
  }
}

</script>
