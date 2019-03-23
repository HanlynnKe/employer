<template>
  <div>
    <Header />
    <h1>Go find employees</h1>
    <el-tabs tab-position="left" style="margin-top: 5%; margin-left: 5%;">
      <el-tab-pane label="查找选项">
        <h3 style="margin-right: 20%">请选择左侧的查找选项进行查找</h3>
        <el-popover placement="right-end" title="查找选项" width="200" trigger="click"
                    content="按照员工的姓名、职位、生日、年龄、工号进行员工信息的查找与删除">
          <el-button type="info" slot="reference" icon="el-icon-back"
                     style="margin-right: 20%; margin-bottom: 10%" circle>
          </el-button>
        </el-popover>
      </el-tab-pane>
      <el-tab-pane label="按姓名">
        <el-form ref="form" label-width="150px">
          <el-form-item label="要查询的员工姓名：" size="small"
                        rules="[{required: true, message: '请输入姓名'}]">
            <el-row class="searchRow">
              <el-col span="16">
                <el-input v-model="name"></el-input>
              </el-col>
              <el-col span="4">
                <el-button type="success" v-on:click="searchItem" circle><i class="el-icon-search"></i></el-button>
              </el-col>
            </el-row>
          </el-form-item>
          <el-table :data="tableData" style="width: 100%; margin-bottom: 5%" max-height="250">
            <el-table-column fixed prop="eid" label="ID" width="120"></el-table-column>
            <el-table-column prop="name" label="姓名" width="120"></el-table-column>
            <el-table-column prop="birth" label="生日" width="120"></el-table-column>
            <el-table-column prop="age" label="年龄" width="120"></el-table-column>
            <el-table-column prop="tel" label="电话" width="150"></el-table-column>
            <el-table-column prop="rank" label="职位" width="150"></el-table-column>
            <!--<el-table-column fixed="right" label="操作" width="120">-->
              <!--<template slot-scope="scope">-->
                <!--<el-button type="warning" size="small" circle>-->
                  <!--<i class="el-icon-edit"></i>-->
                <!--</el-button>-->
                <!--<el-button @click.native.prevent="deleteRow(scope.$index, tableData4)"-->
                           <!--type="danger" size="small" circle>-->
                  <!--<i class="el-icon-delete"></i>-->
                <!--</el-button>-->
              <!--</template>-->
            <!--</el-table-column>-->
          </el-table>
          <el-form-item label="已搜索到：" size="small">
            {{countIndex[0]}} 条记录
          </el-form-item>
          <!--<el-form-item label="已编辑了：" size="small">-->
            <!--{{editTimes}} 条记录-->
          <!--</el-form-item>-->
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="按职位">
        <el-form ref="form" label-width="150px">
          <el-form-item label="要查询的员工职位：" size="small"
                        rules="[{required: true, message: '请输入姓名'}]">
            <el-row class="searchRow">
              <el-col span="16">
                <el-input v-model="rank"></el-input>
              </el-col>
              <el-col span="4">
                <el-button type="success" v-on:click="searchItem" circle><i class="el-icon-search"></i></el-button>
              </el-col>
            </el-row>
          </el-form-item>
          <el-table :data="tableData" style="width: 100%; margin-bottom: 5%" max-height="250">
            <el-table-column fixed prop="eid" label="ID" width="120"></el-table-column>
            <el-table-column prop="name" label="姓名" width="120"></el-table-column>
            <el-table-column prop="birth" label="生日" width="120"></el-table-column>
            <el-table-column prop="age" label="年龄" width="120"></el-table-column>
            <el-table-column prop="tel" label="电话" width="150"></el-table-column>
            <el-table-column prop="rank" label="职位" width="150"></el-table-column>
            <!--<el-table-column fixed="right" label="操作" width="120">-->
              <!--<template slot-scope="scope">-->
                <!--<el-button type="warning" size="small" circle>-->
                  <!--<i class="el-icon-edit"></i>-->
                <!--</el-button>-->
                <!--<el-button @click.native.prevent="deleteRow(scope.$index, tableData4)"-->
                           <!--type="danger" size="small" circle>-->
                  <!--<i class="el-icon-delete"></i>-->
                <!--</el-button>-->
              <!--</template>-->
            <!--</el-table-column>-->
          </el-table>
          <el-form-item label="已搜索到：" size="small">
            {{countIndex[0]}} 条记录
          </el-form-item>
          <!--<el-form-item label="已编辑了：" size="small">-->
            <!--{{editTimes}} 条记录-->
          <!--</el-form-item>-->
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="按生日">
        <el-form ref="form" label-width="150px">
          <el-form-item label="要查询的员工生日：" size="small"
                        rules="[{required: true, message: '请输入姓名'}]">
            <el-row class="searchRow">
              <el-col span="16">
                <el-date-picker v-model="birth" type="date" placeholder="选择日期"></el-date-picker>
              </el-col>
              <el-col span="4">
                <el-button type="success" v-on:click="searchItem" circle><i class="el-icon-search"></i></el-button>
              </el-col>
            </el-row>
          </el-form-item>
          <el-table :data="tableData" style="width: 100%; margin-bottom: 5%" max-height="250">
            <el-table-column fixed prop="eid" label="ID" width="120"></el-table-column>
            <el-table-column prop="name" label="姓名" width="120"></el-table-column>
            <el-table-column prop="birth" label="生日" width="120"></el-table-column>
            <el-table-column prop="age" label="年龄" width="120"></el-table-column>
            <el-table-column prop="tel" label="电话" width="150"></el-table-column>
            <el-table-column prop="rank" label="职位" width="150"></el-table-column>
            <!--<el-table-column fixed="right" label="操作" width="120">-->
              <!--<template slot-scope="scope">-->
                <!--<el-button type="warning" size="small" circle>-->
                  <!--<i class="el-icon-edit"></i>-->
                <!--</el-button>-->
                <!--<el-button @click.native.prevent="deleteRow(scope.$index, tableData4)"-->
                           <!--type="danger" size="small" circle>-->
                  <!--<i class="el-icon-delete"></i>-->
                <!--</el-button>-->
              <!--</template>-->
            <!--</el-table-column>-->
          </el-table>
          <el-form-item label="已搜索到：" size="small">
            {{countIndex[0]}} 条记录
          </el-form-item>
          <!--<el-form-item label="已编辑了：" size="small">-->
            <!--{{editTimes}} 条记录-->
          <!--</el-form-item>-->
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="按年龄">
        <el-form ref="form" label-width="150px">
          <el-form-item label="要查询的员工年龄 >" size="small"
                        rules="[{required: true, message: '请输入姓名'}]">
            <el-row class="searchRow">
              <el-col span="16">
                <el-input v-model="age"></el-input>
              </el-col>
              <el-col span="4">
                <el-button type="success" v-on:click="searchItem" circle><i class="el-icon-search"></i></el-button>
              </el-col>
            </el-row>
          </el-form-item>
          <el-table :data="tableData" style="width: 100%; margin-bottom: 5%" max-height="250">
            <el-table-column fixed prop="eid" label="ID" width="120"></el-table-column>
            <el-table-column prop="name" label="姓名" width="120"></el-table-column>
            <el-table-column prop="birth" label="生日" width="120"></el-table-column>
            <el-table-column prop="age" label="年龄" width="120"></el-table-column>
            <el-table-column prop="tel" label="电话" width="150"></el-table-column>
            <el-table-column prop="rank" label="职位" width="150"></el-table-column>
            <!--<el-table-column fixed="right" label="操作" width="120">-->
              <!--<template slot-scope="scope">-->
                <!--<el-button type="warning" size="small" circle>-->
                  <!--<i class="el-icon-edit"></i>-->
                <!--</el-button>-->
                <!--<el-button @click.native.prevent="deleteRow(scope.$index, tableData4)"-->
                           <!--type="danger" size="small" circle>-->
                  <!--<i class="el-icon-delete"></i>-->
                <!--</el-button>-->
              <!--</template>-->
            <!--</el-table-column>-->
          </el-table>
          <el-form-item label="已搜索到：" size="small">
            {{countIndex[0]}} 条记录
          </el-form-item>
          <!--<el-form-item label="已编辑了：" size="small">-->
            <!--{{editTimes}} 条记录-->
          <!--</el-form-item>-->
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="按ID">
        <el-form ref="form" label-width="150px">
          <el-form-item label="要查询的员工ID：" size="small"
                        rules="[{required: true, message: '请输入姓名'}]">
            <el-row class="searchRow">
              <el-col span="16">
                <el-input v-model="eid"></el-input>
              </el-col>
              <el-col span="4">
                <el-button type="success" v-on:click="searchItem" circle><i class="el-icon-search"></i></el-button>
              </el-col>
            </el-row>
          </el-form-item>
          <el-table :data="tableData" style="width: 100%; margin-bottom: 5%" max-height="250">
            <el-table-column fixed prop="eid" label="ID" width="120"></el-table-column>
            <el-table-column prop="name" label="姓名" width="120"></el-table-column>
            <el-table-column prop="birth" label="生日" width="120"></el-table-column>
            <el-table-column prop="age" label="年龄" width="120"></el-table-column>
            <el-table-column prop="tel" label="电话" width="150"></el-table-column>
            <el-table-column prop="rank" label="职位" width="150"></el-table-column>
            <!--<el-table-column fixed="right" label="操作" width="120">-->
              <!--<template slot-scope="scope">-->
                <!--<el-button type="warning" size="small" circle>-->
                  <!--<i class="el-icon-edit"></i>-->
                <!--</el-button>-->
                <!--<el-button @click.native.prevent="deleteRow(scope.$index, tableData4)"-->
                           <!--type="danger" size="small" circle>-->
                  <!--<i class="el-icon-delete"></i>-->
                <!--</el-button>-->
              <!--</template>-->
            <!--</el-table-column>-->
          </el-table>
          <el-form-item label="已搜索到：" size="small">
            {{countIndex[0]}} 条记录
          </el-form-item>
          <!--<el-form-item label="已编辑了：" size="small">-->
            <!--{{editTimes}} 条记录-->
          <!--</el-form-item>-->
        </el-form>
      </el-tab-pane>
    </el-tabs>
    <el-button id="goHome" type="warning" @click="Home" round>返回主页<i class="el-icon-menu el-icon--right"></i></el-button>
  </div>
