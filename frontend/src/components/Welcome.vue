<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <el-button id="goLog" @click="toLogin" plain round>管理员登录<i class="el-icon-service el-icon--right"></i></el-button>
    <h6 @click="toAdmin">添加管理员？</h6>
  </div>
</template>

<script>
export default {
  name: "Welcome",
  props: {
    msg: String
  },
  methods: {
    toAdmin: function() {
      this.$router.push({ path: "/admin/" });
    },
    toLogin: function() {
      this.$router.push({ path: "/login" });
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
h3 {
  margin: 40px 0 0;
}
h6 {
  margin: 40px 0 0;
  cursor: pointer;
  text-decoration: underline;
}
#goLog {
  margin: 20px 0 0;
}
</style>
