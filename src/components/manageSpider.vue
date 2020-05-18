<template>
    <div>
        <el-container>
            <el-header id="buttonHeader">
                <el-menu mode="horizontal" id="headerMenu" >
                    <el-menu-item @click="selectVisible" >
                        选择脚本
                    </el-menu-item>
                    <el-menu-item @click="run_spider">
                        运行
                    </el-menu-item>
                    <el-menu-item @click="cancel_spider">
                        停止
                    </el-menu-item>
                    <el-menu-item @click="getSpiderOutput">
                        查看输出
                    </el-menu-item>
                    <el-menu-item @click="deleteSpider">
                        删除
                    </el-menu-item>
                    <el-menu-item @click="getProjectList">
                        刷新
                    </el-menu-item>
                </el-menu>
            </el-header>
            <el-main>
                <el-table :data="pyFileList" stripe highlight-current-row @current-change="handleCurrentChange">
                    <el-table-column type="index" label="编号" width="100"></el-table-column>
                    <el-table-column label="脚本" prop="name" width="250"></el-table-column>
                    <el-table-column label="最后运行" prop="time" width="250"></el-table-column>
                    <el-table-column label="状态" prop="state"></el-table-column>
                </el-table>
            </el-main>
            <el-dialog title="选择脚本" :visible.sync="spiderSelect" @close="getProjectList" width="50%">
                <el-container>
                    <el-header style="width: 56%;margin-left: 22%">
                        <el-input v-model="project_name" placeholder="项目名" clearable></el-input>
                        <p></p>
                        <el-input v-model="spider_name" placeholder="脚本名" clearable></el-input>
                    </el-header>
                    <el-main style="width: 56%; margin-left: 22%; margin-top: 40px">
                        <el-upload drag :auto-upload="false" accept=".zip" :limit=1 ref="spiderUpload" >
                            <i class="el-icon-upload"></i>
                            <div style="height: 20px;line-height: 20px">将文件拖到此处，或者<em style="color: #4e73df">点击上传</em></div>
                            <div style="height: 20px;line-height: 20px">请将项目文件打包上传</div>
                        </el-upload>
                    </el-main>
                    <el-footer>
                        <el-popconfirm title="是否确保项目名与脚本名与项目代码设置一致
                        本站生成的脚本脚本名为template_sipder,项目名为文件名"
                            @onConfirm="uploadFile">
                            <el-button slot="reference">上传文件</el-button>
                        </el-popconfirm>
                    </el-footer>
                </el-container>
            </el-dialog>
            <el-dialog title="输出结果" :visible.sync="outputVisible" width="50%">
                <el-header>
                    <el-row>
                        <el-col :span="4" :offset="10">
                            <div>{{ currentSpider }}</div>
                        </el-col>
                        <el-col :offset="6" :span="4">
                            <el-button size="small" type="primary" plain @click="downloadOutput">
                                <i class="el-icon-download"></i>
                                下载输出
                            </el-button>
                        </el-col>
                    </el-row>
                </el-header>
                <el-main>
                    <el-input type="textarea" :disabled="true" v-model="outputContent" autosize>

                    </el-input>
                </el-main>
            </el-dialog>
        </el-container>
<!--        <el-button @click="test">调试函数</el-button>-->
    </div>
</template>

<script>
    export default {
        name: "manageSpider",
        data(){
            return{
                spiderList:[],
                spiderSelect:false,
                outputVisible:false,
                pyFileList:[],
                outputContent:"",
                currentSpider:"",
                currentRow:null,
                project_name:"",
                spider_name:""
            }
        },
        mounted(){
            this.getProjectList()
            window.setInterval(this.getProjectList,1000*60)

        },
        methods:{
            selectVisible(){
                this.spiderSelect=true
            },
            uploadFile(){
                let formData=new FormData
                let file_list=this.$refs.spiderUpload.uploadFiles
                for( let i=0; i<file_list.length;i++  ){
                    formData.append("file",file_list[i].raw)
                }
                formData.append("spider",this.spider_name)
                formData.append("project",this.project_name)
                this.$axios.post("http://121.199.12.225:5000/project/new",formData,
                    {
                        headers:{
                            'Content-Type': 'multipart/form-data'
                        }
                    }).then(response=>{
                    if (response.data.result==="success"){
                        this.$message.success("上传项目成功")
                    }
                    else{
                        this.$message.error(response.data.info)
                    }
                    this.$refs.spiderUpload.uploadFiles=[]
                })
            },
            getProjectList(){
                this.$axios.get("http://121.199.12.225:5000/project/all")
                .then(response=>{
                    this.pyFileList=[]
                    let spiderList=response.data
                    for( let i=0;i<spiderList.length;i++ ) {
                        this.pyFileList.push(spiderList[i])
                    }
                })
            },

            getSpiderOutput(){
                if (this.currentRow==null){
                    this.$message.error("请选择脚本")
                }
                else {
                    let name = this.currentRow.name
                    this.$axios.get("http://121.199.12.225:5000/project/output?name=" + name)
                        .then(response => {
                            let content = response.data.info
                            this.outputContent = content
                        })
                    this.currentSpider = this.currentRow.name
                    this.outputVisible = true
                }
            },

            deleteSpider(){
                if (this.currentRow==null){
                    this.$message.error("请选择脚本")
                }
                else{
                    let name=this.currentRow.name
                    this.$axios.get("http://121.199.12.225:5000/project/delete?name="+name)
                    .then(response=>{
                        let answer=response.data
                        if(answer.result==='success'){
                            this.getProjectList()
                        }
                        else{
                            this.$message.error(answer.info)
                            this.getProjectList()
                        }
                    })
                }
            },

            run_spider(){
                if (this.currentRow==null){
                    this.$message.error("请选择脚本")
                }
                else{
                    let name=this.currentRow.name
                    this.$axios.get("http://121.199.12.225:5000/project/run?name="+name)
                        .then(response=>{
                            let answer=response.data
                            if(answer.result==='success'){
                                this.$message.success(answer.info)
                            }
                            else{
                                this.$message.error(answer.info)
                            }
                        })
                }
            },

            cancel_spider(){
                if (this.currentRow==null){
                    this.$message.error("请选择脚本")
                }
                else{
                    let name=this.currentRow.name
                    this.$axios.get("http://121.199.12.225:5000/project/cancel?name="+name)
                        .then(response=>{
                            let answer=response.data
                            if(answer.result==='success'){
                                this.$message.success(answer.info)
                            }
                            else{
                                this.$message.error(answer.info)
                            }
                        })
                }
            },

            downloadOutput(){
                window.location.href="http://121.199.12.225:5000/project/output/download?name="+this.currentSpider
            },

            handleCurrentChange(val){
                this.currentRow=val
            },

            test(){
                this.$axios.get("http://121.199.12.225:5000/")
                .then(response=>{
                    this.$message.success(response.data)
                })
            }
        }
    }
</script>

<style scoped>

    #buttonHeader{
        height: 120px;
        line-height: 120px;
        /*box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);*/
        /*background-color: gold;*/
    }

    #headerMenu{
        width: 100%;
    }

</style>