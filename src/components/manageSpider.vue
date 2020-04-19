<template>
    <div>
        <el-container>
            <el-header id="buttonHeader">
                <el-menu mode="">

                </el-menu>
            </el-header>
            <el-main>
                <h1>主体</h1>
                <el-button type="text" >test</el-button>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    export default {
        name: "manageSpider"
    }
</script>

<style scoped>

    #buttonHeader{
        height: 120px;
        line-height: 120px;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
        /*background-color: #42b983;*/
    }

</style>