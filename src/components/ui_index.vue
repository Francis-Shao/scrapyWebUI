<template>
    <div style="height: 100%;">
        <el-container style="height: 100%">
            <el-aside id="asideBar" width="14%">
                <span id="asideTitle">
                Web UI
                </span>
                <el-menu text-color="#d2d1cd" v-bind:router="true"  id="menu" default-active="introduction" active-text-color="black" >
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
                </el-menu>
            </el-aside>
            <el-main id="indexMain">
                <el-container>
                    <el-header id="rightHeader" height="50px">
                    </el-header>
                    <el-main>
                        <router-view></router-view>
                    </el-main>
                </el-container>
            </el-main>
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

    }

    #menu{
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

        line-height: 50px;
    }

    #indexMain{

    }

    .el-menu-item{
        height: 50px;
        line-height: 50px;
    }
</style>
