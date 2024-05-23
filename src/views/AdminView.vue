<template>
  <!--上方栏-->
  <header class="navbar navbar-dark sticky-top flex-md-nowrap p-0 topheader">
    <a class="navbar-brand col-md-3 col-lg-2 me-0 px-3 fs-6" href="#"
      style="margin-left: 3%; color: whitesmoke;">Federated Learing</a>
    <ul class="nav col-12 col-md-auto mb-2 justify-content-center mb-md-0" style="margin-right: 8%;">
      <li><a href="#" class="nav-link px-3 link-btn allProject" @click="allProjects">所有项目</a></li>
      <li><a href="#" class="nav-link px-3 link-btn myProject" @click="myProject">我的项目</a></li>
      <li><a href="#" class="nav-link px-3 link-btn userCenter" @click="changePage('page1')">个人中心</a></li>
      <li><a href="#" class="nav-link px-3 link-btn link-help" @click="changePage('page1')">帮助</a></li>
      <div>
        <button type="button" data-bs-toggle="modal" data-bs-target="#exampleModal">创建项目</button>
      </div>
    </ul>
  </header>

  <!-- 上方封面 -->
  <section class="home-banner">
    <div class="container">
      <nav v-if="showNav" class="top-nav"> </nav>
      <!-- 搜索栏 -->
      <nav
        :class="{ 'navbar': true, 'navbar-expand-lg': true, 'bg-body-tertiary': true, 'search-top': true, 'sticky': isSticky }">
        <div class="container-fluid">
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                  aria-expanded="false">
                  疾病类型
                </a>
                <ul class="dropdown-menu">
                  <li><a class="dropdown-item" href="#">心脏</a></li>
                  <li><a class="dropdown-item" href="#">呼吸</a></li>
                  <li><a class="dropdown-item" href="#">消化</a></li>
                  <li><a class="dropdown-item" href="#">泌尿</a></li>
                  <li><a class="dropdown-item" href="#">内分泌</a></li>
                  <li><a class="dropdown-item" href="#">神经</a></li>
                  <li><a class="dropdown-item" href="#">血液</a></li>
                  <li>
                    <hr class="dropdown-divider">
                  </li>
                  <li><a class="dropdown-item" href="#">神经科</a></li>
                </ul>
              </li>
            </ul>
            <form class="d-flex search-bar" role="search" style="width: 85%;">
              <input class="form-control me-2" type="search" placeholder="搜索项目" aria-label="Search">
              <button @click="onSearchClick">搜索</button>
            </form>
          </div>
        </div>
      </nav>
      <!-- 介绍文字 -->
      <div class="banner-row">
        <div>
          <div class="banner-content text-center">
            <div class="section-head">
              <h4 class="section-title banner-title">医智联邦——联邦学习驱动的医疗<br /><span class="primary-color">科研、学习、诊断
                </span>集成平台</h4>
            </div>
            <div class="banner-text">
              <p>"医智联邦"是一款创新的医疗科研、学习、诊断集成平台，为医疗机构、医生和研究人员提供了一个安全、高效的协作环境。</p>
              <p>通过"医智联邦"，医疗机构能够提升诊疗效率和资源配置优化，医生可以依据高精度的全局模型进行疾病风险预测和个性化治疗方案制定。
                本地训练模型并共享模型更新，实现了跨机构的数据隐私保护和知识共享，有效解决了医疗数据孤岛问题，促进了医疗数据的流动性和公开性。</p>
            </div>
            <div class="banner-button">
              <button class="circle"> <a href="#" class="button-round">Learn More</a></button>
              <button class="circle"> <a href="#" to="/money" class="button-round">About Us</a></button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 项目内容 -->
  <div v-show="currentPage === 'page1'" class="project-home content-main">
    <!-- 左侧的主要内容 -->
    <div class="project-home-content">
      <!-- 所有项目-循环渲染 -->
      <div class="project-home-tab-content-list">
        <div class="project-home-tab-content-list-item" v-for="project in projects" :key="project.id">
          <div class="item-content">
            <router-link :to="{ name: 'project', params: { name: project.name } }" class="item-content-link"
              target="_blank">
              <div class="item-content-title">
                <img src="../assets/project-title.png">
                <span class="item-content-title-n">{{ project.name }}</span>
              </div>
              <div class="item-content-abs item-content-abs-public">{{ project.description }}</div>
            </router-link>
            <div class="item-content-msg">
              <a class="item-content-msg-user">
                <div class="fedml-user-avatar">
                  <img class="fedml-user-avatar-img" src="../assets/project-user.png">
                </div>
                <div><span class="fedml-user-name">{{ project.username }}</span></div>
              </a>
              <div class="item-content-msg-tags item-algin-c">
                <i class="item-content-msg-icon tag"></i>
                <span class="item-content-msg-tags-tag">{{ project.type }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- 项目页面索引切换 -->
      <div class="project-home-tab-content-footer">
        <ul class="ant-pagination">
          <li title="Previous Page" class="ant-pagination-prevant-pagination-disabled" aria-disabled="true">
            <button class="ant-pagination-item-link" type="button" tabindex="-1" disabled>
              <img src="../assets/left.png">
            </button>
          </li>
          <li title="1" class="ant-pagination-item ant-pagination-item-1 ant-pagination-item-active" tabindex="0">
            <a href="#">1</a>
          </li>
          <li title="2" class="ant-pagination-item ant-pagination-item-2" tabindex="0">
            <a href="#">2</a>
          </li>
          <li title="3" class="ant-pagination-item ant-pagination-item-3" tabindex="0">
            <a href="#">3</a>
          </li>
          <li title="4" class="ant-pagination-item ant-pagination-item-4" tabindex="0">
            <a href="#">4</a>
          </li>
        </ul>
      </div>
    </div>
    <!-- 右侧的Table -->
    <div class="project-home-right">
      <div class="project-home-recommend">
        <!-- 第一个card -->
        <div class="project-home-recommend-card" id="recommend-1">
          <!-- card头部封面 -->
          <div class="project-home-recommend-card-title"></div>
          <!-- card主体内容 -->
          <div class="project-home-recommend-card-content">
            <!-- 排行榜列表 -->
            <ul class="project-home-recommend-card-content-ul">
              <div class="project-home-recommend-card-content-ul-li">
                <div class="project-home-recommend-card-content-ul-li-index project-home-recommend-top">1
                </div>
                <a target="_blank" href="#">语言学视角下人工智能生成内容...</a>
              </div>
              <div class="project-home-recommend-card-content-ul-li">
                <div class="project-home-recommend-card-content-ul-li-index project-home-recommend-top">2
                </div>
                <a target="_blank" href="#">消化道内窥镜与人工智能精准医...</a>
              </div>
              <div class="project-home-recommend-card-content-ul-li">
                <div class="project-home-recommend-card-content-ul-li-index project-home-recommend-top">3
                </div>
                <a target="_blank" href="#">人工智能知识图谱和图像分类用...</a>
              </div>
              <div class="project-home-recommend-card-content-ul-li">
                <div class="project-home-recommend-card-content-ul-li-index">4
                </div>
                <a target="_blank" href="#">英伟达AI风暴席卷医疗行业 “AI...</a>
              </div>
              <div class="project-home-recommend-card-content-ul-li">
                <div class="project-home-recommend-card-content-ul-li-index">5
                </div>
                <a target="_blank" href="#">皮肤镜图像质量控制标准专家共...</a>
              </div>
              <div class="project-home-recommend-card-content-ul-li">
                <div class="project-home-recommend-card-content-ul-li-index">6
                </div>
                <a target="_blank" href="#">基于5G网络的复合型糖尿病AI管...</a>
              </div>
              <div class="project-home-recommend-card-content-ul-li">
                <div class="project-home-recommend-card-content-ul-li-index">7
                </div>
                <a target="_blank" href="#">基于大语言模型的体检总检结论自...</a>
              </div>
              <div class="project-home-recommend-card-content-ul-li">
                <div class="project-home-recommend-card-content-ul-li-index">8
                </div>
                <a target="_blank" href="#">多方参与的互联网医院运营管理研...</a>
              </div>
              <div class="project-home-recommend-card-content-ul-li">
                <div class="project-home-recommend-card-content-ul-li-index">9
                </div>
                <a target="_blank" href="#">论医疗数据的权属配置——基于公...</a>
              </div>
              <div class="project-home-recommend-card-content-ul-li">
                <div class="project-home-recommend-card-content-ul-li-index">10
                </div>
                <a target="_blank" href="#">构建医疗数据安全与隐私保护新框...</a>
              </div>

            </ul>
          </div>
        </div>
        <!-- 第二个card -->
        <div class="project-home-recommend-card" id="recommend-2">
          <!-- card头部封面 -->
          <div class="project-home-recommend-card-title"></div>
          <!-- card主体内容 -->
          <div class="project-home-recommend-card-content">
            <!-- 排行榜列表 -->
            <ul class="project-home-recommend-card-content-ul">
              <div class="project-home-recommend-card-content-ul-li">
                <div class="project-home-recommend-card-content-ul-li-index project-home-recommend-top">1
                </div>
                <a target="_blank" href="#">语言学视角下人工智能生成内容...</a>
              </div>
              <div class="project-home-recommend-card-content-ul-li">
                <div class="project-home-recommend-card-content-ul-li-index project-home-recommend-top">2
                </div>
                <a target="_blank" href="#">消化道内窥镜与人工智能精准医...</a>
              </div>
              <div class="project-home-recommend-card-content-ul-li">
                <div class="project-home-recommend-card-content-ul-li-index project-home-recommend-top">3
                </div>
                <a target="_blank" href="#">人工智能知识图谱和图像分类用...</a>
              </div>
              <div class="project-home-recommend-card-content-ul-li">
                <div class="project-home-recommend-card-content-ul-li-index">4
                </div>
                <a target="_blank" href="#">英伟达AI风暴席卷医疗行业 “AI...</a>
              </div>
              <div class="project-home-recommend-card-content-ul-li">
                <div class="project-home-recommend-card-content-ul-li-index">5
                </div>
                <a target="_blank" href="#">皮肤镜图像质量控制标准专家共...</a>
              </div>
              <div class="project-home-recommend-card-content-ul-li">
                <div class="project-home-recommend-card-content-ul-li-index">6
                </div>
                <a target="_blank" href="#">基于5G网络的复合型糖尿病AI管...</a>
              </div>
              <div class="project-home-recommend-card-content-ul-li">
                <div class="project-home-recommend-card-content-ul-li-index">7
                </div>
                <a target="_blank" href="#">基于大语言模型的体检总检结论自...</a>
              </div>
              <div class="project-home-recommend-card-content-ul-li">
                <div class="project-home-recommend-card-content-ul-li-index">8
                </div>
                <a target="_blank" href="#">多方参与的互联网医院运营管理研...</a>
              </div>
              <div class="project-home-recommend-card-content-ul-li">
                <div class="project-home-recommend-card-content-ul-li-index">9
                </div>
                <a target="_blank" href="#">论医疗数据的权属配置——基于公...</a>
              </div>
              <div class="project-home-recommend-card-content-ul-li">
                <div class="project-home-recommend-card-content-ul-li-index">10
                </div>
                <a target="_blank" href="#">构建医疗数据安全与隐私保护新框...</a>
              </div>

            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 我的项目-循环渲染 -->
  <div class="project-home-tab-content-list">
    <div class="project-home-tab-content-list-item" v-for="project in myprojects" :key="project.id">
      <div class="item-content">
        <a class="item-content-link" target="_blank" :href="project.link">
          <!-- 标题 -->
          <div class="item-content-title">
            <img src="../assets/project-title.png">
            <span class="item-content-title-n">{{ project.name }}</span>
          </div>
          <!-- 项目介绍 -->
          <div class="item-content-abs item-content-abs-public">{{ project.description }}</div>
        </a>
        <div class="item-content-msg">
          <a class="item-content-msg-user">
            <div class="fedml-user-avatar">
              <img class="fedml-user-avatar-img" src="../assets/project-user.png">
            </div>
            <div><span class="fedml-user-name">{{ project.username }}</span></div>
          </a>
          <div class="item-content-msg-tags item-algin-c">
            <i class="item-content-msg-icon tag"></i>
            <span class="item-content-msg-tags-tag">{{ project.type }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- 创建项目 -->
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">创建项目</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="modal-body-content modal-body-project-name">
            <div><span class="modal-body-project-span">项目名称</span></div>
            <div><input type="text" placeholder="请输入项目名称" v-model="newProjectName"></div>
          </div>
          <div class="modal-body-content modal-body-project-type">
            <span class="modal-body-project-span">项目类型</span>
            <div class="modal-body-dropdown">
              <select v-model="newProjectType">
                <option class="option-disabled" disabled value="">请选择项目类型</option>
                <option>骨科</option>
                <option>神经科</option>
                <option>心血管科</option>
                <option>麻醉科</option>
                <option>眼科</option>
                <option>耳鼻喉科</option>
                <option>口腔科</option>
                <option>肿瘤科</option>
                <option>皮肤科</option>
              </select>
            </div>
          </div>
          <form>
            <fieldset style="display: flex;">
              <legend style="width:30%; font-size:16px">是否为公开项目</legend>
              <div style="width:50%">
                <input type="radio" id="contactChoice1" name="contact" value="email" />
                <label for="contactChoice1">公开</label>

                <input type="radio" id="contactChoice2" name="contact" value="phone" style="margin-left:10px">
                <label for="contactChoice2">私密</label>
              </div>
            </fieldset>
          </form>
          <div class="modal-body-project-decs">
            <span class="modal-body-project-span modal-body-title-desc">项目描述</span>
            <textarea name="" id="model-body-project-desc" cols="30" rows="10" placeholder="请输入项目描述"
              v-model="newProjectDesc"></textarea>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" @click="createProject">创建项目</button>
        </div>
      </div>
    </div>
  </div>

  <!-- 底部黑色栏 -->
  <div class="home-footer">
    <div class="home-footer-content home-footer-about">
      <span class="home-footer-about home-footer-title">关于Fedml</span>
      <span class="home-footer-about-main-content">联邦学习是一种分布式学习，提出该概念的初衷是为了解决数据孤岛问题，从分散、孤立的数据中训练机器学习模型。
        联邦学习与传统基于数据中心的分布式学习主要有三方面的不同</span>
    </div>
    <div class="home-footer-content home-footer-resource">
      <div class="home-footer-resource home-footer-title">相关资源</div>
      <div class="home-footer-main-content home-footer-resource-help"><a href="#">用户指南</a></div>
      <div class="home-footer-main-content home-footer-resource-question"><a href="#">常见问题</a></div>
    </div>
    <div class="home-footer-content home-footer-contact">
      <span class="home-footer-contact home-footer-title">联系我们</span>
      <div class="home-footer-main-content home-footer-contact-email">邮箱: fedml@email.com</div>
      <div class="home-footer-main-content home-footer-contact-qq">官方QQ: 1111111111</div>
    </div>
  </div>
</template>
<style scoped src='../css/admin.css'></style>
<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import axios from 'axios'

// 搜索框滚动效果
const isSticky = ref(false)

const handleScroll = () => {
  const navbar = document.querySelector('.search-top')// 根据实际选择器调整
  isSticky.value = window.scrollY >= navbar.offsetTop
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})

// 新增一个白底导航栏
// 响应式属性，用于控制导航栏的显示
const showNav = ref(false)

// 检查滚动位置的函数
const checkScroll = () => {
  const navbar = document.querySelector('.search-top')// 根据实际选择器调整
  showNav.value = window.scrollY >= navbar.offsetTop
}

onMounted(() => {
  // 组件挂载后，添加滚动事件监听器
  window.addEventListener('scroll', checkScroll)
})

onUnmounted(() => {
  // 组件卸载前，移除滚动事件监听器
  window.removeEventListener('scroll', checkScroll)
})

// 上方栏页面切换
// eslint-disable-next-line
let currentPage = ref('page1') // 默认显示第一个页面
// eslint-disable-next-line
const changePage = (page) => {
  currentPage.value = page
}

// 创建项目
const newProjectName = ref('')
const newProjectType = ref('')
const newProjectDesc = ref('')
console.log(newProjectName.value)
// 创建项目的方法
// eslint-disable-next-line
const createProject = async () => {
  // 构造要发送的数据
  const projectData = {
    project_name: newProjectName.value,
    project_type_id: newProjectType.value,
    project_description: newProjectDesc.value
  }
  // 发送数据到后端API
  try {
    // 发送 POST 请求到后端 API
    // 替换 'YOUR_BACKEND_API_ENDPOINT' 为你的后端 API 端点
    const response = await axios.post('http://10.29.75.164:8000/create_project/', projectData)
    console.log('Project created:', response.data)
    alert('项目创建成功！')
    // 根据需要处理响应，如显示消息或重定向等
  } catch (error) {
    console.error('Failed to create project:', error)
    console.log(newProjectName.value)
    console.log(newProjectType.value)
    console.log(newProjectDesc.value)
    // 处理错误，如显示错误消息等
  }
}

// 获取所有项目列表
// eslint-disable-next-line
const projects = ref([])
// eslint-disable-next-line
const allProjects = async () => {
  try {
    const response = await axios.get('http://10.29.75.164:8000/get_project_list/') // 替换为你的后端 API 路径
    // 转换数据格式以匹配前端代码
    projects.value = response.data.map(project => ({
      name: project.project_name,
      description: project.project_description,
      type: project.project_type,
      username: project.user
    }))
    console.log(response.data)
  } catch (error) {
    console.log(error)
  }
}

// 获取我的项目列表
const myprojects = ref([])
// eslint-disable-next-line
const myallProjects = async () => {
  try {
    const response = await axios.get('/api/projects') // 替换为你的后端 API 路径
    myprojects.value = response.data // 假设后端返回的是一个数组
  } catch (error) {
    console.error('获取项目列表失败:', error)
  }
}
</script>
