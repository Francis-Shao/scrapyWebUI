<template>
    <div style="height: 100%;">
        <el-container style="height: 100%">
            <el-aside id="asideBar" width="14%">
          <span id="asideTitle">
            Web UI
          </span>
                <el-menu text-color="#d2d1cd" v-bind:router="true"  id="menu" default-active="introduction" active-text-color="#f8f9fc" >
                    <el-menu-item index="introduction">
                        <i class="el-icon-menu"></i>
                        <span>简介</span>
                    </el-menu-item>
                    <el-menu-item index="manageSpider">
                        <i class="el-icon-menu"></i>
                        <span slot="title">脚本管理</span>
                    </el-menu-item>
                    <el-menu-item index="autoMake">
                        <i class="el-icon-menu"></i>
                        <span slot="title">自动生成</span>
                    </el-menu-item>
                    <el-menu-item index="wordCloud">
                        <i class="el-icon-menu"></i>
                        <span slot="title">词云生成</span>
                    </el-menu-item>
                    <el-menu-item index="editor">
                        <i class="el-icon-menu"></i>
                        <span slot="title">编辑调试</span>
                    </el-menu-item>
                </el-menu>
            </el-aside>
            <el-container>
                <el-header id="rightHeader" height="50px">
                    <el-row :gutter="60">
                        <el-col :span="2" :offset="20">
                            <el-button type="text" style="color: aliceblue;font-size: 15px" @click="loginClick" v-show="loginButton">登录</el-button>
                            <span v-show="loginName" style="font-size: 15px">{{ nickName }}</span>
                        </el-col>
                        <el-col :span="1" >
                            <el-button type="text" style="color: aliceblue; font-size: 15px" @click="exitLogin" v-show="exitVisible">退出</el-button>
                        </el-col>
                    </el-row>
                </el-header>
                <el-main>
                    <div id="controller">
                        <keep-alive>
                            <router-view />
                        </keep-alive>
                    </div>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script>
    export default {
        name: "ui_index",
        data(){
            return {
                message: "beforeClick"
            }
        },

    }
</script>

<style scoped>
    /*.el-menu-item{*/
    /*    width: 20%;*/
    /*    float: left;*/
    /*}*/

    #asideBar{
        background-color: #4e73df;
        height: 100%;
        float: left;
    }

    #menu{
        background-size: cover;
        height: 100%;
    }

    #asideTitle{
        height: 50px;
        line-height: 50px;
        text-align: left;
        font-size: 24px;
        font-family: "Adobe 黑体 Std R",serif;
        color: white;
    }

    #rightHeader{
        background-color: #37ADF0;
        background-color: #d2d1cd;
        line-height: 50px;
    }

    .el-menu-item{
        height: 50px;
        line-height: 50px;
    }
</style>
