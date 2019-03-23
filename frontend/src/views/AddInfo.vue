<template>
  <div>
    <Header />
    <h1>Add employee info</h1>
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
      <el-form-item label="员工编号" prop="code">
        <el-input v-model="ruleForm.code"></el-input>
      </el-form-item>
      <el-form-item label="员工姓名" prop="name">
        <el-input v-model="ruleForm.name"></el-input>
      </el-form-item>
      <el-form-item label="员工年龄" prop="age">
        <el-input v-model="ruleForm.age"></el-input>
      </el-form-item>
      <el-form-item label="出生日期" required>
        <el-form-item prop="birthDate">
          <el-date-picker type="date" placeholder="选择日期" v-model="ruleForm.birthDate" style="width: 100%;"></el-date-picker>
        </el-form-item>
      </el-form-item>
      <el-form-item label="员工电话" prop="tel">
        <el-input v-model="ruleForm.tel"></el-input>
      </el-form-item>
      <el-form-item label="员工职位" prop="rank">
        <el-input v-model="ruleForm.rank"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm')" round>添加<i class="el-icon-circle-check-outline el-icon--right"></i></el-button>
        <el-button @click="resetForm('ruleForm')" round>重置<i class="el-icon-refresh el-icon--right"></i></el-button>
        <el-button id="goHome" type="warning" @click="Home" round>返回主页<i class="el-icon-menu el-icon--right"></i></el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import Header from "@/components/MainHeader.vue";
export default {
  name: "AddInfo",
  components: {
    Header
  },
  data() {
    return {
      ruleForm: {
        code: "",
        name: "",
        age: "",
        birthDate: "",
        tel: "",
        rank: ""
      },
      rules: {
        code: [
          { required: true, message: "请输入编号", trigger: "blur" },
          { min: 1, max: 20, message: "长度在 1 到 20 个字符", trigger: "blur" }
        ],
        name: [
          { required: true, message: "请输入姓名", trigger: "blur" },
          { min: 3, max: 20, message: "长度在 3 到 20 个字符", trigger: "blur" }
        ],
        age: [
          { required: true, message: "请输入年龄", trigger: "blur" },
          { min: 1, max: 3, message: "长度在 1 到 3 个字符", trigger: "blur" }
        ],
        birthDate: [
          {
            type: "date",
            required: true,
            message: "请选择出生日期",
            trigger: "change"
          }
        ],
        tel: [
          { required: true, message: "请输入电话", trigger: "blur" },
          { min: 11, max: 11, message: "长度为 11 个字符", trigger: "blur" }
        ],
        rank: [
          { required: true, message: "请输入职位", trigger: "blur" },
          { min: 2, max: 50, message: "长度在 2 到 50 个字符", trigger: "blur" }
        ]
      }
    };
  },
  methods: {
    Home: function() {
      this.$router.push({ path: "/main" });
    },
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          let workerInfo = {};
          workerInfo['workerID'] = this.ruleForm.code;
          workerInfo['name'] = this.ruleForm.name;
          workerInfo['age'] = this.ruleForm.age;
          workerInfo['birth'] = this.ruleForm.birthDate;
          workerInfo['phone'] = this.ruleForm.tel;
          workerInfo['position'] = this.ruleForm.rank;
          // console.log(workerInfo);
          let postData = this.$qs.stringify(workerInfo);
          this.axios.post('submit/', postData).then(function (response) {
              alert(response.data);
          });
          this.$refs[formName].resetFields();
        } else {
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    }
  }
};
</script>

<style scoped>
h1 {
  margin-top: 5%;
}
form {
  margin-left: 10%;
  margin-right: 10%;
  margin-top: 5%;
  margin-bottom: 5%;
  padding-top: 5%;
  padding-bottom: 2%;
  padding-left: 2%;
  padding-right: 5%;
  border-style: groove;
  border-color: #409eff;
}
</style>
