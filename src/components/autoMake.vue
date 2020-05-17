<template>
    <el-container>
        <el-header height="0px">
            <el-dialog title="自动生成脚本" :visible.sync="dialogFormVisible">
                <el-form :model="form" :rules="rules" ref="form" :label-position="labelPosition" label-width="110px"  @submit.native.prevent>
                    <el-form-item label="项目名:" prop="projectName">
                        <el-input  type = "text" v-model="form.projectName" placeholder="请输入项目名称"></el-input>
                    </el-form-item>
                    <el-form-item label="网址:" prop="url">
                        <el-input  type = "url" v-model="form.url" placeholder="请输入网址"></el-input>
                    </el-form-item>
                    <el-form-item label="div容器xpath:" prop="div_list_xpath">
                        <el-input  v-model="form.div_list_xpath" placeholder="请输入爬取项的div的xpath"></el-input>
                    </el-form-item>
                    <el-form-item label="next_link:" prop="next_link">
                        <el-input  v-model="form.next_link" placeholder="请输入下一页链接的xpath"></el-input>
                    </el-form-item>
                    <el-row>
                        <el-col :span="8">
                            <el-form-item label="item" prop="item">
                                <el-input v-model="form.item" placeholder="请输入item名称"></el-input>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="xpath" prop="xpath">
                                <el-input v-model="form.xpath" placeholder="请输入相应xpath"></el-input>
                            </el-form-item>
                        </el-col>
                    </el-row>
                    <!--<el-form-item label="item的xpath:" prop="item">
                        <el-input  type = "xpath" placeholder="请输入xpath" v-model="form.item"></el-input>
                    </el-form-item>-->
                    <div  v-for="(domain, index) in form.item_xpath" :key="domain.key">
                        <el-row>
                            <el-col :span="8">
                                <el-form-item
                                        :label="'item'+ index"
                                        :prop="'item_xpath.' + index +'.item'"
                                        :rules="{
                                required: true,message:'item不能为空', trigger:'blur'
                                }"
                                >
                                    <el-input v-model="domain.item" placeholder="请输入item名称"></el-input>
                                </el-form-item>
                            </el-col>
                            <el-col :span="8">
                                <el-form-item
                                        :label="'xpath' + index"
                                        :prop="'item_xpath.' + index + '.xpath'"
                                        :rules="{
                                required: true, message: 'xpath不能为空', trigger: 'blur'
                                }"
                                >

                                    <el-input v-model="domain.xpath" placeholder="请输入相应xpath"></el-input>
                                </el-form-item>
                            </el-col>
                            <el-col :span="8">
                                <el-button @click.prevent="removeDomain(domain)">删除</el-button>
                            </el-col>
                        </el-row>
                    </div>
                    <!--优化复选框-->
                    <div style="margin-bottom:20px">
                        <el-form-item label="优化选项：">
                            <el-checkbox v-model="form.userAgent" label="userAgent" border></el-checkbox>
                            <el-checkbox v-model="form.cookie" label="cookie" border></el-checkbox>
                            <el-checkbox v-model="form.robot" label="robot" border></el-checkbox>
                            <el-checkbox v-model="form.bloom" label="bloom" border></el-checkbox>
                            <el-checkbox v-model="form.ipPool" label="ipPool" @change="Inputdelay" border></el-checkbox>
                        </el-form-item>
                        <el-form-item label="delay" prop="delay" :required="ishaveto">
                            <el-input type="number" v-model.number="form.delay" placeholder="请输入延时时长" :disabled="disabled"></el-input>
                        </el-form-item>

                    </div>
                    <el-form-item>
                        <el-button @click="addDomain">新增一条</el-button>
                        <el-button type="primary" @click="onSubmit('form')">提交</el-button>
                        <el-button @click="dialogFormVisible = false">取 消</el-button>
                    </el-form-item>
                </el-form>
            </el-dialog>
        </el-header>

        <el-main>
            <el-table :data="zipFileList" stripe highlight-current-row @current-change="handlCurrentChange">
                <el-table-column type="index" label="编号" width="100"></el-table-column>
                <el-table-column label="脚本" prop="name" width="250"></el-table-column>
                <el-table-column label="操作">
                    <template slot-scope="scope">
                        <el-button @click="handleDownload(scope.$index)" type="text" size="small">下载</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </el-main>
        <el-button type="primary" @click="dialogFormVisible = true" style="width: 150px;margin: 0 auto">创建新脚本</el-button>
    </el-container>