</template>

<script>
import Header from "@/components/MainHeader.vue";
export default {
  name: "FindHim",
  components: {
    Header
  },
  data() {
    return {
      name: "",
      rank: "",
      birth: "",
      age: "",
      eid: "",
      // editTimes: 0,
      tableData: [],
      countIndex: [0]
    };
  },
  methods: {
    Home: function() {
      this.$router.push({ path: "/main" });
    },
    searchItem: function() {
      let keyInfo = {};
      let index;
      var num = 0;
      var searchAns = [];
      keyInfo['workerID'] = this.eid;
      keyInfo['name'] = this.name;
      keyInfo['age'] = this.age;
      keyInfo['birth'] = this.birth;
      keyInfo['position'] = this.rank;
      let postData = this.$qs.stringify(keyInfo);
      this.axios.post('search/', postData).then(function (response) {
          for ( index in response.data){
              searchAns.push(response.data[index]);
              num = num + 1;
          }
          this.countIndex.pop();
          this.countIndex.push(num);
      }.bind(this));
      this.eid = "";
      this.name = "";
      this.rank = "";
      this.birth = "";
      this.age = "";
      this.tableData = searchAns;
    },
    // deleteRow(index, rows) {
    //   rows.splice(index, 1);
    //   this.editTimes += 1;
    // }
  },
  mounted (){
      var info_list = [];
      var num = 0;
      this.axios.get('search/').then(function (response) {
          for (var index in response.data){
              info_list.push(response.data[index]);
              num = num + 1;
          }
          this.countIndex.pop();
          this.countIndex.push(num);
      }.bind(this));
      this.tableData = info_list;
  }
};
</script>

<style scoped>
h1 {
  margin-top: 5%;
  margin-bottom: 10%;
}
form {
  margin-right: 10%;
}
</style>
