<template>
  <div>
    <el-menu :default-active="$route.path" class="el-menu-demo" mode="horizontal" router>
      <el-menu-item index="add/">
        <span>添加员工信息</span>
        <i class="el-icon-edit-outline" slot></i>
      </el-menu-item>
      <el-menu-item index="/find">
        <span>查询员工信息</span>
        <i class="el-icon-search" slot></i>
      </el-menu-item>
      <el-menu-item index="/admin" @click="authCheck">
        <span>编辑 & 删除</span>
        <i class="el-icon-loading" slot></i>
      </el-menu-item>
      <el-button id="logOut" type="danger" @click="Bye" round>退出<i class="el-icon-circle-close-outline el-icon--right"></i></el-button>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: "Main",
  methods: {
    authCheck: function() {
      this.$confirm("此操作需要有更高权限, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      })
        .then(() => {
          this.$router.push({ path: "/admin/" });
        })
        .catch(() => {
          this.$router.push({ path: "/main" });
        });
    },
    Bye: function() {
      this.$router.push({ path: "/" });
    }
  }
};
</script>

<style lang="less">
#logOut {
  padding: 12px 12px;
  margin-top: 1%;
  margin-left: 10%;
}
</style>