</template>

<script>
    export default {
        name: "autoMake",
        data(){
            return{
                labelPosition: "right",
                dialogFormVisible: false,
                ishaveto:false,
                disabled:true,
                zipFileList:[],
                currentRow:null,
                form:{
                    projectName:'',
                    url:'',
                    div_list_xpath:'',
                    next_link:'',
                    item:'',
                    xpath:'',
                    item_xpath: [{
                        item: '',
                        xpath:''
                    }],
                    userAgent:'',
                    cookie:'',
                    robot:'',
                    bloom:'',
                    ipPool:'',
                    delay:''
                },
                rules:{
                    projectName:[
                        {required:true,message:'请输入项目名',trigger:'blur'},
                        { min: 2, max: 10, message: '长度在 2 到 5 个字符' },
                        {pattern:/^[A-Za-z]/,message:'只能输入大小写字母'}

                    ],
                    url:[
                        {required:true,message:'请输入网址',trigger:'blur'},
                        {type:"url",message:'网址格式错误',trigger:'blur'}
                    ],
                    /*item:[
                        {required:true,message:'请输入xpath',trigger:'blur'},
                         {type:'',message:'xpath格式',trigger:'blur'}

                    ]*/
                    div_list_xpath:[
                        {required: true, message: 'div_list_xpath不能为空', trigger: 'blur'}
                    ],
                    next_link:[
                        {required:true,message:'请输入next_link',trigger:'blur'}

                    ],
                    item:[
                        {required: true,message:'item不能为空', trigger:'blur'}
                    ],
                    xpath:[
                        {required: true, message: 'xpath不能为空', trigger: 'blur'}
                    ]

                },
            }
        },
        mounted(){
            this.getSpiders()
        },
        methods:{

            removeDomain(domain) {
                var index = this.form.item_xpath.indexOf(domain)
                if (index !== -1) {
                    this.form.item_xpath.splice(index, 1)
                }
            },
            addDomain() {
                this.form.item_xpath.push({
                    item: '',
                    xpath:'',
                    key: Date.now()
                });
            },
            getSpiders(){
                this.zipFileList=[]
                this.$axios.get("http://121.199.12.225:5000/autoMake")
                    .then(response=>{
                        let spiderList=response.data
                        for( let i=0;i<spiderList.length;i++ ) {
                            this.zipFileList.push(spiderList[i])
                        }
                    })

            },
            onSubmit(formName){


                /*let form = this.$refs['form'].$el
                let formData = new FormData(form)
                formData.append('url',this.form.url)
                let items=[]
                let pathes=[]
                for(var i=0;i<this.form.item_xpath.length;i++){
                    items.push(this.form.item_xpath[i].item)
                    pathes.push(this.form.item_xpath[i].xpath)
                }
                formData.append('items',items)
                formData.append('xpathes',pathes)*/

                let postData = this.form

                this.$refs[formName].validate((valid)=>{
                    if(valid){
                        this.dialogFormVisible = false;
                        this.$axios({
                            method:'post',
                            url:"http://121.199.12.225:5000/autoMake",
                            data:postData
                        })
                            .then(response => {
                                if(response.data=='success'){

                                    this.$message.success("提交成功")


                                }

                            })
                        this.getSpiders()
                        //this.$refs.form.submit();
                        //alert('submit!');

                    }else{
                        console.log('error submit!!');
                        return false;
                    }

                });
            },
            handlCurrentChange(val){
                this.currentRow=val;
            },
            handleDownload(index){
                let zipFileList = this.zipFileList

                window.location.href = "http://121.199.12.225:5000/download?projectName="+zipFileList[index].name+"&time="+new Date().getTime()

            },
            Inputdelay(){
                if(this.form.ipPool){
                    this.ishaveto = true
                    this.disabled = false
                }
                else{
                    this.ishaveto = false
                    this.form.delay = null

                    this.disabled = true
                }

            }
        }


    }
</script>

<style scoped>

</style>
